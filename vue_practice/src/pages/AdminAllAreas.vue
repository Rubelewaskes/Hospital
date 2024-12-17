<template>
    <div>
      <div class="chekup">
        <h1 v-if="areas.length > 0">Список участков</h1>
        <h2 v-else style="color: red">Отсутствуют участки</h2>
        <div class="btn">
            <my-button @click="showDialog"> Добавить участок </my-button>
          </div>
      </div>
      <area-list
        :areas="areas"
        @update="fetchAreas"
        v-if="!isAreasLoading"
      />
  
      <div v-else>Идет загрузка...</div>
  
      <my-dialog v-model:show="dialogVisible">
    <area-create-form @create="createArea" />
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
  // import PostForm from "@/Components/PostForm";
  import axios from "axios";
import AreaItem from "@/Components/AreaItem.vue";
import AreaList from "@/Components/AreaList.vue";
import AreaCreateForm from "@/Components/AreaCreateForm.vue";
  
  export default {
    components: {
      AreaList,
      AreaCreateForm,
      AreaItem
    
    },
    data() {
      return {
        areas: [],
        dialogVisible: false,
        isAreasLoading: false,
        selectedSort: "",
        page: 1,
        limit: 3,
        totalPages: 0,
      };
    },
    methods: {
      createAreas(area) {
        this.areas.push(area);
        this.dialogVisible = false;
      },
      removeArea(area) {
        this.areas = this.areas.filter((p) => p.id !== area.id);
      },
      showDialog() {
        this.dialogVisible = true;
      },
      changePage(pageNumber) {
        this.page = pageNumber;
        this.fetchAreas();
      },
      async fetchAreas() {
        try {
          this.isAreasLoading = true;
          const response = await axios.get(
            "http://127.0.0.1:8000/area/get_areas",
            {
              
              withCredentials: true,
            
              params: {
                _page: this.page,
                _limit: this.limit,
              },
            }
          );
          this.totalPages = Math.ceil(
            response.headers["x-total-count"] / this.limit
          );
          this.areas = response.data;
        } catch (e) {
          alert("Ошибка при получении симптомов");
        } finally {
          this.isAreasLoading = false;
        }
      },
    },
    mounted() {
      this.fetchAreas();
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
    margin-left: 15px;
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
  