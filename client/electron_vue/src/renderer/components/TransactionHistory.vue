<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { columns } from "./TransactionTable/columns"
import type { Payment } from './TransactionTable/columns';
import DataTable from "./TransactionTable/DataTable.vue"
import { Button } from '../../@/components/ui/Button'
const data = ref<Payment[]>([])
const user_id = localStorage.getItem('userId') ?? '';

async function getData(user_id: string): Promise<Payment[]> {
  try {
    // Replace 'YOUR_BACKEND_API_URL' with the actual URL of your backend API
    const response = await axios.get(`http://localhost:8080/api/v1/transaction/${user_id}`, {
        withCredentials: true,
        
    });
console.log(response.data);
    // Return the data from the response
    return response.data;
  } catch (error) {
    // Handle errors (e.g., network error, API error)
    console.error('Error fetching data:', error);
    throw error; // You can choose to handle or propagate the error
  }
}
  async function fetchDataFromBackend() {

  try {
    const backendData = await getData(user_id);

    // Map the backend data to the desired structure
    const mappedData = backendData.map((backendTransaction) => ({
      id: backendTransaction._id,
      amount: backendTransaction.Amount,
      account: backendTransaction.account_name,
      transactionName: backendTransaction.transaction_name,
      date: backendTransaction.transaction_date,
      payee: backendTransaction.Payee,
      categories: backendTransaction.category,
    }));

    console.log('Mapped data from backend:', mappedData);
    return mappedData;

    // Now 'mappedData' has the structure you provided
  } catch (error) {
    // Handle errors if needed
    console.error('Error fetching data from backend:', error);
  }
}



onMounted(async () => {
  data.value = await fetchDataFromBackend();
});
</script>

<template>
  <header class="  pt-6 pb-0 border-t ps-5  flex items-center w-full ">
    
    <h1 class="font-semibold text-lg w-full flex items-center "><span class="w-max">Transaction History</span>
        <Button class="w-6 h-6 p-0 ms-4 bg-indigo-700 align-middle">
         +
          </Button>
    </h1></header>
  <div class="container pb-8 mx-auto ">
    <DataTable :columns="columns" :data="data" />
  </div>
</template>