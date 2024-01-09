// DataTableDropDown.vue
<script setup lang="ts">
import { MoreHorizontal } from 'lucide-vue-next'
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger } from '../../../@/components/ui/dropdown-menu'
import { Button } from '../../../@/components/ui/button'

defineProps<{
  payment: {
    id: string,
    amount: number,
    account: string,
    transactionName: string,
    date: string,
    payee: string,
    categories: string,
type: string;
  }
}>()

function copy( account: string, amount: number, transactionName: string, date: string, payee: string, categories: string, type: string) {
  navigator.clipboard.writeText(`Account: ${account}, Amount: ${amount}, Transaction name:  ${transactionName}, Date: ${date}, Payee: ${payee}, Category: ${categories}`);

}
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button variant="ghost" class="w-8 h-8 p-0">
        <span class="sr-only">Open menu</span>
        <MoreHorizontal class="w-4 h-4" />
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end">
      <DropdownMenuLabel>Actions</DropdownMenuLabel>
      <DropdownMenuItem @click="() => copy( payment.account, payment.amount, payment.transactionName, payment.date, payment.payee, payment.categories, payment.type)">
        Copy transaction Detail
      </DropdownMenuItem>
      <DropdownMenuSeparator />
     
      <DropdownMenuItem>Delete Transaction</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>