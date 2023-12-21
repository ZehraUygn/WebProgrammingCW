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
                :to="{name: 'Profile Page'}"
            >
                Profile Page
            </router-link>
            |
            <a href="http://localhost:8000/logout/">Logout</a>
        </div>
        <RouterView class="flex-shrink-0" />
    </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { RouterView } from "vue-router";
import 'bootstrap/dist/css/bootstrap.css';

export default defineComponent({
    components: { RouterView },
});

</script>

<style scoped>
</style>
