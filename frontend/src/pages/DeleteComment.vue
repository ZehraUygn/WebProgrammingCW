<template>
    <div>
      <button @click="deleteComment" type="button" class="btn btn-danger">Delete Comment</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      comment: {
        type: Object,
        required: true,
      },
    },
    methods: {
      deleteComment() {
        // Emit an event to inform the parent component (MainPage.vue) to delete the comment
        this.$emit('delete-comment', this.comment.id);
      },
    },
  };
  </script>
  