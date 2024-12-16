<script>
    import { goto } from '$app/navigation';
    import apiEx from '../../api/apiEx'
    import { accessToken, refreshToken, lastAccessTokenUpdate } from '../../store';

    let email = "";
    let password = "";

    let accessToken_temp; // 변수 선언 추가
    let refreshToken_temp;
    let lastAccessTokenUpdate_temp;

    const onLogin = async (event) => {
        event.preventDefault();

        const url = "/auths/login/";

        try {
            const { data } = await apiEx.post(url, { email, password });

            accessToken.set(data.access);
            refreshToken.set(data.refresh);
            lastAccessTokenUpdate.set(Date.now());

            accessToken_temp = data.access;
            refreshToken_temp = data.refresh;
            lastAccessTokenUpdate_temp = Date.now();

            console.log(accessToken_temp);
            console.log("refresh Token: ", {refreshToken_temp});
            console.log(lastAccessTokenUpdate_temp);

            userInfo();
            
            // goto("/mainpage")
        } catch (error) {
            console.error("로그인 실패", error);
        }
    }

    const userInfo = async () => {

        const headers = {
            "Authorization": `Bearer ${accessToken_temp}`
        }

        const url = "/auths/userinfo/";

        try {
            const { data } = await apiEx.post(url, {}, { headers }); // headers는 세 번째 인자로 전달

            console.log("User Info:", data);  // 전체 데이터를 출력
            console.log("Superuser status:", data.data.superuser); // superuser 값만 출력

            if (data.data.superuser) {
                console.log("This user is a superuser.");
                goto("/adminpage")
            } else {
                console.log("This user is not a superuser.");
                goto("/mainpage")
            }

        } catch (error) {
            console.error("유저 정보 가져오기 실패", error);
        }
    }
</script>

<svelte:head>
	<title>Log In</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <div class="login-wrapper">
        <h2>HEXA Server Manager Login</h2>
        <form id="login-form" on:submit={onLogin}>
            <input type="text" name="userName" placeholder="Email" bind:value={email}>
            <input type="password" name="userPassword" placeholder="Password" bind:value={password}>
            <!-- <label for="remember-check">
                <input type="checkbox" id="remember-check"> 아이디 저장하기
            </label> -->
            <input type="submit" value="Login">
        </form>
    </div>
</section>

<style>
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }

    section {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: linear-gradient(to bottom, #eef2f7, #d9e2ef);
    }

    .login-wrapper {
        width: 400px;
        padding: 40px;
        box-sizing: border-box;
        background: white;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        text-align: center;
    }

    .login-wrapper > h2 {
        font-size: 24px;
        color: #6A24FE;
        margin-bottom: 20px;
    }

    #login-form > input {
        width: 100%;
        height: 48px;
        padding: 0 10px;
        margin-bottom: 16px;
        border-radius: 6px;
        background-color: #F8F8F8;
        font-size: 16px;
    }

    #login-form > input::placeholder {
        color: #D2D2D2;
    }

    #login-form > input[type="submit"] {
        color: #fff;
        font-size: 16px;
        background-color: #6A24FE;
        margin-top: 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    #login-form > input[type="submit"]:hover {
        background-color: #8c52ff;
    }

    /* #login-form > input[type="checkbox"] {
        display: none;
    } */

    #login-form > label {
        color: #999999;
        font-size: 14px;
        display: inline-block;
        cursor: pointer;
        padding-left: 26px;
        background-image: url("checkbox.png");
        background-repeat: no-repeat;
        background-size: 16px;
        background-position: left center;
    }

    /* #remember-check:checked + label {
        background-image: url("checkbox-active.png");
    } */
</style>