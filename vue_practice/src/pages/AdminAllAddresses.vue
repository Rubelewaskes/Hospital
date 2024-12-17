<template>
    <div>
      <div class="chekup">
        <h1 v-if="addresses.length > 0">Список адресов</h1>
        <h2 v-else style="color: red">Отсутствуют адреса</h2>
        <div class="btn">
            <my-button @click="showDialog"> Добавить адрес </my-button>
          </div>
      </div>
      <address-list
        :addresses="addresses"
        @update="fetchAddresses"
        v-if="!isAddressesLoading"/>
  
      <div v-else>Идет загрузка...</div>
  
      <my-dialog v-model:show="dialogVisible">
    <address-create-form @create="createAddresses" />
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
import AddressItem from "@/Components/AddressItem.vue";
import AddressList from "@/Components/AddressList.vue";
import AddressCreateForm from "@/Components/AddressCreateForm.vue";
  
  export default {
    components: {
      AddressList,
      AddressCreateForm,
      AddressItem
    
    },
    data() {
      return {
        addresses: [],
        dialogVisible: false,
        isAddressesLoading: false,
        selectedSort: "",
        page: 1,
        limit: 3,
        totalPages: 0,
      };
    },
    methods: {
      createAddresses(address) {
        this.addresses.push(address);
        this.dialogVisible = false;
      },
      removeAddress(address) {
        this.addresses = this.addresses.filter((p) => p.id !== address.id);
      },
      showDialog() {
        this.dialogVisible = true;
      },
      changePage(pageNumber) {
        this.page = pageNumber;
        this.fetchAddresses();
      },
      async fetchAddresses() {
        try {
          this.isAddressesLoading = true;
          const response = await axios.get(
            "http://127.0.0.1:8000/address/get_all",
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
          this.addresses = response.data;
        } catch (e) {
          alert("Ошибка при получении симптомов");
        } finally {
          this.isAddressesLoading = false;
        }
      },
    },
    mounted() {
      this.fetchAddresses();
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
  