<template>
    <div class="form">
      <fwb-modal v-if="isDisplay" @close="closeModal">
        <template #header>
          <div class="flex items-center text-lg p-4">
            Plan your expense
          </div>
        </template>
        <template #body>
          <div>
            <fwb-select
              v-model="category"
              :options="available"
              label="Category"
              class="p-2"
            />
            <fwb-input
              v-model="initialamount"
              placeholder="$1100"
              label="Amount"
              class="p-2"
            />
            <div class="flex justify-between p-2">
              <fwb-button @click="closeModal" color="alternative">
                Cancel
              </fwb-button>
              <fwb-button @click="addPlan" color="alternative">
                Add
              </fwb-button>
            </div>
          </div>
        </template>
      </fwb-modal>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineEmits, onMounted } from 'vue';
  import { FwbButton, FwbModal, FwbInput, FwbSelect } from 'flowbite-vue';
  import axios from 'axios';
  
  const user_id = localStorage.getItem('userId') ?? '';
  const category = ref('');
  let { newmonth } = defineProps(['newmonth']);
  const time = ref(newmonth);
  const available = [
  { value: 'Housing', name: 'Housing' },
  { value: 'Transportation', name: 'Transportation' },
  { value: 'Groceries', name: 'Groceries' },
  { value: 'Entertainment', name: 'Entertainment' },
  { value: 'Food & Dining', name: 'Food & Dining' },
  { value: 'Health & Fitness', name: 'Health & Fitness' },
  { value: 'Debt & Loans', name: 'Debt & Loans' },
  { value: 'Education', name: 'Education' },
] 
  const initialamount = ref('');
  
  const isDisplay = ref(true);
  const emits = defineEmits(['close-modal']);
  
  function closeModal() {
    isDisplay.value = false;
    emits('close-modal');
  }
  
  async function addPlan() {
    // Convert string inputs to numbers using parseFloat
    const initialAmount = parseFloat(initialamount.value);
  
    // Create the request payload
    const requestData = {
      category: category.value,
      initial_amount: initialAmount,
      time_duration: time.value,
    };
  
    // Log the data before making the request
    console.log('Sending data to server:', requestData);
  
    // Make the HTTP request
    try {
      const response = await axios.post(`http://localhost:8080/api/v1/monthly_expense_plan/${user_id}/create`, requestData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      withCredentials: true, // Include credentials in the request
      });
  
      console.log('Server response:', response.data);
      closeModal();
  
      // Handle success or update UI accordingly
    } catch (error) {
      console.error('Error:', error.response.data);
  
      // Handle error or update UI accordingly
    }
  }
  onMounted(() => {
    addPlan();
  });
  </script>
  
  <style scoped>
    /* Your component styles go here */
  </style>