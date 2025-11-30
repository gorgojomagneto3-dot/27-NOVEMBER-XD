from markupsafe import Markup

def get_b01_content_new():
    """
    BASIC 01 - A1 Inicial
    Basado en syllabus oficial ICPNA
    Temas: Personal introductions, names, countries, nationalities, favorites
    """
    return Markup("""
    <h1>🎯 BASIC 01 - Nivel A1 Inicial</h1>
    <p class="level-indicator">CEFR Level: A1 | ICPNA: Básico 1</p>
    
    <div class="learning-objectives">
        <h3>📋 Learning Objectives (Objetivos de Aprendizaje)</h3>
        <ul>
            <li>✅ Greet and introduce yourself using subject pronouns and possessive adjectives</li>
            <li>✅ Ask and answer yes/no questions about personal information</li>
            <li>✅ Talk about favorite TV shows, sports, and music</li>
            <li>✅ Describe places and cities using adjectives</li>
            <li>✅ Ask and answer wh-questions about countries and location</li>
        </ul>
    </div>

    <section id="unit1">
        <h2>📚 UNIT 1: MY FAVORITES</h2>
        
        <h3>🗣️ Lesson A: What's Your Name?</h3>
        
        <div class="grammar-section">
            <h4>Subject Pronouns (Pronombres Personales)</h4>
            <table>
                <thead>
                    <tr><th>English</th><th>Español</th><th>Example</th></tr>
                </thead>
                <tbody>
                    <tr><td>I</td><td>Yo</td><td>I am a student.</td></tr>
                    <tr><td>You</td><td>Tú / Usted</td><td>You are my friend.</td></tr>
                    <tr><td>He</td><td>Él</td><td>He is from Peru.</td></tr>
                    <tr><td>She</td><td>Ella</td><td>She is a teacher.</td></tr>
                    <tr><td>It</td><td>Eso (cosas/animales)</td><td>It is a beautiful city.</td></tr>
                    <tr><td>We</td><td>Nosotros</td><td>We are classmates.</td></tr>
                    <tr><td>They</td><td>Ellos/Ellas</td><td>They are friends.</td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="grammar-section">
            <h4>Possessive Adjectives (Adjetivos Posesivos)</h4>
            <table>
                <thead>
                    <tr><th>Subject</th><th>Possessive</th><th>Español</th><th>Example</th></tr>
                </thead>
                <tbody>
                    <tr><td>I</td><td>my</td><td>mi/mis</td><td>My name is Carlos.</td></tr>
                    <tr><td>You</td><td>your</td><td>tu/tus</td><td>What's your name?</td></tr>
                    <tr><td>He</td><td>his</td><td>su (de él)</td><td>His favorite sport is soccer.</td></tr>
                    <tr><td>She</td><td>her</td><td>su (de ella)</td><td>Her favorite singer is Adele.</td></tr>
                    <tr><td>It</td><td>its</td><td>su (de cosa)</td><td>Its capital is Lima.</td></tr>
                    <tr><td>We</td><td>our</td><td>nuestro/a</td><td>Our teacher is great.</td></tr>
                    <tr><td>They</td><td>their</td><td>su (de ellos)</td><td>Their house is big.</td></tr>
                </tbody>
            </table>
            
            <h5>Exercise: Complete with the correct possessive adjective</h5>
            <ol>
                <li>I have a dog. _____ name is Max. (My)</li>
                <li>She is Maria. _____ last name is Garcia. (Her)</li>
                <li>We are students. _____ school is ICPNA. (Our)</li>
                <li>They are from Brazil. _____ language is Portuguese. (Their)</li>
                <li>He is my brother. _____ favorite sport is basketball. (His)</li>
            </ol>
        </div>
        
        <div class="grammar-section">
            <h4>Verb BE - Contractions (Contracciones)</h4>
            <table>
                <thead>
                    <tr><th>Full Form</th><th>Contraction</th><th>Negative</th><th>Negative Contraction</th></tr>
                </thead>
                <tbody>
                    <tr><td>I am</td><td>I'm</td><td>I am not</td><td>I'm not</td></tr>
                    <tr><td>You are</td><td>You're</td><td>You are not</td><td>You aren't / You're not</td></tr>
                    <tr><td>He is</td><td>He's</td><td>He is not</td><td>He isn't / He's not</td></tr>
                    <tr><td>She is</td><td>She's</td><td>She is not</td><td>She isn't / She's not</td></tr>
                    <tr><td>It is</td><td>It's</td><td>It is not</td><td>It isn't / It's not</td></tr>
                    <tr><td>We are</td><td>We're</td><td>We are not</td><td>We aren't / We're not</td></tr>
                    <tr><td>They are</td><td>They're</td><td>They are not</td><td>They aren't / They're not</td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="speaking-section">
            <h4>Greetings & Introductions (Saludos y Presentaciones)</h4>
            <h5>Formal:</h5>
            <ul>
                <li>Hello, I'm [name]. Nice to meet you. → Hello, I'm Carlos. Nice to meet you.</li>
                <li>Good morning/afternoon/evening. → Good morning, how are you?</li>
                <li>How do you do? → How do you do? (formal response: same phrase)</li>
            </ul>
            
            <h5>Informal:</h5>
            <ul>
                <li>Hi! I'm [name]. → Hi! I'm Ana.</li>
                <li>Hey, what's up? → Hey! Not much, you?</li>
                <li>Nice to meet you! → Nice to meet you too!</li>
            </ul>
            
            <h5>Personal Information Questions:</h5>
            <ul>
                <li>What's your name? → My name is _______. / I'm _______.</li>
                <li>What's your last name? → My last name is _______.</li>
                <li>How do you spell that? → It's M-A-R-T-I-N-E-Z.</li>
                <li>Where are you from? → I'm from Lima, Peru.</li>
                <li>What do you do? → I'm a student. / I work as a _______.</li>
                <li>How old are you? → I'm _______ years old.</li>
            </ul>
        </div>
        
        <h3>🗣️ Lesson B: Introductions & Favorites</h3>
        
        <div class="vocab-section">
            <h4>Vocabulary: Relationships</h4>
            <ul>
                <li>Who are you friends with? → I'm friends with _______ and _______.</li>
                <li>Who's your best friend? → My best friend is _________.</li>
                <li>Who's your boyfriend/girlfriend? → _____ is my boyfriend/girlfriend.</li>
                <li>Who do you live with? → I live with _____. She's my roommate.</li>
                <li>Are you married? → Yes, I am. / No, I'm single.</li>
            </ul>
            
            <h4>Vocabulary: Sports</h4>
            <ul>
                <li>What's your favorite sport? → My favorite sport is _______.</li>
            </ul>
            <p><strong>Sports vocabulary:</strong> soccer, basketball, volleyball, tennis, swimming, running, cycling, boxing, skateboarding, surfing, baseball, golf</p>
            
            <h4>Vocabulary: Music</h4>
            <ul>
                <li>What's your favorite kind of music? → My favorite kind of music is _____.</li>
                <li>Who's your favorite singer? → My favorite singer is ______________.</li>
                <li>What's your favorite song? → My favorite song is ______________.</li>
            </ul>
            <p><strong>Music genres:</strong> Pop, Rock, Hip-Hop/Rap, R&B, Electronic, Classical, Jazz, Reggaeton, Salsa, Metal</p>
            
            <h4>Vocabulary: Movies & TV</h4>
            <ul>
                <li>What's your favorite movie? → My favorite movie is __________________.</li>
                <li>What kind of movies do you like? → I like _______ movies.</li>
                <li>What's your favorite TV show? → My favorite TV show is _________________.</li>
            </ul>
            <p><strong>Movie genres:</strong> Action, Comedy, Drama, Horror, Sci-fi, Romance, Thriller, Documentary</p>
            <p><strong>TV shows:</strong> Sitcom, Reality show, Documentary, News, Cartoon, Drama series, Talk show</p>
        </div>
        
        <div class="grammar-section">
            <h4>Yes/No Questions with BE</h4>
            <p><strong>Structure:</strong> BE + Subject + Complement?</p>
            
            <table>
                <thead>
                    <tr><th>Question</th><th>Yes Answer</th><th>No Answer</th></tr>
                </thead>
                <tbody>
                    <tr><td>Am I late?</td><td>Yes, you are.</td><td>No, you aren't.</td></tr>
                    <tr><td>Are you a student?</td><td>Yes, I am.</td><td>No, I'm not.</td></tr>
                    <tr><td>Is he from Peru?</td><td>Yes, he is.</td><td>No, he isn't.</td></tr>
                    <tr><td>Is she a teacher?</td><td>Yes, she is.</td><td>No, she isn't.</td></tr>
                    <tr><td>Is it expensive?</td><td>Yes, it is.</td><td>No, it isn't.</td></tr>
                    <tr><td>Are we ready?</td><td>Yes, we are.</td><td>No, we aren't.</td></tr>
                    <tr><td>Are they married?</td><td>Yes, they are.</td><td>No, they aren't.</td></tr>
                </tbody>
            </table>
            
            <h5>Exercise: Complete with the correct form of BE</h5>
            <ol>
                <li>_____ you a teacher? → Yes, I am. (Are)</li>
                <li>_____ she from Mexico? → No, she isn't. (Is)</li>
                <li>_____ they your friends? → Yes, they are. (Are)</li>
                <li>_____ he married? → No, he isn't. (Is)</li>
                <li>_____ I late for class? → No, you aren't. (Am)</li>
                <li>_____ it a good movie? → Yes, it is. (Is)</li>
                <li>_____ we in the right classroom? → Yes, we are. (Are)</li>
                <li>_____ you Peruvian? → Yes, I am. (Are)</li>
            </ol>
        </div>
    </section>

    <section id="unit2">
        <h2>🌍 UNIT 2: COUNTRIES</h2>
        
        <h3>🗣️ Lesson A: Around the World</h3>
        
        <div class="vocab-section">
            <h4>Continents</h4>
            <p>North America, South America, Central America, Europe, Asia, Africa, Oceania, Antarctica</p>
            
            <h4>Countries, Nationalities & Languages</h4>
            <table>
                <thead>
                    <tr><th>Country</th><th>Nationality</th><th>Language</th></tr>
                </thead>
                <tbody>
                    <tr><td>Peru</td><td>Peruvian</td><td>Spanish</td></tr>
                    <tr><td>United States</td><td>American</td><td>English</td></tr>
                    <tr><td>Brazil</td><td>Brazilian</td><td>Portuguese</td></tr>
                    <tr><td>France</td><td>French</td><td>French</td></tr>
                    <tr><td>Germany</td><td>German</td><td>German</td></tr>
                    <tr><td>Japan</td><td>Japanese</td><td>Japanese</td></tr>
                    <tr><td>China</td><td>Chinese</td><td>Chinese/Mandarin</td></tr>
                    <tr><td>Italy</td><td>Italian</td><td>Italian</td></tr>
                    <tr><td>Spain</td><td>Spanish</td><td>Spanish</td></tr>
                    <tr><td>United Kingdom</td><td>British</td><td>English</td></tr>
                    <tr><td>Mexico</td><td>Mexican</td><td>Spanish</td></tr>
                    <tr><td>Argentina</td><td>Argentinian</td><td>Spanish</td></tr>
                    <tr><td>Colombia</td><td>Colombian</td><td>Spanish</td></tr>
                    <tr><td>Australia</td><td>Australian</td><td>English</td></tr>
                </tbody>
            </table>
            
            <h5>Questions about origin:</h5>
            <ul>
                <li>Where are you from? → I'm from Lima, Peru.</li>
                <li>What's your nationality? → I'm Peruvian.</li>
                <li>What language do you speak? → I speak Spanish and English.</li>
                <li>Where is [country]? → [Country] is in [continent].</li>
                <li>What's the capital of [country]? → The capital of [country] is [city].</li>
            </ul>
        </div>
        
        <div class="grammar-section">
            <h4>Wh- Questions with BE</h4>
            <p><strong>Structure:</strong> Wh-word + BE + Subject + (Complement)?</p>
            
            <table>
                <thead>
                    <tr><th>Wh-word</th><th>Use</th><th>Example</th></tr>
                </thead>
                <tbody>
                    <tr><td>What</td><td>Things/Information</td><td>What is your name?</td></tr>
                    <tr><td>Where</td><td>Places</td><td>Where are you from?</td></tr>
                    <tr><td>Who</td><td>People</td><td>Who is your best friend?</td></tr>
                    <tr><td>How</td><td>Manner/State</td><td>How are you?</td></tr>
                    <tr><td>How old</td><td>Age</td><td>How old are you?</td></tr>
                    <tr><td>Which</td><td>Choice</td><td>Which city is your favorite?</td></tr>
                </tbody>
            </table>
            
            <h5>Exercise: Complete with the correct Wh-word</h5>
            <ol>
                <li>_____ is Machu Picchu? → It's in Peru. (Where)</li>
                <li>_____ is your teacher? → Ms. Rodriguez. (Who)</li>
                <li>_____ is your favorite sport? → Soccer. (What)</li>
                <li>_____ old are you? → I'm 25 years old. (How)</li>
                <li>_____ are you from? → I'm from Lima. (Where)</li>
                <li>_____ country do you prefer? → I prefer Japan. (Which)</li>
            </ol>
        </div>
        
        <div class="grammar-section">
            <h4>Prepositions of Place: in / on / at</h4>
            <ul>
                <li><strong>IN</strong> → countries, cities, continents, rooms: I live in Peru. She is in the kitchen.</li>
                <li><strong>ON</strong> → streets, floors: I live on Main Street. My office is on the 5th floor.</li>
                <li><strong>AT</strong> → specific addresses, locations: I'm at 123 Main St. I'm at school/work/home.</li>
            </ul>
            
            <h5>Exercise: Complete with in, on, or at</h5>
            <ol>
                <li>I live _____ Lima. (in)</li>
                <li>She works _____ Javier Prado Avenue. (on)</li>
                <li>He's _____ home right now. (at)</li>
                <li>The book is _____ the table. (on)</li>
                <li>We're _____ the classroom. (in)</li>
                <li>Meet me _____ the coffee shop. (at)</li>
                <li>Peru is _____ South America. (in)</li>
                <li>I'm _____ 456 Oak Street. (at)</li>
            </ol>
        </div>
        
        <h3>🗣️ Lesson B: It's a Big City</h3>
        
        <div class="vocab-section">
            <h4>Adjectives to Describe Places</h4>
            
            <h5>Positive Adjectives:</h5>
            <p>beautiful, big, modern, clean, safe, interesting, quiet, relaxing, friendly, famous</p>
            
            <h5>Negative Adjectives:</h5>
            <p>ugly, small, old, dirty, dangerous, boring, noisy, crowded, expensive</p>
            
            <h5>Opposites:</h5>
            <table>
                <thead><tr><th>Adjective</th><th>Opposite</th></tr></thead>
                <tbody>
                    <tr><td>big</td><td>small</td></tr>
                    <tr><td>old</td><td>new/modern</td></tr>
                    <tr><td>clean</td><td>dirty</td></tr>
                    <tr><td>safe</td><td>dangerous</td></tr>
                    <tr><td>quiet</td><td>noisy</td></tr>
                    <tr><td>expensive</td><td>cheap</td></tr>
                    <tr><td>beautiful</td><td>ugly</td></tr>
                    <tr><td>interesting</td><td>boring</td></tr>
                </tbody>
            </table>
        </div>
        
        <div class="grammar-section">
            <h4>Adjectives with BE</h4>
            <p><strong>Structure:</strong> Subject + BE + Adjective</p>
            <ul>
                <li>Lima is big and modern.</li>
                <li>The beaches are beautiful.</li>
                <li>This restaurant is expensive.</li>
            </ul>
            
            <h4>Conjunctions: AND / BUT</h4>
            <ul>
                <li><strong>AND</strong> = connects similar ideas: The city is big AND modern.</li>
                <li><strong>BUT</strong> = connects contrasting ideas: The hotel is nice BUT expensive.</li>
            </ul>
            
            <h5>Exercise: Complete with AND or BUT</h5>
            <ol>
                <li>Tokyo is big _____ modern. (and)</li>
                <li>The hotel is beautiful _____ expensive. (but)</li>
                <li>Paris is interesting _____ crowded. (but)</li>
                <li>The beach is clean _____ relaxing. (and)</li>
                <li>My city is small _____ safe. (but)</li>
                <li>The food is delicious _____ cheap. (and)</li>
            </ol>
        </div>
        
        <div class="speaking-section">
            <h4>Describing Your City</h4>
            <ul>
                <li>What's your city like? → My city is big and modern.</li>
                <li>Is it safe? → Yes, it is. / No, it isn't very safe.</li>
                <li>What's the weather like? → It's usually warm and sunny.</li>
                <li>What's your favorite place? → My favorite place is the beach because it's relaxing.</li>
            </ul>
        </div>
    </section>
    
    <section id="unit3">
        <h2>🎁 UNIT 3: POSSESSIONS</h2>
        
        <h3>🗣️ Lesson A: Gifts</h3>
        
        <div class="vocab-section">
            <h4>Personal Items & Everyday Objects</h4>
            
            <h5>In your bag:</h5>
            <p>wallet, keys, phone, headphones, charger, notebook, pen, water bottle, sunglasses, umbrella</p>
            
            <h5>Electronics:</h5>
            <p>laptop, tablet, camera, watch, earbuds, power bank</p>
            
            <h5>Personal care:</h5>
            <p>comb, makeup, lipstick, perfume, tissues</p>
            
            <h5>Documents:</h5>
            <p>ID card, driver's license, passport, credit card</p>
            
            <h5>Questions:</h5>
            <ul>
                <li>What do you have in your bag? → I have my phone, wallet, and keys.</li>
                <li>What do you always carry with you? → I always carry my phone.</li>
                <li>Do you have a _____? → Yes, I do. / No, I don't.</li>
            </ul>
        </div>
        
        <div class="grammar-section">
            <h4>Articles: A / AN</h4>
            <ul>
                <li><strong>A</strong> → before consonant sounds: a book, a car, a university (sounds like "you")</li>
                <li><strong>AN</strong> → before vowel sounds: an apple, an hour (h is silent), an umbrella</li>
            </ul>
            
            <h5>Exercise: Complete with A or AN</h5>
            <ol>
                <li>It's _____ backpack. (a)</li>
                <li>She has _____ umbrella. (an)</li>
                <li>He's _____ engineer. (an)</li>
                <li>That's _____ university. (a)</li>
                <li>I need _____ hour to finish. (an)</li>
                <li>She's _____ honest person. (an)</li>
                <li>It's _____ European country. (a)</li>
                <li>I have _____ idea. (an)</li>
            </ol>
        </div>
        
        <div class="grammar-section">
            <h4>Demonstratives: This / That / These / Those</h4>
            <table>
                <thead>
                    <tr><th></th><th>Singular</th><th>Plural</th></tr>
                </thead>
                <tbody>
                    <tr><td><strong>Near</strong></td><td>this (este/a)</td><td>these (estos/as)</td></tr>
                    <tr><td><strong>Far</strong></td><td>that (ese/a)</td><td>those (esos/as)</td></tr>
                </tbody>
            </table>
            
            <ul>
                <li>This is my phone. (near, singular)</li>
                <li>That is your bag. (far, singular)</li>
                <li>These are my keys. (near, plural)</li>
                <li>Those are her books. (far, plural)</li>
            </ul>
            
            <h5>Exercise: Complete with this, that, these, or those</h5>
            <ol>
                <li>_____ is my book (here on my desk). (This)</li>
                <li>_____ are your glasses (over there). (Those)</li>
                <li>_____ is a beautiful house (across the street). (That)</li>
                <li>_____ are my friends (here next to me). (These)</li>
            </ol>
        </div>
        
        <div class="grammar-section">
            <h4>Plural Nouns</h4>
            
            <h5>Rules:</h5>
            <table>
                <thead><tr><th>Rule</th><th>Singular</th><th>Plural</th></tr></thead>
                <tbody>
                    <tr><td>Add -s (most nouns)</td><td>book</td><td>books</td></tr>
                    <tr><td>Add -es (s, sh, ch, x, z)</td><td>bus, watch</td><td>buses, watches</td></tr>
                    <tr><td>Consonant + y → -ies</td><td>city, baby</td><td>cities, babies</td></tr>
                    <tr><td>Vowel + y → -s</td><td>key, day</td><td>keys, days</td></tr>
                    <tr><td>f/fe → -ves</td><td>knife, leaf</td><td>knives, leaves</td></tr>
                    <tr><td>Irregular</td><td>man, woman, child</td><td>men, women, children</td></tr>
                </tbody>
            </table>
            
            <h5>Exercise: Write the plural</h5>
            <ol>
                <li>phone → _______ (phones)</li>
                <li>watch → _______ (watches)</li>
                <li>country → _______ (countries)</li>
                <li>key → _______ (keys)</li>
                <li>child → _______ (children)</li>
                <li>box → _______ (boxes)</li>
            </ol>
        </div>
        
        <div class="speaking-section">
            <h4>Giving & Receiving Thanks</h4>
            
            <h5>Thanking:</h5>
            <ul>
                <li>Thank you very much!</li>
                <li>Thanks a lot!</li>
                <li>Thanks so much! I love it!</li>
            </ul>
            
            <h5>Responding:</h5>
            <ul>
                <li>You're welcome!</li>
                <li>My pleasure!</li>
                <li>No problem!</li>
                <li>Anytime!</li>
            </ul>
        </div>
    </section>
    
    <section id="review">
        <h2>📝 BASIC 01 - REVIEW & PRACTICE</h2>
        
        <div class="grammar-section">
            <h4>Complete Review Exercise</h4>
            <ol>
                <li>_____ name is Carlos. I'm from Peru. (My)</li>
                <li>Where _____ you from? (are)</li>
                <li>She _____ a student at ICPNA. (is)</li>
                <li>_____ is your favorite movie? (What)</li>
                <li>Lima is big _____ modern. (and)</li>
                <li>I have _____ umbrella in my bag. (an)</li>
                <li>_____ are my keys (here). (These)</li>
                <li>There are three _____ in my class. (women)</li>
                <li>Tokyo is safe _____ expensive. (but)</li>
                <li>_____ old are you? (How)</li>
            </ol>
        </div>
        
        <div class="communication-section">
            <h4>Speaking Practice: Introduce Yourself</h4>
            <p>Practice this introduction out loud:</p>
            <div class="dialogue-box">
                <p>Hello! My name is _______.</p>
                <p>I'm from _______, _______.</p>
                <p>I'm _______ years old.</p>
                <p>I'm a _______.</p>
                <p>My favorite sport is _______.</p>
                <p>My favorite kind of music is _______.</p>
                <p>Nice to meet you!</p>
            </div>
        </div>
    </section>
    """)
