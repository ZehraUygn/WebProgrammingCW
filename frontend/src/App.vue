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
                :to="{name: 'Other Page'}"
            >
                Other Page
            </router-link>
        </div>
        <RouterView class="flex-shrink-0" />
    </main>
    <div v-if="userData">
        {{ userData }}
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView } from "vue-router";

export default defineComponent({
    components: { RouterView },
    data() {
        return {
            userData: null,
        }
    },
    async mounted() {
    try {
        const response = await fetch('http://localhost:8000/api/getUser/', {
            method: 'GET',
            credentials: 'include',
        });

        if (!response.ok) {
            throw new Error('Failed to fetch user data');
        }

        const data = await response.json();

        console.log('Data from the server:', data);

        if (data.isAuthenticated) {
            this.userData = data;
            alert(`${data.email} is logged in`);
        } else {
            console.warn('Authentication status:', data.isAuthenticated);
            alert('NOT LOGGED IN');
        }

    } catch (error) {
        console.error('Error fetching user data:', error);
        alert('Error fetching user data. Check console for details.');
    }
}
});

</script>

<style scoped>
</style>
