
<script setup lang="ts">

</script>
<template>
    <div>
      <div class="background"></div>
      <div class="welcome-text">
        <h1>Join BudgetBuddy Today</h1>
        <p>Unlock the power of financial management</p>
      </div>
  
      <form method="post" action="/api/customers/register">
        <h3>Register Here</h3>
  
        <label for="username">Username</label>
        <input
          required
          type="text"
          placeholder="Username"
          id="username"
          name="username"
        />
  
        <label for="email">Email</label>
        <input
          required
          type="email"
          placeholder="Email"
          id="email"
          name="email"
        />
  
        <label for="password">Password</label>
        <input
          required
          type="password"
          placeholder="Password"
          id="password"
          name="password"
        />
  
        <label for="repassword">Re-enter Password</label>
        <input
          required
          type="password"
          placeholder="Re-enter Password"
          id="repassword"
          name="repassword"
        />
  
        <button @click="register">Register</button>
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
    margin-top: 50px;
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


  </style>