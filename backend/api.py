"""
English Learning App - Backend API
Flask REST API for the English Learning Application
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
from database import (
    init_db, save_progress, get_progress, 
    get_or_create_stats, add_xp, increment_exercise,
    save_vocabulary, get_vocabulary, update_vocabulary_review,
    unlock_achievement, get_achievements, ACHIEVEMENTS
)
from content import get_all_lessons, get_lesson_by_id

app = Flask(__name__)
CORS(app, origins=['http://localhost:4321', 'http://localhost:4322', 'http://localhost:3000', 'http://127.0.0.1:4321', 'http://127.0.0.1:4322'])
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize database
init_db()

def get_user_id():
    """Get or create user ID from header or generate new one"""
    user_id = request.headers.get('X-User-ID')
    if not user_id:
        user_id = request.cookies.get('user_id', str(uuid.uuid4()))
    return user_id

# ============== LESSONS API ==============

@app.route('/api/lessons', methods=['GET'])
def api_get_lessons():
    """Get all lessons with metadata"""
    user_id = get_user_id()
    lessons = get_all_lessons()
    
    # Get all progress for this user
    all_progress = get_progress(user_id)
    # Create a dict for quick lookup by lesson_id
    progress_by_lesson = {p.get('lesson_id'): p for p in all_progress}
    
    # Add progress info for each lesson
    lessons_with_progress = []
    for lesson in lessons:
        progress = progress_by_lesson.get(lesson['id'])
        lessons_with_progress.append({
            'id': lesson['id'],
            'level': lesson['level'],
            'title': lesson['title'],
            'completed': progress.get('completed', False) if progress else False,
            'lastAccessed': progress.get('last_accessed') if progress else None
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
    save_progress(user_id, lesson_id, completed=False)
    
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
    save_progress(user_id, lesson_id, completed=True)
    add_xp(user_id, 50)  # 50 XP per lesson
    
    # Check for achievements
    stats = get_or_create_stats(user_id)
    
    achievements_unlocked = []
    if stats['total_xp'] >= 100:
        if unlock_achievement(user_id, 'first_100_xp'):
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
    stats = get_or_create_stats(user_id)
    achievements = get_achievements(user_id)
    
    # Calculate level from XP
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
        'achievements': achievements
    })

@app.route('/api/stats/xp', methods=['POST'])
def api_add_xp():
    """Add XP to user"""
    user_id = get_user_id()
    data = request.get_json() or {}
    amount = data.get('amount', 10)
    
    add_xp(user_id, amount)
    stats = get_or_create_stats(user_id)
    
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
    
    increment_exercise(user_id, correct)
    add_xp(user_id, 10 if correct else 2)
    
    return jsonify({'success': True})

# ============== VOCABULARY API ==============

@app.route('/api/vocabulary', methods=['GET'])
def api_get_vocabulary():
    """Get user's saved vocabulary"""
    user_id = get_user_id()
    vocabulary = get_vocabulary(user_id)
    
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
    
    save_vocabulary(user_id, word, translation)
    add_xp(user_id, 5)  # 5 XP for saving vocabulary
    
    return jsonify({
        'success': True,
        'message': 'Vocabulary saved'
    })

@app.route('/api/vocabulary/<word>/review', methods=['POST'])
def api_review_vocabulary(word):
    """Update vocabulary review status"""
    user_id = get_user_id()
    data = request.get_json() or {}
    correct = data.get('correct', True)
    
    update_vocabulary_review(user_id, word, correct)
    
    return jsonify({'success': True})

# ============== ACHIEVEMENTS API ==============

@app.route('/api/achievements', methods=['GET'])
def api_get_achievements():
    """Get all achievements and user's unlocked ones"""
    user_id = get_user_id()
    user_achievements = get_achievements(user_id)
    
    all_achievements = []
    for key, achievement in ACHIEVEMENTS.items():
        unlocked = any(a.get('achievement_id') == key for a in user_achievements)
        all_achievements.append({
            'id': key,
            'name': achievement['name'],
            'description': achievement['description'],
            'icon': achievement['icon'],
            'unlocked': unlocked
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
    vocabulary = get_vocabulary(user_id)
    
    # Sort by due for review
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
        'architecture': 'astro-flask'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
