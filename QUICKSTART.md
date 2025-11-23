# ⚡ Inicio Rápido

## Verificar que todo funciona antes de desplegar

### 1️⃣ Instalar dependencias

```powershell
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Si hay error de permisos, ejecuta:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Instalar dependencias
pip install -r requirements.txt
```

### 2️⃣ Ejecutar la aplicación

```powershell
python app.py
```

Deberías ver algo como:
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

### 3️⃣ Abrir en el navegador

Abre tu navegador en: **http://localhost:5000**

Deberías ver:
- ✅ Lista de 12 niveles básicos (B01-B12)
- ✅ 12 niveles intermedios (placeholders)
- ✅ Cada nivel clickeable que muestra su contenido

### 4️⃣ Probar con Gunicorn (producción)

```powershell
# Detener el servidor anterior (Ctrl+C)

# Iniciar con Gunicorn (como en Render)
gunicorn app:app
```

Deberías ver:
```
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://127.0.0.1:8000
[INFO] Using worker: sync
[INFO] Booting worker with pid: XXXX
```

Abre: **http://localhost:8000**

### 5️⃣ Verificar archivos de despliegue

```powershell
# Verificar que existen los archivos necesarios
ls render.yaml
ls requirements.txt
ls .python-version
ls .gitignore
ls build.sh
```

Todos deben existir ✅

### 6️⃣ Preparar para Git

```powershell
# Inicializar repositorio Git (si no lo has hecho)
git init

# Agregar archivos
git add .

# Revisar qué se va a subir
git status

# Hacer commit
git commit -m "Preparar proyecto ICPNA para despliegue en Render"
```

### 7️⃣ Subir a GitHub

```powershell
# Crear repositorio en GitHub primero (github.com/new)
# Luego conectar:

git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git branch -M main
git push -u origin main
```

---

## ✅ Checklist Pre-Despliegue

Antes de desplegar en Render, verifica:

- [ ] ✅ La app funciona localmente con `python app.py`
- [ ] ✅ La app funciona con gunicorn: `gunicorn app:app`
- [ ] ✅ Existe `render.yaml` con la configuración
- [ ] ✅ `requirements.txt` tiene Flask y gunicorn
- [ ] ✅ `.python-version` existe
- [ ] ✅ `.gitignore` está configurado
- [ ] ✅ El código está en GitHub
- [ ] ✅ README.md tiene instrucciones de despliegue

---

## 🚀 Siguiente Paso

Si todo funciona correctamente:
1. Ve al archivo **DEPLOY.md**
2. Sigue los pasos para desplegar en Render
3. Tu app estará en línea en 2-3 minutos

---

## 🐛 Problemas Comunes

### Error: "No module named 'flask'"
```powershell
pip install Flask
```

### Error: "No module named 'gunicorn'"
```powershell
pip install gunicorn
```

### Error: "Cannot activate virtual environment"
```powershell
# Windows PowerShell - permitir scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Luego activar de nuevo
.\.venv\Scripts\Activate.ps1
```

### El navegador no carga localhost:5000
- Verifica que el servidor esté corriendo (no debe haber errores en la consola)
- Prueba con: http://127.0.0.1:5000
- Revisa que no haya otro proceso usando el puerto 5000

### Git no reconoce cambios
```powershell
git add -A
git status
```

---

**¡Todo listo! Ahora puedes desplegar en Render 🎉**
