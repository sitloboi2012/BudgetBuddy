<template>
    <div class="form">
    <fwb-modal v-if="isShowModal" @close="closeModal">
      <template #header>
        <div class="flex items-center text-lg p-4">
          Add your account
        </div>
      </template>
      <template #body>
        <div>
          <fwb-input
            v-model="youraccount"
            placeholder="enter your account"
            label="Account Name"
            class="p-2"
          />
          <fwb-select
            v-model="accountbank"
            :options="bank"
            label="Bank"
            class="p-2"
          />
          <div class="flex justify-between p-2">
            <fwb-button @click="closeModal" color="alternative">
              Cancel
            </fwb-button>
            <fwb-button @click="createAccount" color="alternative">
              Save
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

const user_id = '657deedb53a90ee98e224654';
let { data } = defineProps(['data']);
let [accountName, currentBalance, accountId, bankName, accountType] = data;
let youraccount = ref(accountName || '');
let balance = ref(currentBalance || 0);
let accountbank = ref(bankName || '');
let selected = ref(accountType || '');
const bank = [
  { value: 'VIB', name: 'VIB' },
  { value: 'VIETCOMBANK', name: 'VIETCOMBANK' },
  { value: 'TECHCOMBANK', name: 'TECHCOMBANK' },
]

const isShowModal = ref(true);

const emits = defineEmits(['close-modal']);

function closeModal() {
  isShowModal.value = false;
  emits('close-modal');
}

async function createAccount() {
  // Convert string inputs to numbers using parseFloat
  const currentBalance = parseFloat(balance.value);

  // Create the request payload
  const requestData = {
    account_name: youraccount.value,
    account_type: selected.value,
    current_balance: currentBalance,
    bank_name: accountbank.value,
  };

  // Log the data before making the request
  console.log('Sending data to server:', requestData);

  // Make the HTTP request
  try {
    const response = await axios.put(`http://localhost:8080/api/v1/${user_id}/${selected.value.toString()}/${youraccount.value.toString()}`, requestData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    withCredentials: true, // Include credentials in the request
    });

    console.log('Server response:', response.data);

    // Handle success or update UI accordingly
  } catch (error) {
    console.error('Error:', error.response.data);

    // Handle error or update UI accordingly
  }
}
  onMounted(() => {
    createAccount();
  });
</script>