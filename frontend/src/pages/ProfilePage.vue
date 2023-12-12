<template>
    <div class="h1">
      {{ title }}
    </div>
    <div v-if="user" class="cards-container">
            <div class="title-text">
                Email: {{ user.email }}
            </div>
            <div class="title-text">
                Birthdate: {{ user.birthdate }}
            </div>
            <div class="title-text">
                <!-- Use user.image if available, otherwise show a default image -->
                <img v-if="user.image" :src="user.image" alt="User Image" />
            </div>
    </div>
</template>
  
<script lang="ts">
import { defineComponent } from "vue";
import { useUserStore } from "../store/User";
  
    export default defineComponent({
        data() {
            return {
                title: "Profile Page",
            }
        },
        computed: {
            user() {
                return useUserStore().user;
            }
        }
    })
</script>
  
<style scoped>
</style>
  