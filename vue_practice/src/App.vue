<template>
  <navbar></navbar>
  <!--ПЕРЕДЕЛАТЬ: НАВБАР ДОЛЖЕН БЫТЬ РАЗНЫЙ ДЛЯ РАЗНЫХ ПОЛЬЗОВАТЕЛЕЙ -->
  <div class="app">
    <router-view></router-view>
  </div>
</template>
<script>
import Navbar from "@/Components/Navbar.vue";
export default {
  components: {
    Navbar,
  },
  watch: {
    page() {
      this.fetchPosts();
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
