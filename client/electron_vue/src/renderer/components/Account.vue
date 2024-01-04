<template>
    <div class="head1">
        <h1 class="inline-block text-white text-xl">Accounts</h1>
        <button class="inline-block text-white font-bold text-xs bg-blue-600 p-2 rounded-2xl" @click="addAccount">+ ACCOUNT</button>
    </div>
    <div v-for="account in allAccounts" :key="account" class="container">
        <h1>{{ account[2] }}</h1>
        <h1>{{ account[1] }}</h1>
        <div class="inner-content">
            <div class="left-content">
                <h5>{{ account[0] }}</h5>
                <p>{{ account[0] }}</p>
            </div>
            <div class="right-content">
                <button>:</button>
            </div>
        </div>
    </div>

</template>
<script setup lang="ts">
    import { ref, defineEmits, onMounted, computed } from 'vue';
    import axios from 'axios';

    const user_id = '657deedb53a90ee98e224654';
    const allAccounts = ref([]);

    const fetchAccount = async () => {
    try {
        const response = await axios.get(`http://localhost:8080/api/v1/${user_id}`);
        allAccounts.value = response.data.list_account_name;
        console.log('Server response:', response.data.list_account_name
);
    } catch (error) {
        console.error('Error fetching account information:', error);
    }
    };

    onMounted(() => {
    fetchAccount();
    });

    const emits = defineEmits(['add-account']);

    const addAccount = () => {
    emits('add-account');
    };
</script>
<style scoped>
    .head1{
        padding-top: 20px;
        padding-left: 30px;
        display: flex;
        justify-content: space-between;
        width: 95%;
    }
    .container{
    background-color: white;
    }

    .inner-content {
    display: flex;
    background-color: gainsboro;
    justify-content: space-between;
    margin: 20px; /* Adjust the margin as needed */
    }

    .left-content {
    margin-right: 20px; /* Adjust the margin as needed */
    }

    .right-content {
    display: flex;
    padding-right: 20px;
    }
</style>