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
