<template>
  <div>
    <form @submit="addTodo">
      <input type="text" v-model="description" name="title" placeholder="Add Todo..." />
      <input type="text" v-model="notes" name="title" placeholder="Notes..." />
      <input type="submit" value="Submit" class="btn" />
    </form>
  </div>
</template>

<script>
export default {
  name: "AddTodo",
  data() {
    return {
      description: "",
      notes: ""
    };
  },

  methods: {
    addTodo(e) {
      e.preventDefault();
      const newTodo = {
        id: this.id,
        description: this.description,
        notes: this.notes,
        done: false
      };

      // Send up to parent
      this.$emit("add-todo", newTodo);
      this.description = "";
      this.notes = "";
    }
  }
};
</script>

<style scoped>
form {
  display: flex;
}

input[type="text"] {
  flex: 10;
  padding: 5px;
}

input[type="submit"] {
  flex: 2;
}
</style>