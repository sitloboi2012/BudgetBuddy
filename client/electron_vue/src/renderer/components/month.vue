<template>
    <p class="text-white">{{ date.month }} {{ date.year }}</p>
    <month-picker-input class="form" :no-default="true" @change="showDate"></month-picker-input>
  </template>
  
  <script>
  import { MonthPickerInput } from 'vue-month-picker'
  
  export default {
    data() {
    return {
     date: {
      from: null,
      to: null,
      month: 1,
      year: 2024
     }
    }
   },
   components: {
    MonthPickerInput
   },
   methods: {
    showDate (date) {
     this.date = date
     this.$emit('send-month', this.date.month);
     this.$emit('send-year', this.date.year);
    }
   }
  }
  </script>
<style scoped>
.form{
    position: relative;
    z-index: 999;
}
</style>