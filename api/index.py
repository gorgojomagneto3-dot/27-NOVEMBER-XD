"""
English Learning App - Backend API for Vercel
Flask REST API - Simplified version for serverless
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
CORS(app, origins='*')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

# ============== IN-MEMORY STORAGE ==============
user_progress = {}
user_stats = {}

ACHIEVEMENTS = {
    'first_lesson': {'name': 'First Steps', 'description': 'Complete your first lesson', 'icon': '🎯'},
    'first_100_xp': {'name': 'Century', 'description': 'Earn 100 XP', 'icon': '💯'},
}

def get_user_id():
    user_id = request.headers.get('X-User-ID')
    if not user_id:
        user_id = str(uuid.uuid4())
    return user_id

def get_user_stats_data(user_id):
    if user_id not in user_stats:
        user_stats[user_id] = {
            'total_xp': 0,
            'current_streak': 0,
            'longest_streak': 0,
            'words_learned': 0,
            'exercises_completed': 0
        }
    return user_stats[user_id]

# ============== LESSONS DATA ==============
LESSONS = [
    {"id": "b1", "level": "Básico", "title": "Básico 01 - Introductions & BE verb"},
    {"id": "b2", "level": "Básico", "title": "Básico 02 - Present Continuous"},
    {"id": "b3", "level": "Básico", "title": "Básico 03 - Time & Schedules"},
    {"id": "b4", "level": "Básico", "title": "Básico 04 - Shopping & Jobs"},
    {"id": "b5", "level": "Básico", "title": "Básico 05 - Descriptions & Food"},
    {"id": "b6", "level": "Básico", "title": "Básico 06 - Past Simple"},
    {"id": "b7", "level": "Básico", "title": "Básico 07 - City Life"},
    {"id": "b8", "level": "Básico", "title": "Básico 08 - Past Continuous"},
    {"id": "b9", "level": "Básico", "title": "Básico 09 - Present Perfect"},
    {"id": "b10", "level": "Básico", "title": "Básico 10 - Future Tenses"},
    {"id": "b11", "level": "Básico", "title": "Básico 11 - Celebrations"},
    {"id": "b12", "level": "Básico", "title": "Básico 12 - Review"},
    {"id": "int1", "level": "Intermedio", "title": "Intermedio 01 - Relative Clauses"},
    {"id": "int2", "level": "Intermedio", "title": "Intermedio 02 - Dynamic Verbs"},
    {"id": "int3", "level": "Intermedio", "title": "Intermedio 03 - Creativity"},
    {"id": "int4", "level": "Intermedio", "title": "Intermedio 04 - Conditionals"},
    {"id": "int5", "level": "Intermedio", "title": "Intermedio 05 - Brainpower"},
    {"id": "int6", "level": "Intermedio", "title": "Intermedio 06 - Storytelling"},
    {"id": "int7", "level": "Intermedio", "title": "Intermedio 07 - Design"},
    {"id": "int8", "level": "Intermedio", "title": "Intermedio 08 - Science"},
    {"id": "int9", "level": "Intermedio", "title": "Intermedio 09 - Social Networks"},
    {"id": "int10", "level": "Intermedio", "title": "Intermedio 10 - Reinvention"},
    {"id": "int11", "level": "Intermedio", "title": "Intermedio 11 - Rules & Luck"},
    {"id": "int12", "level": "Intermedio", "title": "Intermedio 12 - Value for Money"},
]

def get_lesson_content(lesson_id):
    """Return HTML content for a lesson"""
    content = f"""
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">📚 Lesson {lesson_id.upper()}</h1>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎯 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Master key vocabulary for this unit</li>
                <li>Practice essential grammar structures</li>
                <li>Develop listening and speaking skills</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Vocabulary</h2>
            <ul class="space-y-3">
                <li class="flex items-center gap-2">
                    <span class="text-green-400">Hello</span> → Hola 🔊
                </li>
                <li class="flex items-center gap-2">
                    <span class="text-green-400">Goodbye</span> → Adiós 🔊
                </li>
                <li class="flex items-center gap-2">
                    <span class="text-green-400">Thank you</span> → Gracias 🔊
                </li>
                <li class="flex items-center gap-2">
                    <span class="text-green-400">Please</span> → Por favor 🔊
                </li>
                <li class="flex items-center gap-2">
                    <span class="text-green-400">Yes</span> → Sí 🔊
                </li>
                <li class="flex items-center gap-2">
                    <span class="text-green-400">No</span> → No 🔊
                </li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Grammar</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-xl text-yellow-400 mb-2">Verb TO BE</h3>
                <ul class="space-y-2">
                    <li><strong>I am</strong> → Yo soy/estoy</li>
                    <li><strong>You are</strong> → Tú eres/estás</li>
                    <li><strong>He/She is</strong> → Él/Ella es/está</li>
                    <li><strong>We are</strong> → Nosotros somos/estamos</li>
                    <li><strong>They are</strong> → Ellos son/están</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice</h2>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ a student. (am)</li>
                <li>She _____ from Peru. (is)</li>
                <li>They _____ happy. (are)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """
    return content

# ============== API ROUTES ==============

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'version': '2.0.0',
        'platform': 'vercel'
    })

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'English Learning API',
        'version': '2.0.0',
        'endpoints': ['/api/health', '/api/lessons', '/api/stats']
    })

@app.route('/api/lessons', methods=['GET'])
def api_get_lessons():
    user_id = get_user_id()
    progress = user_progress.get(user_id, {})
    
    lessons_with_progress = []
    for lesson in LESSONS:
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
    user_id = get_user_id()
    lesson_meta = next((l for l in LESSONS if l['id'] == lesson_id), None)
    
    if not lesson_meta:
        return jsonify({'success': False, 'error': 'Lesson not found'}), 404
    
    if user_id not in user_progress:
        user_progress[user_id] = {}
    user_progress[user_id][lesson_id] = {'completed': False, 'last_accessed': True}
    
    return jsonify({
        'success': True,
        'lesson': {
            'id': lesson_id,
            'level': lesson_meta['level'],
            'title': lesson_meta['title'],
            'content': get_lesson_content(lesson_id)
        }
    })

@app.route('/api/lessons/<lesson_id>/complete', methods=['POST'])
def api_complete_lesson(lesson_id):
    user_id = get_user_id()
    
    if user_id not in user_progress:
        user_progress[user_id] = {}
    user_progress[user_id][lesson_id] = {'completed': True, 'last_accessed': True}
    
    stats = get_user_stats_data(user_id)
    stats['total_xp'] += 50
    
    return jsonify({
        'success': True,
        'xpEarned': 50,
        'achievementsUnlocked': []
    })

@app.route('/api/stats', methods=['GET'])
def api_get_stats():
    user_id = get_user_id()
    stats = get_user_stats_data(user_id)
    
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
        'achievements': []
    })

@app.route('/api/stats/exercise', methods=['POST'])
def api_complete_exercise():
    user_id = get_user_id()
    data = request.get_json() or {}
    correct = data.get('correct', True)
    
    stats = get_user_stats_data(user_id)
    stats['exercises_completed'] += 1
    stats['total_xp'] += 10 if correct else 2
    
    return jsonify({'success': True})

@app.route('/api/vocabulary', methods=['GET'])
def api_get_vocabulary():
    return jsonify({
        'success': True,
        'vocabulary': []
    })

@app.route('/api/achievements', methods=['GET'])
def api_get_achievements():
    return jsonify({
        'success': True,
        'achievements': list(ACHIEVEMENTS.values())
    })

@app.route('/api/practice/flashcards', methods=['GET'])
def api_get_flashcards():
    return jsonify({
        'success': True,
        'cards': []
    })

# For Vercel
if __name__ == '__main__':
    app.run(debug=True)
