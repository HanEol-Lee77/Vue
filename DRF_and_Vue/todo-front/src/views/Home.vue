<template>
  <div class="home">
    <h1>Todo w/ Django & Vue</h1>
    <input type="text">
    <button>버튼</button>
    <TodoInput @createTodoEvent="createTodo" />
    <TodoList :todos="todos" />
    로그인 구현
  </div>
</template>

<script>
// @ is an alias to /src // 골뱅이는 별명인데..
//from '@/components/helloworld.vue'
import TodoList from '@/components/TodoList.vue'
import TodoInput from '@/components/TodoInput.vue'
import router from '@/router'
import jwtDecode from 'jwt-decode' //
import axios from 'axios'

export default {
  name: 'home',
  data() {
    return {
      todos: [],
      // todos: [
      //   {id: 1, title: 'Django DRF로 로그인 API 구현'},
      //   {id: 2, title: 'JWT 활용한 세션 구현'},
      //   {id: 3, title: 'Todo 관련 API 구현'},
      //   {id: 4, title: 'Vuex 활용한 Flux 아키텍쳐 적용'},
      // ]
    }
  },
  components: {
    TodoList,
    TodoInput,
  },
  methods: {
    loggedIn() {
      this.$session.start()

      if(!this.$session.has('jwt')){
        router.push('/login')
      } // 이 키를 갖는 값이.. 무엇인지?
    },
    getTodos() {
      const token = this.$session.get('jwt')
      // axios -> api/v1/users/현재 접속한 유저의 id
// debugging! : 각각이 잘 들어갔는지 확인!
      // console.log('중간')
      // console.log(token)

      const user_id = jwtDecode(token).user_id
      // axios

      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      } // request header
      console.log(user_id)

      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, options)
      .then(res => {
        console.log(res)// 데이터가 잘 도착해있으면 첫번째 인자로 넘어온 걸 사용 가능
        console.log(res.data.todo_set)
        this.todos = res.data.todo_set
      })
    },
    createTodo(title) {
      console.log('title이다!!')

      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      console.log('options')
      console.log(options)

      const data = new FormData() // FormData javascript : 새로운 FormData 객체를 생성시켜줌.
      data.append('user', user_id)
      console.log(user_id)
      data.append('title', title)
      console.log(data)
      axios.post(`http://localhost:8000/api/v1/todos/`, data, options) // 만들어주는 URL에 보내주자!!
      .then(res => {
        console.log(res)
        console.log('이게 결과야!')
        this.todos.push(res.data) // 
      })
    }
  },
  // 8개의 life cycle hook
  mounted() { //##$$?? 무슨의미??
    // before updated, before created, before mounted, before destroyed
    this.loggedIn()
    this.getTodos()
  },
}
</script>