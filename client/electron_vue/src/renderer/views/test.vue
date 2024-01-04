<template>
  <div>
    <month-picker-input
      :no-default="true"
      @input="handleMonthChange"
      :lang="language"
      :months="customMonths"
    ></month-picker-input>

    <p class="text-white">Month chosen: {{ selectedMonth }}</p>
  </div>
</template>

<script>
import { MonthPickerInput } from 'vue-month-picker';

export default {
  components: {
    MonthPickerInput,
  },
  data() {
    return {
      selectedMonth: null,
      language: 'en', // Change this to your preferred language code
      customMonths: [], // You can provide your own array of custom month names
    };
  },
  methods: {
    handleMonthChange(date) {
      // Handle the month change event
      this.selectedMonth = this.formatDate(date);
    },
    formatDate(date) {
      // Format the date as per your requirement
      const monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December',
      ];

      const monthIndex = date.getMonth();
      const year = date.getFullYear();

      return `${monthNames[monthIndex]} ${year}`;
    },
  },
};
</script>

