<template>
    <div class="plan-income">
    <article class="plann" v-for="goal in allGoals" :key="goal">
        <button>
            <h1 :style="{fontSize: '20px'}">{{ goal.goal_name }}</h1>
            <p :style="{fontSize: '13px', paddingBottom: '20px'}">{{ goal.account }}</p>
            <h2 :style="{fontSize: '20px', paddingBottom: '20px'}">$2356 saved so far</h2>
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
    
    const user_id = '657deedb53a90ee98e224654';
    const allGoals = ref([])
    

    
        const fetchGoals = async () => {
        try {
            const response = await axios.get(`http://localhost:8080/api/v1/goal_saving_setting/${user_id}`);
            allGoals.value = response.data;
            console.log('Monthly Expense Plans:', allGoals.value);
        } catch (error) {
            console.error('Error fetching monthly expense plans:', error);
        }
        };

        onMounted(() => {
        fetchGoals();
        });

        const emits = defineEmits(['add-goal']);

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