<template>
    <div class='store'>
     <div class="profile1">
        <img src="../assets/img1.png" alt="">
        <h1>Diệp Thiện Ngôn</h1>
        <button>Thay đổi thông tin</button>
    </div>
    <div class="profile2">
        <div class="info name">
            <h2>Name</h2>
            <p>Diệp Thiện Ngôn</p>
        </div>
        <div class="info number">
            <h2>Số điện thoại</h2>
            <p>0878623892</p>
        </div>
        <div class="info dc">
            <h2>Address</h2>
            <p>fjsdhjf</p>
        </div>
        <div class="info email">
            <h2>Email</h2>
            <p>dsfb</p>
        </div>
    </div>
    </div>
</template>
<style scoped>
    .store{
            margin: auto;
            padding: 20px;
            display: flex;
            align-items: center;
            text-align: center;

}

.profile1 {
            width: 30%;
            height: 245px;
            align-items: center;
            justify-content: center;
        }

        .profile1 img {
            width: 100px;
            height: 100px;
        }

        .profile2 {
            width: 70%;
            padding: 0 20px;
        }

        h2 {
            font-size: 20px;
            margin-bottom: 5px;
            color: #333;
        }

        p {
            font-size: 16px;
            color: #555;
            margin-bottom: 10px;
        }

        .info {
            width: 100%;
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            height: 50px;
        }
        button{
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            cursor: pointer;
            width: 70%;
            font-size: 16px;
        }
</style>