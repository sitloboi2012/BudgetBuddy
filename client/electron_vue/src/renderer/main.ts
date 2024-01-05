// main.ts
import './style.css';
import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import './tailwind.css';
import router from './router/router';
// import Store from 'electron-store';
// import {  app,BrowserWindow } from 'electron';
// import * as path from 'path';
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

app.use(router);
app.mount('#app');
// const store = new Store();
// app.whenReady().then(createWindow);
