/**
 * API Client for the English Learning App
 */

// Use the deployed backend API or localhost for development
const API_URL = import.meta.env.PUBLIC_API_URL || (typeof window !== 'undefined' && window.location.hostname !== 'localhost' ? 'https://27-november-xd.vercel.app' : 'http://localhost:5000');

// Get or create user ID
function getUserId(): string {
  let userId = localStorage.getItem('userId');
  if (!userId) {
    userId = crypto.randomUUID();
    localStorage.setItem('userId', userId);
  }
  return userId;
}

async function fetchAPI<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const userId = getUserId();
  
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'X-User-ID': userId,
      ...options.headers,
    },
  });
  
  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }
  
  return response.json();
}

// Lessons API
export async function getLessons() {
  return fetchAPI<{ success: boolean; lessons: Lesson[] }>('/api/lessons');
}

export async function getLesson(lessonId: string) {
  return fetchAPI<{ success: boolean; lesson: LessonDetail }>(`/api/lessons/${lessonId}`);
}

export async function completeLesson(lessonId: string) {
  return fetchAPI<{ success: boolean; xpEarned: number }>(`/api/lessons/${lessonId}/complete`, {
    method: 'POST',
  });
}

// Stats API
export async function getStats() {
  return fetchAPI<{ success: boolean; stats: UserStats; achievements: Achievement[] }>('/api/stats');
}

export async function addXp(amount: number) {
  return fetchAPI<{ success: boolean; totalXp: number; level: number }>('/api/stats/xp', {
    method: 'POST',
    body: JSON.stringify({ amount }),
  });
}

export async function recordExercise(correct: boolean) {
  return fetchAPI('/api/stats/exercise', {
    method: 'POST',
    body: JSON.stringify({ correct }),
  });
}

// Vocabulary API
export async function getVocabulary() {
  return fetchAPI<{ success: boolean; vocabulary: VocabWord[] }>('/api/vocabulary');
}

export async function saveVocabulary(word: string, translation: string) {
  return fetchAPI('/api/vocabulary', {
    method: 'POST',
    body: JSON.stringify({ word, translation }),
  });
}

// Types
export interface Lesson {
  id: string;
  level: string;
  title: string;
  completed: boolean;
  lastAccessed?: string;
}

export interface LessonDetail extends Lesson {
  content: string;
}

export interface UserStats {
  totalXp: number;
  currentStreak: number;
  longestStreak: number;
  wordsLearned: number;
  exercisesCompleted: number;
  level: number;
  xpForNextLevel: number;
}

export interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  unlocked: boolean;
}

export interface VocabWord {
  word: string;
  translation: string;
  proficiency: number;
  timesCorrect: number;
  timesWrong: number;
}
