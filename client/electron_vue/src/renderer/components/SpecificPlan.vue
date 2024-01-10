<template>
    <p @click="clickBack()" class="return">&lt;</p>
    <h1 class="title">{{ categories }}</h1>
    <p class="thismonth">THIS MONTH</p>
    <p class="amount">{{ initial - current_amount }} left</p>
    <p class="another">{{ current_amount }} spent</p>
    <fwb-progress
                  :progress="roundedProgress(current_amount,initial)"
                  label-position="inside"
                  label-progress
                  size="xl"
                  class="chart"
                />
    <div class="aanother flex space-between">
        <p class="flex-1">{{ list.length }} transaction</p>
        <p class="flex-1">of {{ initial }}</p>
    </div>

    <h1 class="trans">Related Transaction</h1>
    <fwb-table hoverable>
        <fwb-table-head>
            <fwb-table-head-cell>Transaction name</fwb-table-head-cell>
            <fwb-table-head-cell>Date</fwb-table-head-cell>
            <fwb-table-head-cell>Category</fwb-table-head-cell>
            <fwb-table-head-cell>Amount</fwb-table-head-cell>
        </fwb-table-head>
        <fwb-table-body>
            <fwb-table-row v-for="transaction in list" :key="transaction.transaction_id">
                <fwb-table-cell>{{transaction.transaction_name}}</fwb-table-cell>
                <fwb-table-cell>{{transaction.transaction_date}}</fwb-table-cell>
                <fwb-table-cell>{{ categories }}</fwb-table-cell>
                <fwb-table-cell>{{transaction.Amount}}</fwb-table-cell>
            </fwb-table-row>
        </fwb-table-body>
    </fwb-table>
</template>
<script setup lang="ts">
import { ref, defineEmits, onMounted, computed, toRefs } from 'vue';
import { FwbProgress, FwbA, FwbTable, FwbTableBody, FwbTableCell, FwbTableHead, FwbTableHeadCell, FwbTableRow, } from 'flowbite-vue' 

let { data } = defineProps(['data']);
let { category, current_total_use, id, initial_amount, list_transaction } = toRefs(data);
let categories = ref(category.value);
let current_amount = ref(current_total_use.value);
let initial = ref(initial_amount.value);
let list = ref(list_transaction.value);


console.log("test list", list)

const clickBack = () => {
  emits("go-back");
}
const emits = defineEmits(['go-back']);

const roundedProgress = (currentTotalUse, initialAmount) => {
  return Math.ceil((currentTotalUse / initialAmount) * 100 +1);
};

</script>
<style scoped>
    .return{
        position:fixed;
        margin-left: 30px;
        margin-top: 9px;
        font-weight: 600;
        font-size: 20px;
        cursor: pointer;
        color:rgba(0, 0, 0, 0.888);
    }
    .title{
        position:fixed;
        margin-left: 50px;
        margin-top: 14px;
        font-weight: 600;
        font-size: 20px;
        color:rgba(59, 59, 247, 0.888);
    }
    .thismonth{
        font-size: 14px;
        position:fixed;
        margin-left: 55px;
        margin-top: 60px;
        font-weight: 600;
    }
    .amount{
        position:relative; 
        margin-top: 110px;
        font-size: 24px;
        color: rgba(59, 59, 247, 0.888);
        font-weight: 600;
    }
    .another{
        padding-top: 20px;
        position:relative;
        margin-right: 330px;
        font-size: 14px;
        color: rgb(171, 170, 170)
    }
    .chart{
        margin-left: 80px;
        border: 1px solid #ffffff;
        width:370px;
        border-radius: 20px;
        background-color: white;
    }
    .aanother{
        margin-right: 37px;
        font-size: 14px;
        font-size: 14px;
        color: rgb(171, 170, 170)
    }
    .trans{
        padding: 90px 0px 30px 0px;
        font-weight: 600;
        font-size: 17px;
        color:rgba(59, 59, 247, 0.888);
    }
    .fwb-table {
        width: 100%; 
    }
</style>