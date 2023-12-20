import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useAuthStore } from './store/auth'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)


const initializeApp = async () => {
    const authStore = useAuthStore();
  
    try {
      // Check authentication status when the app is created
      await authStore.authenticate();
  
      // Now, authStore.isAuthenticated and authStore.user are updated
    } catch (error) {
      console.error('Error initializing app:', error);
    }
  };
  
  // Call the initialization function
  initializeApp();
  
  // Set up your router to handle authentication and redirection
  router.beforeEach((to, from, next) => {
    const isAuthenticated = useAuthStore().isAuthenticated;
  
    if (to.meta.requiresAuth && !isAuthenticated) {
      next('http://localhost:8000/login');
    } else {
      next();
    }
  });

app.mount('#app')
