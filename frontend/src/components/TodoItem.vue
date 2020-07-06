<template>
  <div class="todo-item" v-bind:class="{'is-complete':todo.done}">
    <button @click="$emit('del-todo', todo.id)" class="del">x</button>
    <p>
      <b>Todo: {{todo.description}}</b>
      <br />
      <b>Notes: {{todo.notes}}</b>
      <br />
      <b v-if="todo.deadline != null">Deadline: {{formatDeadline(todo)}}</b>
      <br />
    </p>
    <button @click="markComplete" class="button-success pure-button">DONE</button>
  </div>
</template>


<script>
import moment from "moment";

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
    },

    formatDeadline(todo) {
      if (todo.deadline != null) {
        var formatted = moment(todo.deadline);
        return formatted;
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
  background: #ff6166;
  color: #fff;
  border: none;
  padding: 5px 9px;
  border-radius: 50%;
  cursor: pointer;
  float: right;
}

.button-success {
  background: #8cff8a;
}
</style>