<template>
  <div class="container pt-3">
    <div v-for="article in response_data.Article" :key="article.id" class="mb-3 border p-3">
      <div>
        <b>Title:</b> {{ article.Title }}<br>
        <b>Article:</b> {{ article.Article }}<br>
      </div>
      <DeleteArticle :article="article" @delete-article="deleteArticle" />
      <UpdateArticle :article="article" @update-article="updateArticle" />
    </div>
    <PostArticle @update-response="updateResponseData" />
  </div>
</template>

<script>
import PostArticle from './PostArticle.vue';
import DeleteArticle from './DeleteArticle.vue';
import UpdateArticle from './UpdateArticle.vue';

export default {
  data() {
    return {
      response_data: { Article: [] },
    };
  },
  components: {
    PostArticle,
    DeleteArticle,
    UpdateArticle,
  },
  methods: {
    async deleteArticle(articleId) {
      try {
        const response = await fetch(`http://localhost:8080/api/delete/${articleId}/`, {
          method: 'DELETE',
        });

        if (!response.ok) {
          console.error(`Error deleting article: ${response.status} - ${response.statusText}`);
          return;
        }

        this.fetchData();
      } catch (error) {
        console.error('Error deleting article:', error);
      }
    },
    async updateArticle(updatedArticle) {
      try {
        const csrfToken = this.getCookie('csrftoken');
        const response = await fetch(`http://localhost:8080/api/update/${updatedArticle.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
          body: JSON.stringify(updatedArticle),
        });

        if (!response.ok) {
          console.error(`Error updating article: ${response.status} - ${response.statusText}`);
          return;
        }

        this.fetchData();
      } catch (error) {
        console.error('Error updating article:', error);
      }
    },
    async fetchData() {
      try {
        const response = await fetch('http://localhost:8080/api/get.json');
        this.response_data = await response.json();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    updateResponseData(data) {
      this.response_data = data;
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
  async mounted() {
    this.fetchData();
  },
};
</script>
