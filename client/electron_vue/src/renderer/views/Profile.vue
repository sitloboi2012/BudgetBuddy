<script setup lang="ts">
    import {ref, Ref} from 'vue';
    import General from '../components/General.vue'
    import Account from '../components/Account.vue'
    import Form from '../components/Form.vue'
    import EditAcc from '../components/EditAcc.vue'
    import EditPro from '../components/EditProfile.vue'

    const isFormVisible = ref(false);
    const isFormVisible2 = ref(false);
    const isFormVisible3 = ref(false);
    let newdata = ref(null)
    let selectedComponent: Ref<string> = ref('Personal Information');

    const receiveEmit = () => {
    isFormVisible.value = true;
    }
    const collectinfo = (event) => {
    newdata = event
    console.log("seeinfo", newdata)
    isFormVisible3.value = true;
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
    const closeForm3 = () => {
    isFormVisible3.value = false;
    }
    const showComponent = (componentName: string) => {
    selectedComponent.value = componentName;
  };
</script>

<template>
    <EditAcc class="form" v-if="isFormVisible2" @close-modal="closeForm2" :data="newdata"/>
    <EditPro class="form" v-if="isFormVisible3" @close-modal="closeForm3" :data="newdata"/>
    <Form class="form" v-if="isFormVisible" @close-modal="closeForm" />
    <section class="planning">
      <div class="networth">
        <div class="overview-section bg-blue-600" @click="showComponent('Personal Information')" >
          <p class="text-l text-white font-bold">Personal Information</p>
        </div>
        <div class="overview-section bg-amber-500" @click="showComponent('Manage Account')">
          <p class="text-l text-white font-bold">Manage Account</p>
        </div>
      </div>
        <div class="screen">
            <General v-if="selectedComponent === 'Personal Information'" @edit-info="collectinfo($event)"/>
            <Account v-if="selectedComponent === 'Manage Account'" @add-account="receiveEmit" @edit-account="collectaccount($event)"/>
        </div>
    </section>
</template>
<style scoped>
.form{
  position: relative;
  z-index: 999;
}
.overview-section {
    padding: 20px;
    border-radius: 20px;
    margin: 10px;
  }

</style>