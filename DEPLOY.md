# 🚀 Guía Rápida de Despliegue en Render

## Pasos para desplegar tu app ICPNA en Render

### 📋 Pre-requisitos
- Cuenta en GitHub (gratuita)
- Cuenta en Render (gratuita) - [render.com](https://render.com)

---

## 🎯 Método 1: Despliegue Automático (RECOMENDADO)

### Paso 1: Subir a GitHub
```bash
# Inicializar Git (si no lo has hecho)
git init

# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "Preparar para despliegue en Render"

# Crear repositorio en GitHub y conectar
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git branch -M main
git push -u origin main
```

### Paso 2: Conectar con Render
1. Ve a [render.com](https://render.com) y haz login
2. Click en **"New +"** (botón azul arriba a la derecha)
3. Selecciona **"Web Service"**
4. Click en **"Connect account"** para conectar GitHub
5. Busca tu repositorio y click en **"Connect"**

### Paso 3: Configurar (Render lo detecta automáticamente)
Render detectará el archivo `render.yaml` y configurará todo automáticamente:
- ✅ Environment: Python 3
- ✅ Build Command: `pip install -r requirements.txt`
- ✅ Start Command: `gunicorn app:app`
- ✅ Plan: Free

6. Click en **"Apply"** o **"Create Web Service"**
7. Espera 2-3 minutos mientras se despliega
8. ¡Listo! Tu URL será: `https://tu-app-nombre.onrender.com`

---

## 🛠️ Método 2: Configuración Manual

Si Render no detecta el `render.yaml` automáticamente:

1. Después de conectar tu repo, configura manualmente:
   - **Name:** `icpna-basicos-syllabus` (o el que prefieras)
   - **Region:** Oregon (recomendado para Perú)
   - **Branch:** `main`
   - **Root Directory:** (dejar vacío)
   - **Environment:** `Python 3`
   - **Python Version:** `3.11.0`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free

2. Click en **"Create Web Service"**

---

## 📝 Verificar archivos antes de desplegar

Asegúrate de tener estos archivos en tu proyecto:

- ✅ `render.yaml` - Configuración automática
- ✅ `requirements.txt` - Dependencias (Flask, gunicorn)
- ✅ `.python-version` - Versión de Python
- ✅ `.gitignore` - Archivos a ignorar
- ✅ `app.py` - Con configuración de puerto dinámico
- ✅ `build.sh` - Script de construcción (opcional)

---

## 🔧 Actualizar tu App Desplegada

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción de cambios"
git push
```

Render detectará el push y **redesplegará automáticamente** (toma 1-2 minutos).

---

## 🐛 Solución de Problemas

### Error: "Build failed"
- Verifica que `requirements.txt` tenga todas las dependencias
- Revisa los logs en Render Dashboard → tu servicio → "Logs"

### Error: "Application failed to start"
- Verifica que `app.py` tenga el bloque de puerto dinámico
- Revisa que gunicorn esté en `requirements.txt`

### La app está lenta al primer acceso
- Es normal en el plan Free. Render "duerme" tu app después de 15 min de inactividad
- Primera carga puede tomar 30-60 segundos ("cold start")
- Para evitarlo: Upgrade al plan Starter ($7/mes)

### Ver los logs en vivo
En Render Dashboard:
1. Click en tu servicio
2. Click en "Logs" (panel izquierdo)
3. Verás los logs en tiempo real

---

## 💡 Tips Pro

1. **Custom Domain:** Puedes agregar tu dominio personalizado en Settings → Custom Domains

2. **Variables de Entorno:** Si necesitas agregar secrets:
   - Dashboard → tu servicio → Environment
   - Add Environment Variable

3. **Mantener activo 24/7 (Free plan hack):**
   - Usa un servicio como [UptimeRobot](https://uptimerobot.com) para hacer ping cada 5 minutos
   - Esto evita que Render "duerma" tu app

4. **Ver tu app mientras se despliega:**
   - Los despliegues aparecen en tiempo real en "Events"

---

## 📊 Recursos Útiles

- [Documentación Oficial Render](https://render.com/docs)
- [Render Status](https://status.render.com) - Ver si hay problemas de servicio
- [Render Community](https://community.render.com) - Foro de ayuda

---

## ✅ Checklist Final

Antes de desplegar, verifica:

- [ ] Código subido a GitHub
- [ ] `requirements.txt` actualizado con gunicorn
- [ ] `app.py` con configuración de puerto dinámico
- [ ] `render.yaml` en la raíz del proyecto
- [ ] `.gitignore` para no subir archivos innecesarios
- [ ] README.md actualizado
- [ ] Probado localmente con `python app.py`

---

**¡Tu app estará en línea en minutos! 🎉**
