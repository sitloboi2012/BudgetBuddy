<script setup lang="ts">
import {ref} from 'vue';
import Networth from '../components/Networth.vue';
import OverviewVue from '../components/Overview.vue'; 
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
  <section class="display">
    <div><Networth @add-account="receiveEmit"/></div>
    <div class="screen"><OverviewVue/></div>
  </section>
</template>

<style scoped>
.form{
  position: relative;
  z-index: 999;
}
</style>
