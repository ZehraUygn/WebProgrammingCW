import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import { createPinia } from 'pinia';
import { useUserStore } from './store/user';

const app = createApp(App);

app.use(createPinia());
const userStore = useUserStore();

// Fetch user data before mounting the app
(async () => {
    try {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');

        const response = await fetch('http://localhost:8000/api/getUser/', {
            method: 'GET',
            credentials: 'include',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        });
    
        if (!response.ok) {
            throw new Error('Failed to fetch user data');
        }
    
        const data = await response.json();

        console.log('Data from the server(ts):', data);
    
        if (data.isAuthenticated) {
            // Pass user data to the app instance if needed
            // app.config.globalProperties.userData = data;
            userStore.setUser(data); // set the user in the User store
            alert(`${data.email} is logged in`);
            app.mount('#app');
        } else {
            console.warn('Authentication status:', data.isAuthenticated);
            alert('NOT LOGGED IN');
        }
    } catch (error) {
      console.error('Error fetching user data:', error);
      alert('Error fetching user data. Check console for details.');
    }
  })();

app.use(router)