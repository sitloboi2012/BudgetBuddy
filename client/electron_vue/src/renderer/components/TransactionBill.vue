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

const newsData = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8080/api/v1/get_news');
    newsData.value = response.data.list_of_news;
    console.log('News data:', newsData.value);
  } catch (error) {
    console.error('Error fetching news:', error);
  }
});
</script>

<template>
  <div>
    <h1 class="font-semibold text-lg text-left ps-5 pb-5">Upcoming Bills</h1>
   
    <div class="  justify-center gap-4 h-44 carousel rounded-box w-full">
    <div class="carousel-item bg-indigo-500">
        <!-- Use v-for to loop through a range (0 to 3) and create a card for each iteration -->
      <Card
        v-for="(news, index) in newsData"
        :key="index"
        class="w-48  h-36 mt-3 me-4 relative overflow-hidden"
       
      >
    
        <div class="relative z-10 flex flex-col"> <!-- Place text inside a relative container -->
           
            <CardHeader class=" text-ellipsis  font-semibold text-left h:1/2">   
                Bill Title
                <Separator/>
            <CardTitle class="text-black font-bolder text-xs overflow-hidden text-ellipsis hover:underline ">
              <a :href="news.news_url" target="_blank" rel="noopener noreferrer" class="p-0">Time  </a>
            </CardTitle>
            <CardDescription class="text-black text-xs">
           $ Amount
            </CardDescription>
        </CardHeader>
       
         
        </div>
      </Card>
    </div>
    </div>
   
  </div>
</template>
