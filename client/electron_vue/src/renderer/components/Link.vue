<script setup lang="ts">
const username = localStorage.getItem('username') ?? '';
</script>

<template>
  
    <div>
      
      <router-link to="/home" class="text-white" :class="{ 'font-bold': $route.name === 'Home' }">Overview</router-link>
      <router-link to="/transaction" class="text-white" :class="{ 'font-bold': $route.name === 'Transaction' }">Transaction</router-link>
      <router-link to="/plan" class="text-white" :class="{ 'font-bold': $route.name === 'Plan' }">Plan</router-link>
      <!-- Example router-link -->
      <router-link :to="{ name: 'Investment' }" class="text-white" :class="{ 'font-bold': $route.name === 'Investment' }">Investment</router-link>
      <router-link :to="{ name: 'Report' }" class="text-white" :class="{ 'font-bold': $route.name === 'Report' }">Report</router-link>
     
        <router-link :to="{ name: 'Profile' }" class="text-white  p-2 prof rounded-lg " :class="{ 'font-bold': $route.name === 'Profile' }">Hello, welcome back <strong>{{ username }}</strong> !</router-link>
      <router-view />
    </div>
     
   
  </template>
<style scoped>
.prof{
  position:absolute;
  top: 25px;
  right: 7%;
}
</style>
  