<script setup lang="ts">

import InvestmentBalance from '../components/InvesmentBalance.vue';
import News from '../components/News.vue';
import StockMarket from '../components/StockMarket.vue';


import { ref, onMounted } from 'vue';

const userName = ref<string | null>(null);





</script>

<template>
   
  <section >
   
    <div class="grid grid-cols-2 gap-4 pt-5">
  <div class="pt-8">
   <InvestmentBalance/>
  </div>
  <div class="pt-8 pe-5"><StockMarket/></div>
  <div class="col-span-2 news w-full overflow-x-hidden px-5 pt-10">
   <News/>
  </div>

 
  
</div>
    
   
   
  

  </section>  
</template>

<style>
.display {
   
    width: 900px;
    height: 650px ;
    max-height: 100% ;

}


</style>