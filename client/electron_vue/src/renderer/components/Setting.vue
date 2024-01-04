<template>
    <section class="planning">
      <div class="networth">
        <div class="overview-section bg-violet-600" >
          <h2 class="text-xl text-white font-bold">{{ income }}</h2>
          <p class="text-xs text-white">General</p>
        </div>
        <div class="overview-section bg-neutral-100">
          <h2 class="text-xl text-black font-bold">{{ plannedSpending }}</h2>
          <p class="text-xs text-black">Account</p>
        </div>
        <div class="overview-section bg-blue-600">
          <h2 class="text-xl text-white font-bold">{{ savingGoals }}</h2>
          <p class="text-xs text-white">Categories and Tags</p>
        </div>
        <div class="overview-section bg-amber-500">
          <h2 class="text-xl text-white font-bold">{{ otherSpending }}</h2>
          <p class="text-xs text-white">Notifications</p>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        month: 'Jan 2024',
        income: '$8,469.00',
        bills: '-$4,389.00',
        plannedSpending: '$30.00',
        savingGoals: '$500.00',
        otherSpending: '$389.00',
      };
    },
  };
  </script>
  
  <style>
  
  .overview-section {
    padding: 10px;
    border-radius: 20px;
    margin: 10px;
  }
  </style>