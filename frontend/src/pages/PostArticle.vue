<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Add Article
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">New Article</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="title" class="col-form-label">Title:</label>
                <input v-model="form.title" type="text" class="form-control" id="title" autocomplete="title">
              </div>
              <div class="mb-3">
                <label for="content" class="col-form-label">Content:</label>
                <textarea v-model="form.content" class="form-control" id="content" autocomplete="content"></textarea>
              </div>
              <div class="mb-3">
                <!-- Add category selection logic here -->
                <label for="category" class="col-form-label">Category:</label>
                <select v-model="form.category" class="form-select" id="category">
                  <!-- Populate categories based on user preferences or from the backend -->
                  <option value="sport">Sport</option>
                  <option value="world">World</option>
                  <!-- Add more options as needed -->
                </select>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" @click="postArticle" class="btn btn-primary">Add Article</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        title: '',
        content: '',
        category: null,
      },
      response_data: '',
    };
  },
  methods: {
    async postArticle() {
      const csrftoken = getCookie('csrftoken');

      const response = await fetch('http://localhost:8080/api/post_mymodel', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(this.form),
      });

      this.response_data = await response.json();
      this.$emit('update-response', this.response_data); // Emit event to update the response in MainPage.vue
      this.resetForm(); // Reset the form after posting an article
    },
    resetForm() {
      // Reset form fields
      this.form.title = '';
      this.form.content = '';
      this.form.category = null;
    },
  },
};

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {
    return parts.pop().split(';').shift();
  }
  return null;
}
</script>

<style scoped>
/* Add your custom styles here */
</style>
