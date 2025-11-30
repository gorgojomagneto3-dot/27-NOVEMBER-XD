# English Learning App - Development Setup

## Project Structure

```
27 NOVEMBER XD/
├── backend/           # Python Flask API
│   ├── api.py         # Main API server
│   ├── content.py     # Lesson content manager
│   ├── database.py    # Database operations
│   └── *_content*.py  # Lesson content files
│
├── frontend/          # Astro Frontend
│   ├── src/
│   │   ├── pages/     # Routes
│   │   ├── layouts/   # Layout components
│   │   ├── components/# UI components
│   │   └── lib/       # Utilities
│   └── public/        # Static assets
│
└── (legacy files)     # Original Flask monolith
```

## Quick Start

### 1. Start Backend (Python API)

```powershell
cd backend
pip install -r requirements.txt
python api.py
```

API will run on: http://localhost:5000

### 2. Start Frontend (Astro)

```powershell
cd frontend
npm install
npm run dev
```

Frontend will run on: http://localhost:4321

## API Endpoints

### Lessons
- `GET /api/lessons` - Get all lessons
- `GET /api/lessons/:id` - Get lesson content
- `POST /api/lessons/:id/complete` - Mark lesson complete

### Stats
- `GET /api/stats` - Get user statistics
- `POST /api/stats/xp` - Add XP
- `POST /api/stats/exercise` - Record exercise

### Vocabulary
- `GET /api/vocabulary` - Get saved words
- `POST /api/vocabulary` - Save new word
- `POST /api/vocabulary/:word/review` - Update review

### Achievements
- `GET /api/achievements` - Get all achievements

## Development

### Backend (Flask)
- Port: 5000
- CORS enabled for localhost:4321
- SQLite for development
- PostgreSQL for production

### Frontend (Astro)
- Port: 4321
- TailwindCSS for styling
- TypeScript support
- Client-side rendering with API

## Environment Variables

### Backend
- `SECRET_KEY` - Flask secret key
- `DATABASE_URL` - PostgreSQL URL (optional)
- `PORT` - Server port (default: 5000)

### Frontend
- `API_URL` - Backend API URL (default: http://localhost:5000)

## Build for Production

### Backend
```bash
pip install gunicorn
gunicorn api:app
```

### Frontend
```bash
npm run build
npm run preview
```
