<template>
  <div class="login">
  <!-- single file component.  comp가 어디에 위치할지.. 소속될 컴포넌트 : 한테 등록해주는 방향으로..! -->
  <!-- 문지기에게 url 넘겨주기 : router 안에 index.js -->
    <h1>로그인 페이지</h1>
    <LoginForm />
    <!-- <v-btn >haha</v-btn> -->

    <button>login</button>
    <!-- "btn btn-primary" -->
  </div>
  
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
export default {
  name: 'Login',
  components: {
    LoginForm,
  },
}
</script>

<style>

</style>