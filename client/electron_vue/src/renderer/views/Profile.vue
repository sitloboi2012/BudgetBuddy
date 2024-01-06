<script setup lang="ts">
    import {ref} from 'vue';
    import Setting from '../components/Setting.vue'
    import General from '../components/General.vue'
    import Account from '../components/Account.vue'
    import Form from '../components/Form.vue'
    import EditAcc from '../components/EditAcc.vue'

    const isFormVisible = ref(false);
    const isFormVisible2 = ref(false);
    let newdata = ref(null)

    const receiveEmit = () => {
    isFormVisible.value = true;
    }
    const collectaccount = (event) => {
    newdata = event
    console.log("see1", newdata)
    isFormVisible2.value = true;
    }
    const closeForm = () => {
    isFormVisible.value = false;
    }
    const closeForm2 = () => {
    isFormVisible2.value = false;
    }
</script>

<template>
    <section>
        <Setting/>
        <!-- <div class="screen"><General/></div> -->
        <div class="screen"><Account @add-account="receiveEmit" @edit-account="collectaccount($event)"/></div>
        <Form class="form" v-if="isFormVisible" @close-modal="closeForm" />
    </section>
    <EditAcc class="form" v-if="isFormVisible2" @close-modal="closeForm2" :data="newdata"/>
</template>
<style scoped>
.form{
  position: relative;
  z-index: 999;
}

</style>