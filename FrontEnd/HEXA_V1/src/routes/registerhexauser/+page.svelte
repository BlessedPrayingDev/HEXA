<script>
    import { goto } from '$app/navigation';
    import apiEx from '../../api/apiEx'
    import { count, accessToken } from '../../store';

    let user = '';
    let password = '';
    let level = '';
    let serial_number = '';
    let expired_date = '';

    const onRegister = async (event) => {

        event.preventDefault();

        // Authorization 헤더 설정
        const headers = {
            "Authorization": `Bearer ${$accessToken}`
        }

        console.log('user:', user);
        console.log('password:', password);
        console.log('level:', level);
        console.log('serial_number:', serial_number);
        console.log('expired_date:', expired_date);

        const url = "/dashboard/registerhexauser/";

        try {
            const res = await apiEx.post(
                url,
                { user, password, level, serial_number, expired_date },
                { headers } // 헤더는 세 번째 인자로 전달
            );

            console.log('회원가입 응답:', res);

            goto("/hexausers")

        } catch (error) {
            console.error('회원가입 오류:', error);
            // 에러 처리 로직 (예: 에러 메시지 표시)
        }
    }
</script>

<section>
    <h1>Register</h1>

    <form on:submit={onRegister}>
        <input placeholder="User" type="text" bind:value={user} /><br />
        <input placeholder="Password" type="password" bind:value={password} /><br />
        <input placeholder="Level" type="text" bind:value={level} /><br />
        <input placeholder="Serial Number" type="text" bind:value={serial_number} /><br />
        <input placeholder="Expired Date" type="text" bind:value={expired_date} /><br />
        <input type="submit" value="Register" /><br />
    </form>
</section>

<style>
    section {
        text-align: center;
    }

    form {
        width: 80%;
        margin: 20px auto;
    }

    input[type="text"],
    input[type="password"],
    input[type="submit"] {
        width: 60%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
    }

    input[type="submit"] {
        background-color: #6A24FE;
        color: #fff;
        cursor: pointer;
        border: none;
    }

    input[type="submit"]:hover {
        background-color: #8c52ff;
    }

    h1 {
        color: #6A24FE;
    }
</style>