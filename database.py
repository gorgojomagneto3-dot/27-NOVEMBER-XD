import os
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    """Conecta a PostgreSQL (Render) o SQLite (local)"""
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        # Render PostgreSQL
        return psycopg2.connect(database_url, cursor_factory=RealDictCursor)
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
    
    if os.environ.get('DATABASE_URL'):
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
    
    conn.commit()
    cur.close()
    conn.close()

def save_progress(user_id, lesson_id, completed=False):
    """Guarda el progreso del usuario"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    if os.environ.get('DATABASE_URL'):
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
    
    if os.environ.get('DATABASE_URL'):
        cur.execute('SELECT * FROM user_progress WHERE user_id = %s', (user_id,))
    else:
        cur.execute('SELECT * FROM user_progress WHERE user_id = ?', (user_id,))
    
    progress = cur.fetchall()
    cur.close()
    conn.close()
    
    return [dict(row) for row in progress]
