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
        Welcome, 
    </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView } from "vue-router";

export default defineComponent({
    components: { RouterView },
    async mounted() {
        const response = await fetch('localhost:8000/api/getUser/', {
            // credentials: 'include'
        })
        const data = await response.json()
        if (data.user) {
            alert("${data.email} is logged in")
        }
        else {
            alert("NOT LOGGED IN")
        }
    }
});

</script>

<style scoped>
</style>
