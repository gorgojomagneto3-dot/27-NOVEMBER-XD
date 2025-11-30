from markupsafe import Markup

def get_exam_prep_content():
    """Contenido de preparación para exámenes internacionales"""
    return Markup("""
    <h1>🎯 Exam Preparation - International Tests</h1>
    
    <div class="exam-intro">
        <p><strong>This section prepares you for:</strong> Cambridge (KET, PET, FCE), TOEFL, IELTS</p>
    </div>
    
    <section id="reading-strategies">
        <h2>📖 READING STRATEGIES</h2>
        
        <div class="strategy-box">
            <h3>Skimming vs Scanning</h3>
            <ul>
                <li><strong>Skimming:</strong> Read quickly to get the main idea → Look at titles, first sentences, conclusions</li>
                <li><strong>Scanning:</strong> Search for specific information → Names, dates, numbers, keywords</li>
            </ul>
            
            <h4>Practice: Skim this text (30 seconds)</h4>
            <div class="reading-passage">
                <p>The Amazon rainforest is the world's largest tropical rainforest, covering over 5.5 million square kilometers. 
                It is home to approximately 10% of all species on Earth. The forest produces about 20% of the world's oxygen, 
                which is why it's often called "the lungs of the planet." However, deforestation threatens this vital ecosystem. 
                Every minute, an area equivalent to 150 football fields is destroyed.</p>
            </div>
            
            <div class="exercise-item">
                <span class="question">What is the main idea of this text?</span>
                <input type="text" class="answer-input" placeholder="Write the main idea..." data-answer="The Amazon rainforest is important but threatened">
                <button class="check-btn" onclick="checkAnswer(this, 'The Amazon rainforest is important but threatened')">Check</button>
                <button class="reveal-btn" onclick="revealAnswer(this, 'The Amazon rainforest is important but threatened')">Show answer</button>
                <span class="feedback"></span>
            </div>
        </div>
        
        <h3>Reading Comprehension Types</h3>
        <div class="vocab-section">
            <h5>Question Types in Exams:</h5>
            <ul>
                <li><strong>Multiple choice:</strong> Choose A, B, C, or D → Read ALL options before answering</li>
                <li><strong>True/False/Not Given:</strong> Is the information in the text? → Don't use your own knowledge</li>
                <li><strong>Matching:</strong> Match headings to paragraphs → Look for topic sentences</li>
                <li><strong>Gap-fill:</strong> Complete sentences with words from the text → Check grammar fits</li>
            </ul>
        </div>
    </section>
    
    <section id="listening-tips">
        <h2>🎧 LISTENING STRATEGIES</h2>
        
        <div class="strategy-box">
            <h3>Before Listening</h3>
            <ul>
                <li>Read the questions first → Know what to listen for</li>
                <li>Predict answers → What type of word? (number, name, place?)</li>
                <li>Underline keywords in questions</li>
            </ul>
            
            <h3>While Listening</h3>
            <ul>
                <li>Listen for synonyms → The audio may use different words than the question</li>
                <li>Pay attention to signpost words: "however," "but," "on the other hand"</li>
                <li>Write something! Never leave blanks</li>
            </ul>
            
            <h3>Common Listening Traps:</h3>
            <div class="grammar-section">
                <ul>
                    <li>🚫 <strong>Changed mind:</strong> "I thought it was Tuesday... no wait, it's Wednesday"</li>
                    <li>🚫 <strong>Distractors:</strong> They mention wrong answers before the right one</li>
                    <li>🚫 <strong>Similar sounds:</strong> thirteen/thirty, fifty/fifteen</li>
                </ul>
            </div>
        </div>
    </section>
    
    <section id="writing-skills">
        <h2>✍️ WRITING STRUCTURE</h2>
        
        <h3>Essay Organization</h3>
        <div class="vocab-section">
            <h5>Basic Essay Structure:</h5>
            <ul>
                <li><strong>Introduction:</strong> Hook + Background + Thesis statement</li>
                <li><strong>Body Paragraph 1:</strong> Topic sentence + Supporting details + Example</li>
                <li><strong>Body Paragraph 2:</strong> Topic sentence + Supporting details + Example</li>
                <li><strong>Conclusion:</strong> Restate thesis + Summary + Final thought</li>
            </ul>
        </div>
        
        <h3>Linking Words (Conectores)</h3>
        <div class="grammar-section">
            <table>
                <thead>
                    <tr>
                        <th>Function</th>
                        <th>Connectors</th>
                        <th>Example</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Adding</td>
                        <td>Furthermore, Moreover, In addition, Also</td>
                        <td>Furthermore, exercise improves mental health.</td>
                    </tr>
                    <tr>
                        <td>Contrasting</td>
                        <td>However, Nevertheless, On the other hand, Although</td>
                        <td>However, not everyone agrees with this view.</td>
                    </tr>
                    <tr>
                        <td>Cause/Effect</td>
                        <td>Therefore, Consequently, As a result, Because</td>
                        <td>Therefore, we must take action now.</td>
                    </tr>
                    <tr>
                        <td>Example</td>
                        <td>For example, For instance, Such as</td>
                        <td>For instance, renewable energy reduces pollution.</td>
                    </tr>
                    <tr>
                        <td>Conclusion</td>
                        <td>In conclusion, To sum up, Overall, Finally</td>
                        <td>In conclusion, education is essential for progress.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <h4>Exercise: Use the correct connector</h4>
        <ol>
            <li>I love pizza. _______, I try not to eat it every day. (However)</li>
            <li>She studied hard. _______, she passed the exam. (Therefore)</li>
            <li>Many sports are fun, _______ soccer and basketball. (such as)</li>
            <li>_______, I believe technology has more benefits than drawbacks. (In conclusion)</li>
        </ol>
    </section>
    
    <section id="speaking-exam">
        <h2>🗣️ SPEAKING EXAM TIPS</h2>
        
        <h3>Part 1: Introduction & Interview</h3>
        <div class="speaking-section">
            <h5>Common Topics:</h5>
            <ul>
                <li><strong>Work/Study:</strong> What do you do? → I'm a student at... / I work as a...</li>
                <li><strong>Hometown:</strong> Where are you from? → I'm from..., which is a city in...</li>
                <li><strong>Hobbies:</strong> What do you do in your free time? → In my free time, I enjoy...</li>
                <li><strong>Family:</strong> Tell me about your family. → I have a... There are... people in my family.</li>
            </ul>
            
            <h5>Extend Your Answers (Don't give one-word answers!):</h5>
            <ul>
                <li>❌ "Yes." → ✅ "Yes, I do. I really enjoy reading, especially novels."</li>
                <li>❌ "Lima." → ✅ "I'm from Lima, the capital of Peru. It's a busy city on the coast."</li>
            </ul>
        </div>
        
        <h3>Useful Phrases for Speaking</h3>
        <div class="vocab-section">
            <h5>Giving Opinions:</h5>
            <ul>
                <li>In my opinion... → In my opinion, learning languages is very important.</li>
                <li>I think that... → I think that technology has changed our lives.</li>
                <li>From my point of view... → From my point of view, exercise is essential.</li>
                <li>I believe... → I believe education should be free for everyone.</li>
            </ul>
            
            <h5>Agreeing/Disagreeing:</h5>
            <ul>
                <li>I completely agree because... → I completely agree because it helps people communicate.</li>
                <li>I see your point, but... → I see your point, but I think there are some disadvantages.</li>
                <li>That's true, however... → That's true, however, we also need to consider...</li>
            </ul>
            
            <h5>Asking for Clarification:</h5>
            <ul>
                <li>Could you repeat that, please? → Could you repeat that, please? I didn't catch it.</li>
                <li>What do you mean by...? → What do you mean by "sustainable"?</li>
                <li>Sorry, I don't understand. → Sorry, I don't understand. Could you explain?</li>
            </ul>
        </div>
    </section>
    """)

def get_common_mistakes_content():
    """Errores comunes de hispanohablantes"""
    return Markup("""
    <h1>⚠️ Common Mistakes - Spanish Speakers</h1>
    
    <p class="intro-note">These are the most common errors Spanish speakers make in English. Learn to avoid them!</p>
    
    <section id="false-friends">
        <h2>🎭 FALSE FRIENDS (Falsos Amigos)</h2>
        
        <div class="grammar-section">
            <table>
                <thead>
                    <tr>
                        <th>Spanish Word</th>
                        <th>❌ Wrong English</th>
                        <th>✅ Correct English</th>
                        <th>Actual Meaning</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Actualmente</td>
                        <td>Actually</td>
                        <td>Currently / Nowadays</td>
                        <td>"Actually" = en realidad</td>
                    </tr>
                    <tr>
                        <td>Realizar</td>
                        <td>Realize</td>
                        <td>Carry out / Do / Make</td>
                        <td>"Realize" = darse cuenta</td>
                    </tr>
                    <tr>
                        <td>Sensible</td>
                        <td>Sensible</td>
                        <td>Sensitive</td>
                        <td>"Sensible" = sensato</td>
                    </tr>
                    <tr>
                        <td>Éxito</td>
                        <td>Exit</td>
                        <td>Success</td>
                        <td>"Exit" = salida</td>
                    </tr>
                    <tr>
                        <td>Embarazada</td>
                        <td>Embarrassed</td>
                        <td>Pregnant</td>
                        <td>"Embarrassed" = avergonzado</td>
                    </tr>
                    <tr>
                        <td>Librería</td>
                        <td>Library</td>
                        <td>Bookstore</td>
                        <td>"Library" = biblioteca</td>
                    </tr>
                    <tr>
                        <td>Carpeta</td>
                        <td>Carpet</td>
                        <td>Folder</td>
                        <td>"Carpet" = alfombra</td>
                    </tr>
                    <tr>
                        <td>Asistir</td>
                        <td>Assist</td>
                        <td>Attend</td>
                        <td>"Assist" = ayudar</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <h4>Exercise: Choose the correct word</h4>
        <ol>
            <li>I _______ I had made a mistake. (realized)</li>
            <li>She is very _______ about her weight. (sensitive)</li>
            <li>I need to buy a book at the _______. (bookstore)</li>
            <li>The meeting was a great _______. (success)</li>
            <li>Please _______ the conference tomorrow. (attend)</li>
        </ol>
    </section>
    
    <section id="grammar-mistakes">
        <h2>📝 COMMON GRAMMAR MISTAKES</h2>
        
        <div class="grammar-section">
            <h3>1. Subject Always Required</h3>
            <p>In Spanish, you can omit the subject. In English, you CANNOT.</p>
            <ul>
                <li>❌ "Is raining" → ✅ "<strong>It</strong> is raining"</li>
                <li>❌ "Am tired" → ✅ "<strong>I</strong> am tired"</li>
                <li>❌ "Is important to study" → ✅ "<strong>It</strong> is important to study"</li>
            </ul>
            
            <h3>2. Adjective Order</h3>
            <p>In English, adjectives come BEFORE the noun (opposite of Spanish)</p>
            <ul>
                <li>❌ "A car red" → ✅ "A <strong>red car</strong>"</li>
                <li>❌ "The house big" → ✅ "The <strong>big house</strong>"</li>
                <li>❌ "An exam difficult" → ✅ "A <strong>difficult exam</strong>"</li>
            </ul>
            
            <h3>3. Present Simple vs Present Continuous</h3>
            <p>Spanish uses one form; English has two!</p>
            <ul>
                <li><strong>Habitual:</strong> I <strong>work</strong> every day. (Simple)</li>
                <li><strong>Now:</strong> I <strong>am working</strong> right now. (Continuous)</li>
                <li>❌ "I work now" → ✅ "I <strong>am working</strong> now"</li>
                <li>❌ "I am working every day" → ✅ "I <strong>work</strong> every day"</li>
            </ul>
            
            <h3>4. Double Negatives</h3>
            <p>In English, use ONLY ONE negative!</p>
            <ul>
                <li>❌ "I don't have nothing" → ✅ "I don't have <strong>anything</strong>" / "I have <strong>nothing</strong>"</li>
                <li>❌ "I don't know nobody" → ✅ "I don't know <strong>anybody</strong>" / "I know <strong>nobody</strong>"</li>
                <li>❌ "I never go nowhere" → ✅ "I never go <strong>anywhere</strong>"</li>
            </ul>
            
            <h3>5. Make vs Do</h3>
            <ul>
                <li><strong>MAKE</strong> = create/produce something: make breakfast, make a decision, make money, make a mistake, make plans</li>
                <li><strong>DO</strong> = perform an action: do homework, do exercise, do the dishes, do business, do your best</li>
                <li>❌ "I need to make my homework" → ✅ "I need to <strong>do</strong> my homework"</li>
                <li>❌ "She does a lot of mistakes" → ✅ "She <strong>makes</strong> a lot of mistakes"</li>
            </ul>
            
            <h3>6. Say vs Tell</h3>
            <ul>
                <li><strong>SAY</strong> + something (no person needed): He said "hello"</li>
                <li><strong>TELL</strong> + someone + something: He told <strong>me</strong> the truth</li>
                <li>❌ "He said me the answer" → ✅ "He <strong>told me</strong> the answer"</li>
                <li>❌ "He told that he was tired" → ✅ "He <strong>said</strong> that he was tired"</li>
            </ul>
        </div>
        
        <h4>Exercise: Fix the mistakes</h4>
        <ol>
            <li>Is very cold today. (It is)</li>
            <li>She has a dress beautiful. (a beautiful dress)</li>
            <li>I work right now. (am working)</li>
            <li>I don't have nothing to do. (anything)</li>
            <li>I need to make my homework. (do)</li>
        </ol>
    </section>
    
    <section id="pronunciation-mistakes">
        <h2>🔊 PRONUNCIATION MISTAKES</h2>
        
        <div class="vocab-section">
            <h5>Silent Letters:</h5>
            <ul>
                <li><strong>K</strong>nife, <strong>K</strong>now, <strong>K</strong>nee → The K is silent!</li>
                <li><strong>W</strong>rite, <strong>W</strong>rong, <strong>W</strong>rap → The W is silent!</li>
                <li>Lis<strong>t</strong>en, Cas<strong>t</strong>le, Whis<strong>t</strong>le → The T is silent!</li>
                <li><strong>H</strong>our, <strong>H</strong>onest, <strong>H</strong>onor → The H is silent!</li>
            </ul>
            
            <h5>Vowel Sounds Spanish Speakers Confuse:</h5>
            <ul>
                <li><strong>Ship</strong> /ɪ/ vs <strong>Sheep</strong> /iː/ → Short vs Long</li>
                <li><strong>Full</strong> /ʊ/ vs <strong>Fool</strong> /uː/ → Short vs Long</li>
                <li><strong>Cat</strong> /æ/ vs <strong>Cut</strong> /ʌ/ → Different sounds!</li>
                <li><strong>Bed</strong> /e/ vs <strong>Bad</strong> /æ/ → Different sounds!</li>
            </ul>
            
            <h5>Consonant Sounds:</h5>
            <ul>
                <li><strong>V</strong> (vibration) vs <strong>B</strong> (lips): Very ≠ Berry</li>
                <li><strong>TH</strong> voiced /ð/: This, That, The → Tongue between teeth!</li>
                <li><strong>TH</strong> voiceless /θ/: Think, Three, Thank → Tongue between teeth, no voice!</li>
                <li><strong>-ED</strong> endings: worked /t/, played /d/, wanted /ɪd/</li>
            </ul>
        </div>
    </section>
    """)

def get_phrasal_verbs_content():
    """Phrasal verbs esenciales por nivel"""
    return Markup("""
    <h1>🚀 Essential Phrasal Verbs</h1>
    
    <p class="intro-note">Phrasal verbs are ESSENTIAL for natural English. Learn the most common ones!</p>
    
    <section id="basic-phrasal">
        <h2>📗 BASIC LEVEL (A1-A2)</h2>
        
        <div class="grammar-section">
            <table>
                <thead>
                    <tr>
                        <th>Phrasal Verb</th>
                        <th>Meaning</th>
                        <th>Example</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Wake up</td><td>Despertarse</td><td>I wake up at 7 AM every day.</td></tr>
                    <tr><td>Get up</td><td>Levantarse</td><td>She gets up early for work.</td></tr>
                    <tr><td>Turn on</td><td>Encender</td><td>Turn on the lights, please.</td></tr>
                    <tr><td>Turn off</td><td>Apagar</td><td>Don't forget to turn off the TV.</td></tr>
                    <tr><td>Put on</td><td>Ponerse (ropa)</td><td>Put on your jacket. It's cold.</td></tr>
                    <tr><td>Take off</td><td>Quitarse (ropa)</td><td>Take off your shoes at the door.</td></tr>
                    <tr><td>Look for</td><td>Buscar</td><td>I'm looking for my keys.</td></tr>
                    <tr><td>Pick up</td><td>Recoger</td><td>Can you pick up the children?</td></tr>
                    <tr><td>Sit down</td><td>Sentarse</td><td>Please sit down and relax.</td></tr>
                    <tr><td>Stand up</td><td>Pararse</td><td>Stand up when the teacher enters.</td></tr>
                    <tr><td>Come back</td><td>Volver</td><td>When will you come back?</td></tr>
                    <tr><td>Go out</td><td>Salir</td><td>Let's go out tonight!</td></tr>
                </tbody>
            </table>
        </div>
        
        <h4>Exercise: Complete with the correct phrasal verb</h4>
        <ol>
            <li>I need to _______ my coat. It's raining. (put on)</li>
            <li>Please _______ the music. It's too loud! (turn off)</li>
            <li>What time do you usually _______? (wake up)</li>
            <li>I'm _______ my phone. Have you seen it? (looking for)</li>
            <li>Can you _______ the kids from school? (pick up)</li>
        </ol>
    </section>
    
    <section id="intermediate-phrasal">
        <h2>📘 INTERMEDIATE LEVEL (B1-B2)</h2>
        
        <div class="grammar-section">
            <table>
                <thead>
                    <tr>
                        <th>Phrasal Verb</th>
                        <th>Meaning</th>
                        <th>Example</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Figure out</td><td>Descubrir/Resolver</td><td>I can't figure out this problem.</td></tr>
                    <tr><td>Give up</td><td>Rendirse</td><td>Don't give up! You can do it!</td></tr>
                    <tr><td>Look after</td><td>Cuidar</td><td>Can you look after my dog?</td></tr>
                    <tr><td>Run out of</td><td>Quedarse sin</td><td>We ran out of milk.</td></tr>
                    <tr><td>Come up with</td><td>Idear/Inventar</td><td>She came up with a great idea.</td></tr>
                    <tr><td>Put off</td><td>Posponer</td><td>Don't put off your homework.</td></tr>
                    <tr><td>Look forward to</td><td>Esperar con ansias</td><td>I'm looking forward to the vacation.</td></tr>
                    <tr><td>Get along (with)</td><td>Llevarse bien</td><td>Do you get along with your coworkers?</td></tr>
                    <tr><td>Catch up (with)</td><td>Ponerse al día</td><td>I need to catch up with my work.</td></tr>
                    <tr><td>Break down</td><td>Averiarse/Descomponerse</td><td>My car broke down on the highway.</td></tr>
                    <tr><td>Find out</td><td>Descubrir/Enterarse</td><td>I just found out the news!</td></tr>
                    <tr><td>Work out</td><td>1) Ejercitarse 2) Resolver</td><td>I work out three times a week.</td></tr>
                </tbody>
            </table>
        </div>
        
        <h4>Exercise: Complete with the correct phrasal verb</h4>
        <ol>
            <li>I need to _______ a solution to this problem. (figure out)</li>
            <li>Never _______! Keep trying! (give up)</li>
            <li>Can you _______ my cat while I'm on vacation? (look after)</li>
            <li>We've _______ coffee. Can you buy some? (run out of)</li>
            <li>I'm _______ meeting you in person! (looking forward to)</li>
        </ol>
    </section>
    
    <section id="collocations">
        <h2>🔗 COMMON COLLOCATIONS</h2>
        
        <p>Collocations are words that "go together" naturally.</p>
        
        <div class="grammar-section">
            <h3>Make + Noun</h3>
            <ul>
                <li>make a decision → I need to make a decision soon.</li>
                <li>make a mistake → Everybody makes mistakes.</li>
                <li>make progress → You're making great progress!</li>
                <li>make an effort → Please make an effort to arrive on time.</li>
                <li>make money → He makes a lot of money.</li>
                <li>make sense → This doesn't make sense!</li>
            </ul>
            
            <h3>Take + Noun</h3>
            <ul>
                <li>take a photo → Can you take a photo of us?</li>
                <li>take a break → Let's take a break for 10 minutes.</li>
                <li>take a shower → I take a shower every morning.</li>
                <li>take a nap → I need to take a nap. I'm tired.</li>
                <li>take notes → Always take notes in class.</li>
                <li>take your time → Take your time. There's no hurry.</li>
            </ul>
            
            <h3>Have + Noun</h3>
            <ul>
                <li>have a good time → Did you have a good time at the party?</li>
                <li>have a problem → I'm having a problem with my computer.</li>
                <li>have a conversation → We had a long conversation.</li>
                <li>have fun → Have fun on your trip!</li>
                <li>have a dream → I had a strange dream last night.</li>
            </ul>
            
            <h3>Do + Noun</h3>
            <ul>
                <li>do homework → I have to do my homework.</li>
                <li>do exercise → I do exercise every day.</li>
                <li>do business → They do business with many countries.</li>
                <li>do your best → Just do your best on the exam.</li>
                <li>do the dishes → Can you do the dishes tonight?</li>
            </ul>
        </div>
    </section>
    
    <section id="idioms">
        <h2>💬 USEFUL IDIOMS</h2>
        
        <div class="vocab-section">
            <h5>Common English Idioms:</h5>
            <ul>
                <li><strong>Break the ice</strong> → Start a conversation / Romper el hielo</li>
                <li><strong>Piece of cake</strong> → Very easy / Pan comido</li>
                <li><strong>Hit the books</strong> → Study hard / Ponerse a estudiar</li>
                <li><strong>Under the weather</strong> → Feeling sick / Sentirse mal</li>
                <li><strong>Cost an arm and a leg</strong> → Very expensive / Costar un ojo de la cara</li>
                <li><strong>Once in a blue moon</strong> → Very rarely / De vez en cuando</li>
                <li><strong>Kill two birds with one stone</strong> → Accomplish two things at once / Matar dos pájaros de un tiro</li>
                <li><strong>Call it a day</strong> → Stop working / Dar por terminado el día</li>
                <li><strong>Get out of hand</strong> → Get out of control / Salirse de control</li>
                <li><strong>In the long run</strong> → Eventually / A largo plazo</li>
            </ul>
        </div>
        
        <h4>Exercise: Match the idiom with its meaning</h4>
        <ol>
            <li>The exam was a piece of _______. (cake)</li>
            <li>I'm feeling a bit under the _______. (weather)</li>
            <li>That car cost an arm and a _______. (leg)</li>
            <li>Let's call it a _______ and go home. (day)</li>
        </ol>
    </section>
    """)

def get_grammar_advanced_content():
    """Gramática avanzada para consolidación"""
    return Markup("""
    <h1>📚 Advanced Grammar Review</h1>
    
    <section id="tenses-review">
        <h2>⏰ COMPLETE TENSE REVIEW</h2>
        
        <div class="grammar-section">
            <h3>All 12 Tenses at a Glance</h3>
            <table>
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Simple</th>
                        <th>Continuous</th>
                        <th>Perfect</th>
                        <th>Perfect Continuous</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>PAST</strong></td>
                        <td>I worked</td>
                        <td>I was working</td>
                        <td>I had worked</td>
                        <td>I had been working</td>
                    </tr>
                    <tr>
                        <td><strong>PRESENT</strong></td>
                        <td>I work</td>
                        <td>I am working</td>
                        <td>I have worked</td>
                        <td>I have been working</td>
                    </tr>
                    <tr>
                        <td><strong>FUTURE</strong></td>
                        <td>I will work</td>
                        <td>I will be working</td>
                        <td>I will have worked</td>
                        <td>I will have been working</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <h3>When to Use Each Tense</h3>
        
        <div class="grammar-section">
            <h4>PRESENT TENSES</h4>
            <ul>
                <li><strong>Present Simple:</strong> habits, facts, routines → I work every day. Water boils at 100°C.</li>
                <li><strong>Present Continuous:</strong> actions happening now, temporary situations → I'm working right now.</li>
                <li><strong>Present Perfect:</strong> past action with present relevance, experience → I have visited Paris. (sometime in my life)</li>
                <li><strong>Present Perfect Continuous:</strong> action started in past, still continuing → I have been working here for 5 years.</li>
            </ul>
            
            <h4>PAST TENSES</h4>
            <ul>
                <li><strong>Past Simple:</strong> completed actions at specific time → I worked yesterday.</li>
                <li><strong>Past Continuous:</strong> action in progress at past moment → I was working when you called.</li>
                <li><strong>Past Perfect:</strong> action before another past action → I had worked there before I moved.</li>
                <li><strong>Past Perfect Continuous:</strong> duration before past moment → I had been working for 3 hours when the power went out.</li>
            </ul>
            
            <h4>FUTURE TENSES</h4>
            <ul>
                <li><strong>Future Simple:</strong> predictions, spontaneous decisions → I will work tomorrow.</li>
                <li><strong>Future Continuous:</strong> action in progress at future time → I will be working at 3 PM.</li>
                <li><strong>Future Perfect:</strong> action completed before future time → I will have finished by 6 PM.</li>
                <li><strong>Going to:</strong> plans, intentions, predictions with evidence → I'm going to work harder.</li>
            </ul>
        </div>
        
        <h4>Exercise: Choose the correct tense</h4>
        <ol>
            <li>I _______ (work) here since 2020. (have worked / have been working)</li>
            <li>She _______ (study) when the phone rang. (was studying)</li>
            <li>By next year, I _______ (finish) my degree. (will have finished)</li>
            <li>He _______ (never/try) sushi before. (has never tried)</li>
            <li>What _______ you _______ (do) at 8 PM yesterday? (were you doing)</li>
        </ol>
    </section>
    
    <section id="conditionals">
        <h2>🔀 CONDITIONALS</h2>
        
        <div class="grammar-section">
            <h3>The Four Conditionals</h3>
            
            <h4>Zero Conditional (Real facts)</h4>
            <p><strong>If + Present Simple, Present Simple</strong></p>
            <ul>
                <li>If you heat water to 100°C, it boils.</li>
                <li>If I don't eat breakfast, I feel tired.</li>
            </ul>
            
            <h4>First Conditional (Real possibility)</h4>
            <p><strong>If + Present Simple, Will + base verb</strong></p>
            <ul>
                <li>If it rains tomorrow, I will stay home.</li>
                <li>If you study hard, you will pass the exam.</li>
            </ul>
            
            <h4>Second Conditional (Unreal/Hypothetical)</h4>
            <p><strong>If + Past Simple, Would + base verb</strong></p>
            <ul>
                <li>If I won the lottery, I would travel the world.</li>
                <li>If I were you, I would accept the job. (Note: "were" for all subjects)</li>
            </ul>
            
            <h4>Third Conditional (Impossible - past regrets)</h4>
            <p><strong>If + Past Perfect, Would have + past participle</strong></p>
            <ul>
                <li>If I had studied harder, I would have passed.</li>
                <li>If she had left earlier, she wouldn't have missed the train.</li>
            </ul>
        </div>
        
        <h4>Exercise: Complete the conditionals</h4>
        <ol>
            <li>If I _______ rich, I would buy a big house. (were)</li>
            <li>If you heat ice, it _______. (melts)</li>
            <li>If I had known, I _______ you. (would have told)</li>
            <li>If it rains, we _______ stay inside. (will)</li>
            <li>If I _______ you, I would study more. (were)</li>
        </ol>
    </section>
    
    <section id="reported-speech">
        <h2>💬 REPORTED SPEECH</h2>
        
        <div class="grammar-section">
            <h3>Direct → Reported Speech Changes</h3>
            
            <table>
                <thead>
                    <tr>
                        <th>Direct Speech</th>
                        <th>Reported Speech</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Present Simple: "I work..."</td><td>Past Simple: He said he worked...</td></tr>
                    <tr><td>Present Continuous: "I am working..."</td><td>Past Continuous: He said he was working...</td></tr>
                    <tr><td>Past Simple: "I worked..."</td><td>Past Perfect: He said he had worked...</td></tr>
                    <tr><td>Will: "I will work..."</td><td>Would: He said he would work...</td></tr>
                    <tr><td>Can: "I can work..."</td><td>Could: He said he could work...</td></tr>
                </tbody>
            </table>
            
            <h3>Pronoun and Time Changes</h3>
            <ul>
                <li>I → he/she</li>
                <li>my → his/her</li>
                <li>today → that day</li>
                <li>tomorrow → the next day</li>
                <li>yesterday → the day before</li>
                <li>here → there</li>
                <li>now → then</li>
            </ul>
            
            <h3>Examples:</h3>
            <ul>
                <li>"I am tired." → She said <strong>she was tired</strong>.</li>
                <li>"I will call you tomorrow." → He said <strong>he would call me the next day</strong>.</li>
                <li>"I have finished my work." → She said <strong>she had finished her work</strong>.</li>
            </ul>
        </div>
        
        <h4>Exercise: Change to reported speech</h4>
        <ol>
            <li>"I love this movie." → She said... (she loved that movie)</li>
            <li>"I will help you." → He said... (he would help me)</li>
            <li>"I am studying English." → She said... (she was studying English)</li>
        </ol>
    </section>
    
    <section id="passive-voice">
        <h2>🔄 PASSIVE VOICE</h2>
        
        <div class="grammar-section">
            <h3>Structure: Subject + BE + Past Participle (+ by agent)</h3>
            
            <table>
                <thead>
                    <tr>
                        <th>Tense</th>
                        <th>Active</th>
                        <th>Passive</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Present Simple</td><td>They make cars here.</td><td>Cars are made here.</td></tr>
                    <tr><td>Past Simple</td><td>They built the house.</td><td>The house was built.</td></tr>
                    <tr><td>Present Perfect</td><td>They have finished the work.</td><td>The work has been finished.</td></tr>
                    <tr><td>Future</td><td>They will deliver the package.</td><td>The package will be delivered.</td></tr>
                    <tr><td>Modal</td><td>They can repair it.</td><td>It can be repaired.</td></tr>
                </tbody>
            </table>
            
            <h3>When to use Passive:</h3>
            <ul>
                <li>When the action is more important than who did it</li>
                <li>When we don't know who did the action</li>
                <li>In formal/scientific writing</li>
            </ul>
        </div>
        
        <h4>Exercise: Change to passive voice</h4>
        <ol>
            <li>Someone stole my phone. → My phone... (was stolen)</li>
            <li>They speak English here. → English... (is spoken here)</li>
            <li>They will announce the results tomorrow. → The results... (will be announced tomorrow)</li>
        </ol>
    </section>
    """)
