# 📚 ICPNA BÁSICOS (B01-B12) - Syllabus Completo

Aplicación web interactiva con el contenido completo de los 12 niveles básicos del ICPNA (Instituto Cultural Peruano Norteamericano), basada en la serie **World Link**.

## 🌟 Características

- **12 Niveles Básicos (B01-B12)** con contenido detallado
- Gramática, vocabulario, listening y reading de cada unidad
- Interfaz limpia y responsive
- Navegación intuitiva por niveles
- Contenido organizado según syllabus ICPNA oficial

## 📋 Niveles MCER

- **B01-B04:** A1
- **B05-B08:** A2
- **B09-B12:** A2+

## 🚀 Despliegue Rápido en Render

### Opción 1: Despliegue con un clic (Recomendado)

1. Haz fork o sube este proyecto a tu GitHub
2. Ve a [Render](https://render.com) e inicia sesión
3. Click en **"New +"** → **"Web Service"**
4. Conecta tu repositorio de GitHub
5. Render detectará automáticamente el `render.yaml`
6. Click en **"Apply"** y espera el despliegue (2-3 minutos)
7. ¡Listo! Tu app estará en línea en `https://tu-app.onrender.com`

### Opción 2: Configuración manual en Render

1. Sube tu código a GitHub
2. En Render, crea un nuevo **Web Service**
3. Conecta tu repositorio
4. Configura:
   - **Name:** `icpna-basicos-syllabus` (o el que prefieras)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free
5. Click en **"Create Web Service"**

### Variables de entorno (Opcional)

Render configura automáticamente el puerto. No necesitas variables de entorno adicionales.

## 💻 Desarrollo Local

### Requisitos
- Python 3.11+
- Git

### Instalación

```bash
# Clonar el repositorio
git clone <tu-repositorio>
cd 27\ NOVEMBER\ XD

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.\.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar localmente

```bash
python app.py
# Abre http://127.0.0.1:5000/
```

## 📁 Estructura del Proyecto

```
.
├── app.py                 # Aplicación Flask principal
├── b02_content.py         # Contenido B02-B04
├── b03_content.py         # Contenido B03
├── b04_content.py         # Contenido B04
├── b05_content.py         # Contenido B05-B06
├── b06_content.py         # Contenido B06
├── b07_content.py         # Contenido B07-B08
├── b08_content.py         # Contenido B08
├── b09_content.py         # Contenido B09-B10
├── b10_content.py         # Contenido B10
├── b11_content.py         # Contenido B11-B12
├── b12_content.py         # Contenido B12
├── requirements.txt       # Dependencias Python
├── render.yaml            # Configuración de Render
├── .python-version        # Versión de Python
├── .gitignore             # Archivos a ignorar
├── templates/             # Plantillas Jinja2
│   ├── base.html
│   ├── index.html
│   └── lesson.html
└── static/                # Archivos estáticos
    ├── style.css
    └── manifest.json
```

## 🎯 Contenido del Syllabus

### B01-B02: Fundamentos
- Alfabeto, números, saludos
- Verb "to be", pronombres
- Present simple & continuous
- Vocabulario básico

### B03-B04: Construcción
- Rutinas diarias
- Imperativo, can/can't
- Lugares y direcciones
- Ropa y hogar

### B05-B06: Consolidación A2
- Adverbios de frecuencia
- Comparativos y superlativos
- Gerundios e infinitivos
- Descripciones detalladas

### B07-B08: Past & Future
- Simple past (regular/irregular)
- Going to & will
- Should/shouldn't
- Salud y consejos

### B09-B10: Present Perfect
- Present perfect
- Already/yet/just
- For/since
- Experiencias y logros

### B11-B12: Avanzado A2+
- Past continuous
- Solicitudes corteses
- Might/may
- Gerundios e infinitivos avanzados

## 🛠️ Tecnologías

- **Flask** 2.2+ - Framework web
- **Gunicorn** 21.2+ - Servidor WSGI para producción
- **Python** 3.11
- **Jinja2** - Motor de plantillas
- **HTML5/CSS3** - Frontend

## 📝 Notas Importantes

- El plan **Free** de Render puede tener "cold starts" (demora inicial al acceder después de inactividad)
- El servicio se "duerme" después de 15 minutos de inactividad
- Para mantenerlo activo 24/7, considera el plan Starter ($7/mes)

## 🤝 Contribuir

¿Quieres mejorar el contenido o agregar funcionalidades?

1. Fork el proyecto
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -m 'Agregar nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 📧 Contacto

Para preguntas o sugerencias sobre el contenido del syllabus ICPNA, consulta con tu coordinador académico.

---

**¡Buena suerte con tu aprendizaje de inglés! 🎓✨**
