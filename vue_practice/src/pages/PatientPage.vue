<template>
    <div class="nav">
      <div class="nav-in">
        <div class="logo">Логотип</div>
        <div class="right-group">
          <div class="name">Имя, фамилия</div>
          <div class="menu-dropdown">MENU</div>
        </div>
      </div>
    </div>
    <div >
      <div class="chekup">
        <h3 v-if="posts.length > 0">Список пациентов</h3>
        <h2 v-else style="color: red">Отсутствуют пациенты</h2>
        <div class="btn">
          <my-button @click="showDialog"> Новый осмотр </my-button>
        </div>
      </div>
      <post-list :posts="posts" @remove="removePost" v-if="!isPostsLoading" />
  
      <div v-else>Идет загрузка...</div>
  
      <!-- <div class="app__btns">
        <my-select v-model="selectedSort" />
      </div> -->
  
      <my-dialog v-model:show="dialogVisible">
        <post-form @create="createPost" />
      </my-dialog>
    </div>
  
    <!-- <div>
      <my-select v-model="selectedOption" :options="options" />
    </div> -->
    <div class="page__wrapper">
      <div
        class="page"
        v-for="pageNumber in totalPages"
        :key="pageNumber"
        :class="{ 'current-page': page === pageNumber }"
        @click="changePage(pageNumber)"
      >
        {{ pageNumber }}
      </div>
    </div>
  </template>
  
  <script>
  import PostForm from "@/Components/PostForm";
  import PostList from "@/Components/PostList";
  import axios from "axios";
  import MySelect from "@/Components/UI/MySelect";
  import MyButton from "@/Components/UI/MyButton.vue";
  
  export default {
    components: {
      PostForm,
      PostList,
      MySelect,
    },
    data() {
      return {
        posts: [],
        dialogVisible: false,
        isPostsLoading: false,
        selectedSort: "",
        page: 1,
        limit: 3,
        totalPages: 0,
        // options: [], // Данные для выпадающего списка
        // selectedOption: "", // Выбранное значение
      };
    },
    methods: {
      createPost(post) {
        this.posts.push(post);
        this.dialogVisible = false;
      },
      removePost(post) {
        this.posts = this.posts.filter((p) => p.id !== post.id);
      },
      showDialog() {
        this.dialogVisible = true;
      },
      changePage(pageNumber) {
        this.page = pageNumber;
        this.fetchPosts();
      },
      async fetchPosts() {
        try {
          this.isPostsLoading = true;
          const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
              params: {
                _page: this.page,
                _limit: this.limit,
              },
            }
          );
          this.totalPages = Math.ceil(
            response.headers["x-total-count"] / this.limit
          );
          this.posts = response.data;
        } catch (e) {
          alert("Ошибка при получении пациентов");
        } finally {
          this.isPostsLoading = false;
        }
      },
      // async fetchOptions() {
      //   try {
      //     const response = await axios.get(
      //       "https://jsonplaceholder.typicode.com/posts?_limit=10"
      //     );
      //     console.log("Полученные данные:", response.data);
      //     this.options = response.data.map((item) => ({ name: item.id })); // Убедитесь, что name не пустое
      //   } catch (error) {
      //     console.error("Ошибка при загрузке данных:", error);
      //   }
      // },
      // async updateSelection(newValue) {
      //   this.selectedOption = newValue;
      //   try {
      //     await axios.post("/api/save-selection", { value: newValue }); // Сохранение значения
      //     console.log("Выбранное значение сохранено");
      //   } catch (error) {
      //     console.error("Ошибка при сохранении:", error);
      //   }
      // },
    },
    mounted() {
      this.fetchPosts();
      // this.fetchOptions();
    },
  };
  </script>
  
  <style>
  
  
  .chekup {
    display: flex;
    justify-content: space-between;
    margin: 0px 15px;
  }
  
  .app__btns {
    margin: 15px 0px;
    display: flex;
    justify-content: space-between;
  }
  
  .nav {
    width: 100%;
    height: 50px;
    background-color: teal;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
  }
  
  .nav-in {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    width: 100%;
  }
  
  .right-group {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .page__wrapper {
    display: flex;
    margin-top: 15px;
  }
  
  .page {
    border: 1px solid black;
    padding: 10px;
  }
  
  .current-page {
    border: 2px solid teal;
  }
  </style>
  