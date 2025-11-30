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

# ============== LESSON CONTENT ==============
LESSON_CONTENT = {
    "b1": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎯 BASIC 01 - Introductions & BE Verb</h1>
        <p class="text-white/60 mb-6">CEFR Level: A1 | ICPNA: Básico 1</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Greet and introduce yourself using subject pronouns</li>
                <li>Ask and answer yes/no questions about personal information</li>
                <li>Talk about favorite TV shows, sports, and music</li>
                <li>Describe places and cities using adjectives</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Subject Pronouns</h2>
            <div class="bg-white/10 p-4 rounded-lg mb-4">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">I</strong> → Yo → <em>I am a student.</em></li>
                    <li><strong class="text-green-400">You</strong> → Tú/Usted → <em>You are my friend.</em></li>
                    <li><strong class="text-green-400">He</strong> → Él → <em>He is from Peru.</em></li>
                    <li><strong class="text-green-400">She</strong> → Ella → <em>She is a teacher.</em></li>
                    <li><strong class="text-green-400">It</strong> → Eso → <em>It is a beautiful city.</em></li>
                    <li><strong class="text-green-400">We</strong> → Nosotros → <em>We are classmates.</em></li>
                    <li><strong class="text-green-400">They</strong> → Ellos/Ellas → <em>They are friends.</em></li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Possessive Adjectives</h2>
            <div class="bg-white/10 p-4 rounded-lg mb-4">
                <ul class="space-y-2">
                    <li><strong class="text-yellow-400">my</strong> (mi) → My name is Carlos.</li>
                    <li><strong class="text-yellow-400">your</strong> (tu) → What's your name?</li>
                    <li><strong class="text-yellow-400">his</strong> (su - de él) → His favorite sport is soccer.</li>
                    <li><strong class="text-yellow-400">her</strong> (su - de ella) → Her favorite singer is Adele.</li>
                    <li><strong class="text-yellow-400">its</strong> (su - de cosa) → Its capital is Lima.</li>
                    <li><strong class="text-yellow-400">our</strong> (nuestro) → Our teacher is great.</li>
                    <li><strong class="text-yellow-400">their</strong> (su - de ellos) → Their house is big.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Verb TO BE - Contractions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>I am</strong> → I'm → I'm not</li>
                    <li><strong>You are</strong> → You're → You aren't</li>
                    <li><strong>He is</strong> → He's → He isn't</li>
                    <li><strong>She is</strong> → She's → She isn't</li>
                    <li><strong>It is</strong> → It's → It isn't</li>
                    <li><strong>We are</strong> → We're → We aren't</li>
                    <li><strong>They are</strong> → They're → They aren't</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🗣️ Greetings & Introductions</h2>
            <div class="bg-white/10 p-4 rounded-lg mb-4">
                <h3 class="text-lg text-yellow-400 mb-2">Formal:</h3>
                <ul class="space-y-1">
                    <li>Hello, I'm [name]. Nice to meet you. → Hola</li>
                    <li>Good morning/afternoon/evening. → Buenos días/tardes/noches</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Informal:</h3>
                <ul class="space-y-1">
                    <li>Hi! I'm [name]. → ¡Hola!</li>
                    <li>Hey, what's up? → ¿Qué tal?</li>
                    <li>Nice to meet you! → ¡Mucho gusto!</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">❓ Personal Information Questions</h2>
            <ul class="space-y-2 text-white/80">
                <li><strong>What's your name?</strong> → My name is _______.</li>
                <li><strong>Where are you from?</strong> → I'm from Lima, Peru.</li>
                <li><strong>How old are you?</strong> → I'm _______ years old.</li>
                <li><strong>What do you do?</strong> → I'm a student.</li>
                <li><strong>What's your favorite sport?</strong> → My favorite sport is _______.</li>
                <li><strong>What's your favorite music?</strong> → My favorite music is _______.</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🌍 Countries & Nationalities</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>Peru</strong> → Peruvian → Spanish</li>
                    <li><strong>United States</strong> → American → English</li>
                    <li><strong>Brazil</strong> → Brazilian → Portuguese</li>
                    <li><strong>France</strong> → French → French</li>
                    <li><strong>Japan</strong> → Japanese → Japanese</li>
                    <li><strong>Mexico</strong> → Mexican → Spanish</li>
                    <li><strong>United Kingdom</strong> → British → English</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with the correct possessive adjective:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I have a dog. _____ name is Max. (My)</li>
                <li>She is Maria. _____ last name is Garcia. (Her)</li>
                <li>We are students. _____ school is ICPNA. (Our)</li>
                <li>They are from Brazil. _____ language is Portuguese. (Their)</li>
                <li>He is my brother. _____ favorite sport is basketball. (His)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete with the correct form of BE:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>_____ you a teacher? → Yes, I am. (Are)</li>
                <li>_____ she from Mexico? → No, she isn't. (Is)</li>
                <li>_____ they your friends? → Yes, they are. (Are)</li>
                <li>_____ he married? → No, he isn't. (Is)</li>
                <li>_____ I late for class? → No, you aren't. (Am)</li>
            </ol>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📍 Prepositions of Place</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">IN</strong> → countries, cities: I live <em>in</em> Peru.</li>
                    <li><strong class="text-green-400">ON</strong> → streets, floors: I live <em>on</em> Main Street.</li>
                    <li><strong class="text-green-400">AT</strong> → specific addresses: I'm <em>at</em> school.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🏙️ Describing Places</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Positive:</h3>
                <p>beautiful, big, modern, clean, safe, interesting, quiet, friendly, famous</p>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Negative:</h3>
                <p>ugly, small, old, dirty, dangerous, boring, noisy, crowded, expensive</p>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Examples:</h3>
                <ul class="space-y-1">
                    <li>Lima is big <strong>and</strong> modern.</li>
                    <li>The hotel is nice <strong>but</strong> expensive.</li>
                </ul>
            </div>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b2": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎯 BASIC 02 - Present Continuous</h1>
        <p class="text-white/60 mb-6">CEFR Level: A1 | ICPNA: Básico 2</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Describe what you're doing right now</li>
                <li>Tell how you are feeling</li>
                <li>Talk about school subjects and activities</li>
                <li>Use present continuous tense correctly</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Present Continuous Structure</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + BE + Verb-ING</strong></p>
                <ul class="space-y-2">
                    <li>I <strong>am studying</strong> English. → Estoy estudiando inglés.</li>
                    <li>You <strong>are reading</strong> a book. → Estás leyendo un libro.</li>
                    <li>He <strong>is working</strong> today. → Él está trabajando hoy.</li>
                    <li>She <strong>is cooking</strong> dinner. → Ella está cocinando la cena.</li>
                    <li>We <strong>are learning</strong> grammar. → Estamos aprendiendo gramática.</li>
                    <li>They <strong>are playing</strong> soccer. → Están jugando fútbol.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Vocabulary: Activities</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">texting</strong> → enviando mensajes</li>
                    <li><strong class="text-green-400">playing soccer</strong> → jugando fútbol</li>
                    <li><strong class="text-green-400">eating</strong> → comiendo</li>
                    <li><strong class="text-green-400">reading</strong> → leyendo</li>
                    <li><strong class="text-green-400">drinking coffee</strong> → tomando café</li>
                    <li><strong class="text-green-400">exercising</strong> → haciendo ejercicio</li>
                    <li><strong class="text-green-400">talking on the phone</strong> → hablando por teléfono</li>
                    <li><strong class="text-green-400">studying</strong> → estudiando</li>
                    <li><strong class="text-green-400">watching TV</strong> → viendo TV</li>
                    <li><strong class="text-green-400">sleeping</strong> → durmiendo</li>
                    <li><strong class="text-green-400">listening to music</strong> → escuchando música</li>
                    <li><strong class="text-green-400">shopping</strong> → comprando</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📍 Places</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-yellow-400">cafeteria</strong> → cafetería</li>
                    <li><strong class="text-yellow-400">outside</strong> → afuera</li>
                    <li><strong class="text-yellow-400">gym</strong> → gimnasio</li>
                    <li><strong class="text-yellow-400">classroom</strong> → salón de clases</li>
                    <li><strong class="text-yellow-400">library</strong> → biblioteca</li>
                    <li><strong class="text-yellow-400">office</strong> → oficina</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🗣️ Useful Expressions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>How are you doing today?</strong> → Fine, thanks. How about you?</li>
                    <li><strong>What are you doing?</strong> → I'm studying English.</li>
                    <li><strong>Where are you going?</strong> → I'm going to school.</li>
                    <li><strong>Who are you talking to?</strong> → I'm talking to my friend.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">❓ Questions in Present Continuous</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>BE + Subject + Verb-ING?</strong></p>
                <ul class="space-y-2">
                    <li><strong>Are you studying?</strong> → Yes, I am. / No, I'm not.</li>
                    <li><strong>Is she working?</strong> → Yes, she is. / No, she isn't.</li>
                    <li><strong>Are they playing?</strong> → Yes, they are. / No, they aren't.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Spelling Rules for -ING</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>Most verbs:</strong> add -ing → work<em>ing</em>, study<em>ing</em></li>
                    <li><strong>Verbs ending in -e:</strong> drop e, add -ing → mak<em>ing</em>, writ<em>ing</em></li>
                    <li><strong>Short verbs (CVC):</strong> double consonant → run<em>ning</em>, sit<em>ting</em></li>
                    <li><strong>Verbs ending in -ie:</strong> change to y → ly<em>ing</em>, dy<em>ing</em></li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with Present Continuous:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ (study) English right now. (am studying)</li>
                <li>She _____ (read) a book. (is reading)</li>
                <li>They _____ (play) soccer in the park. (are playing)</li>
                <li>We _____ (watch) a movie. (are watching)</li>
                <li>He _____ (eat) lunch. (is eating)</li>
                <li>The children _____ (run) outside. (are running)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Make questions:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>_____ you _____ (work) today? (Are/working)</li>
                <li>_____ she _____ (study) for the exam? (Is/studying)</li>
                <li>What _____ they _____ (do)? (are/doing)</li>
            </ol>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">😊 Feelings & Emotions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">happy</strong> → feliz</li>
                    <li><strong class="text-green-400">sad</strong> → triste</li>
                    <li><strong class="text-green-400">tired</strong> → cansado/a</li>
                    <li><strong class="text-green-400">hungry</strong> → hambriento/a</li>
                    <li><strong class="text-green-400">thirsty</strong> → sediento/a</li>
                    <li><strong class="text-green-400">excited</strong> → emocionado/a</li>
                    <li><strong class="text-green-400">bored</strong> → aburrido/a</li>
                    <li><strong class="text-green-400">nervous</strong> → nervioso/a</li>
                </ul>
                <p class="mt-4"><strong>How are you feeling?</strong> → I'm feeling happy/tired/excited.</p>
            </div>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b3": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎯 BASIC 03 - Time & Schedules</h1>
        <p class="text-white/60 mb-6">CEFR Level: A1 | ICPNA: Básico 3</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Tell time in English</li>
                <li>Talk about daily routines</li>
                <li>Use frequency adverbs</li>
                <li>Describe schedules and habits</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🕐 Telling Time</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>What time is it?</strong> → ¿Qué hora es?</li>
                    <li>It's <strong>one o'clock</strong> → Es la una</li>
                    <li>It's <strong>two fifteen</strong> / quarter past two → Son las dos y cuarto</li>
                    <li>It's <strong>three thirty</strong> / half past three → Son las tres y media</li>
                    <li>It's <strong>four forty-five</strong> / quarter to five → Son las cinco menos cuarto</li>
                    <li>It's <strong>noon</strong> → Es mediodía</li>
                    <li>It's <strong>midnight</strong> → Es medianoche</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📅 Days of the Week</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">Monday</strong> → lunes</li>
                    <li><strong class="text-green-400">Tuesday</strong> → martes</li>
                    <li><strong class="text-green-400">Wednesday</strong> → miércoles</li>
                    <li><strong class="text-green-400">Thursday</strong> → jueves</li>
                    <li><strong class="text-green-400">Friday</strong> → viernes</li>
                    <li><strong class="text-green-400">Saturday</strong> → sábado</li>
                    <li><strong class="text-green-400">Sunday</strong> → domingo</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Simple Present for Routines</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3">Use Simple Present for habits and routines:</p>
                <ul class="space-y-2">
                    <li>I <strong>wake up</strong> at 7:00. → Me despierto a las 7:00.</li>
                    <li>She <strong>goes</strong> to work at 8:30. → Ella va al trabajo a las 8:30.</li>
                    <li>We <strong>have</strong> lunch at noon. → Almorzamos al mediodía.</li>
                    <li>He <strong>watches</strong> TV at night. → Él ve TV por la noche.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🔄 Frequency Adverbs</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">always</strong> (100%) → siempre</li>
                    <li><strong class="text-green-400">usually</strong> (80%) → usualmente</li>
                    <li><strong class="text-green-400">often</strong> (60%) → a menudo</li>
                    <li><strong class="text-green-400">sometimes</strong> (40%) → a veces</li>
                    <li><strong class="text-green-400">rarely</strong> (20%) → raramente</li>
                    <li><strong class="text-green-400">never</strong> (0%) → nunca</li>
                </ul>
                <p class="mt-4 text-yellow-400">Position: Subject + Adverb + Verb</p>
                <ul class="mt-2 space-y-1">
                    <li>I <em>always</em> eat breakfast.</li>
                    <li>She <em>usually</em> arrives early.</li>
                    <li>They <em>never</em> watch TV.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Daily Routine Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>wake up</strong> → despertarse</li>
                    <li><strong>get up</strong> → levantarse</li>
                    <li><strong>take a shower</strong> → ducharse</li>
                    <li><strong>brush teeth</strong> → cepillarse los dientes</li>
                    <li><strong>get dressed</strong> → vestirse</li>
                    <li><strong>have breakfast</strong> → desayunar</li>
                    <li><strong>go to work/school</strong> → ir al trabajo/escuela</li>
                    <li><strong>have lunch</strong> → almorzar</li>
                    <li><strong>come home</strong> → llegar a casa</li>
                    <li><strong>have dinner</strong> → cenar</li>
                    <li><strong>go to bed</strong> → ir a la cama</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with the correct frequency adverb:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ wake up at 6 AM. (100%) (always)</li>
                <li>She _____ drinks coffee for breakfast. (80%) (usually)</li>
                <li>They _____ go to the gym. (40%) (sometimes)</li>
                <li>He _____ eats fast food. (0%) (never)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b4": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎯 BASIC 04 - Shopping & Jobs</h1>
        <p class="text-white/60 mb-6">CEFR Level: A1 | ICPNA: Básico 4</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Talk about jobs and occupations</li>
                <li>Use "there is/there are" correctly</li>
                <li>Shop for clothing and ask prices</li>
                <li>Describe your home and possessions</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">💼 Jobs & Occupations</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">teacher</strong> → profesor/a</li>
                    <li><strong class="text-green-400">doctor</strong> → doctor/a</li>
                    <li><strong class="text-green-400">engineer</strong> → ingeniero/a</li>
                    <li><strong class="text-green-400">lawyer</strong> → abogado/a</li>
                    <li><strong class="text-green-400">nurse</strong> → enfermero/a</li>
                    <li><strong class="text-green-400">accountant</strong> → contador/a</li>
                    <li><strong class="text-green-400">chef</strong> → chef</li>
                    <li><strong class="text-green-400">waiter/waitress</strong> → mesero/a</li>
                    <li><strong class="text-green-400">police officer</strong> → policía</li>
                    <li><strong class="text-green-400">firefighter</strong> → bombero/a</li>
                </ul>
                <p class="mt-4"><strong>What do you do?</strong> → I'm a/an [job].</p>
                <p><strong>Where do you work?</strong> → I work at/in [place].</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 There is / There are</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Singular: There is (There's)</strong></p>
                <ul class="space-y-1 mb-4">
                    <li>There <strong>is</strong> a book on the table.</li>
                    <li>There <strong>isn't</strong> a window in this room.</li>
                    <li><strong>Is there</strong> a bathroom? → Yes, there is. / No, there isn't.</li>
                </ul>
                <p class="text-yellow-400 mb-3"><strong>Plural: There are</strong></p>
                <ul class="space-y-1">
                    <li>There <strong>are</strong> three bedrooms in my house.</li>
                    <li>There <strong>aren't</strong> any chairs in the kitchen.</li>
                    <li><strong>Are there</strong> any students? → Yes, there are. / No, there aren't.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🏠 Rooms & Furniture</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Rooms:</h3>
                <p>bedroom, living room, kitchen, bathroom, dining room, garage</p>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Furniture:</h3>
                <ul class="space-y-1">
                    <li><strong>bed</strong> → cama</li>
                    <li><strong>sofa/couch</strong> → sofá</li>
                    <li><strong>table</strong> → mesa</li>
                    <li><strong>chair</strong> → silla</li>
                    <li><strong>desk</strong> → escritorio</li>
                    <li><strong>lamp</strong> → lámpara</li>
                    <li><strong>closet/wardrobe</strong> → armario</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">👕 Shopping for Clothes</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Clothing:</h3>
                <ul class="space-y-1">
                    <li><strong>shirt</strong> → camisa | <strong>T-shirt</strong> → camiseta</li>
                    <li><strong>pants/trousers</strong> → pantalones | <strong>jeans</strong> → jeans</li>
                    <li><strong>dress</strong> → vestido | <strong>skirt</strong> → falda</li>
                    <li><strong>shoes</strong> → zapatos | <strong>sneakers</strong> → zapatillas</li>
                    <li><strong>jacket</strong> → chaqueta | <strong>coat</strong> → abrigo</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Shopping Expressions:</h3>
                <ul class="space-y-1">
                    <li><strong>How much is this?</strong> → ¿Cuánto cuesta esto?</li>
                    <li><strong>How much are these?</strong> → ¿Cuánto cuestan estos?</li>
                    <li><strong>Can I try this on?</strong> → ¿Puedo probármelo?</li>
                    <li><strong>Do you have this in size...?</strong> → ¿Tiene esto en talla...?</li>
                    <li><strong>I'll take it.</strong> → Me lo llevo.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <ol class="list-decimal pl-6 space-y-3">
                <li>_____ there a bathroom in your house? (Is)</li>
                <li>There _____ three bedrooms upstairs. (are)</li>
                <li>How much _____ this shirt? (is)</li>
                <li>There _____ any chairs in the room. (aren't)</li>
                <li>_____ do you do? I'm a teacher. (What)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b5": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎯 BASIC 05 - Descriptions & Food</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2 | ICPNA: Básico 5</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Describe people's physical appearance</li>
                <li>Talk about food and meals</li>
                <li>Use adjectives to describe personality</li>
                <li>Order food in a restaurant</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">👤 Physical Descriptions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Height & Build:</h3>
                <ul class="space-y-1">
                    <li><strong>tall</strong> / <strong>short</strong> → alto/a / bajo/a</li>
                    <li><strong>thin/slim</strong> / <strong>heavy/overweight</strong> → delgado/a / gordo/a</li>
                    <li><strong>average height</strong> → estatura promedio</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Hair:</h3>
                <ul class="space-y-1">
                    <li><strong>long/short</strong> hair → cabello largo/corto</li>
                    <li><strong>straight/curly/wavy</strong> → lacio/rizado/ondulado</li>
                    <li><strong>blonde/brown/black/red</strong> → rubio/castaño/negro/rojo</li>
                    <li><strong>bald</strong> → calvo</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Eyes:</h3>
                <p>blue, green, brown, hazel, black eyes</p>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Other features:</h3>
                <ul class="space-y-1">
                    <li><strong>beard</strong> → barba | <strong>mustache</strong> → bigote</li>
                    <li><strong>glasses</strong> → lentes | <strong>freckles</strong> → pecas</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">😊 Personality Adjectives</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">friendly</strong> → amigable | <strong class="text-red-400">unfriendly</strong> → antipático</li>
                    <li><strong class="text-green-400">funny</strong> → gracioso | <strong class="text-red-400">serious</strong> → serio</li>
                    <li><strong class="text-green-400">kind</strong> → amable | <strong class="text-red-400">mean</strong> → malo</li>
                    <li><strong class="text-green-400">smart/intelligent</strong> → inteligente</li>
                    <li><strong class="text-green-400">hardworking</strong> → trabajador | <strong class="text-red-400">lazy</strong> → perezoso</li>
                    <li><strong class="text-green-400">outgoing</strong> → extrovertido | <strong class="text-red-400">shy</strong> → tímido</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🍽️ Food & Meals</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Meals:</h3>
                <p><strong>breakfast</strong> (desayuno), <strong>lunch</strong> (almuerzo), <strong>dinner</strong> (cena), <strong>snack</strong> (merienda)</p>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Food categories:</h3>
                <ul class="space-y-1">
                    <li><strong>Fruits:</strong> apple, banana, orange, grape, strawberry</li>
                    <li><strong>Vegetables:</strong> tomato, potato, carrot, onion, lettuce</li>
                    <li><strong>Meat:</strong> chicken, beef, pork, fish</li>
                    <li><strong>Dairy:</strong> milk, cheese, yogurt, butter</li>
                    <li><strong>Grains:</strong> bread, rice, pasta, cereal</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Tastes:</h3>
                <p><strong>sweet</strong> (dulce), <strong>salty</strong> (salado), <strong>spicy</strong> (picante), <strong>sour</strong> (ácido), <strong>bitter</strong> (amargo)</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🍴 Ordering Food</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>Waiter:</strong> Are you ready to order?</li>
                    <li><strong>Customer:</strong> Yes, I'd like the chicken, please.</li>
                    <li><strong>Waiter:</strong> Anything to drink?</li>
                    <li><strong>Customer:</strong> I'll have a soda, please.</li>
                    <li><strong>Customer:</strong> Can I have the bill/check, please?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <ol class="list-decimal pl-6 space-y-3">
                <li>She has long _____ hair. (straight/curly/wavy)</li>
                <li>He is very _____. He always helps people. (kind)</li>
                <li>I'd _____ the fish, please. (like)</li>
                <li>My father is _____. He doesn't have hair. (bald)</li>
                <li>This soup is too _____! I need water. (spicy)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b6": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎯 BASIC 06 - Past Simple</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2 | ICPNA: Básico 6</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Talk about past events and experiences</li>
                <li>Use regular and irregular verbs in past tense</li>
                <li>Form questions and negatives in past simple</li>
                <li>Use time expressions for the past</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Past Simple - Regular Verbs</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Add -ed to the base verb:</strong></p>
                <ul class="space-y-2">
                    <li><strong>work</strong> → worked | I worked yesterday.</li>
                    <li><strong>play</strong> → played | We played soccer last week.</li>
                    <li><strong>study</strong> → studied | She studied English.</li>
                    <li><strong>stop</strong> → stopped | The bus stopped here.</li>
                    <li><strong>live</strong> → lived | They lived in Lima.</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Spelling Rules:</h3>
                <ul class="space-y-1">
                    <li>Verb + -ed: <em>work → worked</em></li>
                    <li>Verb ending in -e + -d: <em>live → lived</em></li>
                    <li>Verb ending in consonant + y → -ied: <em>study → studied</em></li>
                    <li>CVC verbs → double consonant: <em>stop → stopped</em></li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Past Simple - Irregular Verbs</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>be</strong> → was/were | I was tired. They were happy.</li>
                    <li><strong>go</strong> → went | She went to school.</li>
                    <li><strong>have</strong> → had | We had breakfast.</li>
                    <li><strong>eat</strong> → ate | He ate pizza.</li>
                    <li><strong>see</strong> → saw | I saw a movie.</li>
                    <li><strong>come</strong> → came | They came late.</li>
                    <li><strong>buy</strong> → bought | She bought a dress.</li>
                    <li><strong>take</strong> → took | He took a photo.</li>
                    <li><strong>make</strong> → made | We made dinner.</li>
                    <li><strong>get</strong> → got | I got a gift.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">❓ Negatives & Questions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Negative: didn't + base verb</h3>
                <ul class="space-y-1">
                    <li>I <strong>didn't go</strong> to work yesterday.</li>
                    <li>She <strong>didn't eat</strong> breakfast.</li>
                    <li>They <strong>didn't see</strong> the movie.</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions: Did + subject + base verb?</h3>
                <ul class="space-y-1">
                    <li><strong>Did you go</strong> to school? → Yes, I did. / No, I didn't.</li>
                    <li><strong>Did she eat</strong> lunch? → Yes, she did. / No, she didn't.</li>
                    <li><strong>What did you do</strong> yesterday? → I watched TV.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⏰ Time Expressions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>yesterday</strong> → ayer</li>
                    <li><strong>last night/week/month/year</strong> → anoche/la semana pasada...</li>
                    <li><strong>... ago</strong> → hace... (two days ago = hace dos días)</li>
                    <li><strong>in 2020</strong> → en 2020</li>
                    <li><strong>when I was young</strong> → cuando era joven</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ (go) to the beach yesterday. (went)</li>
                <li>She _____ (not/eat) breakfast this morning. (didn't eat)</li>
                <li>_____ you _____ (see) that movie? (Did/see)</li>
                <li>They _____ (buy) a new car last month. (bought)</li>
                <li>We _____ (study) English two years ago. (studied)</li>
                <li>He _____ (be) very tired last night. (was)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int1": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🚀 INTERMEDIATE 01 - Relative Clauses</h1>
        <p class="text-white/60 mb-6">CEFR Level: B1 | ICPNA: Intermedio 1 | World Link Intermediate 1</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Use defining and non-defining relative clauses</li>
                <li>Talk about friends, family, and relationships</li>
                <li>Express quantities using specific vocabulary</li>
                <li>Describe community and social connections</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Defining Relative Clauses</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3">Essential information - no commas needed:</p>
                <ul class="space-y-2">
                    <li><strong>who</strong> (people): The man <em>who lives next door</em> is a doctor.</li>
                    <li><strong>which</strong> (things): The book <em>which I bought</em> is interesting.</li>
                    <li><strong>that</strong> (people/things): The car <em>that she drives</em> is red.</li>
                    <li><strong>where</strong> (places): The restaurant <em>where we met</em> closed down.</li>
                    <li><strong>when</strong> (time): I remember the day <em>when we first met</em>.</li>
                    <li><strong>whose</strong> (possession): The woman <em>whose car was stolen</em> called police.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Non-Defining Relative Clauses</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3">Extra information - USE COMMAS:</p>
                <ul class="space-y-2">
                    <li>My sister, <em>who lives in Madrid</em>, is visiting next week.</li>
                    <li>The Eiffel Tower, <em>which is in Paris</em>, is famous worldwide.</li>
                    <li>My boss, <em>whose office is on the 5th floor</em>, is very kind.</li>
                </ul>
                <p class="mt-4 text-red-400">⚠️ Cannot use "that" in non-defining clauses!</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Vocabulary: Community & Relationships</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>circle of friends</strong> → grupo de amigos</li>
                    <li><strong>keep in touch</strong> → mantenerse en contacto</li>
                    <li><strong>walks of life</strong> → diferentes estilos de vida</li>
                    <li><strong>acquaintance</strong> → conocido</li>
                    <li><strong>close friend</strong> → amigo cercano</li>
                    <li><strong>colleague</strong> → colega de trabajo</li>
                    <li><strong>neighbor</strong> → vecino</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📊 Expressing Quantities</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>the majority</strong> → la mayoría</li>
                    <li><strong>just over</strong> → un poco más de</li>
                    <li><strong>about / around</strong> → aproximadamente</li>
                    <li><strong>nearly</strong> → casi</li>
                    <li><strong>more than half</strong> → más de la mitad</li>
                    <li><strong>a quarter</strong> → un cuarto</li>
                    <li><strong>a third</strong> → un tercio</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <ol class="list-decimal pl-6 space-y-3">
                <li>The man _____ called you is my uncle. (who)</li>
                <li>This is the restaurant _____ we had dinner. (where)</li>
                <li>My brother, _____ is a doctor, works in Lima. (who)</li>
                <li>The book _____ I'm reading is very interesting. (that/which)</li>
                <li>She's the woman _____ husband works with me. (whose)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int2": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🚀 INTERMEDIATE 02 - Dynamic Verbs & Work</h1>
        <p class="text-white/60 mb-6">CEFR Level: B1 | ICPNA: Intermedio 2 | World Link Intermediate 1</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Distinguish between dynamic and stative verbs</li>
                <li>Talk about work-life balance</li>
                <li>Express opinions about work</li>
                <li>Use get/have/need + someone/something</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Dynamic vs Stative Verbs</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Dynamic Verbs (can use continuous):</h3>
                <ul class="space-y-1">
                    <li><strong>work, run, eat, write, play, study</strong></li>
                    <li>I'm working on a project. ✓</li>
                    <li>She's eating lunch. ✓</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Stative Verbs (usually no continuous):</h3>
                <ul class="space-y-1">
                    <li><strong>know, believe, like, love, hate, want, need</strong></li>
                    <li>I know the answer. ✓ | I'm knowing the answer. ✗</li>
                    <li>She loves music. ✓ | She's loving music. ✗</li>
                </ul>
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Verbs with both uses:</h3>
                <ul class="space-y-1">
                    <li><strong>think:</strong> I think it's good. (opinion) / I'm thinking about it. (process)</li>
                    <li><strong>have:</strong> I have a car. (possession) / I'm having dinner. (activity)</li>
                    <li><strong>see:</strong> I see the problem. (understand) / I'm seeing the doctor. (meeting)</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">💼 Work-Life Balance Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>performance</strong> → rendimiento</li>
                    <li><strong>morale</strong> → moral del equipo</li>
                    <li><strong>burn out</strong> → agotarse</li>
                    <li><strong>work overtime</strong> → trabajar horas extras</li>
                    <li><strong>flexible hours</strong> → horario flexible</li>
                    <li><strong>remote work</strong> → trabajo remoto</li>
                    <li><strong>deadline</strong> → fecha límite</li>
                    <li><strong>workload</strong> → carga de trabajo</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Personal Qualities</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>patience</strong> → paciencia</li>
                    <li><strong>motivation</strong> → motivación</li>
                    <li><strong>confident</strong> → seguro de sí mismo</li>
                    <li><strong>experienced</strong> → experimentado</li>
                    <li><strong>reliable</strong> → confiable</li>
                    <li><strong>organized</strong> → organizado</li>
                    <li><strong>creative</strong> → creativo</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Get/Have/Need + Someone/Something</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>I need to get my car fixed.</strong></li>
                    <li><strong>She had her hair cut yesterday.</strong></li>
                    <li><strong>We need someone to help us.</strong></li>
                    <li><strong>They got the house painted last month.</strong></li>
                </ul>
                <p class="mt-4 text-yellow-400">Structure: get/have + object + past participle</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ (think) about changing jobs. (am thinking)</li>
                <li>She _____ (know) the answer. (knows - NOT "is knowing")</li>
                <li>He needs to get his computer _____. (fixed/repaired)</li>
                <li>We _____ (have) a meeting right now. (are having)</li>
                <li>I _____ (believe) you're right. (believe - NOT "am believing")</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b7": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🏙️ BASIC 07 - City Life</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2 | ICPNA: Básico 7 | World Link Intro Units 7-9</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Describe locations in a city</li>
                <li>Use prepositions of place correctly</li>
                <li>Ask for and give directions</li>
                <li>Describe your neighborhood</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🏢 City Places Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">bank</strong> → banco</li>
                    <li><strong class="text-green-400">post office</strong> → correo</li>
                    <li><strong class="text-green-400">hospital</strong> → hospital</li>
                    <li><strong class="text-green-400">pharmacy/drugstore</strong> → farmacia</li>
                    <li><strong class="text-green-400">supermarket</strong> → supermercado</li>
                    <li><strong class="text-green-400">restaurant</strong> → restaurante</li>
                    <li><strong class="text-green-400">café/coffee shop</strong> → cafetería</li>
                    <li><strong class="text-green-400">gas station</strong> → gasolinera/grifo</li>
                    <li><strong class="text-green-400">police station</strong> → comisaría</li>
                    <li><strong class="text-green-400">bus stop</strong> → paradero de bus</li>
                    <li><strong class="text-green-400">train station</strong> → estación de tren</li>
                    <li><strong class="text-green-400">shopping mall</strong> → centro comercial</li>
                    <li><strong class="text-green-400">movie theater</strong> → cine</li>
                    <li><strong class="text-green-400">museum</strong> → museo</li>
                    <li><strong class="text-green-400">park</strong> → parque</li>
                    <li><strong class="text-green-400">church</strong> → iglesia</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📍 Prepositions of Place</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-yellow-400">next to</strong> → al lado de → The bank is <em>next to</em> the post office.</li>
                    <li><strong class="text-yellow-400">across from / opposite</strong> → frente a → The café is <em>across from</em> the park.</li>
                    <li><strong class="text-yellow-400">between</strong> → entre → The pharmacy is <em>between</em> the bank and the restaurant.</li>
                    <li><strong class="text-yellow-400">behind</strong> → detrás de → The parking lot is <em>behind</em> the mall.</li>
                    <li><strong class="text-yellow-400">in front of</strong> → delante de → There's a bus stop <em>in front of</em> the hospital.</li>
                    <li><strong class="text-yellow-400">on the corner of</strong> → en la esquina de → The bank is <em>on the corner of</em> Main St. and 5th Ave.</li>
                    <li><strong class="text-yellow-400">near</strong> → cerca de → Is there a restaurant <em>near</em> here?</li>
                    <li><strong class="text-yellow-400">far from</strong> → lejos de → The airport is <em>far from</em> downtown.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🧭 Giving Directions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Imperatives for Directions:</h3>
                <ul class="space-y-2">
                    <li><strong>Go straight</strong> → Sigue derecho</li>
                    <li><strong>Turn left</strong> → Dobla a la izquierda</li>
                    <li><strong>Turn right</strong> → Dobla a la derecha</li>
                    <li><strong>Go past the...</strong> → Pasa el/la...</li>
                    <li><strong>Take the first/second street on the left/right</strong></li>
                    <li><strong>It's on your left/right</strong> → Está a tu izquierda/derecha</li>
                    <li><strong>Keep going for two blocks</strong> → Sigue por dos cuadras</li>
                    <li><strong>Cross the street</strong> → Cruza la calle</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Example Dialogue:</h3>
                <ul class="space-y-1 text-white/80">
                    <li><strong>A:</strong> Excuse me, how do I get to the bank?</li>
                    <li><strong>B:</strong> Go straight for two blocks. Turn right on Main Street.</li>
                    <li><strong>B:</strong> The bank is on the corner, next to the pharmacy.</li>
                    <li><strong>A:</strong> Thank you!</li>
                    <li><strong>B:</strong> You're welcome!</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">❓ Asking for Directions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>Excuse me, where is the...?</strong> → Disculpe, ¿dónde está el/la...?</li>
                    <li><strong>How do I get to...?</strong> → ¿Cómo llego a...?</li>
                    <li><strong>Is there a... near here?</strong> → ¿Hay un/una... cerca de aquí?</li>
                    <li><strong>Can you tell me how to get to...?</strong> → ¿Puede decirme cómo llegar a...?</li>
                    <li><strong>Is it far from here?</strong> → ¿Está lejos de aquí?</li>
                    <li><strong>How long does it take to get there?</strong> → ¿Cuánto tiempo toma llegar?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🏘️ Describing Your Neighborhood</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Useful Adjectives:</h3>
                <ul class="space-y-1">
                    <li><strong>quiet</strong> → tranquilo | <strong>noisy</strong> → ruidoso</li>
                    <li><strong>safe</strong> → seguro | <strong>dangerous</strong> → peligroso</li>
                    <li><strong>clean</strong> → limpio | <strong>dirty</strong> → sucio</li>
                    <li><strong>modern</strong> → moderno | <strong>old</strong> → antiguo</li>
                    <li><strong>convenient</strong> → conveniente</li>
                    <li><strong>residential</strong> → residencial</li>
                    <li><strong>commercial</strong> → comercial</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Example:</h3>
                <p class="text-white/80">I live in a quiet neighborhood in Miraflores. There are many restaurants and cafés near my house. The supermarket is on the corner, next to the pharmacy. It's a very convenient and safe area.</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 There is / There are (Review)</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>There is</strong> a bank on Main Street.</li>
                    <li><strong>There are</strong> two restaurants near here.</li>
                    <li><strong>Is there</strong> a pharmacy nearby? → Yes, there is. / No, there isn't.</li>
                    <li><strong>Are there</strong> any parks in your neighborhood? → Yes, there are. / No, there aren't.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with the correct preposition:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>The bank is _____ the post office and the restaurant. (between)</li>
                <li>The café is _____ the park. You can see it from there. (across from)</li>
                <li>There's a bus stop _____ the hospital. (in front of)</li>
                <li>The supermarket is _____ my house. I walk there every day. (near/next to)</li>
                <li>The parking lot is _____ the building. (behind)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Give directions from the school to the bank:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>_____ straight for one block. (Go)</li>
                <li>_____ left on Central Avenue. (Turn)</li>
                <li>The bank is _____ the corner. (on)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b8": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">⏳ BASIC 08 - Past Continuous</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2 | ICPNA: Básico 8 | World Link Book 1</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Describe actions in progress in the past</li>
                <li>Use was/were + verb-ing correctly</li>
                <li>Contrast Past Simple vs Past Continuous</li>
                <li>Use time expressions: while, when, as</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Past Continuous Structure</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + was/were + verb-ING</strong></p>
                <ul class="space-y-2">
                    <li><strong>I was</strong> studying at 8 PM. → Yo estaba estudiando a las 8 PM.</li>
                    <li><strong>You were</strong> sleeping when I called. → Estabas durmiendo cuando llamé.</li>
                    <li><strong>He/She was</strong> working all day. → Él/Ella estaba trabajando todo el día.</li>
                    <li><strong>We were</strong> watching TV. → Estábamos viendo TV.</li>
                    <li><strong>They were</strong> playing soccer. → Estaban jugando fútbol.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Negative:</h3>
                <ul class="space-y-1">
                    <li>I <strong>wasn't</strong> sleeping. → No estaba durmiendo.</li>
                    <li>They <strong>weren't</strong> listening. → No estaban escuchando.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>Was</strong> she working? → Yes, she was. / No, she wasn't.</li>
                    <li><strong>Were</strong> they studying? → Yes, they were. / No, they weren't.</li>
                    <li><strong>What were</strong> you doing at 9 PM?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎯 Uses of Past Continuous</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">1. Action in progress at a specific time:</h3>
                <ul class="space-y-1 mb-4">
                    <li>At 10 PM last night, I <strong>was reading</strong> a book.</li>
                    <li>This time yesterday, we <strong>were flying</strong> to Miami.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">2. Interrupted action (with Past Simple):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>was cooking</strong> when the phone <strong>rang</strong>.</li>
                    <li>She <strong>was walking</strong> home when it <strong>started</strong> to rain.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">3. Two parallel actions:</h3>
                <ul class="space-y-1 mb-4">
                    <li><strong>While</strong> I <strong>was studying</strong>, my brother <strong>was playing</strong> video games.</li>
                    <li>She <strong>was cooking</strong> while he <strong>was cleaning</strong>.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">4. Setting the scene (stories):</h3>
                <ul class="space-y-1">
                    <li>The sun <strong>was shining</strong>. Birds <strong>were singing</strong>. It was a beautiful day.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⚡ Past Simple vs Past Continuous</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2 text-yellow-400">Past Simple</th>
                            <th class="py-2 text-yellow-400">Past Continuous</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2">Completed action</td>
                            <td class="py-2">Action in progress</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">I <strong>ate</strong> breakfast.</td>
                            <td class="py-2">I <strong>was eating</strong> breakfast at 8.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">She <strong>called</strong> me.</td>
                            <td class="py-2">She <strong>was calling</strong> when I arrived.</td>
                        </tr>
                        <tr>
                            <td class="py-2">Short action (interruption)</td>
                            <td class="py-2">Long action (background)</td>
                        </tr>
                    </tbody>
                </table>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Key Pattern:</h3>
                <p class="text-white/80"><strong>WHEN</strong> + Past Simple, Past Continuous</p>
                <p class="text-white/80"><strong>WHILE</strong> + Past Continuous, Past Simple/Continuous</p>
                <ul class="mt-2 space-y-1">
                    <li><strong>When</strong> the phone rang, I <strong>was taking</strong> a shower.</li>
                    <li><strong>While</strong> I <strong>was walking</strong> home, I <strong>saw</strong> an accident.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⏰ Time Expressions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">when</strong> → cuando (short action interrupts)</li>
                    <li><strong class="text-green-400">while</strong> → mientras (parallel actions)</li>
                    <li><strong class="text-green-400">as</strong> → mientras/cuando</li>
                    <li><strong class="text-green-400">at that moment</strong> → en ese momento</li>
                    <li><strong class="text-green-400">at 8 o'clock</strong> → a las 8</li>
                    <li><strong class="text-green-400">all day/night/morning</strong> → todo el día/noche/mañana</li>
                    <li><strong class="text-green-400">this time yesterday</strong> → a esta hora ayer</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Spelling Rules for -ING (Review)</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>Most verbs:</strong> + ing → work<em>ing</em>, play<em>ing</em>, study<em>ing</em></li>
                    <li><strong>Verbs ending in -e:</strong> drop e + ing → mak<em>ing</em>, writ<em>ing</em>, danc<em>ing</em></li>
                    <li><strong>Short CVC verbs:</strong> double consonant + ing → run<em>ning</em>, sit<em>ting</em>, swim<em>ming</em></li>
                    <li><strong>Verbs ending in -ie:</strong> ie → y + ing → l<em>ying</em>, d<em>ying</em></li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with Past Simple or Past Continuous:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ (watch) TV when the lights _____ (go) out. (was watching / went)</li>
                <li>While she _____ (cook), the phone _____ (ring). (was cooking / rang)</li>
                <li>They _____ (play) soccer at 5 PM yesterday. (were playing)</li>
                <li>What _____ you _____ (do) when I _____ (call) you? (were/doing / called)</li>
                <li>He _____ (not/sleep) when the alarm _____ (go) off. (wasn't sleeping / went)</li>
                <li>While I _____ (study), my sister _____ (listen) to music. (was studying / was listening)</li>
                <li>The sun _____ (shine) and the birds _____ (sing). It was beautiful. (was shining / were singing)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete the story:</h3>
            <p class="text-white/80 mb-2">Yesterday at 8 PM, I _____ (sit) in my room. I _____ (read) a book. Suddenly, I _____ (hear) a strange noise outside. I _____ (go) to the window. A cat _____ (run) across the garden!</p>
            <p class="text-green-400">(was sitting / was reading / heard / went / was running)</p>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """
}

def get_lesson_content(lesson_id):
    """Return HTML content for a lesson"""
    if lesson_id in LESSON_CONTENT:
        return LESSON_CONTENT[lesson_id]
    
    # Default content for lessons without specific content yet
    lesson_meta = next((l for l in LESSONS if l['id'] == lesson_id), None)
    title = lesson_meta['title'] if lesson_meta else f"Lesson {lesson_id.upper()}"
    
    return f"""
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">📚 {title}</h1>
        
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
                <li><span class="text-green-400">Hello</span> → Hola</li>
                <li><span class="text-green-400">Goodbye</span> → Adiós</li>
                <li><span class="text-green-400">Thank you</span> → Gracias</li>
                <li><span class="text-green-400">Please</span> → Por favor</li>
                <li><span class="text-green-400">Yes</span> → Sí</li>
                <li><span class="text-green-400">No</span> → No</li>
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