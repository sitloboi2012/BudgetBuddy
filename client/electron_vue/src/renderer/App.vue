<script setup lang="ts">
import Networth from './components/Networth.vue';
import OverviewVue from './components/Overview.vue';
window.electronAPI.sendMessage('Hello from App.vue!');
</script>

<template>
  <div class="homebar">
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#transaction">Transaction</a></li>
        <li><a href="#investment">Investment</a></li>
        <li><a href="#plan">Plan</a></li>
        <li><a href="#report">Report</a></li>
    </ul>
  </div>
  <section>
    <div><Networth/></div>
    <div class="screen"><OverviewVue/></div>
  </section>
</template>

