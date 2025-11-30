import os
from datetime import datetime, date

# Try to import psycopg2, fall back to SQLite only if not available
try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False

def is_postgres():
    """Check if using PostgreSQL"""
    return os.environ.get('DATABASE_URL') and POSTGRES_AVAILABLE

def get_db_connection():
    """Conecta a PostgreSQL (Render) o SQLite (local)"""
    if is_postgres():
        # Render PostgreSQL
        return psycopg2.connect(os.environ.get('DATABASE_URL'), cursor_factory=RealDictCursor)
    else:
        # Local SQLite
        import sqlite3
        conn = sqlite3.connect('progress.db')
        conn.row_factory = sqlite3.Row
        return conn

def init_db():
    """Crea las tablas si no existen"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        # PostgreSQL
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_progress (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(100) NOT NULL,
                lesson_id VARCHAR(20) NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, lesson_id)
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_stats (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(100) UNIQUE NOT NULL,
                total_xp INTEGER DEFAULT 0,
                current_streak INTEGER DEFAULT 0,
                longest_streak INTEGER DEFAULT 0,
                last_activity_date DATE,
                words_learned INTEGER DEFAULT 0,
                exercises_completed INTEGER DEFAULT 0,
                time_spent_minutes INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_vocabulary (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(100) NOT NULL,
                word VARCHAR(100) NOT NULL,
                translation VARCHAR(100),
                proficiency INTEGER DEFAULT 0,
                next_review TIMESTAMP,
                times_correct INTEGER DEFAULT 0,
                times_wrong INTEGER DEFAULT 0,
                UNIQUE(user_id, word)
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(100) NOT NULL,
                achievement_id VARCHAR(50) NOT NULL,
                unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, achievement_id)
            )
        ''')
    else:
        # SQLite
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                lesson_id TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, lesson_id)
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE NOT NULL,
                total_xp INTEGER DEFAULT 0,
                current_streak INTEGER DEFAULT 0,
                longest_streak INTEGER DEFAULT 0,
                last_activity_date DATE,
                words_learned INTEGER DEFAULT 0,
                exercises_completed INTEGER DEFAULT 0,
                time_spent_minutes INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_vocabulary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                word TEXT NOT NULL,
                translation TEXT,
                proficiency INTEGER DEFAULT 0,
                next_review TIMESTAMP,
                times_correct INTEGER DEFAULT 0,
                times_wrong INTEGER DEFAULT 0,
                UNIQUE(user_id, word)
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                achievement_id TEXT NOT NULL,
                unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, achievement_id)
            )
        ''')
    
    conn.commit()
    cur.close()
    conn.close()

def save_progress(user_id, lesson_id, completed=False):
    """Guarda el progreso del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        # PostgreSQL
        cur.execute('''
            INSERT INTO user_progress (user_id, lesson_id, completed, last_accessed)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
            ON CONFLICT (user_id, lesson_id) 
            DO UPDATE SET completed = %s, last_accessed = CURRENT_TIMESTAMP
        ''', (user_id, lesson_id, completed, completed))
    else:
        # SQLite
        cur.execute('''
            INSERT OR REPLACE INTO user_progress (user_id, lesson_id, completed, last_accessed)
            VALUES (?, ?, ?, ?)
        ''', (user_id, lesson_id, 1 if completed else 0, datetime.now()))
    
    conn.commit()
    cur.close()
    conn.close()

def get_progress(user_id):
    """Obtiene el progreso del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        cur.execute('SELECT * FROM user_progress WHERE user_id = %s', (user_id,))
    else:
        cur.execute('SELECT * FROM user_progress WHERE user_id = ?', (user_id,))
    
    progress = cur.fetchall()
    cur.close()
    conn.close()
    
    return [dict(row) for row in progress]

# ============== GAMIFICATION FUNCTIONS ==============

def get_or_create_stats(user_id):
    """Obtiene o crea estadísticas del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        cur.execute('SELECT * FROM user_stats WHERE user_id = %s', (user_id,))
        stats = cur.fetchone()
        if not stats:
            cur.execute('''
                INSERT INTO user_stats (user_id, total_xp, current_streak, longest_streak, last_activity_date, level)
                VALUES (%s, 0, 0, 0, CURRENT_DATE, 1)
                RETURNING *
            ''', (user_id,))
            stats = cur.fetchone()
            conn.commit()
    else:
        cur.execute('SELECT * FROM user_stats WHERE user_id = ?', (user_id,))
        stats = cur.fetchone()
        if not stats:
            cur.execute('''
                INSERT INTO user_stats (user_id, total_xp, current_streak, longest_streak, last_activity_date, level)
                VALUES (?, 0, 0, 0, date('now'), 1)
            ''', (user_id,))
            conn.commit()
            cur.execute('SELECT * FROM user_stats WHERE user_id = ?', (user_id,))
            stats = cur.fetchone()
    
    cur.close()
    conn.close()
    return dict(stats) if stats else None

def add_xp(user_id, xp_amount, update_streak=True):
    """Añade XP y actualiza racha"""
    conn = get_db_connection()
    cur = conn.cursor()
    today = date.today()
    
    # Primero obtener stats actuales
    stats = get_or_create_stats(user_id)
    
    new_streak = stats['current_streak']
    longest = stats['longest_streak']
    
    if update_streak and stats['last_activity_date']:
        last_date = stats['last_activity_date']
        if isinstance(last_date, str):
            last_date = datetime.strptime(last_date, '%Y-%m-%d').date()
        
        days_diff = (today - last_date).days
        if days_diff == 1:
            new_streak += 1
        elif days_diff > 1:
            new_streak = 1
        # Si es el mismo día, mantener racha
        
        if new_streak > longest:
            longest = new_streak
    elif update_streak:
        new_streak = 1
    
    # Calcular nivel (cada 500 XP = 1 nivel)
    new_total_xp = stats['total_xp'] + xp_amount
    new_level = (new_total_xp // 500) + 1
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        cur.execute('''
            UPDATE user_stats 
            SET total_xp = total_xp + %s, 
                current_streak = %s, 
                longest_streak = %s,
                last_activity_date = CURRENT_DATE,
                level = %s
            WHERE user_id = %s
        ''', (xp_amount, new_streak, longest, new_level, user_id))
    else:
        cur.execute('''
            UPDATE user_stats 
            SET total_xp = total_xp + ?, 
                current_streak = ?, 
                longest_streak = ?,
                last_activity_date = date('now'),
                level = ?
            WHERE user_id = ?
        ''', (xp_amount, new_streak, longest, new_level, user_id))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return {'xp_added': xp_amount, 'new_streak': new_streak, 'level': new_level, 'total_xp': new_total_xp}

def increment_exercise(user_id):
    """Incrementa contador de ejercicios completados"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    get_or_create_stats(user_id)
    
    if is_postgres():
        cur.execute('UPDATE user_stats SET exercises_completed = exercises_completed + 1 WHERE user_id = %s', (user_id,))
    else:
        cur.execute('UPDATE user_stats SET exercises_completed = exercises_completed + 1 WHERE user_id = ?', (user_id,))
    
    conn.commit()
    cur.close()
    conn.close()

def save_vocabulary(user_id, word, translation):
    """Guarda una palabra en el vocabulario del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        cur.execute('''
            INSERT INTO user_vocabulary (user_id, word, translation, next_review)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
            ON CONFLICT (user_id, word) DO UPDATE SET translation = %s
        ''', (user_id, word.lower(), translation, translation))
    else:
        cur.execute('''
            INSERT OR REPLACE INTO user_vocabulary (user_id, word, translation, next_review)
            VALUES (?, ?, ?, datetime('now'))
        ''', (user_id, word.lower(), translation))
    
    conn.commit()
    cur.close()
    conn.close()

def get_vocabulary(user_id, for_review=False):
    """Obtiene vocabulario del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if for_review:
        if is_postgres():
            cur.execute('''
                SELECT * FROM user_vocabulary 
                WHERE user_id = %s AND next_review <= CURRENT_TIMESTAMP
                ORDER BY proficiency ASC, next_review ASC
                LIMIT 20
            ''', (user_id,))
        else:
            cur.execute('''
                SELECT * FROM user_vocabulary 
                WHERE user_id = ? AND next_review <= datetime('now')
                ORDER BY proficiency ASC, next_review ASC
                LIMIT 20
            ''', (user_id,))
    else:
        if is_postgres():
            cur.execute('SELECT * FROM user_vocabulary WHERE user_id = %s ORDER BY word', (user_id,))
        else:
            cur.execute('SELECT * FROM user_vocabulary WHERE user_id = ? ORDER BY word', (user_id,))
    
    vocab = cur.fetchall()
    cur.close()
    conn.close()
    
    return [dict(row) for row in vocab]

def update_vocabulary_review(user_id, word, correct):
    """Actualiza el vocabulario después de una revisión (Spaced Repetition)"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Intervalos de repaso en horas: 1, 6, 24, 72, 168 (1 semana), 336 (2 semanas)
    intervals = [1, 6, 24, 72, 168, 336, 720]
    
    if is_postgres():
        cur.execute('SELECT proficiency FROM user_vocabulary WHERE user_id = %s AND word = %s', (user_id, word.lower()))
    else:
        cur.execute('SELECT proficiency FROM user_vocabulary WHERE user_id = ? AND word = ?', (user_id, word.lower()))
    
    result = cur.fetchone()
    if result:
        proficiency = result['proficiency'] if isinstance(result, dict) else result[0]
        
        if correct:
            new_proficiency = min(proficiency + 1, len(intervals) - 1)
            col_correct = 'times_correct'
        else:
            new_proficiency = max(proficiency - 1, 0)
            col_correct = 'times_wrong'
        
        hours = intervals[new_proficiency]
        
        if is_postgres():
            cur.execute(f'''
                UPDATE user_vocabulary 
                SET proficiency = %s, 
                    next_review = CURRENT_TIMESTAMP + INTERVAL '{hours} hours',
                    {col_correct} = {col_correct} + 1
                WHERE user_id = %s AND word = %s
            ''', (new_proficiency, user_id, word.lower()))
        else:
            cur.execute(f'''
                UPDATE user_vocabulary 
                SET proficiency = ?, 
                    next_review = datetime('now', '+{hours} hours'),
                    {col_correct} = {col_correct} + 1
                WHERE user_id = ? AND word = ?
            ''', (new_proficiency, user_id, word.lower()))
    
    conn.commit()
    cur.close()
    conn.close()

def unlock_achievement(user_id, achievement_id):
    """Desbloquea un logro"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        if is_postgres():
            cur.execute('''
                INSERT INTO achievements (user_id, achievement_id)
                VALUES (%s, %s)
                ON CONFLICT (user_id, achievement_id) DO NOTHING
            ''', (user_id, achievement_id))
        else:
            cur.execute('''
                INSERT OR IGNORE INTO achievements (user_id, achievement_id)
                VALUES (?, ?)
            ''', (user_id, achievement_id))
        
        conn.commit()
        return True
    except:
        return False
    finally:
        cur.close()
        conn.close()

def get_achievements(user_id):
    """Obtiene logros del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if is_postgres():
        cur.execute('SELECT * FROM achievements WHERE user_id = %s', (user_id,))
    else:
        cur.execute('SELECT * FROM achievements WHERE user_id = ?', (user_id,))
    
    achievements = cur.fetchall()
    cur.close()
    conn.close()
    
    return [dict(row) for row in achievements]

# Lista de logros disponibles
ACHIEVEMENTS = {
    'first_lesson': {'name': '🎯 Primera Lección', 'desc': 'Completa tu primera lección', 'xp': 50},
    'streak_3': {'name': '🔥 Racha de 3', 'desc': '3 días seguidos estudiando', 'xp': 100},
    'streak_7': {'name': '🔥 Semana Perfecta', 'desc': '7 días seguidos estudiando', 'xp': 200},
    'streak_30': {'name': '🏆 Mes Dedicado', 'desc': '30 días seguidos estudiando', 'xp': 500},
    'vocab_50': {'name': '📚 Vocabulario Básico', 'desc': 'Aprende 50 palabras', 'xp': 150},
    'vocab_100': {'name': '📖 Vocabulario Avanzado', 'desc': 'Aprende 100 palabras', 'xp': 300},
    'exercises_100': {'name': '💪 Ejercitador', 'desc': 'Completa 100 ejercicios', 'xp': 200},
    'level_5': {'name': '⭐ Nivel 5', 'desc': 'Alcanza el nivel 5', 'xp': 250},
    'level_10': {'name': '🌟 Nivel 10', 'desc': 'Alcanza el nivel 10', 'xp': 500},
    'basic_complete': {'name': '🎓 Básico Completo', 'desc': 'Completa todos los niveles básicos', 'xp': 1000},
}
