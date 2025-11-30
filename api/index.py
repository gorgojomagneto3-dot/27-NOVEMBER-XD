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
    """,
    
    "b9": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">✨ BASIC 09 - Present Perfect</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2-B1 | ICPNA: Básico 9 | World Link Book 2</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Talk about life experiences</li>
                <li>Use have/has + past participle correctly</li>
                <li>Master time expressions: ever, never, already, yet, just, for, since</li>
                <li>Distinguish Present Perfect from Past Simple</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Present Perfect Structure</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + have/has + past participle</strong></p>
                <ul class="space-y-2">
                    <li><strong>I have</strong> visited Paris. → He visitado París.</li>
                    <li><strong>You have</strong> finished your homework. → Has terminado tu tarea.</li>
                    <li><strong>He/She has</strong> lived here for 5 years. → Ha vivido aquí por 5 años.</li>
                    <li><strong>We have</strong> eaten at that restaurant. → Hemos comido en ese restaurante.</li>
                    <li><strong>They have</strong> seen that movie. → Han visto esa película.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Contractions:</h3>
                <ul class="space-y-1">
                    <li>I have → I've | You have → You've | We have → We've | They have → They've</li>
                    <li>He has → He's | She has → She's | It has → It's</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Negative:</h3>
                <ul class="space-y-1">
                    <li>I <strong>haven't</strong> seen that movie. → No he visto esa película.</li>
                    <li>She <strong>hasn't</strong> finished yet. → Ella no ha terminado todavía.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>Have</strong> you ever been to London? → Yes, I have. / No, I haven't.</li>
                    <li><strong>Has</strong> she called you? → Yes, she has. / No, she hasn't.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Regular & Irregular Past Participles</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Regular Verbs (+ ed):</h3>
                <ul class="space-y-1 mb-4">
                    <li>work → work<strong>ed</strong> | play → play<strong>ed</strong> | visit → visit<strong>ed</strong></li>
                    <li>study → stud<strong>ied</strong> | stop → stopp<strong>ed</strong> | live → liv<strong>ed</strong></li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Irregular Verbs (memorize!):</h3>
                <ul class="space-y-1">
                    <li><strong>be</strong> → been | <strong>go</strong> → gone | <strong>see</strong> → seen</li>
                    <li><strong>do</strong> → done | <strong>eat</strong> → eaten | <strong>have</strong> → had</li>
                    <li><strong>take</strong> → taken | <strong>write</strong> → written | <strong>give</strong> → given</li>
                    <li><strong>buy</strong> → bought | <strong>make</strong> → made | <strong>find</strong> → found</li>
                    <li><strong>know</strong> → known | <strong>speak</strong> → spoken | <strong>read</strong> → read</li>
                    <li><strong>come</strong> → come | <strong>run</strong> → run | <strong>put</strong> → put</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎯 Uses of Present Perfect</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">1. Life Experiences (with ever/never):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>have visited</strong> 10 countries.</li>
                    <li><strong>Have</strong> you <strong>ever eaten</strong> sushi? → ¿Alguna vez has comido sushi?</li>
                    <li>She <strong>has never seen</strong> snow. → Ella nunca ha visto nieve.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">2. Recent Past (with just):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>have just finished</strong> my homework. → Acabo de terminar mi tarea.</li>
                    <li>She <strong>has just arrived</strong>. → Ella acaba de llegar.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">3. Completed/Not completed (with already/yet):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>have already eaten</strong> lunch. → Ya he almorzado.</li>
                    <li>She <strong>hasn't finished yet</strong>. → Ella no ha terminado todavía.</li>
                    <li><strong>Have</strong> you done your homework <strong>yet</strong>? → ¿Ya has hecho tu tarea?</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">4. Duration (with for/since):</h3>
                <ul class="space-y-1">
                    <li>I <strong>have lived</strong> here <strong>for</strong> 5 years. → He vivido aquí por 5 años.</li>
                    <li>She <strong>has worked</strong> here <strong>since</strong> 2020. → Ella ha trabajado aquí desde 2020.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⏰ FOR vs SINCE</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2 text-green-400">FOR (duration)</th>
                            <th class="py-2 text-yellow-400">SINCE (starting point)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2">for 5 minutes</td>
                            <td class="py-2">since 9 o'clock</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">for 2 hours</td>
                            <td class="py-2">since Monday</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">for 3 days</td>
                            <td class="py-2">since January</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">for 6 months</td>
                            <td class="py-2">since 2020</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">for 10 years</td>
                            <td class="py-2">since I was a child</td>
                        </tr>
                        <tr>
                            <td class="py-2">for a long time</td>
                            <td class="py-2">since we met</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⚡ Present Perfect vs Past Simple</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2 text-yellow-400">Present Perfect</th>
                            <th class="py-2 text-yellow-400">Past Simple</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2">No specific time</td>
                            <td class="py-2">Specific time in the past</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">I <strong>have seen</strong> that movie.</td>
                            <td class="py-2">I <strong>saw</strong> that movie <strong>yesterday</strong>.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">She <strong>has been</strong> to Paris.</td>
                            <td class="py-2">She <strong>went</strong> to Paris <strong>in 2019</strong>.</td>
                        </tr>
                        <tr>
                            <td class="py-2">Connection to now</td>
                            <td class="py-2">Finished, no connection to now</td>
                        </tr>
                    </tbody>
                </table>
                
                <p class="mt-4 text-red-400">⚠️ Never use Present Perfect with: yesterday, last week, in 2020, ago, when...?</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with Present Perfect:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ (never/be) to Japan. (have never been)</li>
                <li>She _____ (just/finish) her exam. (has just finished)</li>
                <li>_____ you _____ (ever/eat) Thai food? (Have/ever eaten)</li>
                <li>They _____ (live) here for 10 years. (have lived)</li>
                <li>He _____ (not/call) me yet. (hasn't called)</li>
                <li>We _____ (already/see) that movie. (have already seen)</li>
                <li>I _____ (know) her since 2015. (have known)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Choose FOR or SINCE:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I've lived here _____ 5 years. (for)</li>
                <li>She's worked here _____ 2018. (since)</li>
                <li>We've been friends _____ a long time. (for)</li>
                <li>He's studied English _____ he was 10. (since)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Present Perfect or Past Simple?</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ (see) that movie last week. (saw)</li>
                <li>She _____ (never/try) sushi. (has never tried)</li>
                <li>They _____ (go) to Paris in 2019. (went)</li>
                <li>_____ you _____ (ever/visit) London? (Have/ever visited)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b10": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🚀 BASIC 10 - Future Tenses</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2-B1 | ICPNA: Básico 10 | World Link Book 2</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Express future plans and intentions with "going to"</li>
                <li>Make predictions and spontaneous decisions with "will"</li>
                <li>Talk about scheduled events with Present Continuous</li>
                <li>Choose the correct future form for each situation</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 WILL - Future Simple</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + will + base verb</strong></p>
                <ul class="space-y-2">
                    <li>I <strong>will call</strong> you tomorrow. → Te llamaré mañana.</li>
                    <li>She <strong>will be</strong> 25 next year. → Ella cumplirá 25 el próximo año.</li>
                    <li>They <strong>will arrive</strong> at 8 PM. → Llegarán a las 8 PM.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Contractions:</h3>
                <p>I will → I'll | You will → You'll | He will → He'll | We will → We'll</p>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Negative: will not = won't</h3>
                <ul class="space-y-1">
                    <li>I <strong>won't</strong> be late. → No llegaré tarde.</li>
                    <li>She <strong>won't</strong> forget. → Ella no olvidará.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>Will</strong> you come to the party? → Yes, I will. / No, I won't.</li>
                    <li><strong>What will</strong> you do tomorrow?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎯 Uses of WILL</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">1. Predictions (without evidence):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I think it <strong>will rain</strong> tomorrow.</li>
                    <li>She <strong>will probably be</strong> late.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">2. Spontaneous decisions:</h3>
                <ul class="space-y-1 mb-4">
                    <li>The phone is ringing. I<strong>'ll answer</strong> it.</li>
                    <li>I'm tired. I<strong>'ll go</strong> to bed.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">3. Offers & Promises:</h3>
                <ul class="space-y-1 mb-4">
                    <li>I<strong>'ll help</strong> you with your homework. (offer)</li>
                    <li>I <strong>won't tell</strong> anyone. I promise. (promise)</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">4. Facts about the future:</h3>
                <ul class="space-y-1">
                    <li>She <strong>will be</strong> 30 next month.</li>
                    <li>The meeting <strong>will start</strong> at 9 AM.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 GOING TO</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + am/is/are + going to + base verb</strong></p>
                <ul class="space-y-2">
                    <li>I <strong>am going to study</strong> medicine. → Voy a estudiar medicina.</li>
                    <li>She <strong>is going to travel</strong> to Europe. → Ella va a viajar a Europa.</li>
                    <li>We <strong>are going to buy</strong> a new car. → Vamos a comprar un carro nuevo.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Negative:</h3>
                <ul class="space-y-1">
                    <li>I<strong>'m not going to</strong> work tomorrow.</li>
                    <li>They <strong>aren't going to</strong> come.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>Are</strong> you <strong>going to</strong> study tonight?</li>
                    <li><strong>What are</strong> you <strong>going to</strong> do this weekend?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎯 Uses of GOING TO</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">1. Plans & Intentions (decided before):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I<strong>'m going to visit</strong> my grandparents this weekend. (I already decided)</li>
                    <li>She<strong>'s going to start</strong> a new job next month.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">2. Predictions with evidence:</h3>
                <ul class="space-y-1">
                    <li>Look at those clouds! It<strong>'s going to rain</strong>.</li>
                    <li>She's very tired. She<strong>'s going to fall</strong> asleep.</li>
                    <li>Watch out! You<strong>'re going to fall</strong>!</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Present Continuous for Future</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>For fixed arrangements (with time/place)</strong></p>
                <ul class="space-y-2">
                    <li>I<strong>'m meeting</strong> John at 6 PM. → (already arranged with John)</li>
                    <li>We<strong>'re flying</strong> to Miami on Friday. → (tickets bought)</li>
                    <li>She<strong>'s having</strong> dinner with her boss tonight.</li>
                </ul>
                <p class="mt-4 text-white/60">Usually with verbs: meet, have, fly, leave, arrive, come, go</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⚡ Comparison Table</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2 text-yellow-400">Form</th>
                            <th class="py-2 text-yellow-400">Use</th>
                            <th class="py-2 text-yellow-400">Example</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">WILL</td>
                            <td class="py-2">Predictions, spontaneous decisions, offers, promises</td>
                            <td class="py-2">I'll help you.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">GOING TO</td>
                            <td class="py-2">Plans/intentions, predictions with evidence</td>
                            <td class="py-2">I'm going to study law.</td>
                        </tr>
                        <tr>
                            <td class="py-2 text-green-400">PRESENT CONT.</td>
                            <td class="py-2">Fixed arrangements</td>
                            <td class="py-2">I'm meeting John at 6.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⏰ Time Expressions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong>tomorrow</strong> → mañana</li>
                    <li><strong>next week/month/year</strong> → la próxima semana/mes/año</li>
                    <li><strong>in a few days</strong> → en unos días</li>
                    <li><strong>this weekend</strong> → este fin de semana</li>
                    <li><strong>tonight</strong> → esta noche</li>
                    <li><strong>soon</strong> → pronto</li>
                    <li><strong>in the future</strong> → en el futuro</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Choose: WILL, GOING TO, or PRESENT CONTINUOUS:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>Look at those clouds! It _____ rain. (is going to - evidence)</li>
                <li>I'm thirsty. I _____ get some water. (will - spontaneous)</li>
                <li>We _____ dinner with the Smiths on Saturday. (are having - arrangement)</li>
                <li>I've decided. I _____ learn French next year. (am going to - plan)</li>
                <li>I think Brazil _____ win the World Cup. (will - prediction)</li>
                <li>She _____ the doctor at 3 PM tomorrow. (is seeing - appointment)</li>
                <li>Don't worry, I _____ help you. (will - offer)</li>
                <li>Watch out! You _____ drop that! (are going to - evidence)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete with the correct future form:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>A: Why are you buying paint? B: I _____ (paint) my room. (am going to paint)</li>
                <li>A: The phone is ringing! B: I _____ (get) it. (will get)</li>
                <li>What time _____ (you/leave) tomorrow? (are you leaving)</li>
                <li>I promise I _____ (not/be) late again. (won't be)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b11": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎉 BASIC 11 - Celebrations</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2-B1 | ICPNA: Básico 11 | World Link Book 2</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Talk about celebrations and holidays</li>
                <li>Describe traditions and customs</li>
                <li>Use vocabulary for parties and events</li>
                <li>Review tenses to describe past and future celebrations</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎊 Celebrations Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Life Events:</h3>
                <ul class="space-y-2">
                    <li><strong class="text-green-400">birthday</strong> → cumpleaños</li>
                    <li><strong class="text-green-400">wedding</strong> → boda</li>
                    <li><strong class="text-green-400">anniversary</strong> → aniversario</li>
                    <li><strong class="text-green-400">graduation</strong> → graduación</li>
                    <li><strong class="text-green-400">baby shower</strong> → baby shower</li>
                    <li><strong class="text-green-400">retirement party</strong> → fiesta de jubilación</li>
                    <li><strong class="text-green-400">housewarming</strong> → inauguración de casa</li>
                    <li><strong class="text-green-400">engagement</strong> → compromiso</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📅 Holidays Around the World</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">Christmas</strong> → Navidad (December 25)</li>
                    <li><strong class="text-green-400">New Year's Eve/Day</strong> → Año Nuevo (December 31/January 1)</li>
                    <li><strong class="text-green-400">Easter</strong> → Semana Santa / Pascua</li>
                    <li><strong class="text-green-400">Halloween</strong> → Halloween (October 31)</li>
                    <li><strong class="text-green-400">Thanksgiving</strong> → Día de Acción de Gracias</li>
                    <li><strong class="text-green-400">Valentine's Day</strong> → Día de San Valentín (February 14)</li>
                    <li><strong class="text-green-400">Mother's Day</strong> → Día de la Madre</li>
                    <li><strong class="text-green-400">Father's Day</strong> → Día del Padre</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">🇵🇪 Peruvian Celebrations:</h3>
                <ul class="space-y-2">
                    <li><strong class="text-green-400">Fiestas Patrias</strong> → Independence Day (July 28-29)</li>
                    <li><strong class="text-green-400">Inti Raymi</strong> → Festival of the Sun (June 24)</li>
                    <li><strong class="text-green-400">Señor de los Milagros</strong> → Lord of Miracles (October)</li>
                    <li><strong class="text-green-400">Carnaval</strong> → Carnival (February)</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎈 Party Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Things at a Party:</h3>
                <ul class="space-y-1">
                    <li><strong>cake</strong> → torta/pastel</li>
                    <li><strong>candles</strong> → velas</li>
                    <li><strong>balloons</strong> → globos</li>
                    <li><strong>decorations</strong> → decoraciones</li>
                    <li><strong>gifts/presents</strong> → regalos</li>
                    <li><strong>invitations</strong> → invitaciones</li>
                    <li><strong>confetti</strong> → confeti</li>
                    <li><strong>fireworks</strong> → fuegos artificiales</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Party Actions:</h3>
                <ul class="space-y-1">
                    <li><strong>celebrate</strong> → celebrar</li>
                    <li><strong>invite guests</strong> → invitar invitados</li>
                    <li><strong>blow out candles</strong> → soplar las velas</li>
                    <li><strong>make a wish</strong> → pedir un deseo</li>
                    <li><strong>open presents</strong> → abrir regalos</li>
                    <li><strong>dance</strong> → bailar</li>
                    <li><strong>toast</strong> → brindar</li>
                    <li><strong>sing Happy Birthday</strong> → cantar Feliz Cumpleaños</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🗣️ Useful Expressions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Congratulations & Wishes:</h3>
                <ul class="space-y-2">
                    <li><strong>Happy Birthday!</strong> → ¡Feliz cumpleaños!</li>
                    <li><strong>Congratulations!</strong> → ¡Felicitaciones!</li>
                    <li><strong>Merry Christmas!</strong> → ¡Feliz Navidad!</li>
                    <li><strong>Happy New Year!</strong> → ¡Feliz Año Nuevo!</li>
                    <li><strong>Happy Anniversary!</strong> → ¡Feliz aniversario!</li>
                    <li><strong>Best wishes!</strong> → ¡Mis mejores deseos!</li>
                    <li><strong>Cheers!</strong> → ¡Salud! (when toasting)</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Inviting:</h3>
                <ul class="space-y-2">
                    <li><strong>Would you like to come to my party?</strong></li>
                    <li><strong>You're invited to...</strong></li>
                    <li><strong>We're having a party on Saturday. Can you come?</strong></li>
                    <li><strong>I'd love to invite you to...</strong></li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Accepting/Declining:</h3>
                <ul class="space-y-2">
                    <li><strong>Yes, I'd love to!</strong> → ¡Sí, me encantaría!</li>
                    <li><strong>That sounds great!</strong> → ¡Suena genial!</li>
                    <li><strong>I'm sorry, I can't make it.</strong> → Lo siento, no puedo ir.</li>
                    <li><strong>I'm afraid I have other plans.</strong> → Me temo que tengo otros planes.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Describing Traditions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Useful Structures:</h3>
                <ul class="space-y-2">
                    <li><strong>We usually...</strong> → Usualmente nosotros...</li>
                    <li><strong>People often...</strong> → La gente a menudo...</li>
                    <li><strong>It's traditional to...</strong> → Es tradicional...</li>
                    <li><strong>In my country, we celebrate... by...</strong></li>
                    <li><strong>On this day, families...</strong></li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Example:</h3>
                <p class="text-white/80">In Peru, we celebrate Fiestas Patrias on July 28th and 29th. It's traditional to have a big parade. People usually wear red and white. Families often get together and eat traditional food like ceviche and anticuchos.</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Tense Review for Celebrations</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Past (describing what happened):</h3>
                <ul class="space-y-1 mb-4">
                    <li>We <strong>had</strong> a great party last year.</li>
                    <li>She <strong>received</strong> many gifts.</li>
                    <li>Everyone <strong>was dancing</strong> all night.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Present (traditions/habits):</h3>
                <ul class="space-y-1 mb-4">
                    <li>We always <strong>celebrate</strong> Christmas with family.</li>
                    <li>My mom usually <strong>makes</strong> a special cake.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Future (plans):</h3>
                <ul class="space-y-1">
                    <li>We<strong>'re going to have</strong> a party next Saturday.</li>
                    <li>I<strong>'m inviting</strong> 20 people to my birthday.</li>
                    <li>It <strong>will be</strong> amazing!</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete the sentences:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>Last year, we _____ (celebrate) my grandmother's 80th birthday. (celebrated)</li>
                <li>In Peru, people usually _____ (eat) turkey on Christmas. (eat)</li>
                <li>Next month, I _____ (have) a graduation party. (am going to have)</li>
                <li>Everyone _____ (dance) when the music started. (was dancing)</li>
                <li>We always _____ (sing) Happy Birthday before cutting the cake. (sing)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Match the celebration with the activity:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>Birthday → blow out candles, make a wish</li>
                <li>New Year's Eve → watch fireworks, toast at midnight</li>
                <li>Wedding → exchange rings, dance the first dance</li>
                <li>Christmas → exchange gifts, decorate a tree</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Write about a celebration:</h3>
            <p class="text-white/80">Describe your favorite celebration. Use: What is it? When is it? What do people do? What do you usually eat? How do you feel?</p>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "b12": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🎓 BASIC 12 - Complete Review</h1>
        <p class="text-white/60 mb-6">CEFR Level: A2 | ICPNA: Básico 12 | Final Review & Preparation for Intermediate</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Review all grammar from Basic 1-11</li>
                <li>Consolidate vocabulary from all units</li>
                <li>Identify and correct common errors</li>
                <li>Prepare for Intermediate level</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Grammar Summary: All Tenses</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2 text-yellow-400">Tense</th>
                            <th class="py-2 text-yellow-400">Structure</th>
                            <th class="py-2 text-yellow-400">Use</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Present Simple</td>
                            <td class="py-2">I work / She works</td>
                            <td class="py-2">Habits, routines, facts</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Present Continuous</td>
                            <td class="py-2">I am working</td>
                            <td class="py-2">Now, temporary actions</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Past Simple</td>
                            <td class="py-2">I worked / I went</td>
                            <td class="py-2">Completed past actions</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Past Continuous</td>
                            <td class="py-2">I was working</td>
                            <td class="py-2">Action in progress in past</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Present Perfect</td>
                            <td class="py-2">I have worked</td>
                            <td class="py-2">Experience, recent past, for/since</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Future (will)</td>
                            <td class="py-2">I will work</td>
                            <td class="py-2">Predictions, decisions, promises</td>
                        </tr>
                        <tr>
                            <td class="py-2 text-green-400">Future (going to)</td>
                            <td class="py-2">I am going to work</td>
                            <td class="py-2">Plans, intentions</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Key Grammar Structures</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Verb TO BE:</h3>
                <p class="mb-4">I am, You are, He/She/It is, We are, They are</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">There is / There are:</h3>
                <p class="mb-4">There is a book. There are three books.</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">Possessive Adjectives:</h3>
                <p class="mb-4">my, your, his, her, its, our, their</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">Prepositions of Place:</h3>
                <p class="mb-4">in, on, at, next to, between, behind, in front of, across from</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">Frequency Adverbs:</h3>
                <p class="mb-4">always, usually, often, sometimes, rarely, never</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">Time Expressions:</h3>
                <ul class="space-y-1">
                    <li><strong>Past:</strong> yesterday, last week, ago, in 2020</li>
                    <li><strong>Present Perfect:</strong> ever, never, already, yet, just, for, since</li>
                    <li><strong>Future:</strong> tomorrow, next week, soon, in the future</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📝 Vocabulary Categories Review</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">👤 People:</h3>
                <p class="mb-4">family members, jobs, physical descriptions, personality adjectives</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">🏠 Places:</h3>
                <p class="mb-4">rooms, furniture, city locations, countries, neighborhoods</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">⏰ Time:</h3>
                <p class="mb-4">days, months, telling time, daily routines</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">🍽️ Food:</h3>
                <p class="mb-4">meals, food types, tastes, ordering at a restaurant</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">👕 Shopping:</h3>
                <p class="mb-4">clothes, prices, sizes, shopping expressions</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">🎉 Celebrations:</h3>
                <p class="mb-4">holidays, parties, traditions, congratulations</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⚠️ Common Errors to Avoid</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-3">
                    <li>❌ <span class="text-red-400">She work every day.</span> → ✅ <span class="text-green-400">She works every day.</span> (3rd person -s)</li>
                    <li>❌ <span class="text-red-400">I am agree.</span> → ✅ <span class="text-green-400">I agree.</span> (agree doesn't use BE)</li>
                    <li>❌ <span class="text-red-400">I have 25 years.</span> → ✅ <span class="text-green-400">I am 25 years old.</span> (age uses BE)</li>
                    <li>❌ <span class="text-red-400">I am knowing him.</span> → ✅ <span class="text-green-400">I know him.</span> (stative verbs)</li>
                    <li>❌ <span class="text-red-400">I went there yesterday ago.</span> → ✅ <span class="text-green-400">I went there yesterday.</span> (don't mix)</li>
                    <li>❌ <span class="text-red-400">I have seen him yesterday.</span> → ✅ <span class="text-green-400">I saw him yesterday.</span> (Past Simple with specific time)</li>
                    <li>❌ <span class="text-red-400">Where you are going?</span> → ✅ <span class="text-green-400">Where are you going?</span> (question word order)</li>
                    <li>❌ <span class="text-red-400">I no like coffee.</span> → ✅ <span class="text-green-400">I don't like coffee.</span> (use auxiliaries)</li>
                    <li>❌ <span class="text-red-400">He don't work here.</span> → ✅ <span class="text-green-400">He doesn't work here.</span> (3rd person doesn't)</li>
                    <li>❌ <span class="text-red-400">I'm going to the home.</span> → ✅ <span class="text-green-400">I'm going home.</span> (no article with home)</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Comprehensive Practice Test</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Part 1: Choose the correct option:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>She _____ to work every day. (goes)</li>
                <li>I _____ TV when the phone rang. (was watching)</li>
                <li>They _____ here since 2015. (have lived)</li>
                <li>Look! It _____ rain! (is going to)</li>
                <li>_____ there a bank near here? (Is)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Part 2: Correct the errors:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>He have been to Paris. → He <strong>has</strong> been to Paris.</li>
                <li>I am study English. → I am <strong>studying</strong> English.</li>
                <li>She don't like pizza. → She <strong>doesn't</strong> like pizza.</li>
                <li>Where you work? → Where <strong>do you</strong> work?</li>
                <li>I have saw that movie. → I have <strong>seen</strong> that movie.</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Part 3: Complete with the correct tense:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>Right now, I _____ (study) for my exam. (am studying)</li>
                <li>Yesterday, we _____ (go) to the beach. (went)</li>
                <li>She _____ (never/eat) sushi before. (has never eaten)</li>
                <li>Next week, I _____ (travel) to Cusco. (am going to travel / am traveling)</li>
                <li>While I _____ (cook), my mom _____ (call). (was cooking / called)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Part 4: Vocabulary - Match:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>bank → where you keep money</li>
                <li>graduation → finishing school/university</li>
                <li>bald → without hair</li>
                <li>straight → type of hair (not curly)</li>
                <li>toast → drink to celebrate</li>
            </ol>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🚀 Ready for Intermediate?</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-white/80 mb-4">If you can do the following, you're ready for Intermediate level:</p>
                <ul class="space-y-2">
                    <li>✅ Introduce yourself and talk about personal information</li>
                    <li>✅ Describe people, places, and things</li>
                    <li>✅ Talk about daily routines and habits</li>
                    <li>✅ Describe past events and experiences</li>
                    <li>✅ Make plans for the future</li>
                    <li>✅ Give and follow directions</li>
                    <li>✅ Order food and go shopping</li>
                    <li>✅ Talk about celebrations and traditions</li>
                </ul>
            </div>
        </section>
        
        <div class="mt-8 p-4 bg-purple-500/20 rounded-lg border border-purple-500/50">
            <p class="text-purple-400 font-semibold text-xl">🎓 ¡Congratulations! You've completed the Basic Level!</p>
            <p class="text-white/80 mt-2">You're now ready to start Intermediate 01 - Relative Clauses</p>
        </div>
        
        <div class="mt-4 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 100 XP! (Bonus for finishing Basic!)</p>
        </div>
    </div>
    """,
    
    "int3": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">💡 INTERMEDIATE 03 - Creativity</h1>
        <p class="text-white/60 mb-6">CEFR Level: B1 | ICPNA: Intermedio 3 | World Link Intermediate 1, Unit 3</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Use vocabulary related to problem solving</li>
                <li>Give suggestions and advice using should, could, why don't you</li>
                <li>Express opinions effectively</li>
                <li>Talk about ability in the past: could, was able to, managed to</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🧩 Problem Solving Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">solve a problem</strong> → resolver un problema</li>
                    <li><strong class="text-green-400">reach a decision</strong> → llegar a una decisión</li>
                    <li><strong class="text-green-400">make up your mind</strong> → decidirse</li>
                    <li><strong class="text-green-400">come up with an idea</strong> → tener/proponer una idea</li>
                    <li><strong class="text-green-400">think outside the box</strong> → pensar de forma creativa</li>
                    <li><strong class="text-green-400">find a solution</strong> → encontrar una solución</li>
                    <li><strong class="text-green-400">face a challenge</strong> → enfrentar un desafío</li>
                    <li><strong class="text-green-400">overcome an obstacle</strong> → superar un obstáculo</li>
                    <li><strong class="text-green-400">weigh the options</strong> → evaluar las opciones</li>
                    <li><strong class="text-green-400">consider the alternatives</strong> → considerar las alternativas</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Giving Suggestions & Advice</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Strong Advice (SHOULD):</h3>
                <ul class="space-y-1 mb-4">
                    <li>You <strong>should</strong> talk to your boss. → Deberías hablar con tu jefe.</li>
                    <li>You <strong>shouldn't</strong> ignore the problem. → No deberías ignorar el problema.</li>
                    <li><strong>Should</strong> I apply for that job? → ¿Debería aplicar a ese trabajo?</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Softer Suggestions (COULD):</h3>
                <ul class="space-y-1 mb-4">
                    <li>You <strong>could</strong> try a different approach. → Podrías intentar un enfoque diferente.</li>
                    <li>We <strong>could</strong> ask for help. → Podríamos pedir ayuda.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Friendly Suggestions:</h3>
                <ul class="space-y-1 mb-4">
                    <li><strong>Why don't you</strong> take a break? → ¿Por qué no tomas un descanso?</li>
                    <li><strong>How about</strong> trying something new? → ¿Qué tal si pruebas algo nuevo?</li>
                    <li><strong>What about</strong> asking Maria for help? → ¿Qué tal pedirle ayuda a María?</li>
                    <li><strong>Have you tried</strong> talking to him? → ¿Has intentado hablar con él?</li>
                    <li><strong>If I were you</strong>, I would wait. → Si yo fuera tú, esperaría.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Responding to Suggestions:</h3>
                <ul class="space-y-1">
                    <li><strong>That's a good idea!</strong> → ¡Es buena idea!</li>
                    <li><strong>I'll try that.</strong> → Lo intentaré.</li>
                    <li><strong>I'm not sure about that.</strong> → No estoy seguro/a de eso.</li>
                    <li><strong>I've already tried that.</strong> → Ya lo intenté.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">💬 Expressing Opinions</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Giving Your Opinion:</h3>
                <ul class="space-y-1 mb-4">
                    <li><strong>I think (that)</strong>... → Pienso que...</li>
                    <li><strong>In my opinion</strong>,... → En mi opinión,...</li>
                    <li><strong>I believe (that)</strong>... → Creo que...</li>
                    <li><strong>From my point of view</strong>,... → Desde mi punto de vista,...</li>
                    <li><strong>As I see it</strong>,... → Como lo veo,...</li>
                    <li><strong>It seems to me that</strong>... → Me parece que...</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Agreeing:</h3>
                <ul class="space-y-1 mb-4">
                    <li><strong>I agree (with you).</strong></li>
                    <li><strong>That's true.</strong> / <strong>That's right.</strong></li>
                    <li><strong>Exactly!</strong> / <strong>Absolutely!</strong></li>
                    <li><strong>I think so too.</strong></li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Disagreeing (politely):</h3>
                <ul class="space-y-1">
                    <li><strong>I'm not sure about that.</strong></li>
                    <li><strong>I see your point, but...</strong></li>
                    <li><strong>I don't really agree.</strong></li>
                    <li><strong>Actually, I think...</strong></li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🎨 Creativity Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">creativity</strong> → creatividad</li>
                    <li><strong class="text-green-400">imagination</strong> → imaginación</li>
                    <li><strong class="text-green-400">intelligence</strong> → inteligencia</li>
                    <li><strong class="text-green-400">innovation</strong> → innovación</li>
                    <li><strong class="text-green-400">inspiration</strong> → inspiración</li>
                    <li><strong class="text-green-400">original</strong> → original</li>
                    <li><strong class="text-green-400">inventive</strong> → inventivo</li>
                    <li><strong class="text-green-400">artistic</strong> → artístico</li>
                    <li><strong class="text-green-400">talented</strong> → talentoso</li>
                    <li><strong class="text-green-400">gifted</strong> → dotado/talentoso</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Ability in the Past</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">COULD (general ability):</h3>
                <ul class="space-y-1 mb-4">
                    <li>When I was young, I <strong>could</strong> run very fast. (general ability)</li>
                    <li>She <strong>could</strong> speak French when she was 10.</li>
                    <li>I <strong>couldn't</strong> swim until I was 12.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">WAS/WERE ABLE TO (specific achievement):</h3>
                <ul class="space-y-1 mb-4">
                    <li>After hours of trying, I <strong>was able to</strong> fix the computer. ✓</li>
                    <li>After hours of trying, I <strong>could</strong> fix the computer. ✗ (NOT for specific achievements)</li>
                    <li>She <strong>was able to</strong> finish the project on time.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">MANAGED TO (with difficulty):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>managed to</strong> pass the exam. (it was difficult, but I did it)</li>
                    <li>We <strong>managed to</strong> find a solution.</li>
                    <li>He <strong>didn't manage to</strong> finish on time.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Summary Table:</h3>
                <table class="w-full text-left mt-2">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2">Form</th>
                            <th class="py-2">Use</th>
                            <th class="py-2">Example</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">could</td>
                            <td class="py-2">General ability in the past</td>
                            <td class="py-2">I could swim when I was 5.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">was/were able to</td>
                            <td class="py-2">Specific achievement</td>
                            <td class="py-2">I was able to finish the race.</td>
                        </tr>
                        <tr>
                            <td class="py-2 text-green-400">managed to</td>
                            <td class="py-2">Success despite difficulty</td>
                            <td class="py-2">I managed to pass the exam.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Give advice using should, could, why don't you:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I'm stressed about my exams. → You _____ take breaks while studying. (should)</li>
                <li>I can't sleep at night. → _____ trying to read before bed? (How about)</li>
                <li>I don't know what career to choose. → You _____ talk to a career counselor. (could)</li>
                <li>I'm always late to work. → _____ set your alarm earlier? (Why don't you)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Choose: could, was able to, or managed to:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>When I was a child, I _____ play the piano very well. (could - general ability)</li>
                <li>After trying for hours, she _____ solve the puzzle. (was able to / managed to - specific)</li>
                <li>The traffic was terrible, but we _____ arrive on time. (managed to - with difficulty)</li>
                <li>He _____ speak three languages when he was 10. (could - general ability)</li>
                <li>I _____ find the information I needed online. (was able to / managed to)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Express your opinion:</h3>
            <p class="text-white/80">Complete with an opinion phrase:</p>
            <ol class="list-decimal pl-6 space-y-3">
                <li>_____, creativity can be learned. (In my opinion / I believe that)</li>
                <li>_____, practice is more important than talent. (I think / As I see it)</li>
                <li>_____ everyone has some creative ability. (It seems to me that)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int4": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🔀 INTERMEDIATE 04 - Conditionals</h1>
        <p class="text-white/60 mb-6">CEFR Level: B1 | ICPNA: Intermedio 4 | World Link Intermediate 1, Unit 4</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Use Zero Conditional for general truths</li>
                <li>Use First Conditional for real possibilities</li>
                <li>Use Second Conditional for unreal/hypothetical situations</li>
                <li>Use unless, as long as, provided that</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Zero Conditional</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>If + Present Simple, Present Simple</strong></p>
                <p class="text-white/60 mb-3">Use: General truths, scientific facts, things that are always true</p>
                <ul class="space-y-2">
                    <li>If you heat water to 100°C, it <strong>boils</strong>.</li>
                    <li>If it rains, the streets <strong>get</strong> wet.</li>
                    <li>If you don't eat, you <strong>get</strong> hungry.</li>
                    <li>Plants die if they <strong>don't get</strong> water.</li>
                </ul>
                <p class="mt-4 text-white/60">Note: You can use "when" instead of "if" for things that always happen.</p>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 First Conditional</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>If + Present Simple, will + base verb</strong></p>
                <p class="text-white/60 mb-3">Use: Real possibilities in the future, likely situations</p>
                <ul class="space-y-2">
                    <li>If it rains tomorrow, I <strong>will stay</strong> home.</li>
                    <li>If you study hard, you <strong>will pass</strong> the exam.</li>
                    <li>If she calls me, I <strong>will tell</strong> her the news.</li>
                    <li>I <strong>won't go</strong> to the party if I'm tired.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>What will you do</strong> if it rains?</li>
                    <li><strong>Will you come</strong> if I invite you?</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Other modals (instead of will):</h3>
                <ul class="space-y-1">
                    <li>If you're tired, you <strong>can</strong> take a break.</li>
                    <li>If he's late, we <strong>might</strong> miss the movie.</li>
                    <li>If you finish early, you <strong>should</strong> review your answers.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Second Conditional</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>If + Past Simple, would + base verb</strong></p>
                <p class="text-white/60 mb-3">Use: Unreal/hypothetical situations, imaginary scenarios, advice</p>
                <ul class="space-y-2">
                    <li>If I <strong>had</strong> more money, I <strong>would travel</strong> the world.</li>
                    <li>If she <strong>spoke</strong> English, she <strong>would get</strong> that job.</li>
                    <li>If I <strong>were</strong> you, I <strong>would accept</strong> the offer.</li>
                    <li>I <strong>wouldn't buy</strong> that car if I <strong>were</strong> you.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Important: If I were (not "was")</h3>
                <ul class="space-y-1">
                    <li>If I <strong>were</strong> rich, I would buy a house. ✓</li>
                    <li>If I was rich... (informal, but grammatically "were" is correct)</li>
                    <li>If I <strong>were</strong> you, I would study harder. (giving advice)</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>What would you do</strong> if you won the lottery?</li>
                    <li><strong>Where would you go</strong> if you could travel anywhere?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">⚡ Comparison Table</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <table class="w-full text-left">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2 text-yellow-400">Conditional</th>
                            <th class="py-2 text-yellow-400">Structure</th>
                            <th class="py-2 text-yellow-400">Use</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">Zero</td>
                            <td class="py-2">If + present, present</td>
                            <td class="py-2">General truths (100% true)</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2 text-green-400">First</td>
                            <td class="py-2">If + present, will + verb</td>
                            <td class="py-2">Real future possibility</td>
                        </tr>
                        <tr>
                            <td class="py-2 text-green-400">Second</td>
                            <td class="py-2">If + past, would + verb</td>
                            <td class="py-2">Unreal/hypothetical</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Other Conditional Words</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">UNLESS (= if not):</h3>
                <ul class="space-y-1 mb-4">
                    <li>I won't go <strong>unless</strong> you come with me. (= if you don't come)</li>
                    <li><strong>Unless</strong> it rains, we'll have a picnic.</li>
                    <li>She won't pass <strong>unless</strong> she studies.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">AS LONG AS / PROVIDED (THAT) (= only if):</h3>
                <ul class="space-y-1 mb-4">
                    <li>You can borrow my car <strong>as long as</strong> you drive carefully.</li>
                    <li>I'll help you <strong>provided that</strong> you help me later.</li>
                    <li>We'll go to the beach <strong>as long as</strong> the weather is good.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">IN CASE (= because something might happen):</h3>
                <ul class="space-y-1">
                    <li>Take an umbrella <strong>in case</strong> it rains.</li>
                    <li>I'll give you my number <strong>in case</strong> you need help.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with the correct form (Zero, First, or Second):</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>If you _____ (heat) ice, it _____ (melt). (heat / melts - Zero)</li>
                <li>If it _____ (rain) tomorrow, I _____ (take) an umbrella. (rains / will take - First)</li>
                <li>If I _____ (be) you, I _____ (talk) to the manager. (were / would talk - Second)</li>
                <li>If she _____ (have) more time, she _____ (learn) another language. (had / would learn - Second)</li>
                <li>If you _____ (not study), you _____ (fail) the exam. (don't study / will fail - First)</li>
                <li>Water _____ (freeze) if the temperature _____ (drop) below 0°C. (freezes / drops - Zero)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Rewrite using UNLESS:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>If you don't hurry, you'll be late. → _____ (Unless you hurry, you'll be late.)</li>
                <li>If she doesn't call, I won't know. → _____ (Unless she calls, I won't know.)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">What would you do if...?</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>...you won a million dollars?</li>
                <li>...you could travel anywhere?</li>
                <li>...you met a famous person?</li>
                <li>...you could have any superpower?</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int5": """
    <div class="lesson-container">
        <h1 class="text-3xl font-bold text-green-400 mb-6">🧠 INTERMEDIATE 05 - Brainpower</h1>
        <p class="text-white/60 mb-6">CEFR Level: B1 | ICPNA: Intermedio 5 | World Link Intermediate 1, Unit 5</p>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📋 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2 text-white/80">
                <li>Use vocabulary related to memory and learning</li>
                <li>Talk about past habits with used to and would</li>
                <li>Use phrasal verbs related to learning</li>
                <li>Understand verb + -ing or infinitive patterns</li>
            </ul>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">🧠 Memory Vocabulary</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">remember</strong> → recordar</li>
                    <li><strong class="text-green-400">forget</strong> → olvidar</li>
                    <li><strong class="text-green-400">memorize</strong> → memorizar</li>
                    <li><strong class="text-green-400">recall</strong> → recordar/evocar</li>
                    <li><strong class="text-green-400">retain</strong> → retener información</li>
                    <li><strong class="text-green-400">retrieve</strong> → recuperar información</li>
                    <li><strong class="text-green-400">refresh your memory</strong> → refrescar la memoria</li>
                    <li><strong class="text-green-400">recollect</strong> → rememorar</li>
                    <li><strong class="text-green-400">remind</strong> → recordar a alguien</li>
                    <li><strong class="text-green-400">short-term memory</strong> → memoria a corto plazo</li>
                    <li><strong class="text-green-400">long-term memory</strong> → memoria a largo plazo</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Used To (Past Habits)</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + used to + base verb</strong></p>
                <p class="text-white/60 mb-3">Use: Things that were true in the past but are not true now</p>
                
                <h3 class="text-lg text-yellow-400 mb-2">Affirmative:</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>used to</strong> live in Lima. (Now I don't live there)</li>
                    <li>She <strong>used to</strong> smoke. (Now she doesn't smoke)</li>
                    <li>We <strong>used to</strong> play together as children.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Negative:</h3>
                <ul class="space-y-1 mb-4">
                    <li>I <strong>didn't use to</strong> like coffee. (Now I like it)</li>
                    <li>He <strong>didn't use to</strong> exercise. (Now he does)</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Questions:</h3>
                <ul class="space-y-1">
                    <li><strong>Did you use to</strong> play sports? → Yes, I did. / No, I didn't.</li>
                    <li><strong>Where did you use to</strong> live?</li>
                    <li><strong>What did you use to</strong> do on weekends?</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Would (Past Habits)</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <p class="text-yellow-400 mb-3"><strong>Subject + would + base verb</strong></p>
                <p class="text-white/60 mb-3">Use: Repeated actions in the past (NOT states)</p>
                
                <ul class="space-y-2">
                    <li>When I was young, I <strong>would play</strong> in the park every day. ✓</li>
                    <li>My grandmother <strong>would tell</strong> us stories at night. ✓</li>
                    <li>We <strong>would visit</strong> our grandparents every summer. ✓</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mt-4 mb-2">⚠️ Cannot use WOULD for states:</h3>
                <ul class="space-y-1">
                    <li>I <strong>used to</strong> live in Lima. ✓</li>
                    <li>I <strong>would</strong> live in Lima. ✗ (live = state, not action)</li>
                    <li>She <strong>used to</strong> have long hair. ✓</li>
                    <li>She <strong>would</strong> have long hair. ✗ (have = state)</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📚 Learning Phrasal Verbs</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <ul class="space-y-2">
                    <li><strong class="text-green-400">look up</strong> → buscar (en diccionario/internet) → I need to look up this word.</li>
                    <li><strong class="text-green-400">pick up</strong> → aprender de forma natural → She picked up Spanish while living in Peru.</li>
                    <li><strong class="text-green-400">catch on</strong> → entender/comprender → It took me a while to catch on.</li>
                    <li><strong class="text-green-400">figure out</strong> → descifrar/resolver → I can't figure out this problem.</li>
                    <li><strong class="text-green-400">go over</strong> → repasar → Let's go over the lesson again.</li>
                    <li><strong class="text-green-400">hand in</strong> → entregar → Don't forget to hand in your homework.</li>
                    <li><strong class="text-green-400">drop out</strong> → abandonar (estudios) → He dropped out of university.</li>
                    <li><strong class="text-green-400">sign up</strong> → inscribirse → I signed up for a cooking class.</li>
                    <li><strong class="text-green-400">keep up with</strong> → seguir el ritmo → I can't keep up with the class.</li>
                    <li><strong class="text-green-400">fall behind</strong> → atrasarse → Don't fall behind on your studies.</li>
                </ul>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">📖 Verb + -ING or Infinitive</h2>
            <div class="bg-white/10 p-4 rounded-lg">
                <h3 class="text-lg text-yellow-400 mb-2">Verbs followed by -ING:</h3>
                <p class="mb-2">enjoy, finish, avoid, mind, suggest, keep, practice, consider, imagine</p>
                <ul class="space-y-1 mb-4">
                    <li>I enjoy <strong>learning</strong> new things.</li>
                    <li>She finished <strong>studying</strong> at 10 PM.</li>
                    <li>Avoid <strong>making</strong> the same mistake.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Verbs followed by INFINITIVE:</h3>
                <p class="mb-2">want, need, decide, hope, plan, expect, promise, learn, agree, refuse</p>
                <ul class="space-y-1 mb-4">
                    <li>I want <strong>to learn</strong> French.</li>
                    <li>She decided <strong>to study</strong> abroad.</li>
                    <li>He promised <strong>to help</strong> me.</li>
                </ul>
                
                <h3 class="text-lg text-yellow-400 mb-2">Verbs with DIFFERENT meanings:</h3>
                <table class="w-full text-left mt-2">
                    <thead>
                        <tr class="border-b border-white/20">
                            <th class="py-2">Verb + -ing</th>
                            <th class="py-2">Verb + infinitive</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="py-2"><strong>stop + -ing</strong> = quit doing</td>
                            <td class="py-2"><strong>stop + to</strong> = pause to do</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">I stopped smoking. (quit)</td>
                            <td class="py-2">I stopped to smoke. (paused)</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2"><strong>remember + -ing</strong> = recall past</td>
                            <td class="py-2"><strong>remember + to</strong> = not forget</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2">I remember meeting him. (I recall)</td>
                            <td class="py-2">Remember to call me. (don't forget)</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="py-2"><strong>try + -ing</strong> = experiment</td>
                            <td class="py-2"><strong>try + to</strong> = attempt</td>
                        </tr>
                        <tr>
                            <td class="py-2">Try eating less sugar. (experiment)</td>
                            <td class="py-2">I tried to open the door. (attempted)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
        
        <section class="mb-8">
            <h2 class="text-2xl text-blue-400 mb-4">✏️ Practice Exercises</h2>
            <h3 class="text-lg text-yellow-400 mb-3">Complete with used to or would:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I _____ live in a small town. (used to - state)</li>
                <li>When I was a child, I _____ play outside every day. (would/used to - action)</li>
                <li>She _____ have long hair, but now it's short. (used to - state)</li>
                <li>My father _____ read me stories every night. (would/used to - action)</li>
                <li>They _____ be best friends. (used to - state)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete with -ing or infinitive:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I enjoy _____ (learn) new languages. (learning)</li>
                <li>She decided _____ (study) medicine. (to study)</li>
                <li>Don't forget _____ (call) me tomorrow! (to call)</li>
                <li>I remember _____ (meet) him at the party. (meeting - recalling past)</li>
                <li>He stopped _____ (smoke) last year. (smoking - quit)</li>
                <li>We want _____ (improve) our English. (to improve)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete with the correct phrasal verb:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I need to _____ this word in the dictionary. (look up)</li>
                <li>She _____ French while living in Paris. (picked up)</li>
                <li>Don't forget to _____ your homework tomorrow. (hand in)</li>
                <li>I _____ for a yoga class last week. (signed up)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int6": """
    <div class="lesson-container max-w-4xl mx-auto p-6">
        <h1 class="text-3xl font-bold text-green-400 mb-4">🎭 INTERMEDIATE 6 - Storytelling</h1>
        <p class="text-gray-300 mb-6">ICPNA Intermediate Level - CEFR B1/B2 | Narrative Tenses & Drama</p>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-green-400 mb-3">🎯 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2">
                <li>Use narrative tenses to tell stories (Past Simple, Past Continuous, Past Perfect)</li>
                <li>Order events using time sequencers and connectors</li>
                <li>Use adverbs and adverbial phrases for vivid storytelling</li>
                <li>Vocabulary: drama, theater, and storytelling expressions</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">📖 Narrative Tenses - Telling Stories</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Past Simple - Main Events</h3>
            <p class="text-gray-300 mb-2">Use for completed actions, the main events of the story:</p>
            <ul class="list-disc pl-6 space-y-1 text-gray-300 mb-4">
                <li>She <span class="text-green-400">walked</span> into the room and <span class="text-green-400">saw</span> a strange figure.</li>
                <li>He <span class="text-green-400">grabbed</span> his bag and <span class="text-green-400">ran</span> out.</li>
                <li>The detective <span class="text-green-400">found</span> the evidence.</li>
            </ul>
            
            <h3 class="text-lg text-yellow-400 mb-3">Past Continuous - Background/Atmosphere</h3>
            <p class="text-gray-300 mb-2">Use to set the scene, describe ongoing actions:</p>
            <ul class="list-disc pl-6 space-y-1 text-gray-300 mb-4">
                <li>It <span class="text-blue-400">was raining</span> heavily that night.</li>
                <li>People <span class="text-blue-400">were rushing</span> to find shelter.</li>
                <li>She <span class="text-blue-400">was waiting</span> nervously when the phone rang.</li>
            </ul>
            
            <h3 class="text-lg text-yellow-400 mb-3">Past Perfect - Earlier Events</h3>
            <p class="text-gray-300 mb-2">Use for events that happened before the main story:</p>
            <ul class="list-disc pl-6 space-y-1 text-gray-300 mb-4">
                <li>She realized she <span class="text-purple-400">had forgotten</span> her keys.</li>
                <li>By the time he arrived, everyone <span class="text-purple-400">had left</span>.</li>
                <li>He didn't recognize her because she <span class="text-purple-400">had changed</span> so much.</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">⏰ Time Sequencers & Connectors</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-yellow-400 mb-2">Beginning of Story</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li>• Once upon a time...</li>
                        <li>• One day...</li>
                        <li>• It all started when...</li>
                        <li>• A long time ago...</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-yellow-400 mb-2">Sequence of Events</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li>• First... Then... After that...</li>
                        <li>• Meanwhile... At the same time...</li>
                        <li>• Later... Eventually...</li>
                        <li>• As soon as... The moment...</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-yellow-400 mb-2">Contrast/Surprise</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li>• Suddenly... All of a sudden...</li>
                        <li>• Unexpectedly... To my surprise...</li>
                        <li>• However... Although...</li>
                        <li>• But just then...</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-yellow-400 mb-2">Ending</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li>• In the end... Finally...</li>
                        <li>• At last... Eventually...</li>
                        <li>• And they lived happily ever after</li>
                        <li>• That's how it all ended</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">✨ Adverbs for Vivid Storytelling</h2>
            
            <h3 class="text-lg text-yellow-400 mb-2">Manner Adverbs</h3>
            <ul class="list-disc pl-6 space-y-1 text-gray-300 mb-4">
                <li><span class="text-green-400">slowly, quickly, quietly, loudly, carefully, nervously</span></li>
                <li>She walked <span class="text-green-400">slowly</span> down the dark corridor.</li>
                <li>He whispered <span class="text-green-400">nervously</span> into her ear.</li>
            </ul>
            
            <h3 class="text-lg text-yellow-400 mb-2">Degree Adverbs</h3>
            <ul class="list-disc pl-6 space-y-1 text-gray-300 mb-4">
                <li><span class="text-blue-400">extremely, incredibly, absolutely, completely, hardly</span></li>
                <li>I was <span class="text-blue-400">absolutely</span> terrified.</li>
                <li>The room was <span class="text-blue-400">completely</span> empty.</li>
            </ul>
            
            <h3 class="text-lg text-yellow-400 mb-2">Adverbial Phrases for Atmosphere</h3>
            <ul class="list-disc pl-6 space-y-1 text-gray-300">
                <li><span class="text-purple-400">in the middle of the night, out of nowhere, all of a sudden</span></li>
                <li><span class="text-purple-400">without warning, bit by bit, step by step</span></li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🎭 Drama & Theater Vocabulary</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">People</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">actor/actress</span> - person who performs</li>
                        <li><span class="text-yellow-400">director</span> - leads the production</li>
                        <li><span class="text-yellow-400">playwright</span> - writes plays</li>
                        <li><span class="text-yellow-400">audience</span> - people watching</li>
                        <li><span class="text-yellow-400">cast</span> - all actors in a play</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Parts of a Play</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">act</span> - main division</li>
                        <li><span class="text-yellow-400">scene</span> - smaller section</li>
                        <li><span class="text-yellow-400">script</span> - written text</li>
                        <li><span class="text-yellow-400">dialogue</span> - conversation</li>
                        <li><span class="text-yellow-400">monologue</span> - one person speaks</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Theater Elements</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">stage</span> - where actors perform</li>
                        <li><span class="text-yellow-400">scenery/set</span> - decorations</li>
                        <li><span class="text-yellow-400">costume</span> - clothes worn</li>
                        <li><span class="text-yellow-400">props</span> - objects used</li>
                        <li><span class="text-yellow-400">lighting</span> - lights for effect</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Story Elements</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">plot</span> - the main story</li>
                        <li><span class="text-yellow-400">twist</span> - unexpected turn</li>
                        <li><span class="text-yellow-400">climax</span> - most exciting part</li>
                        <li><span class="text-yellow-400">ending</span> - how it finishes</li>
                        <li><span class="text-yellow-400">moral</span> - lesson learned</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🎬 Types of Stories</h2>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                <div class="bg-white/5 p-2 rounded text-center">
                    <span class="text-green-400">comedy</span>
                    <p class="text-sm text-gray-400">funny</p>
                </div>
                <div class="bg-white/5 p-2 rounded text-center">
                    <span class="text-green-400">tragedy</span>
                    <p class="text-sm text-gray-400">sad ending</p>
                </div>
                <div class="bg-white/5 p-2 rounded text-center">
                    <span class="text-green-400">thriller</span>
                    <p class="text-sm text-gray-400">suspenseful</p>
                </div>
                <div class="bg-white/5 p-2 rounded text-center">
                    <span class="text-green-400">mystery</span>
                    <p class="text-sm text-gray-400">solving puzzles</p>
                </div>
                <div class="bg-white/5 p-2 rounded text-center">
                    <span class="text-green-400">romance</span>
                    <p class="text-sm text-gray-400">love stories</p>
                </div>
                <div class="bg-white/5 p-2 rounded text-center">
                    <span class="text-green-400">fairy tale</span>
                    <p class="text-sm text-gray-400">magical stories</p>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-yellow-500/20 rounded-lg border border-yellow-500/50">
            <h2 class="text-xl text-yellow-400 mb-3">📝 Practice Exercises</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Choose the correct tense:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>While I _____ (walk) home, I _____ (see) an accident.
                    <span class="text-gray-400">(was walking / saw)</span></li>
                <li>She _____ (realize) that she _____ (leave) her phone at home.
                    <span class="text-gray-400">(realized / had left)</span></li>
                <li>They _____ (talk) when suddenly the lights _____ (go) out.
                    <span class="text-gray-400">(were talking / went)</span></li>
                <li>By the time we _____ (arrive), the movie _____ (start).
                    <span class="text-gray-400">(arrived / had started)</span></li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Add appropriate time sequencers:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>_____, there was a young girl who lived in a forest.</li>
                <li>She was cooking dinner. _____, she heard a loud noise.</li>
                <li>We waited for hours. _____, the bus came.</li>
                <li>_____ I opened the door, I knew something was wrong.</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Add adverbs to make these sentences more vivid:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>She opened the door _____. (carefully/nervously)</li>
                <li>The children ran _____ through the park. (happily/excitedly)</li>
                <li>He spoke _____, so no one could hear. (quietly/softly)</li>
                <li>I was _____ shocked by the news. (completely/absolutely)</li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int7": """
    <div class="lesson-container max-w-4xl mx-auto p-6">
        <h1 class="text-3xl font-bold text-green-400 mb-4">🏙️ INTERMEDIATE 7 - Design</h1>
        <p class="text-gray-300 mb-6">ICPNA Intermediate Level - CEFR B1/B2 | Passive Voice & Urban Planning</p>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-green-400 mb-3">🎯 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2">
                <li>Use the passive voice in different tenses</li>
                <li>Form and use adjectives ending in -able/-ible</li>
                <li>Vocabulary: architecture, urban planning, and design</li>
                <li>Describe buildings, cities, and design features</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">📖 The Passive Voice</h2>
            
            <p class="text-gray-300 mb-4">We use passive when the action is more important than who does it, or when the doer is unknown.</p>
            
            <h3 class="text-lg text-yellow-400 mb-3">Formation: be + past participle</h3>
            
            <div class="overflow-x-auto mb-4">
                <table class="w-full text-gray-300">
                    <thead class="bg-white/10">
                        <tr>
                            <th class="p-2 text-left text-green-400">Tense</th>
                            <th class="p-2 text-left text-green-400">Active</th>
                            <th class="p-2 text-left text-green-400">Passive</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="p-2">Present Simple</td>
                            <td class="p-2">They build houses.</td>
                            <td class="p-2 text-blue-400">Houses are built.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">Past Simple</td>
                            <td class="p-2">They built this bridge.</td>
                            <td class="p-2 text-blue-400">This bridge was built.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">Present Perfect</td>
                            <td class="p-2">They have designed it.</td>
                            <td class="p-2 text-blue-400">It has been designed.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">Future (will)</td>
                            <td class="p-2">They will complete it.</td>
                            <td class="p-2 text-blue-400">It will be completed.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">Modal</td>
                            <td class="p-2">They can repair it.</td>
                            <td class="p-2 text-blue-400">It can be repaired.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <h3 class="text-lg text-yellow-400 mb-2">When to use passive:</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300">
                <li><span class="text-green-400">Unknown agent:</span> My bike was stolen. (we don't know who)</li>
                <li><span class="text-green-400">Obvious agent:</span> The criminal was arrested. (by police - obvious)</li>
                <li><span class="text-green-400">Formal/Scientific:</span> The experiment was conducted carefully.</li>
                <li><span class="text-green-400">Focus on action:</span> The building was designed in 1920.</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">✨ Adjectives with -able/-ible</h2>
            
            <p class="text-gray-300 mb-3">These suffixes mean "can be" or "possible to":</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">-able (from verbs)</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">renewable</span> - can be renewed</li>
                        <li><span class="text-yellow-400">sustainable</span> - can be sustained</li>
                        <li><span class="text-yellow-400">livable</span> - good to live in</li>
                        <li><span class="text-yellow-400">affordable</span> - can afford</li>
                        <li><span class="text-yellow-400">walkable</span> - easy to walk</li>
                        <li><span class="text-yellow-400">adjustable</span> - can adjust</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">-ible (Latin roots)</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">accessible</span> - easy to access</li>
                        <li><span class="text-yellow-400">flexible</span> - can bend/change</li>
                        <li><span class="text-yellow-400">visible</span> - can be seen</li>
                        <li><span class="text-yellow-400">responsible</span> - has responsibility</li>
                        <li><span class="text-yellow-400">sensible</span> - makes sense</li>
                        <li><span class="text-yellow-400">possible</span> - can happen</li>
                    </ul>
                </div>
            </div>
            
            <h3 class="text-lg text-yellow-400 mb-2">Negative forms (un-, in-, im-):</h3>
            <ul class="list-disc pl-6 space-y-1 text-gray-300">
                <li><span class="text-red-400">un</span>available, <span class="text-red-400">un</span>acceptable, <span class="text-red-400">un</span>bearable</li>
                <li><span class="text-red-400">in</span>accessible, <span class="text-red-400">in</span>visible, <span class="text-red-400">in</span>credible</li>
                <li><span class="text-red-400">im</span>possible, <span class="text-red-400">im</span>permeable</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🏗️ Architecture & Design Vocabulary</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Building Types</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">skyscraper</span> - very tall building</li>
                        <li><span class="text-yellow-400">high-rise</span> - tall apartment building</li>
                        <li><span class="text-yellow-400">warehouse</span> - storage building</li>
                        <li><span class="text-yellow-400">townhouse</span> - multi-floor row house</li>
                        <li><span class="text-yellow-400">landmark</span> - famous recognizable building</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Architectural Features</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">facade</span> - front of building</li>
                        <li><span class="text-yellow-400">balcony</span> - outdoor platform</li>
                        <li><span class="text-yellow-400">column</span> - vertical support</li>
                        <li><span class="text-yellow-400">dome</span> - rounded roof</li>
                        <li><span class="text-yellow-400">arch</span> - curved structure</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Urban Planning</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">zoning</span> - area use rules</li>
                        <li><span class="text-yellow-400">infrastructure</span> - basic facilities</li>
                        <li><span class="text-yellow-400">public spaces</span> - parks, plazas</li>
                        <li><span class="text-yellow-400">pedestrian zone</span> - walking area</li>
                        <li><span class="text-yellow-400">green spaces</span> - parks, gardens</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Design Concepts</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">eco-friendly</span> - good for environment</li>
                        <li><span class="text-yellow-400">minimalist</span> - simple design</li>
                        <li><span class="text-yellow-400">functional</span> - practical use</li>
                        <li><span class="text-yellow-400">innovative</span> - new ideas</li>
                        <li><span class="text-yellow-400">sustainable</span> - long-lasting</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🏠 Describing Buildings</h2>
            
            <h3 class="text-lg text-yellow-400 mb-2">Useful Adjectives:</h3>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-2 mb-4">
                <span class="bg-white/5 p-2 rounded text-center text-green-400">modern</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">traditional</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">spacious</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">compact</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">elegant</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">stunning</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">iconic</span>
                <span class="bg-white/5 p-2 rounded text-center text-green-400">impressive</span>
            </div>
            
            <h3 class="text-lg text-yellow-400 mb-2">Example Descriptions (Passive):</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300">
                <li>The museum <span class="text-blue-400">was designed</span> by a famous architect.</li>
                <li>The building <span class="text-blue-400">was constructed</span> in the 19th century.</li>
                <li>It <span class="text-blue-400">is made</span> of glass and steel.</li>
                <li>The park <span class="text-blue-400">will be opened</span> next year.</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-yellow-500/20 rounded-lg border border-yellow-500/50">
            <h2 class="text-xl text-yellow-400 mb-3">📝 Practice Exercises</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Change to passive voice:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>They designed the building in 1990.
                    <span class="text-gray-400">(The building was designed in 1990.)</span></li>
                <li>Someone has stolen my car.
                    <span class="text-gray-400">(My car has been stolen.)</span></li>
                <li>They will finish the project next month.
                    <span class="text-gray-400">(The project will be finished next month.)</span></li>
                <li>People speak English everywhere.
                    <span class="text-gray-400">(English is spoken everywhere.)</span></li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete with -able or -ible:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>This area is very access_____ by public transport. (accessible)</li>
                <li>The prices are afford_____ for most people. (affordable)</li>
                <li>Is this material wash_____? (washable)</li>
                <li>That's an incred_____ design! (incredible)</li>
                <li>The building is sustain_____ and eco-friendly. (sustainable)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Describe these using passive:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>The Eiffel Tower / build / 1889
                    <span class="text-gray-400">(The Eiffel Tower was built in 1889.)</span></li>
                <li>This bridge / make / steel
                    <span class="text-gray-400">(This bridge is made of steel.)</span></li>
                <li>A new park / open / next year
                    <span class="text-gray-400">(A new park will be opened next year.)</span></li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int8": """
    <div class="lesson-container max-w-4xl mx-auto p-6">
        <h1 class="text-3xl font-bold text-green-400 mb-4">🔬 INTERMEDIATE 8 - Science</h1>
        <p class="text-gray-300 mb-6">ICPNA Intermediate Level - CEFR B1/B2 | Future Predictions & Scientific Language</p>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-green-400 mb-3">🎯 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2">
                <li>Make predictions with will, going to, and might</li>
                <li>Use future time clauses (when, as soon as, until, before)</li>
                <li>Use connectors of cause and effect</li>
                <li>Vocabulary: science, technology, and environment</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🔮 Making Predictions</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Will - Predictions based on opinion/belief</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300 mb-4">
                <li>I think robots <span class="text-green-400">will</span> replace many jobs in the future.</li>
                <li>Scientists <span class="text-green-400">will probably</span> find a cure for cancer.</li>
                <li>Technology <span class="text-green-400">won't</span> solve all our problems.</li>
            </ul>
            
            <h3 class="text-lg text-yellow-400 mb-3">Going to - Evidence-based predictions</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300 mb-4">
                <li>Look at those clouds! It <span class="text-blue-400">is going to</span> rain.</li>
                <li>The ice caps are melting. Sea levels <span class="text-blue-400">are going to</span> rise.</li>
                <li>Based on current trends, pollution <span class="text-blue-400">is going to</span> get worse.</li>
            </ul>
            
            <h3 class="text-lg text-yellow-400 mb-3">Might/May - Uncertain predictions</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300">
                <li>We <span class="text-purple-400">might</span> discover life on other planets.</li>
                <li>Electric cars <span class="text-purple-400">may</span> become more affordable.</li>
                <li>This experiment <span class="text-purple-400">might not</span> work as expected.</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">⏰ Future Time Clauses</h2>
            
            <p class="text-gray-300 mb-3">Use <span class="text-red-400">Present Simple</span> (not will) after: when, as soon as, until, before, after, if</p>
            
            <div class="bg-white/5 p-4 rounded mb-4">
                <p class="text-red-400 mb-2">❌ When I will finish...</p>
                <p class="text-green-400">✅ When I <span class="text-yellow-400">finish</span>, I will call you.</p>
            </div>
            
            <h3 class="text-lg text-yellow-400 mb-2">Examples:</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300">
                <li><span class="text-blue-400">When</span> scientists find a solution, they will announce it.</li>
                <li><span class="text-blue-400">As soon as</span> the experiment ends, we'll analyze the results.</li>
                <li>I'll wait <span class="text-blue-400">until</span> the data is complete.</li>
                <li><span class="text-blue-400">Before</span> we start, we need to check the equipment.</li>
                <li><span class="text-blue-400">After</span> we finish, we'll write the report.</li>
                <li><span class="text-blue-400">If</span> the test succeeds, we'll continue the research.</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🔗 Cause & Effect Connectors</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Expressing Cause</h4>
                    <ul class="text-gray-300 space-y-2">
                        <li><span class="text-yellow-400">because</span> - The ice melted because temperatures rose.</li>
                        <li><span class="text-yellow-400">since/as</span> - Since pollution increased, air quality worsened.</li>
                        <li><span class="text-yellow-400">due to</span> - Due to climate change, weather is more extreme.</li>
                        <li><span class="text-yellow-400">because of</span> - Species are dying because of deforestation.</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Expressing Effect</h4>
                    <ul class="text-gray-300 space-y-2">
                        <li><span class="text-yellow-400">so</span> - It rained heavily, so the river flooded.</li>
                        <li><span class="text-yellow-400">therefore</span> - CO2 increased; therefore, temperatures rose.</li>
                        <li><span class="text-yellow-400">as a result</span> - Forests were cut. As a result, animals lost their homes.</li>
                        <li><span class="text-yellow-400">consequently</span> - The experiment failed; consequently, we started over.</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🧪 Science & Environment Vocabulary</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Scientific Method</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">hypothesis</span> - educated guess</li>
                        <li><span class="text-yellow-400">experiment</span> - test to prove something</li>
                        <li><span class="text-yellow-400">data</span> - collected information</li>
                        <li><span class="text-yellow-400">evidence</span> - proof</li>
                        <li><span class="text-yellow-400">conclusion</span> - final result</li>
                        <li><span class="text-yellow-400">research</span> - study of a topic</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Environment</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">climate change</span> - global warming</li>
                        <li><span class="text-yellow-400">pollution</span> - contamination</li>
                        <li><span class="text-yellow-400">renewable energy</span> - solar, wind</li>
                        <li><span class="text-yellow-400">carbon footprint</span> - CO2 we produce</li>
                        <li><span class="text-yellow-400">ecosystem</span> - community of living things</li>
                        <li><span class="text-yellow-400">biodiversity</span> - variety of life</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Technology</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">artificial intelligence</span> - AI</li>
                        <li><span class="text-yellow-400">breakthrough</span> - important discovery</li>
                        <li><span class="text-yellow-400">innovation</span> - new idea/method</li>
                        <li><span class="text-yellow-400">sustainable</span> - eco-friendly</li>
                        <li><span class="text-yellow-400">cutting-edge</span> - very modern</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Scientific Verbs</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">discover</span> - find something new</li>
                        <li><span class="text-yellow-400">analyze</span> - study carefully</li>
                        <li><span class="text-yellow-400">predict</span> - say what will happen</li>
                        <li><span class="text-yellow-400">prove</span> - show to be true</li>
                        <li><span class="text-yellow-400">develop</span> - create/improve</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-yellow-500/20 rounded-lg border border-yellow-500/50">
            <h2 class="text-xl text-yellow-400 mb-3">📝 Practice Exercises</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Make predictions with will, going to, or might:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I'm sure technology _____ change our lives. (will)</li>
                <li>Look at those dark clouds! It _____ storm. (is going to)</li>
                <li>Scientists _____ find a cure, but I'm not sure. (might)</li>
                <li>Based on the data, temperatures _____ rise by 2°C. (are going to)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Complete with the correct verb form:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>When scientists _____ (find) a solution, they will publish it. (find)</li>
                <li>I'll call you as soon as I _____ (arrive). (arrive)</li>
                <li>We won't start until everyone _____ (be) ready. (is)</li>
                <li>After we _____ (finish) the experiment, we'll clean up. (finish)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Join using cause/effect connectors:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>Forests are cut down. Animals lose their homes.
                    <span class="text-gray-400">(Because forests are cut down, animals lose their homes.)</span></li>
                <li>Pollution increased. Air quality worsened.
                    <span class="text-gray-400">(Pollution increased; therefore, air quality worsened.)</span></li>
                <li>Global warming / sea levels rising
                    <span class="text-gray-400">(Due to global warming, sea levels are rising.)</span></li>
            </ol>
        </section>
        
        <div class="mt-8 p-4 bg-green-500/20 rounded-lg border border-green-500/50">
            <p class="text-green-400 font-semibold">🎉 Complete this lesson to earn 50 XP!</p>
        </div>
    </div>
    """,
    
    "int9": """
    <div class="lesson-container max-w-4xl mx-auto p-6">
        <h1 class="text-3xl font-bold text-green-400 mb-4">📱 INTERMEDIATE 9 - Social Networks</h1>
        <p class="text-gray-300 mb-6">ICPNA Intermediate Level - CEFR B1/B2 | Reflexive Pronouns & Digital Communication</p>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-green-400 mb-3">🎯 Learning Objectives</h2>
            <ul class="list-disc pl-6 space-y-2">
                <li>Use reflexive pronouns correctly (myself, yourself, etc.)</li>
                <li>Distinguish reflexive vs. reciprocal pronouns (each other)</li>
                <li>Vocabulary: social media, digital communication, online interactions</li>
                <li>Discuss advantages and disadvantages of social networks</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🪞 Reflexive Pronouns</h2>
            
            <p class="text-gray-300 mb-4">Use when the subject and object are the same person:</p>
            
            <div class="overflow-x-auto mb-4">
                <table class="w-full text-gray-300">
                    <thead class="bg-white/10">
                        <tr>
                            <th class="p-2 text-left text-green-400">Subject</th>
                            <th class="p-2 text-left text-green-400">Reflexive</th>
                            <th class="p-2 text-left text-green-400">Example</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-white/10">
                            <td class="p-2">I</td>
                            <td class="p-2 text-yellow-400">myself</td>
                            <td class="p-2">I taught <span class="text-yellow-400">myself</span> to code.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">you</td>
                            <td class="p-2 text-yellow-400">yourself</td>
                            <td class="p-2">Did you hurt <span class="text-yellow-400">yourself</span>?</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">he</td>
                            <td class="p-2 text-yellow-400">himself</td>
                            <td class="p-2">He introduced <span class="text-yellow-400">himself</span> online.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">she</td>
                            <td class="p-2 text-yellow-400">herself</td>
                            <td class="p-2">She took a photo of <span class="text-yellow-400">herself</span>.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">it</td>
                            <td class="p-2 text-yellow-400">itself</td>
                            <td class="p-2">The app updates <span class="text-yellow-400">itself</span>.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">we</td>
                            <td class="p-2 text-yellow-400">ourselves</td>
                            <td class="p-2">We enjoyed <span class="text-yellow-400">ourselves</span> at the party.</td>
                        </tr>
                        <tr class="border-b border-white/10">
                            <td class="p-2">they</td>
                            <td class="p-2 text-yellow-400">themselves</td>
                            <td class="p-2">They protect <span class="text-yellow-400">themselves</span> online.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <h3 class="text-lg text-yellow-400 mb-2">Special Uses:</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300">
                <li><span class="text-green-400">Emphasis:</span> I did it <span class="text-yellow-400">myself</span>! (without help)</li>
                <li><span class="text-green-400">by + reflexive:</span> She lives <span class="text-yellow-400">by herself</span>. (alone)</li>
                <li><span class="text-green-400">Help yourself:</span> Help <span class="text-yellow-400">yourself</span> to some food. (take what you want)</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">🤝 Reflexive vs. Reciprocal (Each Other)</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded border-l-4 border-yellow-400">
                    <h4 class="text-yellow-400 mb-2">Reflexive (same person)</h4>
                    <p class="text-gray-300">They looked at <span class="text-yellow-400">themselves</span> in the mirror.</p>
                    <p class="text-sm text-gray-400">(each person looked at their own reflection)</p>
                </div>
                <div class="bg-white/5 p-3 rounded border-l-4 border-blue-400">
                    <h4 class="text-blue-400 mb-2">Reciprocal (different people)</h4>
                    <p class="text-gray-300">They looked at <span class="text-blue-400">each other</span>.</p>
                    <p class="text-sm text-gray-400">(person A looked at B, B looked at A)</p>
                </div>
            </div>
            
            <h3 class="text-lg text-yellow-400 mb-2">More examples:</h3>
            <ul class="list-disc pl-6 space-y-2 text-gray-300">
                <li>We message <span class="text-blue-400">each other</span> every day. (I message you, you message me)</li>
                <li>They follow <span class="text-blue-400">each other</span> on Instagram.</li>
                <li>We taught <span class="text-yellow-400">ourselves</span> Spanish. (each person learned alone)</li>
            </ul>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">📲 Social Media Vocabulary</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Actions</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">post</span> - share content</li>
                        <li><span class="text-yellow-400">like</span> - show approval</li>
                        <li><span class="text-yellow-400">comment</span> - write a response</li>
                        <li><span class="text-yellow-400">share/repost</span> - share others' content</li>
                        <li><span class="text-yellow-400">follow</span> - subscribe to someone</li>
                        <li><span class="text-yellow-400">unfollow</span> - stop following</li>
                        <li><span class="text-yellow-400">block</span> - prevent contact</li>
                        <li><span class="text-yellow-400">tag</span> - mention someone</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Content Types</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">selfie</span> - photo of yourself</li>
                        <li><span class="text-yellow-400">story</span> - temporary post (24h)</li>
                        <li><span class="text-yellow-400">reel/video</span> - short video</li>
                        <li><span class="text-yellow-400">meme</span> - funny image/video</li>
                        <li><span class="text-yellow-400">livestream</span> - live video</li>
                        <li><span class="text-yellow-400">thread</span> - connected posts</li>
                        <li><span class="text-yellow-400">DM</span> - direct message</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Platform Terms</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">profile</span> - your page</li>
                        <li><span class="text-yellow-400">feed</span> - content stream</li>
                        <li><span class="text-yellow-400">followers</span> - people who follow you</li>
                        <li><span class="text-yellow-400">algorithm</span> - content selection system</li>
                        <li><span class="text-yellow-400">trending</span> - popular now</li>
                        <li><span class="text-yellow-400">viral</span> - spreading fast</li>
                        <li><span class="text-yellow-400">hashtag (#)</span> - topic label</li>
                    </ul>
                </div>
                <div class="bg-white/5 p-3 rounded">
                    <h4 class="text-green-400 mb-2">Issues & Concerns</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li><span class="text-yellow-400">privacy</span> - keeping info private</li>
                        <li><span class="text-yellow-400">cyberbullying</span> - online harassment</li>
                        <li><span class="text-yellow-400">fake news</span> - false information</li>
                        <li><span class="text-yellow-400">addiction</span> - unable to stop using</li>
                        <li><span class="text-yellow-400">screen time</span> - hours on device</li>
                        <li><span class="text-yellow-400">digital detox</span> - break from tech</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-white/10 rounded-lg">
            <h2 class="text-xl text-blue-400 mb-3">⚖️ Advantages vs. Disadvantages</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-green-500/10 p-3 rounded border border-green-500/30">
                    <h4 class="text-green-400 mb-2">✅ Advantages</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li>• Stay connected with friends/family</li>
                        <li>• Meet people with similar interests</li>
                        <li>• Access to information quickly</li>
                        <li>• Platform for self-expression</li>
                        <li>• Business and networking opportunities</li>
                        <li>• Learn new skills for free</li>
                    </ul>
                </div>
                <div class="bg-red-500/10 p-3 rounded border border-red-500/30">
                    <h4 class="text-red-400 mb-2">❌ Disadvantages</h4>
                    <ul class="text-gray-300 space-y-1">
                        <li>• Privacy concerns</li>
                        <li>• Addiction and time waste</li>
                        <li>• Cyberbullying and negativity</li>
                        <li>• Fake news and misinformation</li>
                        <li>• Comparison and low self-esteem</li>
                        <li>• Less face-to-face interaction</li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section class="mb-8 p-4 bg-yellow-500/20 rounded-lg border border-yellow-500/50">
            <h2 class="text-xl text-yellow-400 mb-3">📝 Practice Exercises</h2>
            
            <h3 class="text-lg text-yellow-400 mb-3">Complete with reflexive pronouns:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>I taught _____ how to edit videos. (myself)</li>
                <li>She takes photos of _____ for Instagram. (herself)</li>
                <li>The app updated _____. (itself)</li>
                <li>We enjoyed _____ at the concert. (ourselves)</li>
                <li>Did you create this account _____? (yourself)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Choose: reflexive or each other?</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>They follow _____ on TikTok. (each other)</li>
                <li>He looked at _____ in the camera before going live. (himself)</li>
                <li>We send _____ memes every day. (each other)</li>
                <li>She introduced _____ to the audience. (herself)</li>
                <li>The twins always defend _____. (each other)</li>
            </ol>
            
            <h3 class="text-lg text-yellow-400 mt-6 mb-3">Match the social media term:</h3>
            <ol class="list-decimal pl-6 space-y-3">
                <li>A photo of yourself = _____ (selfie)</li>
                <li>Content that spreads quickly = _____ (viral)</li>
                <li>People who subscribe to your content = _____ (followers)</li>
                <li>A private message = _____ (DM)</li>
                <li>A break from technology = _____ (digital detox)</li>
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