<template>
    <div style="display: none;" class="border rounded bg-secondary shadow p-4 mb-4" :id="'commentForm' + article_id">
        <p class="h1 mb-4">Make a comment</p>
        <form :id="'newMessageForm' + article_id" @submit.prevent method="POST">
            <div class="form-group">
                <input class="form-control" type="text" name="text" id="text" placeholder="Enter comment" /><br>
                <input style="display:none" class="form-control" name="articleId" id="articleId" :placeholder=article_id
                    :value=article_id /><br>

                <div class="row justify-content-center">
                    <button v-on:click="send_comment()" class="btn btn-light justify-content-center"
                        type="button">Post</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';

type Comment = {
    id: number;
    user: string;
    text: string;
    article: number;
}


export default defineComponent({
    props: ["article_id"],


    data() {

        return {
            comments: [] as Comment[],
        };
    },

    methods: {

        async send_comment() {
            let commentForm = document.getElementById('newCommentForm' + this.article_id) as HTMLFormElement;
            let formData: FormData = new FormData(commentForm)
            let response = await fetch("http://localhost:8000/api/comments", {
                method: "POST",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",

                body: formData
            });
            let data = await response.json();
            this.$emit('changeComments', data.comments)
        },
    }
})
</script>