<template>
  <div id="chart">
    <apexchart type="pie" width="380" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';
import axios from 'axios';

const user_id = localStorage.getItem('userId') ?? '';

export default {
  name: 'Chart',
  components: {
    apexcharts: VueApexCharts,
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          width: 380,
          type: 'pie',
        },
        labels: ['Entertainment','Personal','Transportation','Food & Dining','Health & Fitness'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200,
            },
            legend: {
              position: 'bottom',
            },
          },
        }],
      },
    };
  },
  async mounted() {
    await this.fetchTransactionData();
  },
  methods: {
    async fetchTransactionData() {
      try {
        const response = await axios.get(`http://localhost:8080/api/v1/transaction/${user_id}`);
        const transactions = response.data;

        const currentYear = new Date().getFullYear();

        const filteredTransactions = transactions.filter((transaction) => {
          const transactionDate = new Date(transaction.transaction_date);
          return (
            transactionDate.getFullYear() === currentYear &&
            transaction.transaction_type === 'Outcome'
          );
        });

        const groupedTransactions = this.groupByCategory(filteredTransactions);

        this.chartOptions.labels = Object.keys(groupedTransactions);
        console.log('Chart Labels:', this.chartOptions.labels);
        this.series = Object.values(groupedTransactions);
      } catch (error) {
        console.error('Error fetching transaction data:', error);
      }
    },
    groupByCategory(transactions) {
      return transactions.reduce((acc, transaction) => {
        const category = transaction.category;

        if (!acc[category]) {
          acc[category] = 0;
        }

        acc[category] += transaction.Amount;

        return acc;
      }, {});
    },
  },
};
</script>