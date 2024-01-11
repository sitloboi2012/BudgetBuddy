<template> 
  <button @click="prevMonth">&lt;</button>
  <span >{{ monthNames[currentMonth] }} {{ currentYear }}</span>
  <button  @click="nextMonth">&gt;</button>
  <div class="plan-income">
    <article class="plann" v-for="plan in monthlyExpensePlans" :key="plan" @click="clickView(plan)">
          <div class='ti flex'>  
            <h1 :style="{fontSize: '20px', paddingRight: '70px'}" class='flex-1'>{{ plan.category }}</h1>
            <h1 :style="{fontSize: '25px', color:'blue'}" class='flex-1' @click="clickDelete(plan.id)">-</h1>
          </div>
            <p :style="{fontSize: '13px',paddingTop:'20px', paddingBottom: '5px', color:'gray'}">{{ plan.current_total_use }} spent</p>
            <fwb-progress
              :progress="roundedProgress(plan.current_total_use, plan.initial_amount)"
              label-position="inside"
              label-progress
              size="xl"
              class="chart"
            />
            <p :style="{fontSize: '13px', paddingTop:'5px', paddingBottom: '20px', color:'gray'}">of {{ plan.initial_amount }}</p>
            <h2 :style="{fontSize: '20px'}">$ {{ plan.initial_amount - plan.current_total_use }} left</h2>
    </article>
    <article class="addplan" @click="addPlan(formattedMonth, currentYear)">
      <h1>+</h1>
    </article>
  </div>

</template>
<script setup lang="ts">
import { ref, defineEmits, onMounted, computed, watch } from 'vue';
import { FwbProgress } from 'flowbite-vue'
import axios from 'axios';
import { faCommentsDollar } from '@fortawesome/free-solid-svg-icons';
const  currentMonth= ref(new Date().getMonth())
const  currentYear= ref(new Date().getFullYear())
const  monthNames= ref([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
  ])

const  prevMonth =() => {
    if (currentMonth.value === 0) {
      currentMonth.value = 11;
      currentYear.value -= 1;
    } else {
      currentMonth.value -= 1;
    }};
const  nextMonth =()=> {
    if (currentMonth.value === 11) {
      currentMonth.value = 0;
      currentYear.value += 1;
    } else {
      currentMonth.value += 1;
    }
  };

  watch (currentMonth,async(newMonth)=>{
    console.log('newMonth', newMonth)
    console.log('year', currentYear.value)
    console.log('formatMonth', formattedMonth.value)
    fetchMonthlyExpensePlans();
    emits('send-month1', newMonth);
    emits('send-year1', currentYear.value);
  }
  )

const user_id = localStorage.getItem('userId') ?? '';
const monthlyExpensePlans = ref([]);
let viewData = ref(null)
let deleteId = ref(null)
let sendMonth = ref(null)
let that_year = ref( "2024");

let formattedMonth = ref(
  computed(() => {
    return new Date(`${that_year.value}-${currentMonth.value + 1}-10`)
      .toLocaleString('en-US', { month: 'short' });
  })
);

const fetchMonthlyExpensePlans = async () => {
  try {
    const response = await axios.get(`http://localhost:8080/api/v1/monthly_expense_plan/${user_id}`);
    const planInMonth = response.data.filter((plan) => {
      const planDate = `${formattedMonth.value} ${currentYear.value}`;
      console.log('showmwe',planDate)
      return planDate === plan.time_duration;
    });
    monthlyExpensePlans.value = planInMonth;
    console.log('Monthly Expense Plans:', monthlyExpensePlans.value);
    const totalInitialAmount = monthlyExpensePlans.value.reduce((sum, expense) => sum + expense.initial_amount, 0);
    console.log("Total Initial Amount:", totalInitialAmount);
    emits('send-total-1',totalInitialAmount)
  } catch (error) {
    console.error('Error fetching monthly expense plans:', error);
  }
};
const Delete = async (deleteId) => {
  try {
    const response = await axios.delete(`http://localhost:8080/api/v1/monthly_expense_plan/${user_id}/${deleteId}`);
    console.log('Delete this ID', response.data);
    await fetchMonthlyExpensePlans();
  } catch (error) {
    console.error('Error deleting entry:', error);
  }
};

onMounted(() => {
  fetchMonthlyExpensePlans();
});

const clickView = (itemView: any) => {
  viewData = itemView,
  emits("view-plan", viewData);
}
const clickDelete = (itemDelete: any) => {
  deleteId = itemDelete;
  Delete(deleteId);
};
const emits = defineEmits(['add-plan', 'view-plan', 'send-month1', 'send-year1', 'send-total-1']);

const addPlan = (formattedMonth: any, currentYear: any) => {
  const sendMonth = `${formattedMonth} ${currentYear}`;
  console.log("viewbeforsend", sendMonth)
  emits('add-plan', sendMonth);
};
const roundedProgress = (currentTotalUse, initialAmount) => {
  return Math.ceil((currentTotalUse / initialAmount) * 100);
};

</script>

<style scoped>
.plan-income {
    position: absolute;
    top: 40px;
    left: 20px;
    width: 93%;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
}

.plann {
    background-color: lavender;
    border-radius: 10px;
    padding: 10px;
    width: 48%;
    margin: 7px auto;
}
.addplan {
    background-color: rgba(189, 189, 189, 0.58);
    border-radius: 10px;
    padding: 10px;
    width: 48%;
    height: 190px;
    float: left;
    margin: 7px auto;
    align-content: center;
}

.chart{
        border: 1px solid #ddd;
        width:90%;
        background-color: white;
    }
.ti {
  display: flex;
  justify-content: space-between;/* Align items vertically in the center if needed */
}


</style>