<script>
    import { goto } from '$app/navigation';
    import apiEx from '../../api/apiEx'
    import { count, accessToken } from '../../store';

    const navigateToAdminPage = () => {
        goto('/adminpage');
    };

    let email = '';
    let username = '';
    let password = '';
    let phone = '';
    let gender = '';
    let nickname = '';

    const onRegister = async (event) => {

        event.preventDefault();

        // Authorization 헤더 설정
        const headers = {
            "Authorization": `Bearer ${$accessToken}`
        }

        console.log('email:', email);
        console.log('username:', username);
        console.log('password:', password);
        console.log('phone:', phone);
        console.log('gender:', gender);
        console.log('nickname:', nickname);

        const url = "/auths/register/";

        try {
            const res = await apiEx.post(
                url,
                { email, password, username, phone, gender, nickname },
                { headers } // 헤더는 세 번째 인자로 전달
            );

            console.log('회원가입 응답:', res);

            goto("/mainpage")

        } catch (error) {
            console.error('회원가입 오류:', error);
            // 에러 처리 로직 (예: 에러 메시지 표시)
        }
    }
</script>

<section>
    <h1>Register</h1>

    <form on:submit={onRegister}>
        <input placeholder="Email" type="email" bind:value={email} /><br />
        <input placeholder="Username" type="text" bind:value={username} /><br />
        <input placeholder="Password" type="password" bind:value={password} /><br />
        <input placeholder="Phone" type="text" bind:value={phone} /><br />
        <input placeholder="Gender" type="text" bind:value={gender} /><br />
        <input placeholder="Nickname" type="text" bind:value={nickname} /><br />
        <input type="submit" value="Register" /><br />
    </form>

    <button on:click={navigateToAdminPage}>메인 페이지</button>
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
    input[type="email"],
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

    button {
        padding: 10px 20px;
        margin-top: 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
        background-color: #6A24FE;
        color: #fff;
        border: none;
    }

    button:hover {
        background-color: #8c52ff;
    }
</style>