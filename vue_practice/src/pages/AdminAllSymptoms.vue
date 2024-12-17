<template>
    <div>
      <div class="chekup">
        <h1 v-if="symptoms.length > 0">Список симптомов</h1>
        <h2 v-else style="color: red">Отсутствуют симптомы</h2>
        <div class="btn">
            <my-button @click="showDialog"> Добавить симптом </my-button>
          </div>
      </div>
      <symptom-list
        :symptoms="symptoms"
        @update="fetchSymptoms"
        v-if="!isSymptomsLoading"
      />
  
      <div v-else>Идет загрузка...</div>
  
      <my-dialog v-model:show="dialogVisible">
    <symptom-create-form @create="createSymptom" />
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
  import SymptomItem from "@/Components/SymptomItem.vue";
  import axios from "axios";
import SymptomList from "@/Components/SymptomList.vue";
import SymptomCreateForm from "@/Components/SymptomCreateForm.vue";
  
  export default {
    components: {
      SymptomList,
      SymptomCreateForm,
      SymptomItem
    
    },
    data() {
      return {
        symptoms: [],
        dialogVisible: false,
        isSymptomsLoading: false,
        selectedSort: "",
        page: 1,
        limit: 3,
        totalPages: 0,
      };
    },
    methods: {
      createSymptom(symptom) {
        this.symptoms.push(symptom);
        this.dialogVisible = false;
      },
      removeSymptom(symptom) {
        this.symptoms = this.symptoms.filter((p) => p.id !== symptom.id);
      },
      showDialog() {
        this.dialogVisible = true;
      },
      changePage(pageNumber) {
        this.page = pageNumber;
        this.fetchSymptoms();
      },
      async fetchSymptoms() {
        try {
          this.isSymptomsLoading = true;
          const response = await axios.get(
            "http://127.0.0.1:8000/symptom/get_all",
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
          this.symptoms = response.data;
        } catch (e) {
          alert("Ошибка при получении симптомов");
        } finally {
          this.isSymptomsLoading = false;
        }
      },
    },
    mounted() {
      this.fetchSymptoms();
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
  