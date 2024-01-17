<template>
  <div class=" w-full bg-white rounded-lg shadow dark:bg-gray-800 p-2 md:p-0">
    <a href="#">
      <div id="chart">
        <apexcharts width="550" height="200" type="line" :options="chartOptions" :series="series"></apexcharts>
      </div>
    </a>
  </div>
</template>

<script >
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
      chartOptions: {
        chart: {
          id: 'basic-bar'
        },
        xaxis: {
          categories: [], 
        },
      },
      series: [
        {
          name: 'Income',
          data: [], 
        }
      ],
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
          return new Date(transaction.transaction_date).getFullYear() === currentYear;
        });

        const groupedTransactions = this.groupByMonth(filteredTransactions);

        const categories = Object.keys(groupedTransactions);
        const incomeData = categories.map((month) => this.calculateTotal(groupedTransactions[month], 'Income'));
    
        this.chartOptions.xaxis.categories = categories;
        this.series[0].data = incomeData;
      } catch (error) {
        console.error('Error fetching transaction data:', error);
      }
    },
    groupByMonth(transactions) {
      return transactions.reduce((acc, transaction) => {
        const month = new Date(transaction.transaction_date).getMonth() + 1;
        const key = month.toString();

        if (!acc[key]) {
          acc[key] = [];
        }

        acc[key].push(transaction);

        return acc;
      }, {});
    },
    calculateTotal(transactions, type) {
      return transactions.reduce((total, transaction) => {
        return total + (transaction.transaction_type === type ? transaction.Amount : 0);
      }, 0);
    },
  },
};
</script>