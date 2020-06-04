<template>
  <div id="app" class="small-container">
    <img alt="Vue logo" src="./assets/logo.png" />
    <todo-table v-bind:todos="todos" />
  </div>
</template>

<script>
import TodoTable from "./components/TodoTable.vue";

export default {
  name: "App",
  components: {
    TodoTable
  },

  data() {
    return {
      todos: []
    };
  },

  mounted() {
    this.getTodos();
  },

  methods: {
    async getTodos() {
      try {
        const response = await fetch("http://localhost:8000/api/v1/todo/list");
        const data = await response.json();
        console.log(data);
        this.todos = data;
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.small-container {
  max-width: 680px;
}
</style>
