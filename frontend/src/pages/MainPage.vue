<template>
  <div>
    <div class="container">
      <div class="h1">
        {{ title }}
      </div>

      <div>
        <div v-for="article in articles" :key="article.id" class="card mb-3">
          <div class="card-body">
            <h2 class="card-title">{{ article.title }}</h2>
            <p class="card-text">
              <span class="category-text">Category: {{ article.category.name }}</span>
            </p>
            <p class="card-text">{{ article.content }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

type Article = {
  id: number,
  title: string,
  content: string,
  category: string,
}

type Category = {
  id: number,
  name: string,
}

export default defineComponent({
  mounted() {
    this.get_articles();
  },
  data() {
    return {
      title: "Main Page",
      articles: [] as Article[],
      categories: [] as Category[],
    };
  },

  methods: {
    async get_articles() {
      let response = await fetch("http://localhost:8000/api/articles", {
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
        this.articles = data.articles
      }
      else {
        alert("Failed to fetch articles")
      }
    },
  },
});
</script>

<style scoped>
.category-text {
  font-weight: bold;
  color: #007bff; 
}
</style>
