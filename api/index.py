"""
English Learning App - Backend API for Vercel
Flask REST API for the English Learning Application
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
import json

app = Flask(__name__)

# Get the allowed origins from environment or use defaults
allowed_origins = os.environ.get('ALLOWED_ORIGINS', '*').split(',')
CORS(app, origins=allowed_origins if allowed_origins != ['*'] else '*')

app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# ============== IN-MEMORY STORAGE (for serverless) ==============
# Note: In production, use a database like Vercel Postgres, MongoDB, or Supabase

user_progress = {}
user_stats = {}
user_vocabulary = {}
user_achievements = {}

ACHIEVEMENTS = {
    'first_lesson': {'name': 'First Steps', 'description': 'Complete your first lesson', 'icon': '🎯'},
    'first_100_xp': {'name': 'Century', 'description': 'Earn 100 XP', 'icon': '💯'},
    'streak_7': {'name': 'Week Warrior', 'description': '7 day streak', 'icon': '🔥'},
    'vocab_50': {'name': 'Word Collector', 'description': 'Learn 50 words', 'icon': '📚'},
    'perfect_10': {'name': 'Perfect 10', 'description': '10 exercises in a row', 'icon': '⭐'},
}

def get_user_id():
    """Get or create user ID from header"""
    user_id = request.headers.get('X-User-ID')
    if not user_id:
        user_id = str(uuid.uuid4())
    return user_id

def get_user_stats(user_id):
    """Get or create user stats"""
    if user_id not in user_stats:
        user_stats[user_id] = {
            'total_xp': 0,
            'current_streak': 0,
            'longest_streak': 0,
            'words_learned': 0,
            'exercises_completed': 0
        }
    return user_stats[user_id]

# ============== CONTENT ==============

from content import get_all_lessons, get_lesson_by_id

# ============== LESSONS API ==============

@app.route('/api/lessons', methods=['GET'])
def api_get_lessons():
    """Get all lessons with metadata"""
    user_id = get_user_id()
    lessons = get_all_lessons()
    
    # Get progress for this user
    progress = user_progress.get(user_id, {})
    
    lessons_with_progress = []
    for lesson in lessons:
        lesson_progress = progress.get(lesson['id'], {})
        lessons_with_progress.append({
            'id': lesson['id'],
            'level': lesson['level'],
            'title': lesson['title'],
            'completed': lesson_progress.get('completed', False),
            'lastAccessed': lesson_progress.get('last_accessed')
        })
    
    return jsonify({
        'success': True,
        'lessons': lessons_with_progress
    })

@app.route('/api/lessons/<lesson_id>', methods=['GET'])
def api_get_lesson(lesson_id):
    """Get a specific lesson content"""
    user_id = get_user_id()
    lesson = get_lesson_by_id(lesson_id)
    
    if not lesson:
        return jsonify({'success': False, 'error': 'Lesson not found'}), 404
    
    # Mark as accessed
    if user_id not in user_progress:
        user_progress[user_id] = {}
    user_progress[user_id][lesson_id] = {'completed': False, 'last_accessed': True}
    
    return jsonify({
        'success': True,
        'lesson': {
            'id': lesson['id'],
            'level': lesson['level'],
            'title': lesson['title'],
            'content': lesson['content']
        }
    })

@app.route('/api/lessons/<lesson_id>/complete', methods=['POST'])
def api_complete_lesson(lesson_id):
    """Mark a lesson as completed"""
    user_id = get_user_id()
    
    if user_id not in user_progress:
        user_progress[user_id] = {}
    user_progress[user_id][lesson_id] = {'completed': True, 'last_accessed': True}
    
    # Add XP
    stats = get_user_stats(user_id)
    stats['total_xp'] += 50
    
    achievements_unlocked = []
    if stats['total_xp'] >= 100:
        if user_id not in user_achievements:
            user_achievements[user_id] = []
        if 'first_100_xp' not in user_achievements[user_id]:
            user_achievements[user_id].append('first_100_xp')
            achievements_unlocked.append(ACHIEVEMENTS['first_100_xp'])
    
    return jsonify({
        'success': True,
        'xpEarned': 50,
        'achievementsUnlocked': achievements_unlocked
    })

# ============== STATS API ==============

@app.route('/api/stats', methods=['GET'])
def api_get_stats():
    """Get user statistics"""
    user_id = get_user_id()
    stats = get_user_stats(user_id)
    
    level = 1 + (stats.get('total_xp', 0) // 500)
    xp_for_next = 500 - (stats.get('total_xp', 0) % 500)
    
    return jsonify({
        'success': True,
        'stats': {
            'totalXp': stats.get('total_xp', 0),
            'currentStreak': stats.get('current_streak', 0),
            'longestStreak': stats.get('longest_streak', 0),
            'wordsLearned': stats.get('words_learned', 0),
            'exercisesCompleted': stats.get('exercises_completed', 0),
            'level': level,
            'xpForNextLevel': xp_for_next
        },
        'achievements': user_achievements.get(user_id, [])
    })

@app.route('/api/stats/xp', methods=['POST'])
def api_add_xp():
    """Add XP to user"""
    user_id = get_user_id()
    data = request.get_json() or {}
    amount = data.get('amount', 10)
    
    stats = get_user_stats(user_id)
    stats['total_xp'] += amount
    
    return jsonify({
        'success': True,
        'totalXp': stats.get('total_xp', 0),
        'level': 1 + (stats.get('total_xp', 0) // 500)
    })

@app.route('/api/stats/exercise', methods=['POST'])
def api_complete_exercise():
    """Record exercise completion"""
    user_id = get_user_id()
    data = request.get_json() or {}
    correct = data.get('correct', True)
    
    stats = get_user_stats(user_id)
    stats['exercises_completed'] += 1
    stats['total_xp'] += 10 if correct else 2
    
    return jsonify({'success': True})

# ============== VOCABULARY API ==============

@app.route('/api/vocabulary', methods=['GET'])
def api_get_vocabulary():
    """Get user's saved vocabulary"""
    user_id = get_user_id()
    vocabulary = user_vocabulary.get(user_id, [])
    
    return jsonify({
        'success': True,
        'vocabulary': vocabulary
    })

@app.route('/api/vocabulary', methods=['POST'])
def api_save_vocabulary():
    """Save a new vocabulary word"""
    user_id = get_user_id()
    data = request.get_json() or {}
    
    word = data.get('word', '').strip()
    translation = data.get('translation', '').strip()
    
    if not word:
        return jsonify({'success': False, 'error': 'Word is required'}), 400
    
    if user_id not in user_vocabulary:
        user_vocabulary[user_id] = []
    
    user_vocabulary[user_id].append({
        'word': word,
        'translation': translation,
        'proficiency': 0
    })
    
    stats = get_user_stats(user_id)
    stats['total_xp'] += 5
    stats['words_learned'] += 1
    
    return jsonify({
        'success': True,
        'message': 'Vocabulary saved'
    })

# ============== ACHIEVEMENTS API ==============

@app.route('/api/achievements', methods=['GET'])
def api_get_achievements():
    """Get all achievements and user's unlocked ones"""
    user_id = get_user_id()
    unlocked = user_achievements.get(user_id, [])
    
    all_achievements = []
    for key, achievement in ACHIEVEMENTS.items():
        all_achievements.append({
            'id': key,
            'name': achievement['name'],
            'description': achievement['description'],
            'icon': achievement['icon'],
            'unlocked': key in unlocked
        })
    
    return jsonify({
        'success': True,
        'achievements': all_achievements
    })

# ============== PRACTICE API ==============

@app.route('/api/practice/flashcards', methods=['GET'])
def api_get_flashcards():
    """Get flashcards for practice"""
    user_id = get_user_id()
    vocabulary = user_vocabulary.get(user_id, [])
    
    cards = sorted(vocabulary, key=lambda x: x.get('proficiency', 0))[:20]
    
    return jsonify({
        'success': True,
        'cards': cards
    })

# ============== HEALTH CHECK ==============

@app.route('/api/health', methods=['GET'])
def health_check():
    """API health check"""
    return jsonify({
        'status': 'healthy',
        'version': '2.0.0',
        'platform': 'vercel'
    })

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        'message': 'English Learning API',
        'version': '2.0.0',
        'docs': '/api/health'
    })

# For Vercel
if __name__ == '__main__':
    app.run(debug=True)
