<template>
  <div class="todo-item">
    <button @click="$emit('del-todo', todo.id)" class="del">x</button>
    <p>
      <b v-bind:class="{'is-complete':todo.done}">TODO: &nbsp;</b>
      <b v-if="editing === todo.id">
        <input type="text" v-model="todo.description" />
      </b>
      <b v-else v-bind:class="{'is-complete':todo.done}">{{todo.description}}</b>
      <br />
      <b v-bind:class="{'is-complete':todo.done}">Notes: &nbsp;</b>
      <b v-if="editing === todo.id">
        <input type="text" v-model="todo.notes" />
      </b>
      <b v-else v-bind:class="{'is-complete':todo.done}">{{todo.notes}}</b>
      <br />
      <b
        v-if="todo.deadline != null"
        v-bind:class="{'is-complete':todo.done}"
      >Deadline: {{formatDeadline(todo)}}</b>
      <br />
    </p>
    <b v-if="editing === todo.id">
      <button @click="edit(todo)" class="button-save pure-button">Save</button>
      &Tab;
      <button class="button-cancel pure-button" @click="editing = null">Cancel</button>
    </b>
    <b v-else>
      <button @click="editMode(todo.id)" class="button-edit pure-button">EDIT</button>
      &Tab;
      <button @click="markComplete" class="button-success pure-button">DONE</button>
    </b>
  </div>
</template>


<script>
import moment from "moment";

export default {
  name: "TodoItem",
  props: ["todo"],
  data() {
    return {
      editing: null
    };
  },
  methods: {
    editMode(id) {
      this.editing = id;
    },

    edit(todo) {
      if (todo.description === "") return;
      this.$emit("edit-todo", todo);
      this.editing = null;
    },

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

.button-edit {
  background: #69f5ff;
}

.button-save {
  background: #69f5ff;
}

.button-cancel {
  background: #ff7063;
}
</style>