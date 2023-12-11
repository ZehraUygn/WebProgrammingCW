<template>
  <div>
    <button @click="deleteArticle">Delete Article {{ article.id }}</button>
  </div>
</template>

<script>
export default {
  props: {
    article: {
      type: Object,
      required: true,
    },
  },
  methods: {
    deleteArticle() {
      this.$emit('delete-article', this.article.id);
    },
  },
};
</script>
