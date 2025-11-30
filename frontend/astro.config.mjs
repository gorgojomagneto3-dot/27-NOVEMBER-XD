import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  server: {
    port: 4321
  },
  vite: {
    define: {
      'import.meta.env.API_URL': JSON.stringify(process.env.API_URL || 'http://localhost:5000')
    }
  }
});
