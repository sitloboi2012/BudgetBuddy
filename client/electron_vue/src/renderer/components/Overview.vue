<template>
  <div class='grid'>
    <div class="calender">
      <Calendar :attributes="attributes" />
    </div>
    <div class="twolines">
      <div class="total_saving">Total Saving: {{ totalSaving }}</div>
      <div class="investment">Investment: {{ totalInvestment }}</div>
    </div>
    <div id="chart" class="income"><IncomeChart/></div>
  </div> 
    <div class="recentTrans">
      <h1 class="pb-4">Recent transaction</h1>
      <div class="trans flex justify-between pb-4">
        <h1 class="block">D</h1>
        <div>
          <h1 class="tit">Monthly PayBack Usage</h1>
          <p class="cat">Entertainment</p>
        </div>
        <div>
          <h1 class="num">200000</h1>
          <p class="cat">2024-02-03</p>
        </div>
      </div>
      <div class="trans flex justify-between pb-4">
        <h1 class="block ">D</h1>
        <div>
          <h1 class="tit">Monthly PayBack Usage</h1>
          <p class="cat">Entertainment</p>
        </div>
        <div>
          <h1 class="num">200000</h1>
          <p class="cat">2024-02-03</p>
        </div>
      </div>
      <div class="trans flex justify-between">
        <h1 class="block">D</h1>
        <div>
          <h1 class="tit">Monthly PayBack Usage</h1>
          <p class="cat">Entertainment</p>
        </div>
        <div>
          <h1 class="num">200000</h1>
          <p class="cat">2024-02-03</p>
        </div>
      </div>
    </div>
    <div id="chart" class="expense"><ExpenseChart/></div> 
</template>

<script lang="ts" setup>
  import { ref, computed, onMounted } from 'vue';
  import { Calendar, DatePicker } from 'v-calendar';
  import 'v-calendar/style.css';
  import IncomeChart from './IncomeChart.vue'
  import ExpenseChart from './ExpenseChart.vue'
  import axios from 'axios';

  const userAccounts = ref([]);
  const todos = ref([
  ]);
  const user_id = '657deedb53a90ee98e224654';
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


  onMounted(() => {
    fetchBankAccount();
    fetchUserBills();
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
.grid{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-gap: 10px;
  margin: 20px;
}

.calender{ 
  border-radius: 15px;
}
.total_saving{
  padding: 25px;
  background-image: url(../assets/img2.png);
  background-repeat: no-repeat;
  background-size: cover;
  width:fit-content;
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
  width: 350px;
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
}
.num{
  font-size: 15px;
  font-weight: 700;
  color: rgb(33, 36, 78);
  padding-bottom: 10px;
}
.recentTrans{
  width: 400px;
}
.investment{
  padding: 25px;
  background-color: rgb(220, 220, 220);
  background-repeat: no-repeat;
  background-size: cover;
  width:fit-content;
  height: fit-content;
  color: rgb(60, 44, 161);
  font-weight: 600;
  border-radius: 15px;
}
</style>