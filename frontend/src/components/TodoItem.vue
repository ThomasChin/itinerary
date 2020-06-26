<template>
  <div class="todo-item" v-bind:class="{'is-complete':todo.done}">
    <button @click="$emit('del-todo', todo.id)" class="del">x</button>
    <p>
      <b>Todo:</b>
      {{todo.description}}
      <br />
      <b>Notes:</b>
      {{todo.notes}}
      <br />
      <b>Deadline:</b>
      {{todo.deadline}}
      <br />
    </p>
    <button @click="markComplete" class="btn btn-success">DONE</button>
  </div>
</template>


<script>
export default {
  name: "TodoItem",
  props: ["todo"],
  methods: {
    async markComplete() {
      try {
        const done = this.todo.done;

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
              done: !done
            })
          }
        );
        const data = await response.json();
        console.log(data);
        this.todo.done = !this.todo.done;
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