<template>
    <div>
      <h1>Articles</h1>
      <div v-for="article in articles" :key="article.id" class="article">
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        articles: [
          { id: 1, title: 'Article 1', content: 'Content of article 1...' },
          { id: 2, title: 'Article 2', content: 'Content of article 2...' },
        ],
      };
    },
  };
  </script>
  
  <style>
  .article {
    margin-bottom: 20px;
    border: 1px solid #ccc;
    padding: 10px;
  }
  </style>
  