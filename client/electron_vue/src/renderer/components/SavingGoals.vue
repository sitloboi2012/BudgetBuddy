<template>
    <div class="plan-income">
    <article class="plann" v-for="goal in allGoals" :key="goal">
        <button>
            <div class="flex space-between">
            <h1 class="flex-1" :style="{fontSize: '20px'}">{{ goal.goal_name }}</h1>
            <p class="flex-1" @click="clickEdit(goal)">:</p>
            <p class="flex-1" @click="clickDelete(goal.id)">d</p>
            </div>
            <h2 :style="{fontSize: '20px', paddingBottom: '20px'}">${{ goal.current_balance || 0}} saved so far</h2>
            <div class="details">    
                <div class="left-column">
                    <p>saved</p>
                    <p>left to save</p>
                </div>
                <div class="right-column">
                    <p :style="{textAlign: 'right'}">Goal: {{ goal.saving_amount }}</p>
                    <p :style="{textAlign: 'right'}">Expected by {{ goal.goal_end_date }}</p>
                </div>
            </div>
        </button>
    </article>
    <article class="addplan" @click="addGoal">
          <h1>+</h1>
    </article>
</div>
</template>

<script setup lang="ts">
    import { ref, defineEmits, onMounted } from 'vue';
    import axios from 'axios';
    
    const user_id = '6593ccdf025b256e0ffe24e8';
    const allGoals = ref([])
    let editData = ref(null)
    let deleteId = ref(null)

    
        const fetchGoals = async () => {
        try {
            const response = await axios.get(`http://localhost:8080/api/v1/goal_saving_setting/${user_id}`);
            allGoals.value = response.data;
            console.log('Monthly Expense Plans:', allGoals.value);
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
        };

        const emits = defineEmits(['add-goal','edit-goal']);

        const addGoal = () => {
        emits('add-goal');
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
button {
border: none;
width: 100%;
text-align: left;
padding-left: 13px ;
padding-top: 3px;
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
</style>