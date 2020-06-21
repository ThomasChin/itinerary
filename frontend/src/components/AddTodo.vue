<template>
  <div>
    <form @submit="addTodo">
      <input type="text" v-model="description" name="title" placeholder="Add Todo..." />
      <input type="submit" value="Submit" class="btn" />
    </form>
  </div>
</template>

<script>
export default {
  name: "AddTodo",
  data() {
    return {
      description: ""
    };
  },

  methods: {
    async addTodo(e) {
      e.preventDefault();

      try {
        const response = await fetch("http://localhost:8000/api/v1/todo/list", {
          method: "post",
          headers: {
            "Content-type": "application/json"
          },
          body: JSON.stringify({
            description: this.description,
            notes: "",
            deadline: null,
            complete: false
          })
        });
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.log(error);
      }

      const newTodo = {
        id: this.id,
        description: this.description,
        complete: false
      };

      // Send up to parent
      this.$emit("add-todo", newTodo);
      this.description = "";
    },

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