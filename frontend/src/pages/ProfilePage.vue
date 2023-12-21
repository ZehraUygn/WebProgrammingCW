<template>
    <div class="h3">
      {{ title }}
    </div>

    <div>
        <li class="list-group-item border border-2 mb-3">
        <p class="display-5 border rounded border-4"><strong>{{ username }}</strong></p>

        <p class="h5">{{ profile.email }}</p>
        <p class="h5"><img :src="'http://localhost:8000' + profile.profile_picture" /></p>

        <p v-if="profile.date_of_birth != null" class="h5">Date of birth: {{ profile.date_of_birth }}</p>
    </li>
    </div>
</template>
  
<script lang="ts">
import { defineComponent } from "vue";

type Profile = {
    id: number,
    email: string;
    date_of_birth: Date;
    profile_picture: string;
}

export default defineComponent({
    mounted() {
        this.get_user_data()
    },

    data() {
        return {
            title: "Profile Page",
            profile: {} as Profile,
            username: '',
        }
    },

    methods: {
        async get_user_data() {
            let response = await fetch("http://localhost:8000/api/profile", {
                method: 'GET',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            if (response.ok) {
                let data = await response.json()
                if (data.logged_in == false) {
                    window.location.href = "http://localhost:8000/login/"
                }
                this.username = data.username
                this.profile = data.profile
                console.log(this.profile)
            }
            else {
                alert("Failed to fetch data")
            }
        } 
    }
})
</script>
  
<style scoped>
</style>
  