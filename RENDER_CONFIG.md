# Configuración Render - Referencia Rápida

## 📋 Configuración Manual en Render Dashboard

Si no usas `render.yaml`, estos son los valores para configurar manualmente:

### General
- **Name:** `icpna-basicos-syllabus` (o el que prefieras)
- **Region:** Oregon (US West)
- **Branch:** main
- **Root Directory:** (vacío)

### Build & Deploy
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

### Advanced
- **Auto-Deploy:** Yes (recomendado)
- **Health Check Path:** / (opcional)

---

## 🔧 Variables de Entorno (Opcionales)

Render configura automáticamente `PORT`, pero si necesitas otras:

```
PYTHON_VERSION=3.11.0
FLASK_ENV=production
```

---

## 📊 Especificaciones del Plan Free

- **RAM:** 512 MB
- **CPU:** Compartida
- **Almacenamiento:** Efímero
- **Instancias:** 1
- **Sleep después de:** 15 min de inactividad
- **Cold start:** 30-60 segundos
- **Deploy time:** 2-3 minutos
- **Bandwidth:** 100 GB/mes

---

## 🎯 Comandos Render CLI (Opcional)

Si prefieres usar CLI:

```bash
# Instalar Render CLI
npm install -g render

# Login
render login

# Crear servicio
render services create web \
  --name icpna-basicos-syllabus \
  --env python \
  --buildCommand "pip install -r requirements.txt" \
  --startCommand "gunicorn app:app" \
  --region oregon \
  --plan free

# Ver servicios
render services list

# Ver logs
render logs
```

---

## 🔍 Monitoreo

### Ver métricas en Render:
1. Dashboard → Tu servicio
2. Panel lateral → **Metrics**

Verás:
- CPU usage
- Memory usage
- HTTP requests
- Response times

### Ver logs:
- Dashboard → Tu servicio → **Logs**

---

## 🚨 Límites del Plan Free

### Límites mensuales:
- ✅ 750 horas de servicio (suficiente para 24/7)
- ✅ 100 GB de ancho de banda
- ✅ Deploys ilimitados

### Limitaciones:
- ⚠️ El servicio "duerme" después de 15 min sin tráfico
- ⚠️ Cold starts de 30-60 segundos
- ⚠️ No SSL personalizado (incluye SSL de Render)
- ⚠️ Dominio: `tu-app.onrender.com`

---

## 💡 Upgrade a Plan Starter ($7/mes)

Beneficios:
- ✅ Sin "sleep" - siempre activo
- ✅ Sin cold starts
- ✅ Más RAM y CPU
- ✅ Custom domains con SSL gratis
- ✅ Soporte prioritario

Para upgrade:
1. Dashboard → Tu servicio
2. Settings → Plan
3. Upgrade to Starter

---

## 🔐 Configuración de Dominio Personalizado

Si tienes un dominio (ejemplo: `icpna-basicos.com`):

1. Dashboard → Tu servicio → Settings → Custom Domains
2. Add Custom Domain: `icpna-basicos.com`
3. Render te dará un CNAME record
4. En tu registrador de dominios (GoDaddy, Namecheap, etc.):
   - Agrega CNAME record apuntando a Render
5. Espera propagación DNS (15 min - 24 horas)
6. Render genera automáticamente certificado SSL

---

## 🔄 Configuración de Auto-Deploy

Por defecto, Render detecta automáticamente los push a GitHub:

```
GitHub Push → Render detecta cambio → Build automático → Deploy
```

Para deshabilitar:
- Settings → Build & Deploy → Auto-Deploy: Off

---

## 📧 Notificaciones

Configurar notificaciones de deploy:

1. Dashboard → Tu servicio → Settings → Notifications
2. Add notification
3. Opciones:
   - Email
   - Slack
   - Discord
   - Webhook

---

## 🧹 Mantenimiento

### Ver historial de deploys:
Dashboard → Tu servicio → Events

### Rollback a versión anterior:
1. Events → Encuentra el deploy exitoso anterior
2. Click en "..." → Redeploy

### Suspender servicio temporalmente:
Settings → Suspend Service (no se cobrará)

---

## 📱 Aplicación Móvil Render

Descarga la app de Render para:
- Ver estado de servicios
- Ver logs en tiempo real
- Recibir notificaciones de deploy
- Iniciar redeploys

Disponible para:
- iOS: App Store
- Android: Google Play

---

## 🆘 Soporte

Si tienes problemas:

1. **Documentación:** https://render.com/docs
2. **Community:** https://community.render.com
3. **Status:** https://status.render.com (ver si hay incidentes)
4. **Email:** support@render.com (planes pagos)

---

## ✅ Archivo render.yaml (Referencia Completa)

```yaml
services:
  - type: web
    name: icpna-basicos-syllabus
    env: python
    region: oregon
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
    # Configuración avanzada (opcional)
    healthCheckPath: /
    autoDeploy: true
    # disk:
    #   name: data
    #   mountPath: /data
    #   sizeGB: 1
```

---

**¡Tu configuración está lista! 🎉**
