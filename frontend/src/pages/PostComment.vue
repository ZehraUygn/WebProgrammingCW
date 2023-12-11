<template>
    <div>
      <!-- Your comment form goes here -->
      <form @submit.prevent="postComment">
        <div class="mb-3">
          <label for="comment" class="col-form-label">Comment:</label>
          <textarea v-model="commentText" class="form-control" id="comment" autocomplete="comment"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Post Comment</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        commentText: '',
      };
    },
    methods: {
      async postComment() {
        // Perform the logic to post the comment to the server
        try {
          const csrfToken = this.getCookie('csrftoken');
          const response = await fetch('http://localhost:8080/api/post_comment', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
              text: this.commentText,
              // Include any other necessary data, such as article ID, user ID, etc.
            }),
          });
  
          if (!response.ok) {
            console.error(`Error posting comment: ${response.status} - ${response.statusText}`);
            return;
          }
  
          // Clear the comment text after posting
          this.commentText = '';
  
          // Emit an event to inform the parent component (MainPage.vue) to update comments
          this.$emit('update-comments');
        } catch (error) {
          console.error('Error posting comment:', error);
        }
      },
      getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) {
            return parts.pop().split(';').shift();
        }
        return null;
        },
    },
  };
  </script>
  
  <style scoped>
  /* Your custom styles go here */
  </style>
  