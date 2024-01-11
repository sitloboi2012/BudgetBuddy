<template>
    <div class="form">
      <fwb-modal v-if="isDisplay" @close="closeModal">
        <template #header>
          <div class="flex items-center text-lg p-4">
            Add Income
          </div>
        </template>
        <template #body>
          <div>
            <fwb-input
              v-model="incomename"
              placeholder="enter your income name"
              label="Name"
              class="p-2"
            />
            <fwb-input
              v-model="amount"
              placeholder="$1100"
              label="Amount"
              class="p-2"
            />
            <div class="flex justify-between p-2">
              <fwb-button @click="closeModal" color="alternative">
                Cancel
              </fwb-button>
              <fwb-button @click="addIncome" color="alternative">
                Add
              </fwb-button>
            </div>
          </div>
        </template>
      </fwb-modal>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineEmits, onMounted, toRefs } from 'vue';
  import { FwbButton, FwbModal, FwbInput, FwbSelect } from 'flowbite-vue';
  import axios from 'axios';
  
  const user_id = localStorage.getItem('userId') ?? '';
  const incomename = ref('');
  const amount = ref('');
  let { newmonth } = defineProps(['newmonth']);
  const time = ref(newmonth);
  const type = ref('Income')
  console.log('showtime', time.value)
  
  const isDisplay = ref(true);
  const emits = defineEmits(['close-modal']);
  
  function closeModal() {
    isDisplay.value = false;
    emits('close-modal');
  }
  
  async function addIncome() {
    // Convert string inputs to numbers using parseFloat
    const currentAmount = parseFloat(amount.value);
  
    // Create the request payload
    const requestData = {
      spending_name: incomename.value,
      spending_type: type.value,
      amount: currentAmount,
      time_duration: time.value,
    };
  
    // Log the data before making the request
    console.log('Sending data to server:', requestData);
  
    // Make the HTTP request
    try {
      const response = await axios.post(`http://localhost:8080/api/v1/plan_spending/${user_id}/create`, requestData, {
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
    addIncome();
  });
  </script>
  
  <style scoped>
    /* Your component styles go here */
  </style>