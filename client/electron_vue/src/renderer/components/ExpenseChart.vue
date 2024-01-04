<template>
    <div>
      <apexchart width="380" type="donut" :options="options" :series="series"></apexchart>
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
      options: {},
      series: [30, 40, 45, 50]
    }
  },
}
</script>