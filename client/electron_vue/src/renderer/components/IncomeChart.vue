<template>
    <div class="max-w-xs w-full bg-white rounded-lg shadow dark:bg-gray-800 p-2 md:p-0">
                <a href="#">
                    <div id="chart">
                      <apexcharts width="300" height="200" type="line" :options="chartOptions" :series="series"></apexcharts>
                    </div>
                </a>
    </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts'

export default {
  name: 'Chart',
  components: {
    apexcharts: VueApexCharts,
  },
  data: function() {
    return {
      chartOptions: {
        chart: {
          id: 'basic-bar'
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", "Jul", 'Aug', 'Sep', 'Otc', 'Nov', "Dec"]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91, 19, 20, 67, 30]
      }]
    }
  },
}
</script>