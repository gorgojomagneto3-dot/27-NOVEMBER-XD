from flask import Flask, render_template, abort
from markupsafe import Markup
from b02_content import get_b02_content
from b03_content import get_b03_content
from b04_content import get_b04_content
from b05_content import get_b05_content
from b06_content import get_b06_content
from b07_content import get_b07_content
from b08_content import get_b08_content
from b09_content import get_b09_content
from b10_content import get_b10_content
from b11_content import get_b11_content
from b12_content import get_b12_content

app = Flask(__name__)

def get_b01_content():
    return Markup("""
    <h1>WorldLink Basic 01 - Complete Course Content</h1>
    
    <section id="unit1">
        <h2>UNIT 1: MY FAVORITES</h2>
        
        <h3>Lesson B: Introductions</h3>
        
        <h4>Personal Information Topics:</h4>
        <ul>
            <li>Full name</li>
            <li>Hometown</li>
            <li>Birthday</li>
            <li>Occupation</li>
            <li>Friends</li>
            <li>Marital status</li>
            <li>Favorite sports</li>
            <li>Favorite kinds of music</li>
            <li>Favorite artists</li>
            <li>Favorite TV shows</li>
        </ul>
        
        <h4>1. VOCABULARY</h4>
        
        <div class="vocab-section">
            <h5>Relationships:</h5>
            <ul>
                <li>Who are you friends with? → I'm friends with _______ and _______.</li>
                <li>Who's your best friend? → My best friend is _________.</li>
                <li>Who's your boyfriend/girlfriend? → _____ is my girlfriend.</li>
                <li>Who do you live with? → I live with _____. She's my roommate.</li>
            </ul>
            
            <h5>Sports:</h5>
            <ul>
                <li>What's your favorite sport? → My favorite sport is _______.</li>
                <li><strong>Examples:</strong> Soccer, basketball, volleyball, roller skating, tennis, bowling, skateboarding, swimming, boxing, cycling</li>
            </ul>
            
            <h5>Music:</h5>
            <ul>
                <li>What's your favorite kind of music? → My favorite kind of music is _____. / _____ is my favorite kind of music.</li>
                <li><strong>Examples:</strong> Pop, Rap/Hip-Hop, Rock, R&B, Metal, Electronic, Classical, Jazz, Soul/Blues</li>
                <li>Who's your favorite singer? → My favorite singer is ______________.</li>
                <li>What's your favorite song? → My favorite song is ______________.</li>
            </ul>
            
            <h5>Movies:</h5>
            <ul>
                <li>What's your favorite movie? → My favorite movie is __________________.</li>
                <li>What's your favorite kind of movie? → My favorite kind of movie is _______.</li>
                <li><strong>Examples:</strong> Action, Thriller, War, Sci-fi, Crime, Comedy, Romantic, Drama, Horror</li>
                <li>Who's your favorite actor/actress? → My favorite actor/actress is ______________.</li>
            </ul>
            
            <h5>TV Shows:</h5>
            <ul>
                <li>What's your favorite TV show? → My favorite TV show is _________________.</li>
                <li>What kind of TV programs do you like to watch? → I like to watch __________________.</li>
                <li><strong>Examples:</strong> Documentary, Sports, Soap Opera, Sitcom, Reality show, Local news, Cartoon, Drama, Late Night Show</li>
            </ul>
        </div>
        
        <h4>2. LISTENING</h4>
        <div class="listening-section">
            <h5>Listening Strategies:</h5>
            <ul>
                <li><strong>Listen for gist:</strong> Pay attention to the main idea.</li>
                <li><strong>Listen for details:</strong> Pay attention to specific information.</li>
            </ul>
        </div>
        
        <h4>3. READING</h4>
        <div class="reading-section">
            <h5>Famous Name Changers:</h5>
            <ul>
                <li>Pitbull: Real name is Armando Christian Perez</li>
                <li>Katy Perry: Real name is Katheryn Hudson</li>
            </ul>
            <p><strong>Do you like your name?</strong></p>
            <ul>
                <li>Yes, I do. I really like my name.</li>
                <li>No, I don't. I'd like to be named ______.</li>
            </ul>
        </div>
        
        <h4>4. GRAMMAR: Yes/No Questions with BE</h4>
        <div class="grammar-section">
            <p><strong>Structure:</strong> BE + Subject + Complement?</p>
            
            <table>
                <thead>
                    <tr>
                        <th>Subject Pronoun</th>
                        <th>BE Verb</th>
                        <th>Yes Answer</th>
                        <th>No Answer</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>I</td>
                        <td>am</td>
                        <td>Yes, I am.</td>
                        <td>No, I'm not.</td>
                    </tr>
                    <tr>
                        <td>You</td>
                        <td>are</td>
                        <td>Yes, you are.</td>
                        <td>No, you aren't.</td>
                    </tr>
                    <tr>
                        <td>He/She/It</td>
                        <td>is</td>
                        <td>Yes, he/she/it is.</td>
                        <td>No, he/she/it isn't.</td>
                    </tr>
                    <tr>
                        <td>We/They</td>
                        <td>are</td>
                        <td>Yes, we/they are.</td>
                        <td>No, we/they aren't.</td>
                    </tr>
                </tbody>
            </table>
            
            <h5>Exercise: Make questions using the correct form of "Be"</h5>
            <ol>
                <li>______ you a teacher? (Are)</li>
                <li>______ I late for the class? (Am)</li>
                <li>______ he Patrick? (Is)</li>
                <li>______ you Danna? (Are)</li>
                <li>______ your friends at the park? (Are)</li>
                <li>______ Messi from Mexico? (Is)</li>
                <li>______ they married? (Are)</li>
                <li>______ you peruvian? (Are)</li>
            </ol>
        </div>
        
        <h4>5. WRITING</h4>
        <div class="writing-section">
            <h5>Write about your favorite celebrity:</h5>
            <ul>
                <li>Who is your favorite_______? My favorite_______ is ______.</li>
                <li>What's his/her real name? His/her real name is ______.</li>
                <li>What's his/her nickname? His/her nickname is ______.</li>
                <li>Is he/she peruvian? Yes, he/she is. | No, he/she isn't. He/She is_______.</li>
                <li>Who is he/she friends with? He/she is friends with______.</li>
                <li>What's his/her favorite sport? His/her favorite sport is______.</li>
                <li>What's his/her favorite kind of music? His/her favorite kind of music is______.</li>
            </ul>
        </div>
        
        <h4>6. COMMUNICATION</h4>
        <div class="communication-section">
            <h5>Find your partner activity:</h5>
            <p>Is Rihanna your favorite singer? → No, she isn't. / Yes, she is.</p>
        </div>
    </section>
    
    <section id="unit2">
        <h2>UNIT 2: COUNTRIES</h2>
        
        <h3>Lesson A: Around the World</h3>
        
        <h4>Unit Goals:</h4>
        <ol>
            <li>Name cities and countries.</li>
            <li>Ask questions about people and places.</li>
            <li>Identify adjectives and nouns.</li>
            <li>Describe a city.</li>
        </ol>
        
        <h4>Vocabulary:</h4>
        <ul>
            <li>mountain, beach, building, city</li>
        </ul>
        
        <h5>Compass Directions:</h5>
        <p>North, West, East, South</p>
        
        <h5>Continents:</h5>
        <p>South America, North America, Central America & the Caribbean, Africa, Oceania, Asia, Europe, The Middle East, Antarctica</p>
        
        <h5>Countries & Capitals:</h5>
        <ul>
            <li>What's the capital city of _____? → _____ is the capital of _____.</li>
            <li>Where's _____? → _____ is in _________.</li>
            <li><strong>Example:</strong> What's the capital city of Peru? Lima is the capital of Peru. Where's Peru? Peru is in South America.</li>
        </ul>
        
        <h4>Nationalities & Languages:</h4>
        
        <table>
            <thead>
                <tr>
                    <th>Region</th>
                    <th>Country</th>
                    <th>Nationality</th>
                    <th>Language</th>
                </tr>
            </thead>
            <tbody>
                <tr><td colspan="4"><strong>North America</strong></td></tr>
                <tr><td></td><td>The United States</td><td>American</td><td>English</td></tr>
                <tr><td></td><td>Canada</td><td>Canadian</td><td>English/French</td></tr>
                <tr><td></td><td>Mexico</td><td>Mexican</td><td>Spanish</td></tr>
                <tr><td colspan="4"><strong>Central America</strong></td></tr>
                <tr><td></td><td>Guatemala</td><td>Guatemalan</td><td>Spanish</td></tr>
                <tr><td></td><td>Costa Rica</td><td>Costa Rican</td><td>Spanish</td></tr>
                <tr><td></td><td>Panama</td><td>Panamanian</td><td>Spanish</td></tr>
                <tr><td></td><td>Jamaica</td><td>Jamaican</td><td>English</td></tr>
                <tr><td></td><td>Cuba</td><td>Cuban</td><td>Spanish</td></tr>
                <tr><td colspan="4"><strong>South America</strong></td></tr>
                <tr><td></td><td>Colombia</td><td>Colombian</td><td>Spanish</td></tr>
                <tr><td></td><td>Ecuador</td><td>Ecuadorian</td><td>Spanish</td></tr>
                <tr><td></td><td>Peru</td><td>Peruvian</td><td>Spanish</td></tr>
                <tr><td></td><td>Chile</td><td>Chilean</td><td>Spanish</td></tr>
                <tr><td></td><td>Argentina</td><td>Argentinian</td><td>Spanish</td></tr>
                <tr><td></td><td>Brazil</td><td>Brazilian</td><td>Portuguese</td></tr>
                <tr><td></td><td>Venezuela</td><td>Venezuelan</td><td>Spanish</td></tr>
                <tr><td colspan="4"><strong>Europe</strong></td></tr>
                <tr><td></td><td>The United Kingdom</td><td>British</td><td>English</td></tr>
                <tr><td></td><td>France</td><td>French</td><td>French</td></tr>
                <tr><td></td><td>Portugal</td><td>Portuguese</td><td>Portuguese</td></tr>
                <tr><td></td><td>Spain</td><td>Spanish</td><td>Spanish</td></tr>
                <tr><td></td><td>Italy</td><td>Italian</td><td>Italian</td></tr>
                <tr><td></td><td>Germany</td><td>German</td><td>German</td></tr>
                <tr><td colspan="4"><strong>Middle East</strong></td></tr>
                <tr><td></td><td>Syria</td><td>Syrian</td><td>Arabic</td></tr>
                <tr><td></td><td>Israel</td><td>Israeli</td><td>Hebrew/Arabic</td></tr>
                <tr><td></td><td>Saudi Arabia</td><td>Saudi Arabian</td><td>Arabic</td></tr>
                <tr><td></td><td>The U.A.E.</td><td>Emirati</td><td>Arabic</td></tr>
                <tr><td colspan="4"><strong>Africa</strong></td></tr>
                <tr><td></td><td>Morocco</td><td>Moroccan</td><td>Arabic/French</td></tr>
                <tr><td></td><td>Nigeria</td><td>Nigerian</td><td>English</td></tr>
                <tr><td></td><td>South Africa</td><td>South African</td><td>Multiple</td></tr>
                <tr><td colspan="4"><strong>Asia</strong></td></tr>
                <tr><td></td><td>China</td><td>Chinese</td><td>Chinese</td></tr>
                <tr><td></td><td>Japan</td><td>Japanese</td><td>Japanese</td></tr>
                <tr><td></td><td>South Korea</td><td>South Korean</td><td>Korean</td></tr>
                <tr><td></td><td>India</td><td>Indian</td><td>Hindi/English</td></tr>
                <tr><td colspan="4"><strong>Oceania</strong></td></tr>
                <tr><td></td><td>Australia</td><td>Australian</td><td>English</td></tr>
                <tr><td></td><td>New Zealand</td><td>New Zealander</td><td>English</td></tr>
            </tbody>
        </table>
        
        <h5>Questions:</h5>
        <ul>
            <li>Where are you from? → I'm from _____, _____. (city) (country)</li>
            <li>What's your nationality? → I'm _____.</li>
            <li>What language(s) do you speak? → I speak _____.</li>
        </ul>
        
        <h5>Word Stress Examples:</h5>
        <ul>
            <li>Australia → Australian</li>
            <li>China → Chinese</li>
            <li>Brazil → Brazilian</li>
            <li>Mexico → Mexican</li>
        </ul>
        
        <h4>3. LISTENING</h4>
        <div class="listening-section">
            <h5>Did you know? Facts:</h5>
            <ul>
                <li>Ottawa is the capital of Canada</li>
                <li>The UK is 4 countries in 1</li>
                <li>People from New Zealand are called Kiwi</li>
                <li>France is #1 in tourism</li>
                <li>Machu Picchu is in Peru</li>
                <li>The Mekong River is in Vietnam</li>
            </ul>
            
            <h5>Checking Predictions:</h5>
            <ul>
                <li>That's right. / That's correct.</li>
                <li>That's wrong. / That's incorrect.</li>
            </ul>
        </div>
        
        <h4>4. SPEAKING</h4>
        <div class="speaking-section">
            <h5>Asking where someone is from:</h5>
            <ul>
                <li>Where are you from? → I'm from ______.</li>
                <li>Are you ___________? (nationality) → Yes, I am. / No, I'm from _____. (country)</li>
            </ul>
            
            <h5>Asking for specifics:</h5>
            <ul>
                <li>Really? Which city?</li>
                <li>Where exactly?</li>
                <li>Where in _____?</li>
                <li>Whereabouts in _____?</li>
            </ul>
        </div>
        
        <h4>5. GRAMMAR</h4>
        <div class="grammar-section">
            <h5>Wh- Questions: Who & Where</h5>
            <p><strong>Use Who for people. Use Where for places.</strong></p>
            <p><strong>Structure:</strong> Wh- + Verb Be + Subject + (Complement)?</p>
            
            <h6>Where Questions:</h6>
            <ul>
                <li>Where are the pyramids? → They are in Egypt.</li>
                <li>Where is the Statue of Liberty? → It is in the United States.</li>
            </ul>
            
            <h6>Who Questions:</h6>
            <ul>
                <li>Who is she? → She is the teacher.</li>
                <li>Who are they? → They are my classmates.</li>
            </ul>
            
            <h5>Exercise: Complete with "Who" or "Where"</h5>
            <ol>
                <li>________ is Machu Picchu? (Where)</li>
                <li>________ is with you? (Who)</li>
                <li>________ is the Great Wall? (Where)</li>
                <li>________ is the teacher? (Who)</li>
                <li>________ are the Iguazu Falls? (Where)</li>
                <li>________ is your best friend? (Who)</li>
                <li>________ are they? (Who)</li>
                <li>________ is ICPNA? (Where)</li>
                <li>________ are your classmates? (Where)</li>
                <li>________ is he? (Who)</li>
            </ol>
            
            <h5>Prepositions of Place: in / on / at</h5>
            <ul>
                <li><strong>in:</strong> general (I live in Miraflores.)</li>
                <li><strong>on:</strong> specific street/avenue (I live on Arequipa Avenue.)</li>
                <li><strong>at:</strong> specific address/location (I live at 253 Arequipa Avenue.)</li>
            </ul>
            
            <h5>Exercise: Complete with in, on, or at</h5>
            <ol>
                <li>Tim & Jill are _____ Larcomar. (at)</li>
                <li>Linda is _____ the street. (on)</li>
                <li>I'm _____ home. (at)</li>
                <li>Mario is _____ the classroom. (in)</li>
                <li>My friend is _____ school. (at)</li>
                <li>I'm _____ Javier Prado Avenue. (on)</li>
                <li>He is _____ Australia. (in)</li>
                <li>We are _____ work now. (at)</li>
                <li>They're _____ Buenos Aires. (in)</li>
                <li>She is _____ the university. (at)</li>
            </ol>
        </div>
        
        <h3>Lesson B: It's a Big City</h3>
        
        <h4>Vocabulary: Adjectives</h4>
        
        <h5>Positive:</h5>
        <p>beautiful, big/large, busy, interesting, clean, modern, expensive, crowded, safe, quiet, relaxing</p>
        
        <h5>Negative:</h5>
        <p>boring, old, dirty, empty, inexpensive, small, dangerous, ugly</p>
        
        <h5>Asking about opposites:</h5>
        <ul>
            <li>What's the opposite of ____? → The opposite of ____ is _____.</li>
            <li><strong>Example:</strong> What's the opposite of hot? → The opposite of hot is cold.</li>
        </ul>
        
        <h5>Cities Mentioned:</h5>
        <p>Havana, Amsterdam, Marrakech, Lisbon, Singapore, Venice, Hong Kong, Varanasi, Quito, Cuzco</p>
        
        <h5>Questions:</h5>
        <ul>
            <li>What's your city like? → My city is _________. (adjective)</li>
            <li>What's your country like? → My country is _________.</li>
            <li>What's ______ like? → ______ is ______. (city) (adjective)</li>
        </ul>
        
        <h4>2. LISTENING</h4>
        <div class="listening-section">
            <h5>Blogging:</h5>
            <ul>
                <li>Do you read blogs? → Yes, I usually read them. / No, I don't like blogs.</li>
                <li>What do bloggers post? → Bloggers post about _____. (idea)</li>
            </ul>
        </div>
        
        <h4>3. READING</h4>
        <div class="reading-section">
            <ul>
                <li>Which places do you want to visit? → I want to visit _________.</li>
                <li>Which places did you visit in the past? → I visited _________.</li>
            </ul>
        </div>
        
        <h4>4. GRAMMAR</h4>
        <div class="grammar-section">
            <h5>Conjunctions: And / But</h5>
            
            <ul>
                <li><strong>And</strong> connects similar ideas.
                    <ul>
                        <li>Example: The house is big and beautiful.</li>
                        <li>Example: The city is dirty and dangerous.</li>
                    </ul>
                </li>
                <li><strong>But</strong> connects different ideas.
                    <ul>
                        <li>Example: The hotel is safe but expensive.</li>
                        <li>Example: The house is ugly but cheap.</li>
                    </ul>
                </li>
            </ul>
            
            <h5>Exercise: Complete with "and" or "but"</h5>
            <ol>
                <li>Singapore is clean ____ modern. (and)</li>
                <li>India is big ____ dirty. (but)</li>
                <li>Panama City is modern ____ safe. (and)</li>
                <li>Jamaica is relaxing ____ cheap. (and)</li>
                <li>Cuzco is old ____ beautiful. (but)</li>
                <li>Syria is dangerous ____ poor. (and)</li>
                <li>Paris is beautiful ____ expensive. (but)</li>
                <li>Brunei is interesting ____ small. (but)</li>
                <li>Amsterdam is old ____ small. (and)</li>
                <li>Brazil is modern ____ dangerous. (but)</li>
            </ol>
            
            <h5>Adjectives with Be</h5>
            <p><strong>Structure:</strong> Subject + Be + Adjective.</p>
            <ul>
                <li>Moscow is beautiful.</li>
                <li>Brazil is expensive.</li>
                <li>The buildings are modern.</li>
            </ul>
            
            <h5>Exercise: Complete with correct "Verb Be"</h5>
            <ol>
                <li>Bangkok ____ beautiful. (is)</li>
                <li>London ____ big. (is)</li>
                <li>Seoul and Tokyo ____ modern. (are)</li>
                <li>Barcelona ____ clean. (is)</li>
                <li>Milan ____ safe. (is)</li>
                <li>Bali and Phuket ____ relaxing. (are)</li>
                <li>Cartagena ____ traditional. (is)</li>
                <li>Dubai and Paris ____ expensive. (are)</li>
                <li>New York ____ noisy. (is)</li>
                <li>Cuzco and Quito ____ small. (are)</li>
            </ol>
            
            <h5>Be + Adjective + Noun</h5>
            <ul>
                <li>Rome is a traditional city.</li>
                <li>Peru and Colombia are beautiful countries.</li>
                <li>Miami is a modern city.</li>
                <li>Sydney and Loja are clean cities.</li>
                <li>China is a big country.</li>
            </ul>
        </div>
        
        <h4>5. WRITING</h4>
        <div class="writing-section">
            <h5>Write about your favorite city:</h5>
            <ol>
                <li>What's your favorite city? My favorite city is ______.</li>
                <li>Where is it? It's in _____ in _______. (country) (continent)</li>
                <li>What language do people speak there? People in _____ speak ______.</li>
                <li>What is it famous for? _____ is famous for its _______.</li>
                <li>What's the city like? It's ______ and _________. / It's ______, but __________.</li>
                <li>What are the streets like? They are __________.</li>
                <li>What are the people like? People in _____ are ________.</li>
                <li>What's your favorite place in the city? Why? My favorite place is __________ because it's _________.</li>
            </ol>
        </div>
        
        <h4>6. COMMUNICATION</h4>
        <div class="communication-section">
            <h5>Good vacation places:</h5>
            <ul>
                <li>What are good places for vacations in your country?</li>
                <li>Do you like to travel? → Yes, I do. / No, I don't.</li>
            </ul>
            
            <h5>Dialogue:</h5>
            <ul>
                <li>Where's _______? (city) → _______ is in _______.</li>
                <li>How is it there? → It's ____ and/,but ______.</li>
            </ul>
        </div>
    </section>
    
    <section id="unit3">
        <h2>UNIT 3: POSSESSIONS</h2>
        
        <h3>Lesson A: Gifts</h3>
        
        <h4>Unit Goals:</h4>
        <ol>
            <li>Identify everyday objects.</li>
            <li>Give and reply to thanks.</li>
            <li>Talk about having more than one of something.</li>
            <li>Use adjectives to describe and rate items.</li>
        </ol>
        
        <h4>Video Vocabulary - Stuff:</h4>
        <p>a computer, a soccer ball, a cellphone, a photo, candy, books, keys, a ring, a tape measure, safety kit, snacks, a map, a wallet, a camera, lipstick, an apple</p>
        
        <h4>Personal Items:</h4>
        <ul>
            <li><strong>Bags:</strong> a backpack, a bag, a briefcase, a purse</li>
            <li><strong>Electronics:</strong> a charger, headphones, a watch, a gift card, a notebook, a pencil case, a tablet, sunglasses</li>
            <li><strong>Personal Care:</strong> a comb, credit card, Band-aids, earrings, a water bottle, chewing gum, make-up, pills</li>
            <li><strong>Documents:</strong> a driver's license, a coin purse, coins, a toothbrush, toothpaste, a passport, an ID card, bills</li>
        </ul>
        
        <h5>Questions:</h5>
        <ul>
            <li>What do you carry with you? → I always carry __________.</li>
            <li>What's in your bag? → I have __________.</li>
            <li>Which items do you have? → I have _____.</li>
            <li>What's the best gift for a student? → The best gift for a student is ______.</li>
            <li>Which of these gifts is your favorite? → My favorite gift is ______.</li>
        </ul>
        
        <h5>Events:</h5>
        <p>a birthday, a wedding, a graduation</p>
        
        <h5>Perfect Gifts:</h5>
        <ul>
            <li>What's the perfect gift for a birthday? A wedding? A graduation?</li>
            <li>I think the perfect gift for ______ is/are ______. (event) (item)</li>
            <li><strong>Examples:</strong> a teddy bear, a necklace, perfume, a ring, a mug, a phone, chocolate, a gift basket, a bracelet, a photo album, a car, money, flowers</li>
        </ul>
        
        <h4>4. SPEAKING: Giving and Replying to Thanks</h4>
        
        <h5>Thanking:</h5>
        <ul>
            <li>Thank you very much.</li>
            <li>Thank you.</li>
            <li>Thanks a lot.</li>
            <li>Thanks.</li>
            <li>Thanks a bunch.</li>
            <li>Thank you so much.</li>
        </ul>
        
        <h5>Replying (Formal):</h5>
        <ul>
            <li>You're welcome.</li>
            <li>My pleasure.</li>
        </ul>
        
        <h5>Replying (Informal):</h5>
        <ul>
            <li>Sure, no problem.</li>
            <li>You bet.</li>
            <li>Anytime.</li>
            <li>Not at all.</li>
        </ul>
        
        <h4>5. GRAMMAR</h4>
        <div class="grammar-section">
            <h5>A/An Articles:</h5>
            <ul>
                <li>Use <strong>A</strong> with consonant sounds: a book, a desk, a stapler, a marker</li>
                <li>Use <strong>An</strong> with vowel sounds: an eraser, an elephant, an umbrella, an invitation</li>
            </ul>
            
            <h5>Exercise: Complete with A or An</h5>
            <ol>
                <li>It's ____ backpack. (a)</li>
                <li>It's ____ hour. (an - h is silent)</li>
                <li>It's ____ desk. (a)</li>
                <li>It's ____ elephant. (an)</li>
                <li>It's ____ stapler. (a)</li>
                <li>It's ____ marker. (a)</li>
                <li>It's ____ umbrella. (an)</li>
                <li>It's ____ university. (a - u sounds like 'you')</li>
                <li>It's ____ paper punch. (a)</li>
                <li>It's ____ invitation. (an)</li>
            </ol>
            
            <h5>Plural Nouns - Spelling Rules:</h5>
            
            <ol>
                <li><strong>Add -s</strong> (most words): car → cars, apple → apples</li>
                
                <li><strong>Add -es</strong> (words ending in -s, -ch, -sh, -x, -z, consonant + -o):
                    <ul>
                        <li>bus → buses</li>
                        <li>match → matches</li>
                        <li>dish → dishes</li>
                        <li>box → boxes</li>
                        <li>quiz → quizzes</li>
                        <li>tomato → tomatoes</li>
                    </ul>
                </li>
                
                <li><strong>Change -y to -ies</strong> (consonant + -y):
                    <ul>
                        <li>baby → babies</li>
                        <li>city → cities</li>
                    </ul>
                </li>
                
                <li><strong>Change -f/-fe to -ves</strong>:
                    <ul>
                        <li>leaf → leaves</li>
                        <li>knife → knives</li>
                    </ul>
                </li>
            </ol>
            
            <p><strong>NOTE:</strong> Don't use 'a' or 'an' with plural nouns.</p>
            
            <h5>-s Endings Pronunciation:</h5>
            <ul>
                <li>/IZ/: races, buses, boxes, kisses, watches, dishes</li>
                <li>/S/: lamps, books, hats, roofs, laughs</li>
                <li>/Z/: crabs, words, bags, waterfalls, fans, earrings</li>
            </ul>
            
            <h5>Exercise: Convert to plural</h5>
            <ol>
                <li>It is a dictionary and a book. → They are dictionaries and books.</li>
                <li>It is a big box. → They are big boxes.</li>
                <li>It is an amazing phone. → They are amazing phones.</li>
                <li>It is a modern bus. → They are modern buses.</li>
                <li>It is an expensive and small watch. → They are expensive and small watches.</li>
            </ol>
        </div>
        
        <h4>6. COMMUNICATION</h4>
        <div class="communication-section">
            <h5>Birthday Dialogue:</h5>
            <p><strong>A:</strong> Happy birthday, Cindy! I have a surprise for you.<br>
            <strong>B:</strong> Oh... let's see. What's this? Wow, it's a cool watch. Thanks, David. I really like it.<br>
            <strong>A:</strong> No problem, Cindy. I'm glad you like it.</p>
        </div>
        
        <h3>Lesson B: Important Items</h3>
        
        <h4>1. VOCABULARY</h4>
        
        <h5>Adjectives:</h5>
        <ul>
            <li>cheap vs. expensive</li>
            <li>comfortable vs. uncomfortable</li>
            <li>messy vs. clean</li>
            <li>easy vs. hard</li>
            <li>important vs. unimportant</li>
        </ul>
        
        <p><strong>Pack Rat:</strong> a person who collects unnecessary objects.</p>
        
        <h5>Questions:</h5>
        <ul>
            <li>Are you a "pack rat"? → Yes, I am. / No, I'm not.</li>
            <li>Is your room clean? → Yes, my room is clean. / No, my room is messy.</li>
            <li>Is it easy or hard to find things in your room? → Yes, it's easy. / No, it's hard.</li>
            <li>Do you usually keep or throw out old things? → Yes, I keep old things. / No, I throw out old things.</li>
            <li>Do you buy things just because they're cheap? → Yes, I sometimes buy things because they're cheap. / No, I never buy things because they're cheap.</li>
        </ul>
        
        <h4>2. LISTENING</h4>
        <div class="listening-section">
            <p><strong>Keepsakes:</strong> things people keep to remember something happy.</p>
            <ul>
                <li>Do you have any keepsakes? → Yes, I keep keychains from the places I visited. / No, I don't keep anything.</li>
            </ul>
            
            <h5>Listening Vocabulary:</h5>
            <p>Box, Post card, T-shirt, Photo</p>
            
            <ul>
                <li>Do you have any similar objects? → Yes, I have _____.</li>
                <li>What's your favorite keepsake? → My favorite keepsake is my ____ because it____.</li>
            </ul>
        </div>
        
        <h4>3. READING</h4>
        <div class="reading-section">
            <h5>Important Items:</h5>
            <ul>
                <li>What's your most important item? → My most important item is my laptop because it is (adjectives)...</li>
            </ul>
            
            <h5>Reading Vocabulary:</h5>
            <p>Sunblock/Sunscreen, Hat, GPS, Bracelet</p>
            
            <h5>Pictures:</h5>
            <ul>
                <li>A: Chef → important item: uniform</li>
                <li>B: Teacher</li>
                <li>C: Student</li>
                <li>D: Tourist</li>
            </ul>
        </div>
        
        <h4>4. GRAMMAR: Demonstratives</h4>
        <div class="grammar-section">
            <h5>This / That / These / Those</h5>
            
            <p>We use them to talk about a thing or person that is near or far from us.</p>
            
            <p><strong>Structure:</strong> Demonstrative + be + complement</p>
            
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>Singular</th>
                        <th>Plural</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Near</strong></td>
                        <td>This is my cell phone.</td>
                        <td>These are your keys.</td>
                    </tr>
                    <tr>
                        <td><strong>Far</strong></td>
                        <td>That is my best friend.</td>
                        <td>Those are your pencils.</td>
                    </tr>
                </tbody>
            </table>
            
            <h5>Questions:</h5>
            <ul>
                <li>What's this/that? → This/That is (a/an) ________ (item)</li>
                <li>What are these/those? → These/Those are ________ (items)</li>
            </ul>
            
            <h5>Exercise: Complete with demonstratives</h5>
            <ol>
                <li>_____ is a police officer. (This/That)</li>
                <li>_____ is a desk. (This/That)</li>
                <li>_____ are photographers. (These/Those)</li>
                <li>_____ is a taxi driver. (This/That)</li>
                <li>_____ are staplers. (These/Those)</li>
            </ol>
        </div>
        
        <h4>5. WRITING</h4>
        <div class="writing-section">
            <h5>Describe a product with adjectives:</h5>
            <p>Comfortable, Uncomfortable, Cheap, Expensive, Nice, Interesting, Cool, Bad</p>
            <p><strong>Structure:</strong> It's...</p>
        </div>
        
        <h4>6. COMMUNICATION</h4>
        <div class="communication-section">
            <h5>Product Review:</h5>
            <ul>
                <li>What product do you like or dislike? → I like/dislike drones</li>
                <li>What are 2 things you like about it? → It has a great camera and good battery.</li>
                <li>What are 2 things you dislike about it? → It's expensive and very fragile.</li>
            </ul>
        </div>
    </section>
    
    <div style="margin-top: 3em; padding: 1em; background-color: #f0f0f0; border-left: 4px solid #0066cc;">
        <p><strong>END OF WORLDLINK BASIC 01 COURSE CONTENT</strong></p>
    </div>
    """)

def make_lessons():
    lessons = []
    
    # B01 with full content
    lessons.append({
        "id": "b1",
        "level": "Básico",
        "title": "Básico 01 - WorldLink Complete Course",
        "content": get_b01_content()
    })
    
    # B02 with full content
    lessons.append({
        "id": "b2",
        "level": "Básico",
        "title": "Básico 02 - WorldLink Complete Course",
        "content": get_b02_content()
    })
    
    # B03 with full content
    lessons.append({
        "id": "b3",
        "level": "Básico",
        "title": "Básico 03 - WorldLink Complete Course",
        "content": get_b03_content()
    })
    
    # B04 with full content
    lessons.append({
        "id": "b4",
        "level": "Básico",
        "title": "Básico 04 - WorldLink Complete Course",
        "content": get_b04_content()
    })
    
    # B05 with full content
    lessons.append({
        "id": "b5",
        "level": "Básico",
        "title": "Básico 05 - WorldLink Complete Course",
        "content": get_b05_content()
    })
    
    # B06 with full content
    lessons.append({
        "id": "b6",
        "level": "Básico",
        "title": "Básico 06 - WorldLink Complete Course",
        "content": get_b06_content()
    })
    
    # B07 with full content
    lessons.append({
        "id": "b7",
        "level": "Básico",
        "title": "Básico 07 - WorldLink Complete Course",
        "content": get_b07_content()
    })
    
    # B08 with full content
    lessons.append({
        "id": "b8",
        "level": "Básico",
        "title": "Básico 08 - Health, Achievement, Movies",
        "content": get_b08_content()
    })
    
    # B09 with full content
    lessons.append({
        "id": "b9",
        "level": "Básico",
        "title": "Básico 09 - My Life, Let's Eat, Mysteries",
        "content": get_b09_content()
    })
    
    # B10 with full content
    lessons.append({
        "id": "b10",
        "level": "Básico",
        "title": "Básico 10 - Trends",
        "content": get_b10_content()
    })
    
    # B11 with full content
    lessons.append({
        "id": "b11",
        "level": "Básico",
        "title": "Básico 11 - Celebrations, Storytelling, Work",
        "content": get_b11_content()
    })
    
    # B12 with full content - FINAL BASIC COURSE!
    lessons.append({
        "id": "b12",
        "level": "Básico",
        "title": "Básico 12 - Telephoning, Technology, Travel",
        "content": get_b12_content()
    })
    
    # Intermediates
    for i in range(1, 13):
        lessons.append({
            "id": f"i{i}",
            "level": "Intermedio",
            "title": f"Intermedio {i:02d}",
            "content": "Contenido por llenar."
        })
    
    return lessons

LESSONS = {l["id"]: l for l in make_lessons()}


@app.route("/")
def index():
    lessons = list(LESSONS.values())
    return render_template("index.html", lessons=lessons)


@app.route("/lesson/<lesson_id>")
def lesson(lesson_id):
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        abort(404)
    return render_template("lesson.html", lesson=lesson)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
