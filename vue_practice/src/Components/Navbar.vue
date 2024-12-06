<template>
  <div class="navbar">
    <div @click="$router.push('/')">Логотип(главная)</div>
    <div class="navbar__btns">
      <my-button @click="$router.push('/patients')">Пациенты</my-button>
      <my-button style="margin-left: 20px" @click="$router.push('/')">Выход из акка(-)</my-button>  <!--ДОЛЖЕН БЫТЬ ВЫХОД ИЗ ТЕКУЩЕГО АККАУНТА -->
      <my-button @click="$router.push('/')">Профиль(-)</my-button>   <!--У КАЖДОГО СВОЙ ПРОФИЛЬ -->
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.navbar {
  height: 50px;
  background-color: lightgrey;
  box-shadow: 2px 2px 4px grey;
  display: flex;
  align-items: center;
  padding: 0 15px;
  margin-bottom: 15px;
}
.navbar__btns {
  margin-left: auto;
}
</style>
