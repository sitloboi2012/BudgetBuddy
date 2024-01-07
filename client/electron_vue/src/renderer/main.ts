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


/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)

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
app..component('font-awesome-icon', FontAwesomeIcon).mount('#app');
// const store = new Store();
// app.whenReady().then(createWindow);
