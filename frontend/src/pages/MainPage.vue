<template>
  <div class="container pt-3">
    <!-- Display Articles -->
    <div v-for="article in response_data.articles" :key="article.id" class="mb-3 border p-3">
      <div>
        <b>Title:</b> {{ article.title }}<br>
        <b>Content:</b> {{ article.content }}<br>
      </div>
      <DeleteArticle :article="article" @delete-article="deleteArticle" />
      <UpdateArticle :article="article" @update-article="updateArticle" />
    </div>

    <!-- Display Comments -->
    <div v-for="comment in response_data.comments" :key="comment.id" class="mb-3 border p-3">
      <div>
        <b>Comment:</b> {{ comment.text }}<br>
      </div>
      <DeleteComment :comment="comment" @delete-comment="deleteComment" />
      <EditComment :comment="comment" @edit-comment="editComment" />
    </div>

    <!-- Post Article Form -->
    <PostArticle @updateResponse="updateResponseData" />

    <!-- Post Comment Form -->
    <PostComment @update-comments="fetchData" />
  </div>
</template>

<script>
import Vue from 'vue';
import PostArticle from './PostArticle.vue';
import DeleteArticle from './DeleteArticle.vue';
import UpdateArticle from './UpdateArticle.vue';
import PostComment from './PostComment.vue';
import DeleteComment from './DeleteComment.vue';
import EditComment from './EditComment.vue';

export default {
  data() {
    return {
      response_data: { articles: [], comments: [] },
    };
  },
  components: {
    PostArticle,
    DeleteArticle,
    UpdateArticle,
    PostComment,
    DeleteComment,
    EditComment,
  },
  methods: {
    async fetchData() {
      try {
        const articlesResponse = await fetch('http://localhost:8080/api/get_articles');
        const commentsResponse = await fetch('http://localhost:8080/api/get_comments');

        const articlesData = await articlesResponse.json();
        const commentsData = await commentsResponse.json();

        this.response_data = { articles: articlesData, comments: commentsData };
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    updateArticle(updatedArticle) {
      console.log('Update Article:', updatedArticle);
      this.fetchData();
    },
    deleteArticle(articleId) {
      console.log('Delete Article:', articleId);
      this.fetchData();
    },
    editComment(editedComment) {
      console.log('Edit Comment:', editedComment);
      this.fetchData();
    },
    deleteComment(commentId) {
      console.log('Delete Comment:', commentId);
      this.fetchData();
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>
