<template>
    <div>
      <div class="chekup">
        <h1 v-if="diagnoses && diagnoses.length > 0">Список Диагнозов</h1>
        <h2 v-else style="color: red">Отсутствуют диагнозы</h2>
        <div class="btn">
            <my-button @click="showDialog"> Добавить диагноз </my-button>
          </div>
      </div>
      <diagnosis-list
        :diagnoses="diagnoses"
        @update="fetchDiagnoses"
        v-if="!isDiagnosesLoading"
      />
  
      <div v-else>Идет загрузка...</div>
  
      <my-dialog v-model:show="dialogVisible">
    <diagnosis-create-form @create="createDiagnosis" />
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
import DiagnosisItem from "@/Components/DiagnosisItem.vue";
import DiagnosisList from "@/Components/DiagnosisList.vue";
import DiagnosisCreateForm from "@/Components/DiagnosisCreateForm.vue";
  // import MySelect from "@/Components/UI/MySelect";
  // import MyButton from "@/Components/UI/MyButton.vue";
  
  export default {
    components: {
      DiagnosisList,
      DiagnosisCreateForm,
      DiagnosisItem
    
    },
    data() {
      return {
        diagnoses: [],
        dialogVisible: false,
        isDiagnosesLoading: false,
        selectedSort: "",
        page: 1,
        limit: 3,
        totalPages: 0,
      };
    },
    methods: {
      createDiagnosis(diagnosis) {
        this.diagnoses.push(this.diagnosis);
        this.dialogVisible = false;
      },
      removeDiagnosis(diagnosis) {
        this.diagnoses = this.diagnoses.filter((p) => p.id !== diagnosis.id);
      },
      showDialog() {
        this.dialogVisible = true;
      },
      changePage(pageNumber) {
        this.page = pageNumber;
        this.fetchDiagnoses();
      },
      async fetchDiagnoses() {
        try {
          this.isDiagnosesLoading = true;
          const response = await axios.get(
            "http://127.0.0.1:8000/diagnosis/get_all",
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
          this.diagnoses = response.data;
        } catch (e) {
          alert("Ошибка при получении пациентов");
        } finally {
          this.isDiagnosesLoading = false;
        }
      },
    },
    mounted() {
      this.fetchDiagnoses();
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
  