<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '../../@/components/ui/card';
import { Separator } from '../../@/components/ui/separator'

const billData = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8080/api/v1/user_bill/6593ccdf025b256e0ffe24e8/sorted');
    billData.value = response.data;
    console.log('bill data:', billData.value);
  } catch (error) {
    console.error('Error fetching bill:', error);
  }
});
</script>

<template>
  <div>
    <h1 class="font-semibold text-lg text-left ps-5 pb-5">Upcoming Bills</h1>
   
    <div class="  justify-center gap-4 h-44 carousel rounded-box w-full">
    <div class="carousel-item bg-indigo-800 w-full">
        <!-- Use v-for to loop through a range (0 to 3) and create a card for each iteration -->
      <Card
        v-for="(bill, index) in billData"
        :key="index"
        class="w-48  h-36 mt-3 me-4 relative overflow-hidden ms-4"
       
       
      >
    
        <div class="relative z-10 flex flex-col" v-if="bill.recurrent_reminder==true" > <!-- Place text inside a relative container -->
           
            <CardHeader class=" text-ellipsis  font-semibold text-left h:1/2">   
                {{bill.bill_name}}
                <Separator/>
            <CardTitle class="text-black font-bolder text-xs overflow-hidden text-ellipsis hover:underline ">
              <a :href="bill.bill_url" target="_blank" rel="noopener noreferrer" class="p-0">{{bill.recurrent_date_value}}  </a>
            </CardTitle>
            <CardDescription class="text-black text-xs">
           $ {{bill.bill_value}}
            </CardDescription>
        </CardHeader>
       
         
        </div>
      </Card>
    </div>
    </div>
   
  </div>
</template>
