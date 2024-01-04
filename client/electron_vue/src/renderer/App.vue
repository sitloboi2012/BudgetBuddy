<script setup lang="ts">
import '@syncfusion/ej2-base/styles/material.css'
import '@syncfusion/ej2-buttons/styles/material.css'
import '@syncfusion/ej2-calendars/styles/material.css'
import '@syncfusion/ej2-dropdowns/styles/material.css'
import '@syncfusion/ej2-inputs/styles/material.css'
import '@syncfusion/ej2-navigations/styles/material.css'
import '@syncfusion/ej2-popups/styles/material.css'
import '@syncfusion/ej2-splitbuttons/styles/material.css'
import '@syncfusion/ej2-vue-grids/styles/material.css'
import { GridComponent as EjsGrid, ColumnsDirective as EColumns, ColumnDirective as EColumn } from '@syncfusion/ej2-vue-grids';
</script>

<template>
  <router-view/>
  <router-link to="/home">Overview</router-link>
  <router-link to="/transaction">Transaction</router-link>
  <router-link to="/plan">Plan</router-link>
  <router-link to="/report">Report</router-link>
  <router-link to="/profile">Profile</router-link>
</template>



