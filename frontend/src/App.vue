<template>
  <div id="app" class="small-container">
    <img alt="Vue logo" src="rocketship.jpg" />
    <Header />
    <AddTodo v-on:add-todo="addTodo" />
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo" />
    <!-- 
    <todo-table v-bind:todos="todos" />
    -->
  </div>
</template>

<script>
import Header from "./components/layout/Header.vue";
import Todos from "./components/Todos.vue";
import AddTodo from "./components/AddTodo.vue";
// import TodoTable from "./components/TodoTable.vue";

export default {
  name: "App",
  components: {
    Todos,
    Header,
    AddTodo
    // TodoTable
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
    },

    addTodo(newTodo) {
      this.todos = [...this.todos, newTodo];
    },

    async deleteTodo(id) {
      try {
        console.log(
          await fetch(`http://localhost:8000/api/v1/todo/${id}`, {
            method: "delete"
          })
        );
        this.todos = this.todos.filter(todo => todo.id !== id);
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
  margin: auto;
  width: 50%;
}
.small-container {
  max-width: 680px;
}

.btn {
  display: inline-block;
  border: none;
  background: #555;
  color: #fff;
  padding: 7px 20px;
  cursor: pointer;
}
</style>
