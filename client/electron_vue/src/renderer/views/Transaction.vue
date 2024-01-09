<script setup lang="ts">
import {ref} from 'vue';
import Networth from '../components/Networth.vue';
import OverviewVue from '../components/Overview.vue'; 
import TransactionComponent from '../components/TransactionComponent.vue';

import Form from '../components/Form.vue'
import Links from  '../components/Link.vue';

const isFormVisible = ref(false);

const receiveEmit = () => {
  isFormVisible.value = true;
}

const closeForm = () => {
  isFormVisible.value = false;
}

</script>

<template>
   <Links/>
   <Form class="form" v-if="isFormVisible" @close-modal="closeForm" />
  <section class="display grid-cols-4">
    <div class=""><Networth @add-account="receiveEmit"/></div>
    <div class="investment rounded-lg bg-gray-200 w-full col-span-3 mt-14">
   
      <div> <TransactionComponent/></div>
    </div>
  </section>  
</template>