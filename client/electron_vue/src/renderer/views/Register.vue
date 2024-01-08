
<script setup lang="ts">
import axios from 'axios';
import { ref, reactive} from 'vue';

const user_name = ref('');
const full_name = ref('');
const email = ref('');
const number = ref('');
const address = ref('');
const password = ref('');
const repassword = ref('');

const state = {
  use_name: {
    value: '',
    error: '',
  },
  full_ame: {
    value: '',
    error: '',
  },
  email: {
    value: '',
    error: '',
  },
  number: {
    value: '',
    error: '',
  },
  address: {
    value: '',
    error: '',
  },
  password: {
    value: '',
    error: '',
  },
  repassword: {
    value: '',
    error: '',
  },
};


const validateEmail = () => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(state.email.value)) {
    state.email.error = 'Invalid email address';
    return false;
  } else {
    state.email.error = '';
    return true;
  }
};

const validateNumber = () => {
  const numberRegex = /^\d+$/;
  if (!numberRegex.test(state.number.value)) {
    state.number.error = 'Invalid phone number';
    return false;
  } else {
    state.number.error = '';
    return true;
  }
};
const validatePasswordMatch = () => {
  if (state.password.value !== state.repassword.value) {
    state.repassword.error = 'Passwords do not match';
    return false;
  } else {
    state.repassword.error = '';
    return true;
  }
};
  
const register = async () => {
  for (const field in state) {
    state[field].error = '';
  }
  // Validate email, number, and password match
  const isEmailValid = validateEmail();
  const isNumberValid = validateNumber();
  const isPasswordMatchValid = validatePasswordMatch();

  // Check if there are any validation errors
  if (!isEmailValid || !isNumberValid || !isPasswordMatchValid) {
    // Handle validation errors, e.g., show error messages and add red border
    console.log('Form validation failed');
    return;
  }
  // Create a FormData object to send form data
  const formData = new FormData();
  formData.append('user_name', user_name.value);
  formData.append('password', password.value);
  formData.append('full_Name', full_name.value);
  formData.append('number', number.value);
  formData.append('email', email.value);

  formData.append('address', address.value);

console.log(formData)

  try {
    const response = await axios.post('http://localhost:8080/api/v1/register', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    withCredentials: true, // Include credentials in the request
  });

    // Handle successful registration
    console.log('Registration successful!', response.data);
  } catch (error) {
    // Handle registration error
    console.error('Registration failed:', error.message);
  }
};
</script>
<template>
    <div >
      <div class="background"></div>
      <div class="welcome-text">
        <h1>Join BudgetBuddy Today</h1>
        <p>Unlock the power of financial management</p>
      </div>
  
      <form @submit.prevent="register">
        <h3>Register Here</h3>
  <div class="grid grid-cols-2">
    <div class="form-input"><label for="user_name">Username *</label>
        <input
          required
          type="text"
          placeholder="user_name"
          id="user_name"
          name="user_name"
          v-model="user_name"
        /></div>
        <div class="form-input"><label for="full_name">Full Name *</label>
      <input
        required
        type="text"
        placeholder="Full Name"
        id="full_name"
        v-model="full_Name"
      /></div> 
        
      
        
        <div class="form-input">  <label for="number">Phone Number</label>
      <input
       
        type="text"
        placeholder="Phone Number"
        id="number"
        v-model="number"
      />
      <span v-if="state.phone.error" class="error-message">{{ state.phone.error }}</span>
</div>
<div class="form-input"><label for="address">Address</label>
      <input
       
        type="text"
        placeholder="Address"
        id="address"
        v-model="address"
      /> </div>
      
      <div class="form-input">  <label for="password">Password *</label>
        <input
          required
          type="password"
          placeholder="Password"
          id="password"
          name="password"
          v-model="password"
        />
  </div> 
   <div class="form-input"> <label for="repassword">Re-enter Password *</label>
        <input
          required
          type="password"
          placeholder="Re-enter Password"
          id="repassword"
          name="repassword"
          v-model="repassword"
        /> 
        <span v-if="state.repassword.error" class="error-message">{{ state.repassword.error }}</span>
      </div>
        <div class="form-input  col-span-2"><label for="email">Email *</label>
        <input
          required
          type="email"
          placeholder="Email"
          id="email"
          name="email"
          v-model="email"
        />
        <span v-if="state.email.error" class="error-message">{{ state.email.error }}</span>
        <p class="text-sm italic pt-3"> Enter valid email to recieve authentication key </p>
      </div>
       
  </div>
  
        <button class="mt-5 text-center justify-center" type="submit">Register</button>
        <p class="m-auto mt-3 text-center fst-italic">
          <router-link to="/login" class="text-decoration-none">
            Already have an account? Sign in!
          </router-link>
        </p>
      </form>
    </div>
  </template>

  
  <style scoped>
  /* ... your existing styles ... */
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap');
body {
    height: 100vh;
    width: 100vw;
    background-image: url("/budgetBuddyLogin.jpg");
    background-size: cover;
    background-position: 30% center;
  }
  
  /* ... your existing styles ... */
  
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
    width: 95%;
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
    
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
  
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
  .error-border {
  border: 1px solid red;
}

.error-message {
  color: red;
  font-size: 14px;
  margin-top: 5px;
  display: block;
}


  </style>