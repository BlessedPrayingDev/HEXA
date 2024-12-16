<script>
    import { goto } from '$app/navigation';
    import { count, accessToken } from '../../store';
    import apiEx from '../../api/apiEx';
    import { onMount } from 'svelte';

    let userName = ""; // 사용자 이름을 저장할 변수
    
    // 페이지 이동 함수
    const navigateToRegister = () => goto('/register');
    const navigateToAllUsers = () => goto('/alluser');
    const navigateToHexaUsers = () => goto('/hexausers');
    const navigateToHexaOrders = () => goto('/hexaorders');
    const navigateToDockerImage = () => goto('/apidockercontainer');
    const navigateToHexaSessionUsers = () => goto('/hexasessionusers');

    const getUserInfo = async () => {
        const headers = {
            "Authorization": `Bearer ${$accessToken}`
        };
        const url = "/auths/userinfo/";

        try {
            const { data } = await apiEx.post(url, {}, { headers });
            console.log(data.data.username);
            userName = data.data.username; // 사용자 이름 업데이트
        } catch (error) {
            console.error("유저 정보 가져오기 실패", error);
        }
    };

    // 페이지가 로드되면 getUserInfo 함수를 실행하여 사용자 정보를 가져옴
    onMount(() => {
        getUserInfo();
    });
</script>

<svelte:head>
	<title>Main Page</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <div class="main-wrapper">
        <h1>Welcome to the Main Page</h1>
        <p>{userName ? `${userName}님이 로그인에 성공했습니다!` : '로그인에 성공했습니다! 아래 버튼들을 통해 테이블 정보를 볼 수 있습니다.'}</p>

        <!-- 헥사 등록된 유저로 이동하는 버튼 -->
        <!-- <button on:click={navigateToHexaUsers}>헥사 등록된 유저 보기</button> -->

        <!-- 헥사 세션 유저로 이동하는 버튼 -->
        <!-- <button on:click={navigateToHexaSessionUsers}>헥사 세션 유저 보기</button> -->

        <!-- 헥사 Order 테이블로 이동하는 버튼 -->
        <button on:click={navigateToHexaOrders}>헥사 Order 보기</button>

        <!-- 헥사 Order 테이블로 이동하는 버튼 -->
        <!-- <button on:click={navigateToDockerImage}>현재 실행 Docker 보기</button><br /> -->

        <!-- 회원가입 페이지로 이동하는 버튼 -->
        <!-- <button on:click={navigateToRegister}>회원가입</button> -->
 
        <!-- 유저 정보를 가져오는 페이지로 이동하는 버튼 -->
        <!-- <button on:click={navigateToAllUsers}>유저 정보 조회</button> -->

    </div>
</section>

<style>
    /* 스타일 */
    .main-wrapper {
        text-align: center;
        padding: 20px;
    }

    button {
        margin: 10px;
        padding: 10px 20px;
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
