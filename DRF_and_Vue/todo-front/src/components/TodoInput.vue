<template>
  <div class="todo-input">
    <h2>Todo Input</h2>
    <form class="input-group mb-3" @submit.prevent="createTodo()"> <!-- 원래 하던 행위를 멈춘다. ' ' 메소드만 실행하게 된다. -->
      <input v-model="title" type="text" class="form-control">
      <button  type="submit" class="btn btn-primary">+</button>
    </form>      
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: '',
      // todos: {
        
      // }

    }
  },
  methods: {
    createTodo() {
      this.$emit('createTodoEvent', this.title)
      console.log('입력전송')

      console.log(this.title)
      this.title=''

    }
  }
}
</script>

<style>

</style>