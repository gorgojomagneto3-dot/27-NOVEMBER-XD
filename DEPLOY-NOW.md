# 🚀 DESPLEGAR AHORA - Guía Express

## ✅ Estado: LISTO PARA DEPLOY

Tu proyecto está completamente configurado. Sigue estos pasos:

---

## 📋 Opción 1: Deploy Automático (RECOMENDADO - 10 minutos)

### Paso 1: Verificar Git Status
```powershell
git status
```

**¿Qué deberías ver?**
- Si dice "nothing to commit" → **Perfecto, ve al Paso 2**
- Si hay archivos sin commit → Continúa con los comandos de abajo

```powershell
git add .
git commit -m "Proyecto ICPNA B01-B12 listo para Render"
```

### Paso 2: Verificar Remote de GitHub
```powershell
git remote -v
```

**¿Tienes un remote configurado?**
- ✅ **SÍ** → Ve al Paso 3
- ❌ **NO** → Ejecuta esto:

```powershell
# Crea el repo en GitHub primero: https://github.com/new
# Luego ejecuta (reemplaza con tus datos):
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
```

### Paso 3: Push a GitHub
```powershell
git push origin main
```

**Si te pide autenticación:**
- Usuario: tu usuario de GitHub
- Contraseña: usa un **Personal Access Token** (no tu contraseña)
  - Créalo en: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - Permisos: marca solo "repo"

### Paso 4: Desplegar en Render

1. **Ve a:** https://render.com
2. **Login** o crea cuenta (gratis)
3. Click **"New +"** (botón azul arriba a la derecha)
4. Selecciona **"Web Service"**
5. Click **"Connect account"** para conectar GitHub
6. Busca tu repositorio y click **"Connect"**
7. Render detectará `render.yaml` automáticamente
8. Click **"Apply"**
9. **Espera 2-3 minutos** mientras se despliega
10. ¡Listo! Tu URL será: `https://tu-app-nombre.onrender.com`

---

## 📋 Opción 2: Deploy Manual (si no detecta render.yaml)

Si Render no detecta el archivo automáticamente:

**Configuración Manual:**
- **Name:** `icpna-basicos-syllabus` (o el que prefieras)
- **Region:** Oregon
- **Branch:** main
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Plan:** Free

Click **"Create Web Service"** y espera 2-3 minutos.

---

## 🔍 Verificar el Deploy

Una vez desplegado:

1. ✅ Abre la URL de tu app
2. ✅ Verifica que se ve la lista de niveles B01-B12
3. ✅ Click en un nivel para ver su contenido
4. ✅ Verifica que el CSS se aplica correctamente

---

## 🐛 Si Algo Sale Mal

### Error: "Build failed"
**Ver logs en Render:**
- Dashboard → Tu servicio → Logs

**Causas comunes:**
- `requirements.txt` incorrecto
- Python version incompatible

### Error: "Application failed to start"
**Verificar:**
- Logs en Render
- Que `gunicorn` esté en `requirements.txt`
- Que `app.py` use puerto dinámico

### La app está muy lenta
**Es normal en plan Free:**
- Primer acceso después de inactividad toma 30-60 seg (cold start)
- Solución: usa UptimeRobot para mantenerla activa (gratis)
- O upgrade a Starter ($7/mes)

---

## ✅ Checklist Rápido

Antes de desplegar:

- [x] ✅ Archivos críticos verificados (render.yaml, requirements.txt, etc.)
- [x] ✅ Git inicializado
- [x] ✅ Remote configurado
- [ ] 📋 Código en GitHub (push completado)
- [ ] 📋 Cuenta en Render creada
- [ ] 📋 Repositorio conectado a Render
- [ ] 📋 Deploy completado
- [ ] 📋 URL verificada funcionando

---

## 🎯 Comandos Rápidos (Copiar y Pegar)

```powershell
# 1. Verificar estado
git status

# 2. Si hay cambios sin commit
git add .
git commit -m "Listo para Render"

# 3. Ver remote
git remote -v

# 4. Push a GitHub
git push origin main

# 5. Ahora ve a render.com y despliega
```

---

## 📱 Tu App Estará en:

```
https://TU-NOMBRE-APP.onrender.com
```

Ejemplo:
```
https://icpna-basicos-syllabus.onrender.com
```

---

## 💡 Después del Deploy

### Mantener Activa tu App (Plan Free)
Usa **UptimeRobot** (gratis) para hacer ping cada 5 minutos:
1. Ve a https://uptimerobot.com
2. Crea cuenta gratis
3. Add New Monitor
4. URL: tu app de Render
5. Monitoring Interval: 5 minutos

### Dominio Personalizado (Opcional)
Si tienes un dominio:
- Render Dashboard → Settings → Custom Domains
- Add Custom Domain
- Configura CNAME en tu registrador
- SSL gratuito automático

### Ver Logs en Tiempo Real
- Render Dashboard → Tu servicio → Logs

### Actualizar tu App
Cada vez que hagas cambios:
```powershell
git add .
git commit -m "Descripción de cambios"
git push
```
Render redesplegará automáticamente en 1-2 minutos.

---

## 📞 Ayuda

**Documentación completa:**
- [DEPLOY.md](DEPLOY.md) - Guía detallada
- [GIT_COMMANDS.md](GIT_COMMANDS.md) - Ayuda con Git
- [RENDER_CONFIG.md](RENDER_CONFIG.md) - Configuración avanzada

**Soporte Render:**
- https://render.com/docs
- https://community.render.com
- https://status.render.com

---

## 🎉 ¡Listo para Desplegar!

**Siguiente acción:** Ejecuta los comandos Git de arriba y ve a render.com

**Tiempo estimado:** 10 minutos total

**¡Éxito con tu deploy! 🚀**
