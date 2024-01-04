<script setup lang="ts">
    import {ref} from 'vue';
    import Setting from '../components/Setting.vue'
    import General from '../components/General.vue'
    import Account from '../components/Account.vue'
    import Form from '../components/Form.vue'

    const isFormVisible = ref(false);

    const receiveEmit = () => {
    isFormVisible.value = true;
    }

    const closeForm = () => {
    isFormVisible.value = false;
    }
</script>

<template>
    <section>
        <Setting/>
        <div class="screen"><General/></div>
        <!-- <div class="screen"><Account @add-account="receiveEmit"/></div>
        <Form v-if="isFormVisible" @close-modal="closeForm" /> -->
    </section>
</template>