<template>
    <div class="h3">
      {{ title }}
    </div>

    <div>
        <li class="list-group-item border border-2 mb-3">
            <p><img :src="'http://localhost:8000' + profile.profile_picture" /></p>
            <p class="display-5 border rounded border-4"><strong>{{ username }}</strong></p>
            <p>Email: {{ profile.email }}</p>
            <p v-if="profile.date_of_birth != null">Date of birth: {{ profile.date_of_birth }}</p>
        </li>
    </div>

    <button @click="button_edit_profile">Edit Profile</button>

    <div style="display: block; background-color: #f0f0f0; padding: 20px; margin-bottom: 20px; border: 2px solid #333; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);" id="editProfileForm">
        <p class="h1 mb-4" style="color: black;">Edit your profile</p>
        <form id="updateProfileForm" @submit.prevent method="POST">
            <div class="form-group">
                <label for="username" style="font-weight: bold;">Username</label><br><br>
                <input class="form-control" type="text" name="username" id="username" placeholder="Change username" :value=username /><br>

                <label for="email" style="font-weight: bold;">Email</label><br><br>
                <input class="form-control" type="email" name="email" id="email" placeholder="Change email" :value=profile.email /><br>

                <label for="date" style="font-weight: bold;">Date of birth</label><br><br>
                <input class="form-control" type="date" name="date_of_birth" id="date_of_birth" :value=profile.date_of_birth /><br><br>

                <label for="profile_picture" style="font-weight: bold;">Profile picture</label><br><br>
                <input class="form-control-image" type="file" name="profile_picture" id="profile_picture"/><br>

                <div class="row justify-content-center">
                    <button type="submit" @click="edit_profile()" class="btn btn-primary btn-lg d-flex justify-content-center mt-3" style="background-color: #28a745; color: #fff;">Edit</button>
                </div>
            </div>
        </form>
    </div>
</template>
  
<script lang="ts">
import { defineComponent } from "vue";

type Profile = {
    id: number,
    email: string,
    date_of_birth: Date,
    profile_picture: string,
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
            let response = await fetch("http://localhost:8000/api/profile/", {
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
            }
            else {
                alert("Failed to fetch data")
            }
        },
        button_edit_profile() {
            let form1 = document.getElementById('editProfileForm') as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }
        },
        async edit_profile() {
            let updateProfile = document.getElementById('updateProfileForm') as HTMLFormElement;
            let formData: FormData = new FormData(updateProfile)
            var input = document.getElementById('profile_picture') as HTMLFormElement
            var username = document.getElementById('username') as HTMLFormElement
            var email = document.getElementById('email') as HTMLFormElement
            var birthdate = document.getElementById('date_of_birth') as HTMLFormElement

            formData.append('profile_picture', input.files[0])
            formData.append('username', username.value)
            formData.append('email', email.value)
            formData.append('dob', birthdate.value)

            let response = await fetch("http://localhost:8000/api/profile/" + this.profile.id, {
                method: "PUT",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",

                body: formData
            });
            if (response.ok) {
                let data = await response.json();
                this.username = data.username;
                this.profile = data.profile;
                this.button_edit_profile();
            }
            else {
                alert("Failed to edit profile")
            }
        },
    }
})
</script>
  
<style scoped>
</style>
  