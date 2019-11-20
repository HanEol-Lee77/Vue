<template>
  <div class="todo-list">
    <h2>Todo-목록 (Todo-list 만들기)</h2>
    <ul class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body">
        <span>{{ todo.title }}</span>
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
    }
  },
}
</script>

<style>

</style>