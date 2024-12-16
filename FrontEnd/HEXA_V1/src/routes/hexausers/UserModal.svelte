<script>
    import { createEventDispatcher } from 'svelte';
    
    // 선택된 유저 데이터를 props로 받아온다
    export let user = {};

    const dispatch = createEventDispatcher();

    const closeModal = () => {
        dispatch('close');
    };

    const saveChanges = () => {
        // 유저 정보 수정 후 저장
        dispatch('save', user);
    };

    const deleteUser = () => {
        dispatch('delete', user);
    };
</script>

<div class="modal">
    <div class="modal-content">
        <span class="close" on:click={closeModal}>&times;</span>
        <h2>유저 정보 수정</h2>
        
        <!-- 유저 정보 필드들 -->
        <div>
            <label>User:</label>
            <input type="text" bind:value={user.user}/> <!-- 수정 불가능하도록 readonly 설정 -->
        </div>
        
        <div>
            <label>Level:</label>
            <input type="number" bind:value={user.level} />
        </div>
        
        <div>
            <label>Password:</label>
            <input type="text" bind:value={user.password} />
        </div>
        
        <div>
            <label>Serial Number:</label>
            <input type="text" bind:value={user.serial_number} />
        </div>
        
        <!-- <div>
            <label>Expired Date:</label>
            <input type="date" bind:value={user.expired_date} />
        </div> -->
        
        <!-- 저장 및 삭제 버튼 -->
        <button on:click={saveChanges}>저장</button>
        <button on:click={deleteUser}>삭제</button>
    </div>
</div>

<style>
    .modal {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
    }

    .modal-content {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        width: 400px;
    }

    .close {
        float: right;
        cursor: pointer;
        font-size: 1.2em;
    }

    h2 {
        text-align: center;
    }

    div {
        margin-bottom: 15px;
    }

    label {
        display: block;
        font-weight: bold;
        margin-bottom: 5px;
    }

    input {
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
        font-size: 1em;
    }

    button {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
        font-size: 1em;
        cursor: pointer;
        border: none;
        border-radius: 5px;
    }

    button:nth-of-type(1) {
        background-color: #4CAF50;
        color: white;
    }

    button:nth-of-type(2) {
        background-color: #f44336;
        color: white;
    }

    button:hover {
        opacity: 0.9;
    }
</style>
