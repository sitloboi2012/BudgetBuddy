import type { ColumnDef } from '@tanstack/vue-table'
import { ArrowUpDown, ChevronDown } from 'lucide-vue-next'
import { Button } from '../../../@/components/ui/button'
import DropdownAction from './DataTableDropDown.vue'
import { h } from 'vue'
// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export interface Payment {
    id: string
  amount: number
  status: 'pending' | 'processing' | 'success' | 'failed'
  email: string
}

export const payments: Payment[] = [
  {
    id: '728ed52f',
    amount: 100,
    status: 'pending',
    transactionName: 'm@example.com',
  },
  {
    id: '489e1d42',
    amount: 125,
    status: 'processing',
    transactionName: 'example@gmail.com',
  },
]


export const columns: ColumnDef<Payment>[] = [
    {
        accessorKey: 'account',
        header: 'Account',
      },
    
      {
        accessorKey: 'date',
        header: ({ column }) => {
          return h(Button, {
              variant: 'ghost',
              onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
              class: 'flex items-center w-max',
          }, () => ['Date', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
      },
      },
      {
        accessorKey: 'payee',
        header: 'Payee',
      },
      {
        accessorKey: 'categories',
        header: 'Categories',
      },
      {
        accessorKey: 'transactionName',
        header: 'Transaction Name',
      },
   
    {
        accessorKey: "amount",
        header: ({ column }) => {
          return h(Button, {
              variant: 'ghost',
              onClick: () => column.toggleSorting(column.getIsSorted() === 'asc'),
              class: 'flex items-center w-max',
          }, () => ['Amount', h(ArrowUpDown, { class: 'ml-2 h-4 w-4' })])
      },
      

        cell: ({ row }) => {
            const amount = parseFloat(row.getValue("amount"))
            const formatted = new Intl.NumberFormat("en-US", {
                style: "currency",
                currency: "USD",
            }).format(amount)

            return h('div', { class: 'text-right font-medium' }, formatted)
        },

    },
    {
        id: 'actions',
        enableHiding: false,
        cell: ({ row }) => {
            const payment = row.original

            return h('div', { class: 'relative' }, h(DropdownAction, {
                payment,
            }))
        },
    },
]