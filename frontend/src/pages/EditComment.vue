<template>
    <div>
      <button type="button" class="btn btn-info" @click="toggleEditForm">Edit</button>
  
      <div v-if="showEditForm">
        <h3>Edit Comment</h3>
        <form @submit.prevent="saveEdit">
          <div class="mb-3">
            <label for="editComment" class="col-form-label">Edit Comment:</label>
            <input v-model="editForm.Comment" id="editComment" class="form-control" required>
          </div>
  
          <div class="mb-3">
            <button type="button" class="btn btn-secondary" @click="cancelEdit">Cancel</button>
            <button type="submit" class="btn btn-primary">Save</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      comment: Object, // Pass the comment object as a prop
    },
    data() {
      return {
        showEditForm: false,
        editForm: { ...this.comment },
      };
    },
    methods: {
      toggleEditForm() {
        this.showEditForm = !this.showEditForm;
      },
      cancelEdit() {
        this.showEditForm = false;
      },
      saveEdit() {
        // Emit an event to inform the parent component (MainPage.vue) to save the edited comment
        this.$emit('edit-comment', this.editForm);
        this.showEditForm = false;
      },
    },
  };
  </script>
  