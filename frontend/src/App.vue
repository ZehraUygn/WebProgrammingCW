<template>
    <main class="container pt-4">
        <div>
            <router-link
                class=""
                :to="{name: 'Main Page'}"
            >
                Main Page
            </router-link>
            |
            <router-link
                class=""
                :to="{name: 'Health'}"
            >
                Health
            </router-link>
            |
            <router-link
                class=""
                :to="{name: 'Profile Page'}"
            >
                Profile Page
            </router-link>
        </div>
        <RouterView class="flex-shrink-0" />
    </main>
    <!-- <div v-if="user">
        Welcome, {{ user.email }}
    </div> -->
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView } from "vue-router";
import { useUserStore } from "./store/User";

export default defineComponent({
    components: { RouterView },
    computed: {
        user() {
            return useUserStore().user;
        }
    }
    // data() {
    //     return {
    //         userData: null,
    //         isAuthenticated: false,
    //     }
    // },
    // async mounted() {
    // try {
    //     const response = await fetch('http://localhost:8000/api/getUser/', {
    //         method: 'GET',
    //         credentials: 'include',
    //     });

    //     if (!response.ok) {
    //         throw new Error('Failed to fetch user data');
    //     }

    //     const data = await response.json();

    //     console.log('Data from the server(App):', data);

    //     if (data.isAuthenticated) {
    //         this.userData = data;
    //         this.isAuthenticated = true;
    //         alert(`${data.email} is logged in`);
    //     } else {
    //         this.isAuthenticated = false;
    //         console.warn('Authentication status:', data.isAuthenticated);
    //         alert('NOT LOGGED IN');
    //     }

    // } catch (error) {
    //     console.error('Error fetching user data:', error);
    //     alert('Error fetching user data. Check console for details.');
    // }
    // }
});

</script>

<style scoped>
</style>
