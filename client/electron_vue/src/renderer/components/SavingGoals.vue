<template>
    <div class="plan-income">
    <article class="plann" v-for="goal in allGoals" :key="goal">
       <div class="p-4">
            <div class="flex space-between ">
            <h1 class="flex-1 text-lg font-bold text-left" >{{ goal.goal_name }}</h1>
            <div>
            <Button class="flex-1 bg-indigo-800 text-white me-4" @click="clickEdit(goal)">Edit</Button>
            <Button class="flex-1  bg-orange-800 text-white " @click="clickDelete(goal.id)">Del</Button></div>  
            </div>
            <h2 :style="{fontSize: '12px',paddingTop:'20px', paddingBottom: '5px', color:'grey'}">${{ goal.current_balance || 0}} saved so far</h2>
            <fwb-progress
                  :progress="roundedProgress(goal.current_balance, goal.saving_amount)"
                  label-position="inside"
                  label-progress
                  size="xl"
                  class="chart" 
                  color="indigo"
                />
            <div class="details">    
                <div class="left-column">
                    
                </div>
                <div class="right-column pt-2">
                    <p class="text-sm" :style="{textAlign: 'right'}"> <strong>Goal:</strong>$ {{ goal.saving_amount }}</p>
                    <p class="text-sm" :style="{textAlign: 'right'}"><strong>Expected by </strong><i>{{ goal.goal_end_date }}</i> </p>
                </div>
            </div>
        </div>
    </article>
    <article class="addplan cursor-pointer" @click="addGoal">
          <h1>+</h1>
    </article>
</div>
</template>

<script setup lang="ts">
    import { ref, defineEmits, onMounted } from 'vue';
    import { FwbProgress } from 'flowbite-vue'
    import axios from 'axios';
    import {Button} from '../../@/components/ui/button';
    
    const user_id = localStorage.getItem('userId') ?? '';
    const allGoals = ref([])
    let editData = ref(null)
    let deleteId = ref(null)

    
        const fetchGoals = async () => {
        try {
            const response = await axios.get(`http://localhost:8080/api/v1/goal_saving_setting/${user_id}`);
            allGoals.value = response.data;
            console.log('Monthly Expense Plans:', allGoals.value);
            const totalGoal = allGoals.value.reduce((sum, goal) => sum + goal.saving_amount, 0);
            console.log("Total Goal:", totalGoal);
            emits('send-total-goal',totalGoal)
        } catch (error) {
            console.error('Error fetching monthly expense plans:', error);
        }
        };

        const Delete = async (deleteId) => {
            try {
                const response = await axios.delete(`http://localhost:8080/api/v1/goal_saving_setting/${user_id}/${deleteId}/delete`);
                console.log('Delete this ID', response.data);
                await fetchGoals();
            } catch (error) {
                console.error('Error deleting entry:', error);
            }
        };

        onMounted(() => {
        fetchGoals();
        });
        const clickEdit = (itemEdit: any) => {
            editData = itemEdit,
            
            emits("edit-goal", editData);
            console.log("edit-goal:",editData)
         
        }
        const clickDelete = (itemDelete: any) => {
        deleteId = itemDelete;
        Delete(deleteId);
        fetchGoals();
        };

        const emits = defineEmits(['add-goal','edit-goal', 'send-total-goal']);

        const addGoal = () => {
        emits('add-goal');
        };
        const roundedProgress = (currentTotalUse, initialAmount) => {
        return Math.ceil((currentTotalUse / initialAmount) * 100);
        };
</script>

<style scoped>
.plan-income {
position: absolute;
top: 20px;
left: 20px;
width: 93%;
display: flex;
flex-wrap: wrap;
}

.plann {
background-color: lavender;
border-radius: 10px;
padding: 10px;
width: 48%;
float: left;
margin: 7px auto;
}

.addplan {
    background-color: rgb(145, 145, 175);
    border-radius: 10px;
    padding: 10px;
    width: 48%;
    height: 150px;
    float: left;
    margin: 7px auto;
}

.details {
  display: flex;
  justify-content: space-between;
}

.left-column,
.right-column {
  flex: 1;
}

.left-column p,
.right-column p {
  margin: 0;
}
.chart{
        border: 1px solid #ddd;
        width:90%;
        background-color: white;
    }
</style>