

<template>
    <div>
      <div class="background"></div>
      <div class="welcome-text">
        <h1>Welcome back to BudgetBuddy</h1>
        <p>Manage your finance and more</p>
      </div>
  
      <form @submit.prevent="submitForm">
        <h3>Login Here</h3>
  
        <label for="username">Username</label>
        <input
        required
        type="text"
        placeholder="Username"
        id="username"
        name="username"
        v-model="usernameInput"
        />
  
        <label for="password">Password</label>
        <input  required
        placeholder="Password"
        id="password"
        name="password"
        type="password"
        v-model="passwordInput" />
  
        <button type="submit">Log In</button>
        <div class="social">
          <div class="go"><i class="fab fa-google"></i> Google</div>
          <div class="fb"><i class="fab fa-facebook"></i> Facebook</div>
        </div>
  
        <p class="m-auto mt-3 text-center fst-italic">
          <router-link to="/register" class="text-decoration-none">
            Doesn't have an account? Sign up!
          </router-link>
        </p>
      </form>
      </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';
  const usernameInput = ref('');
  const passwordInput = ref('');
  
  const submitForm = async () => {
    const username = usernameInput.value;
    const password = passwordInput.value;
    const key = "8f270c659c4211eebf9404ea5623eaeb";
    console.log(username, password, key);
  
    const formData = new FormData();
formData.append('user_name', username);
formData.append('password', password);
formData.append('key', key);

try {
  const response = await axios.post('http://localhost:8080/api/v1/login', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    withCredentials: true, // Include credentials in the request
  });

  console.log('Login successful:', response.data);
} catch (error) {
  if (error.response) {
    // The request was made and the server responded with a status code
    // that falls out of the range of 2xx
    console.error('Server responded with error status:', error.response.status);
    console.error('Response data:', error.response.data);
  } else if (error.request) {
    // The request was made but no response was received
    console.error('No response received from the server');
  } else {
    // Something happened in setting up the request that triggered an Error
    console.error('Error setting up the request:', error.message);
  }
}
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap');

  /* Responsive styles for smaller screens */

  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }
  
 body {
  height: 100vh;
  width: 100vw;
  background-size: cover; 
  background-position: 30% center;

}

  

  
  .welcome-text {
    color: #e5e5e5;
    position: absolute;
    transform: translate(-10%, -50%);
    top: 50%;
    left: 10%;
    width: 520px;
    word-wrap: break-word;
    text-align: start;
  }

  h1 {
    font-size: 5em;
    background: -webkit-linear-gradient(#eee, #5ed7ef);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  }
  
  form {
    height: max-content;
    width: 400px;
    background-color: rgba(107, 95, 197, 0.5);
    position: absolute;
    transform: translate(-80%, -50%);
    top: 50%;
    left: 80%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
   
    box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
    padding: 40px 35px;
  }
  
  form * {
    font-family: "Poppins", sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
  }
  
  form h3 {
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
  }
 
  label {
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
    text-align: start;
  }
  
  input {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
  }
  
  ::placeholder {
    color: #e5e5e5;
  }
  
  button {
    margin-top: 50px;
    width: 100%;
    background-color: #ffffff;
    
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer; 
    text-align: center;
  }
  
  .social {
    margin-top: 30px;
    display: flex;
  }
  
  .social div {
    width: 150px;
    border-radius: 3px;
    padding: 5px 10px 10px 5px;
    background-color: rgba(255, 255, 255, 0.27);
    color: #eaf0fb;
    text-align: center;
  }
  
  .social div:hover {
    background-color: rgba(255, 255, 255, 0.47);
  }
  
  .social .fb {
    margin-left: 25px;
  }
  
  .social i {
    margin-right: 4px;
  }
  
  a:hover {
    color: #ffffff;
  }
  
  a {
    color: #e5e5e5;
  }
  </style>
  