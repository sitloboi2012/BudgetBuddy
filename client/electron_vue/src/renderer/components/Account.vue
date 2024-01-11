<template>
    <div class="head1">
        <h1 class="inline-block text-black text-xl">Accounts</h1>
        <button class="inline-block text-white font-bold text-xs bg-blue-600 p-2 rounded-2xl" @click="addAccount">+ ACCOUNT</button>
    </div>
    <div v-for="account in allAccounts" :key="account" class="container mt-8 m-4 p-1">
        <div class="flex space-between">
            <h1 class="flex-1 acc_name">{{ account[0] }}</h1>
            <h1 class="flex-1 font-bold edit_butt" @click="clickEdit(account)">...</h1>
        </div>
        <div class="inner-content">
            <div class="left-content">
                <h5>{{ account[4] }}</h5>
                <h5>{{ account[3] }}</h5>
            </div>
        </div>
    </div>

</template>
<script setup lang="ts">
    import { ref, defineEmits, onMounted, computed } from 'vue';
    import axios from 'axios';

    const user_id = localStorage.getItem('userId') ?? '';
    const allAccounts = ref([]);
    let editData = ref(null)

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
    const clickEdit = (itemEdit: any) => {
            editData = itemEdit,
            emits("edit-account", editData);
            console.log("edit-account:",editData)
    }

    onMounted(() => {
    fetchAccount();
    });

    const emits = defineEmits(['add-account', 'edit-account']);

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
    .acc_name{
        text-align: left;
        margin-left: 20px;
        padding-top: 10px;
        font-weight: 500;
    }
    .edit_butt{
        text-align: right;
        margin-right: 20px;
        padding-top: 10px;
        font-weight: 500;
    }
    .container{
    background-color: rgb(193, 184, 236);
    border-radius: 20px;
    width: 95%;
    }

    .inner-content {
    text-align: left;
    background-color: rgb(255, 255, 255);
    border-radius: 10px;
    justify-content: space-between;
    margin: 20px; /* Adjust the margin as needed */
    }

    .left-content {
    margin-left: 20px; /* Adjust the margin as needed */
    }

    .right-content {
    display: flex;
    padding-right: 20px;
    }
</style>