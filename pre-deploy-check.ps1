# Script de verificación pre-despliegue
# Ejecutar con: .\pre-deploy-check.ps1

Write-Host "`n=== 🔍 VERIFICACIÓN PRE-DESPLIEGUE ===" -ForegroundColor Cyan
Write-Host ""

$errors = 0
$warnings = 0

# 1. Verificar archivos críticos
Write-Host "1. Verificando archivos críticos..." -ForegroundColor Yellow

$criticalFiles = @(
    "app.py",
    "render.yaml",
    "requirements.txt",
    ".python-version",
    ".gitignore",
    "README.md"
)

foreach ($file in $criticalFiles) {
    if (Test-Path $file) {
        Write-Host "   ✅ $file existe" -ForegroundColor Green
    } else {
        Write-Host "   ❌ $file NO ENCONTRADO" -ForegroundColor Red
        $errors++
    }
}

# 2. Verificar archivos de contenido
Write-Host "`n2. Verificando archivos de contenido..." -ForegroundColor Yellow

$contentFiles = @(
    "b02_content.py",
    "b03_content.py",
    "b04_content.py",
    "b05_content.py",
    "b06_content.py",
    "b07_content.py",
    "b08_content.py",
    "b09_content.py",
    "b10_content.py",
    "b11_content.py",
    "b12_content.py"
)

$missingContent = 0
foreach ($file in $contentFiles) {
    if (!(Test-Path $file)) {
        Write-Host "   ⚠️  $file NO ENCONTRADO" -ForegroundColor Yellow
        $missingContent++
    }
}

if ($missingContent -eq 0) {
    Write-Host "   ✅ Todos los archivos de contenido existen" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Faltan $missingContent archivos de contenido" -ForegroundColor Yellow
    $warnings++
}

# 3. Verificar templates y static
Write-Host "`n3. Verificando directorios..." -ForegroundColor Yellow

if (Test-Path "templates") {
    Write-Host "   ✅ Directorio templates/ existe" -ForegroundColor Green
} else {
    Write-Host "   ❌ Directorio templates/ NO ENCONTRADO" -ForegroundColor Red
    $errors++
}

if (Test-Path "static") {
    Write-Host "   ✅ Directorio static/ existe" -ForegroundColor Green
} else {
    Write-Host "   ❌ Directorio static/ NO ENCONTRADO" -ForegroundColor Red
    $errors++
}

# 4. Verificar contenido de requirements.txt
Write-Host "`n4. Verificando requirements.txt..." -ForegroundColor Yellow

$reqContent = Get-Content "requirements.txt" -Raw
if ($reqContent -match "Flask") {
    Write-Host "   ✅ Flask está en requirements.txt" -ForegroundColor Green
} else {
    Write-Host "   ❌ Flask NO está en requirements.txt" -ForegroundColor Red
    $errors++
}

if ($reqContent -match "gunicorn") {
    Write-Host "   ✅ gunicorn está en requirements.txt" -ForegroundColor Green
} else {
    Write-Host "   ❌ gunicorn NO está en requirements.txt" -ForegroundColor Red
    $errors++
}

# 5. Verificar configuración de app.py
Write-Host "`n5. Verificando app.py..." -ForegroundColor Yellow

$appContent = Get-Content "app.py" -Raw
if ($appContent -match "0\.0\.0\.0") {
    Write-Host "   ✅ app.py tiene host='0.0.0.0'" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  app.py podría no tener host='0.0.0.0'" -ForegroundColor Yellow
    $warnings++
}

if ($appContent -match "PORT") {
    Write-Host "   ✅ app.py usa PORT de entorno" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  app.py podría no usar PORT de entorno" -ForegroundColor Yellow
    $warnings++
}

# 6. Verificar .gitignore
Write-Host "`n6. Verificando .gitignore..." -ForegroundColor Yellow

$gitignoreContent = Get-Content ".gitignore" -Raw
if ($gitignoreContent -match "__pycache__") {
    Write-Host "   ✅ .gitignore incluye __pycache__" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  .gitignore podría no incluir __pycache__" -ForegroundColor Yellow
    $warnings++
}

if ($gitignoreContent -match "\.venv|venv") {
    Write-Host "   ✅ .gitignore incluye venv" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  .gitignore podría no incluir venv" -ForegroundColor Yellow
    $warnings++
}

# 7. Verificar Git
Write-Host "`n7. Verificando Git..." -ForegroundColor Yellow

if (Test-Path ".git") {
    Write-Host "   ✅ Repositorio Git inicializado" -ForegroundColor Green
    
    # Verificar si hay remote
    $remotes = git remote
    if ($remotes) {
        Write-Host "   ✅ Remote configurado: $remotes" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️  No hay remote configurado (necesario para Render)" -ForegroundColor Yellow
        $warnings++
    }
} else {
    Write-Host "   ⚠️  Git no inicializado (ejecuta: git init)" -ForegroundColor Yellow
    $warnings++
}

# 8. Verificar Python
Write-Host "`n8. Verificando Python..." -ForegroundColor Yellow

try {
    $pythonVersion = python --version 2>&1
    Write-Host "   ℹ️  $pythonVersion instalado" -ForegroundColor Cyan
    
    if ($pythonVersion -match "3\.(9|10|11|12)") {
        Write-Host "   ✅ Versión de Python compatible" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️  Versión de Python podría no ser compatible (recomendado: 3.11)" -ForegroundColor Yellow
        $warnings++
    }
} catch {
    Write-Host "   ❌ Python no encontrado en PATH" -ForegroundColor Red
    $errors++
}

# 9. Verificar documentación
Write-Host "`n9. Verificando documentación..." -ForegroundColor Yellow

$docFiles = @(
    "DEPLOY.md",
    "QUICKSTART.md",
    "GIT_COMMANDS.md",
    "SUMMARY.md"
)

$missingDocs = 0
foreach ($file in $docFiles) {
    if (!(Test-Path $file)) {
        $missingDocs++
    }
}

if ($missingDocs -eq 0) {
    Write-Host "   ✅ Toda la documentación está presente" -ForegroundColor Green
} else {
    Write-Host "   ℹ️  Faltan $missingDocs archivos de documentación (opcional)" -ForegroundColor Cyan
}

# Resumen final
Write-Host "`n=== 📊 RESUMEN ===" -ForegroundColor Cyan
Write-Host ""

if ($errors -eq 0 -and $warnings -eq 0) {
    Write-Host "✅ ¡TODO PERFECTO! Tu proyecto está listo para desplegarse." -ForegroundColor Green
    Write-Host ""
    Write-Host "Próximos pasos:" -ForegroundColor Cyan
    Write-Host "1. git add ." -ForegroundColor White
    Write-Host "2. git commit -m 'Proyecto listo para Render'" -ForegroundColor White
    Write-Host "3. git push" -ForegroundColor White
    Write-Host "4. Desplegar en Render (ver DEPLOY.md)" -ForegroundColor White
} elseif ($errors -eq 0) {
    Write-Host "⚠️  Verificación completada con $warnings advertencias." -ForegroundColor Yellow
    Write-Host "   El proyecto debería funcionar, pero revisa las advertencias." -ForegroundColor Yellow
} else {
    Write-Host "❌ Verificación completada con $errors errores y $warnings advertencias." -ForegroundColor Red
    Write-Host "   Corrige los errores antes de desplegar." -ForegroundColor Red
}

Write-Host ""
Write-Host "Para más información, consulta:" -ForegroundColor Cyan
Write-Host "- QUICKSTART.md (probar localmente)" -ForegroundColor White
Write-Host "- DEPLOY.md (desplegar en Render)" -ForegroundColor White
Write-Host "- GIT_COMMANDS.md (comandos Git)" -ForegroundColor White
Write-Host ""
