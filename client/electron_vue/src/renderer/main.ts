// main.ts
import './try.css';
import './assets/tailwind.css';
import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { setupCalendar } from 'v-calendar';
import VueApexCharts from 'vue3-apexcharts';
import { MonthPicker } from 'vue-month-picker';
import { MonthPickerInput } from 'vue-month-picker';

import router from './router/router';
// Import the 'cors' middleware


// Enable CORS for all routes

// Your routes and other middleware




const app = createApp(App);

// Configure Axios instance
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8080/api/v1', // Replace with your API base URL
  timeout: 5000, // Adjust the timeout as needed
  // Add any other Axios configurations here
});


// Make Axios available globally in the app
app.config.globalProperties.$axios = axiosInstance;

app.use(MonthPicker)
app.use(MonthPickerInput)
app.use(VueApexCharts);
app.use(setupCalendar, {})
app.use(router);
app.mount('#app');
