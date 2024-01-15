<template>
  <section>
  <div class=" grid grid-cols-5 p-6 gap-4">
    <div class="twolines  col-span-5 flex flex-row justify-end items-center p-4 gap-3 w-full h-fit">
      <div class="total_saving w-full"><router-link to="/plan"><strong>Total Saving: </strong>$ {{ totalSaving }}</router-link></div>
      <div style="{margin: 0 !important;}" class="investment w-full rounded bg-indigo-800 text-white h-full"><router-link to="/investment"><strong>Investment:</strong> $ {{ totalInvestment }}</router-link></div>
    </div>
    <div class="recentTrans col-span-3 w-full ">
      <div class="flex space-between w-full">
        <p class="w-full text-right py-2 pe-6 font-bold rounded bg-indigo-800 text-white">Recent Transactions  <router-link to="/transaction"  class="flex-1 ">></router-link></p>
       
      </div>
      <div class=" bg-white shadow-lg rounded-lg py-4 w-full trans-bg ">
      <div v-for="(transaction, index) in recentTrans.slice(0, 3)" :key="index" class="trans flex space-between pb-4 w-max">
        <h1 class="block">{{ transaction.transaction_name.charAt(0) }}</h1>
        <div class="pl-2">
          <h1 class="tit " >{{ transaction.transaction_name }}</h1>
          <p class="cat">{{ transaction.category }}</p>
        </div>
        <div class="pl-2">
          <h1 class="num">$ {{ transaction.Amount }}</h1>
          <p class="cat">{{ transaction.transaction_date }}</p>
        </div>
      </div>
    </div>
    </div>
    <div class="calender col-span-2    ">
      <p class="w-full text-right py-2 pe-6 font-bold rounded bg-indigo-800 text-white">Dates and Event </p>
      <Calendar  :attributes="attributes" expanded/>
    </div>
    
  
    <div id="chart" class="income col-span-3  w-full">
      <p class="w-full text-right py-2 pe-6 font-bold rounded bg-indigo-800 text-white">Your Income </p>
      <IncomeChart class="w-full"/></div>
    <div id="chart" class="expense col-span-1 w-96">
      <p class="w-full text-right py-2 pe-6 font-bold rounded bg-indigo-800 text-white">Expenses </p>
      <ExpenseChart/>
    </div>
  
    
   
  
   
  </div>
</section>
</template>

<script lang="ts" setup>
  import { ref, computed, onMounted } from 'vue';
  import { Calendar, DatePicker } from 'v-calendar';
  import 'v-calendar/style.css';
  import IncomeChart from './IncomeChart.vue'
  import ExpenseChart from './ExpenseChart.vue'
  import axios from 'axios';

  const recentTrans = ref([])
  const userAccounts = ref([]);
  const todos = ref([
  ]);
  const user_id = localStorage.getItem('userId') ?? '';
  const fetchBankAccount = async () => {
    try {
      const response = await axios.get(`http://localhost:8080/api/v1/${user_id}`);
      userAccounts.value = response.data.list_account_name;
    } catch (error) {
      console.error('Error fetching account information:', error);
    }
  };
  const fetchUserBills = async () => {
    try {
      const response = await axios.get(`http://localhost:8080/api/v1/user_bill/${user_id}`);
      const userBills = response.data;

      // Update todos with userBills data
      todos.value = userBills.map((bill: { bill_name: any; recurrent_date_value: any; }) => ({
        description: bill.bill_name,
        isComplete: false,
        dates:  bill.recurrent_date_value,
        color: 'red', // Set your desired color
      }));
    } catch (error) {
      console.error('Error fetching user bills:', error);
    }
  };
  const fetchTrans = async () => {
    try {
      const response = await axios.get(`http://localhost:8080/api/v1/transaction/${user_id}`);
      recentTrans.value = response.data;
      console.log('recentTrans', recentTrans)
    } catch (error) {
      console.error('Error fetching account information:', error);
    }
  };


  onMounted(() => {
    fetchBankAccount();
    fetchUserBills();
    fetchTrans();
    });

  const totalSaving = computed(() => {
    return userAccounts.value
      .filter(account => account[4] === 'Saving')
      .reduce((sum, account) => sum + parseFloat(account[1]), 0)
      .toFixed(2);
  });
  
  const totalInvestment = computed(() => {
    return userAccounts.value
      .filter(account => account[4] === 'Investment')
      .reduce((sum, account) => sum + parseFloat(account[1]), 0)
      .toFixed(2);
  });
  
  const attributes = computed(() => [
    // Attributes for todos
    ...todos.value.map(todo => ({
      dates: todo.dates,
      dot: {
        color: todo.color,
        ...(todo.isComplete && { class: 'opacity-75' }),
      },
      popover: {
        label: todo.description,
      },
    })),
  ]);


</script>
<style scoped>


.calender{ 
  border-radius: 15px;
}
.total_saving{
  padding: 25px;
  background-image: url(../assets/img2.png);
  background-repeat: no-repeat;
  background-size: cover;
 
  height: fit-content;
  color: white;
  font-weight: 600;
  border-radius: 15px;
}
.block{
  background-color: blue;
  border-radius: 15px 15px 0px 15px;
  padding: 14px 17px;
  width: fit-content;
  color: white;
  font-weight: 600;
}
.trans{
  margin-left:20px;
  
}
.cat{
  font-size: 11px;
  font-weight: 400;
  color: rgb(197, 195, 195);
}
.tit{
  font-size: 16px;
  font-weight: 700;
  color: rgb(76, 73, 164);
  padding-bottom: 10px;
  width:300px;
}
.num{
  font-size: 15px;
  font-weight: 700;
  color: rgb(33, 36, 78);
  padding-bottom: 10px;
  width:200px;
}
.trans-bg {
  height: 17rem;
}
.investment{
  padding: 25px;

  background-repeat: no-repeat;
  background-size: cover;
 
  height: fit-content;
  
  font-weight: 600;
  border-radius: 15px;
}
</style>