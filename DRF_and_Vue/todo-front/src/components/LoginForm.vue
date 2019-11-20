<template>
  <div>
    <!-- 데이터를 보내는 역할. : 쓸 일이 없다. -->
    <div class="form-group">
      <label for="id">아이디</label>
      <input v-model="credentials.username" type="text" id="id" class="form-control" placeholder="아이디를 입력해주세요.">
    </div>
    <div class="form-group">
      <label for="password">비밀번호</label>
      <input v-model="credentials.password" type="text" id="password" class="form-control" placeholder="비밀번호를 입력해주세요.">
    </div>
  <button @click="login()" class="btn btn-primary">로그인</button>

    <!-- <form action="">
    </form> -->

  </div>
</template>

<script>
import axios from 'axios'

import router from '@/router' // src로부터 시작된다고 하니까 /넣어줘야 한다. // '../router' // export router 해놓았어서 여기까지만 써도 된다.
// import router from '../router/index.js'

export default {
  name: 'LoginForm',
  data() {
    return{
      //로그인 정보의 키밸류 패어
      credentials: {
        // username: '',
        // password: '',
        // // form data를 장고 폼에 맞게 보내야 한다.
      },
    }
  },
  methods: {
    login() {
      console.log(this.credentials)
      axios.post('http://localhost:8000/api-token-auth/', this.credentials)
      .then(res => {
        console.log(res.data.token)
        this.$session.start()
        this.$session.set('jwt', res.data.token) // key, value pair의 storage
        // 로그인 끝나고 리다이렉트..
        // 홈 컴포넌트 라우팅 슬래쉬
        router.push('/')
      })
    }
  }
}
</script>

<style>

</style>