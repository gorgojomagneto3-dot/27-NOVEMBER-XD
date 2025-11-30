"""
Content Module - Manages all lesson content
"""
from markupsafe import Markup

# Import all content functions
from b01_content_new import get_b01_content_new
from b02_content_new import get_b02_content_new
from b03_content_new import get_b03_content_new
from b04_content_new import get_b04_content_new
from b05_content_new import get_b05_content_new
from b06_content_new import get_b06_content_new
from b07_content_new import get_b07_content_new
from b08_content_new import get_b08_content_new
from b09_content_new import get_b09_content_new
from b10_content_new import get_b10_content_new
from b11_content_new import get_b11_content_new
from b12_content_new import get_b12_content_new
from int01_content import get_int01_content
from int02_content import get_int02_content
from int03_content import get_int03_content
from int04_content import get_int04_content
from int05_content import get_int05_content
from int06_content import get_int06_content
from int07_content import get_int07_content
from int08_content import get_int08_content
from int09_content import get_int09_content
from int10_content import get_int10_content
from int11_content import get_int11_content
from int12_content import get_int12_content
from exam_prep_content import (
    get_exam_prep_content, 
    get_common_mistakes_content,
    get_phrasal_verbs_content,
    get_grammar_advanced_content
)

def get_all_lessons():
    """Return all lessons metadata"""
    lessons = [
        # Basic Level (B01-B12)
        {"id": "b1", "level": "Básico", "title": "Básico 01 - A1 Inicial: Introductions & BE verb"},
        {"id": "b2", "level": "Básico", "title": "Básico 02 - A1 Inicial: Present Continuous & Daily Life"},
        {"id": "b3", "level": "Básico", "title": "Básico 03 - A1 Final: Time, Schedules & Past BE"},
        {"id": "b4", "level": "Básico", "title": "Básico 04 - A1 Final: Shopping, Jobs & Modals"},
        {"id": "b5", "level": "Básico", "title": "Básico 05 - A2 Inicial: Descriptions & Food"},
        {"id": "b6", "level": "Básico", "title": "Básico 06 - A2 Inicial: Past Simple & Comparatives"},
        {"id": "b7", "level": "Básico", "title": "Básico 07 - A2 Avanzado: City Life & Superlatives"},
        {"id": "b8", "level": "Básico", "title": "Básico 08 - A2 Avanzado: Past Continuous & Storytelling"},
        {"id": "b9", "level": "Básico", "title": "Básico 09 - B1 Inicial: Present Perfect & Advice"},
        {"id": "b10", "level": "Básico", "title": "Básico 10 - B1 Inicial: Future Tenses & Goals"},
        {"id": "b11", "level": "Básico", "title": "Básico 11 - B1.1: Celebrations, Storytelling & Work"},
        {"id": "b12", "level": "Básico", "title": "Básico 12 - B1.2 FINAL: People, Feelings & Shopping"},
        
        # Intermediate Level (INT01-INT12)
        # I01-I04: World Link Intermediate 1 (3rd Ed.)
        {"id": "int1", "level": "Intermedio", "title": "Intermedio 01 - Friends & Family: Relative Clauses"},
        {"id": "int2", "level": "Intermedio", "title": "Intermedio 02 - Working Week: Dynamic/Stative Verbs"},
        {"id": "int3", "level": "Intermedio", "title": "Intermedio 03 - Creativity: Problem Solving & Ability"},
        {"id": "int4", "level": "Intermedio", "title": "Intermedio 04 - Second Self: Wish/If Only & Conditionals"},
        # I05-I08: World Pass Book 1
        {"id": "int5", "level": "Intermedio", "title": "Intermedio 05 - Brainpower: Memory & Gerund/Infinitive"},
        {"id": "int6", "level": "Intermedio", "title": "Intermedio 06 - Storytelling: Narrative Tenses & Adverbs"},
        {"id": "int7", "level": "Intermedio", "title": "Intermedio 07 - Design: Passive Voice & Materials"},
        {"id": "int8", "level": "Intermedio", "title": "Intermedio 08 - Science: Future Forms & Connectors"},
        # I09-I12: American Big Picture B2-C1
        {"id": "int9", "level": "Intermedio", "title": "Intermedio 09 - Social Networks: Auxiliary Verbs & Reflexives"},
        {"id": "int10", "level": "Intermedio", "title": "Intermedio 10 - Reinvention: Word Formation & Idioms"},
        {"id": "int11", "level": "Intermedio", "title": "Intermedio 11 - Rules & Luck: Past Modals & Cleft Sentences"},
        {"id": "int12", "level": "Intermedio", "title": "Intermedio 12 - Value for Money: Past Perfect & Finance"},
        
        # Special Sections
        {"id": "exam-prep", "level": "Especial", "title": "🎯 Exam Preparation - TOEFL/IELTS/Cambridge"},
        {"id": "common-mistakes", "level": "Especial", "title": "⚠️ Common Mistakes - Spanish Speakers"},
        {"id": "phrasal-verbs", "level": "Especial", "title": "🚀 Phrasal Verbs & Idioms"},
        {"id": "advanced-grammar", "level": "Especial", "title": "📚 Advanced Grammar Review"},
    ]
    return lessons

def get_lesson_by_id(lesson_id):
    """Get lesson by ID with full content"""
    content_map = {
        'b1': get_b01_content_new,
        'b2': get_b02_content_new,
        'b3': get_b03_content_new,
        'b4': get_b04_content_new,
        'b5': get_b05_content_new,
        'b6': get_b06_content_new,
        'b7': get_b07_content_new,
        'b8': get_b08_content_new,
        'b9': get_b09_content_new,
        'b10': get_b10_content_new,
        'b11': get_b11_content_new,
        'b12': get_b12_content_new,
        'int1': get_int01_content,
        'int2': get_int02_content,
        'int3': get_int03_content,
        'int4': get_int04_content,
        'int5': get_int05_content,
        'int6': get_int06_content,
        'int7': get_int07_content,
        'int8': get_int08_content,
        'int9': get_int09_content,
        'int10': get_int10_content,
        'int11': get_int11_content,
        'int12': get_int12_content,
        'exam-prep': get_exam_prep_content,
        'common-mistakes': get_common_mistakes_content,
        'phrasal-verbs': get_phrasal_verbs_content,
        'advanced-grammar': get_grammar_advanced_content,
    }
    
    lessons = get_all_lessons()
    lesson_meta = next((l for l in lessons if l['id'] == lesson_id), None)
    
    if not lesson_meta or lesson_id not in content_map:
        return None
    
    content = content_map[lesson_id]()
    # Convert Markup to string for JSON serialization
    content_str = str(content) if isinstance(content, Markup) else content
    
    return {
        'id': lesson_id,
        'level': lesson_meta['level'],
        'title': lesson_meta['title'],
        'content': content_str
    }
