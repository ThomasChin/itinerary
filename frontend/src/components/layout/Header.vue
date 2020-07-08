<template>
  <header class="header">
    <h1>Mission Control Center</h1>
    <b>Timers:</b>
    <br />
    <input type="submit" value="Pomodoro" class="btn" />
    &Tab;
    <input type="submit" value="CodeBuddy" class="btn" />
    <br />
    <br />
  </header>
</template>

<script>
export default {
  name: "Header"
};
</script>

<style scoped>
.header {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
}

.header a {
  color: #fff;
  padding-right: 5px;
}
</style>