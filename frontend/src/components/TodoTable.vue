<template>
  <div id="todo-table">
    <h1>Todo List</h1>
    <p v-if="todos.length < 1" class="empty-table">No To-Do's</p>
    <table v-else>
      <thead>
        <tr>
          <th>Description</th>
          <th>Notes</th>
          <th>Deadline</th>
          <th>Completed</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="todo in todos" :key="todo.id">
          <div id="todo-elements">
            <td>{{todo.description}}</td>
          </div>
          <td>{{todo.notes}}</td>
          <td>{{todo.deadline}}</td>

          <button v-on:click="buttonClick">?</button>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "todo-table",
  props: {
    todos: Array
  },
  methods: {
    buttonClick: function() {
      console.log("Button Click yay!");
      document.getElementById("todo-elements").setAttribute("class", "style1");
    }
  }
};
</script>

<style scoped>
.style1 {
  text-decoration: line-through;
}
</style>