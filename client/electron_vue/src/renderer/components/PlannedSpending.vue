<template>
        <div class="plan-income">
        <article class="plann" v-for="plan in monthlyExpensePlans" :key="plan" @click="clickView(plan)">
            <button>
              <div class='ti flex space-between'>  
                <h1 :style="{fontSize: '20px'}" class='flex-1'>{{ plan.category }}</h1>
                <h1 :style="{fontSize: '20px'}" class='flex-1' @click="clickDelete(plan.id)">Delete</h1>
              </div>
                <p :style="{fontSize: '13px', paddingBottom: '20px'}">{{ plan.current_total_use }} spent</p>
                <fwb-progress
                  :progress="50"
                  label-position="inside"
                  label-progress
                  size="xl"
                  class="chart"
                />
                <p :style="{fontSize: '13px', paddingBottom: '20px'}">of {{ plan.initial_amount }}</p>
                <h2 :style="{fontSize: '20px'}">$ {{ plan.initial_amount - plan.current_total_use }} left</h2>
            </button>
        </article>
        <article class="addplan" @click="addPlan">
          <h1>+</h1>
        </article>

    </div>

</template>
<script setup lang="ts">
import { ref, defineEmits, onMounted, computed } from 'vue';
import { FwbProgress } from 'flowbite-vue'
import axios from 'axios';

const user_id = '6593ccdf025b256e0ffe24e8';
const monthlyExpensePlans = ref([]);
let viewData = ref(null)
let deleteId = ref(null)

const fetchMonthlyExpensePlans = async () => {
  try {
    const response = await axios.get(`http://localhost:8080/api/v1/monthly_expense_plan/${user_id}`);
    monthlyExpensePlans.value = response.data;
    console.log('Monthly Expense Plans:', monthlyExpensePlans.value);
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
const emits = defineEmits(['add-plan', 'view-plan']);

const addPlan = () => {
  emits('add-plan');
};

</script>

<style scoped>
.plan-income {
    position: absolute;
    top: 20px;
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
    float: left;
    margin: 7px auto;
}
.addplan {
    background-color: rgb(145, 145, 175);
    border-radius: 10px;
    padding: 10px;
    width: 48%;
    height: 150px;
    float: left;
    margin: 7px auto;
}

button {
    border: none;
    width: 100%;
    text-align: left;
    padding-left: 13px ;
    padding-top: 3px;
}
.chart{
        border: 1px solid #ddd;
        width:90%;
        background-color: white;
    }
.ti{
  width: 98%
}
</style>