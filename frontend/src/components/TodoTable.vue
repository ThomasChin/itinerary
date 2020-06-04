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
        </tr>
      </thead>
      <tbody>
        <tr v-for="todo in todos" :key="todo.id">
          <td>{{todo.description}}</td>
          <td>{{todo.notes}}</td>
          <td>{{todo.deadline}}</td>
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
  }
};
</script>

<style scoped>
</style>