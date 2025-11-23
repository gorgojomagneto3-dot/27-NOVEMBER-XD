# 🔄 Comandos Git - Referencia Rápida

## Para subir tu proyecto a GitHub y desplegar en Render

---

## 📋 Pasos Completos (Primera vez)

### 1. Inicializar Git (si no lo has hecho)
```powershell
git init
```

### 2. Agregar todos los archivos
```powershell
git add .
```

### 3. Ver qué archivos se van a subir
```powershell
git status
```

Deberías ver en verde:
- ✅ render.yaml
- ✅ requirements.txt
- ✅ .python-version
- ✅ app.py
- ✅ Todos los archivos .md
- ✅ Archivos b02-b12_content.py
- ✅ Templates y static

**NO deberías ver:**
- ❌ .venv/ (ignorado)
- ❌ __pycache__/ (ignorado)
- ❌ *.pyc (ignorado)

### 4. Hacer commit
```powershell
git commit -m "Proyecto ICPNA B01-B12 listo para despliegue en Render"
```

### 5. Crear repositorio en GitHub
1. Ve a [github.com/new](https://github.com/new)
2. Nombre del repositorio: `icpna-basicos-syllabus` (o el que prefieras)
3. Descripción: "ICPNA Básicos B01-B12 - Syllabus interactivo"
4. **Public** o **Private** (ambos funcionan con Render)
5. **NO marques** "Add README" (ya tienes uno)
6. Click **"Create repository"**

### 6. Conectar tu repo local con GitHub
```powershell
# Reemplaza TU-USUARIO y TU-REPOSITORIO con tus datos
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

Ejemplo:
```powershell
git remote add origin https://github.com/dpovida/icpna-basicos-syllabus.git
```

### 7. Renombrar rama a main (si es necesario)
```powershell
git branch -M main
```

### 8. Subir a GitHub
```powershell
git push -u origin main
```

Te pedirá autenticación:
- **Usuario:** tu usuario de GitHub
- **Contraseña:** usa un **Personal Access Token** (no tu contraseña)

#### ¿Cómo crear un Personal Access Token?
1. GitHub → Settings (tu perfil, arriba a la derecha)
2. Developer settings (abajo a la izquierda)
3. Personal access tokens → Tokens (classic)
4. Generate new token (classic)
5. Nombre: "Render Deploy"
6. Permisos: marca solo **"repo"**
7. Generate token
8. **Copia el token** (solo se muestra una vez)
9. Úsalo como contraseña en el push

---

## 🔄 Actualizar tu app (después del primer push)

Cada vez que hagas cambios:

```powershell
# Ver archivos modificados
git status

# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "Descripción de los cambios"

# Subir a GitHub
git push
```

Render detectará el push y redesplegará automáticamente (1-2 minutos).

---

## 🛠️ Comandos Git Útiles

### Ver historial de commits
```powershell
git log --oneline
```

### Ver diferencias antes de commit
```powershell
git diff
```

### Deshacer cambios no commiteados
```powershell
# Deshacer cambios en un archivo específico
git checkout -- nombre-archivo.py

# Deshacer todos los cambios
git checkout -- .
```

### Ver ramas
```powershell
git branch
```

### Crear nueva rama
```powershell
git checkout -b nueva-funcionalidad
```

### Volver a main
```powershell
git checkout main
```

### Ver el remote configurado
```powershell
git remote -v
```

### Cambiar URL del remote (si te equivocaste)
```powershell
git remote set-url origin https://github.com/TU-USUARIO/TU-REPO.git
```

---

## 📦 .gitignore (Ya está configurado)

Tu `.gitignore` ya incluye:
```
__pycache__/
*.pyc
.venv/
venv/
.env
*.log
.DS_Store
```

Esto evita subir archivos innecesarios a GitHub.

---

## 🔐 Autenticación SSH (Alternativa más segura)

En lugar de HTTPS + token, puedes usar SSH:

### 1. Generar clave SSH (una sola vez)
```powershell
ssh-keygen -t ed25519 -C "tu-email@example.com"
```

Presiona Enter 3 veces (usar valores por defecto).

### 2. Copiar la clave pública
```powershell
cat ~/.ssh/id_ed25519.pub
```

### 3. Agregar en GitHub
1. GitHub → Settings → SSH and GPG keys
2. New SSH key
3. Pega la clave pública
4. Save

### 4. Cambiar remote a SSH
```powershell
git remote set-url origin git@github.com:TU-USUARIO/TU-REPO.git
```

Ahora no necesitarás token para hacer push.

---

## 🐛 Solución de Problemas

### Error: "fatal: not a git repository"
```powershell
git init
```

### Error: "remote origin already exists"
```powershell
# Ver el remote actual
git remote -v

# Cambiarlo si es necesario
git remote set-url origin https://github.com/TU-USUARIO/TU-REPO.git
```

### Error: "failed to push some refs"
```powershell
# Pull primero (si hay cambios en GitHub)
git pull origin main --rebase

# Luego push
git push origin main
```

### Error: "Permission denied (publickey)"
Si usas SSH y tienes este error:
```powershell
# Agregar la clave al ssh-agent
ssh-add ~/.ssh/id_ed25519

# Verificar conexión
ssh -T git@github.com
```

### Olvidé hacer commit de algunos archivos
```powershell
# Agregar los archivos faltantes
git add archivo-olvidado.py

# Añadir al último commit (no crear commit nuevo)
git commit --amend --no-edit

# Si ya hiciste push, necesitas:
git push --force
```

---

## 📝 Mensajes de Commit Recomendados

Buenos ejemplos:
```powershell
git commit -m "Agregar contenido B05"
git commit -m "Corregir error en app.py"
git commit -m "Actualizar README con instrucciones de despliegue"
git commit -m "Mejorar estilos CSS"
```

Evita:
```powershell
git commit -m "fix"
git commit -m "update"
git commit -m "cambios"
```

---

## 🚀 Workflow Completo

```powershell
# 1. Hacer cambios en tu código (editar archivos)

# 2. Ver qué cambió
git status
git diff

# 3. Agregar cambios
git add .

# 4. Commit
git commit -m "Descripción clara de los cambios"

# 5. Push a GitHub
git push

# 6. Render redespliega automáticamente (espera 1-2 min)

# 7. Verificar en: https://tu-app.onrender.com
```

---

## ✅ Checklist Git

Antes de hacer push:

- [ ] ✅ Ejecuté `git status` para ver cambios
- [ ] ✅ Agregué todos los archivos necesarios con `git add`
- [ ] ✅ Commit tiene un mensaje descriptivo
- [ ] ✅ `.gitignore` está configurado (no subir .venv ni __pycache__)
- [ ] ✅ Probé la app localmente antes de subir
- [ ] ✅ README.md está actualizado

---

## 🔗 Enlaces Útiles

- **GitHub:** https://github.com
- **Git Documentation:** https://git-scm.com/doc
- **GitHub CLI:** https://cli.github.com (alternativa a comandos git)
- **GitKraken:** https://www.gitkraken.com (GUI para Git)

---

**¡Listo para subir tu código! 🎉**

Siguiente paso: [DEPLOY.md](DEPLOY.md) para desplegar en Render.
