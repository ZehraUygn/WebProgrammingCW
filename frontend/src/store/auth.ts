import { defineStore } from 'pinia'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    user: null,
  }),
  actions: {
    async authenticate() {
      try {
        axios.defaults.withCredentials = true;

        // Make an API request to your Django backend
        const response = await axios.get('http://localhost:8000/api/user');

        // Assuming the response contains user data
        const userData = response.data;

        // Update the store's user property
        this.user = userData;

        // Set isAuthenticated to true since the user is authenticated
        this.isAuthenticated = true;
      } catch (error) {
        // Handle errors, e.g., set isAuthenticated to false
        console.error('Error fetching user data:', error);
        this.isAuthenticated = false;
      }
    },
  },
});
