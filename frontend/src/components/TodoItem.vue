<template>
  <div class="todo-item" v-bind:class="{'is-complete':todo.complete}">
    <p>
      <input type="checkbox" v-on:change="markComplete" />
      {{todo.description}}
      <button @click="$emit('del-todo', todo.id)" class="del">x</button>
    </p>
  </div>
</template>


<script>
export default {
  name: "TodoItem",
  props: ["todo"],
  methods: {
    async markComplete() {
      try {
        const completed = this.todo.complete;

        const response = await fetch(
          `http://localhost:8000/api/v1/todo/${this.todo.id}`,
          {
            method: "put",
            headers: {
              "Content-type": "application/json"
            },
            body: JSON.stringify({
              description: this.todo.description,
              notes: this.todo.notes,
              deadline: this.todo.deadline,
              complete: !completed
            })
          }
        );
        const data = await response.json();
        console.log(data);
        this.todo.complete = !this.todo.complete;
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>

<style scoped>
.todo-item {
  background: #f4f4f4;
  padding: 10px;
  border-bottom: 1px #ccc dotted;
}

.is-complete {
  text-decoration: line-through;
}

.del {
  background: #ff0000;
  color: #fff;
  border: none;
  padding: 5px 9px;
  border-radius: 50%;
  cursor: pointer;
  float: right;
}
</style>