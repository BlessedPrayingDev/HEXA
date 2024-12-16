<script>
    import { goto } from '$app/navigation';
    import { count, accessToken, refreshToken } from '../../store';
    import { onMount, onDestroy } from 'svelte';
    import apiEx from '../../api/apiEx';

    let userName = "";
    let users = [];
    let dockerImages = [];
    let interval;
    
    // Navigation functions
    const navigateToRegister = () => goto('/register');
    const navigateToAllUsers = () => goto('/alluser');
    const navigateToHexaUsers = () => goto('/hexausers');
    const navigateToHexaOrders = () => goto('/hexaorders');

    // API functions
    const getUserInfo = async () => {
        const headers = { "Authorization": `Bearer ${$accessToken}` };
        const url = "/auths/userinfo/";

        try {
            const { data } = await apiEx.post(url, {}, { headers });
            userName = data.data.username;
        } catch (error) {
            console.error("Failed to retrieve user info", error);
            alert("로그인 세션이 만료되었습니다. 로그인 페이지로 이동합니다."); // Alert 창 추가
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    };

    const fetchHexaSessionUsers = async () => {
        const headers = { "Authorization": `Bearer ${$accessToken}` };
        const url = "/dashboard/hexasessionuser/";

        try {
            const { data } = await apiEx.get(url, { headers });
            users = data;
        } catch (error) {
            console.error("Error fetching session users: ", error);
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    };

    const fetchDockerImages = async () => {
        const headers = { "Authorization": `Bearer ${$accessToken}` };
        const url = "/dashboard/apidockercontainer/";

        try {
            const { data } = await apiEx.get(url, { headers });
            dockerImages = data.containers;
        } catch (error) {
            console.error("Error fetching Docker images: ", error);
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    };

    // Function to fetch data
    const fetchData = () => {
        getUserInfo();
        fetchHexaSessionUsers();
        fetchDockerImages();
    };

    // Set up interval on mount and clean up on destroy
    onMount(() => {
        fetchData(); // Initial fetch
        interval = setInterval(fetchData, 60000); // 1 minute interval (60000 ms)

        // Clear interval on destroy
        // onDestroy(() => clearInterval(interval));
    });

    // Clear interval on destroy
    onDestroy(() => {
        clearInterval(interval);
    });
</script>

<svelte:head>
    <title>Admin Page</title>
    <meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <div class="main-wrapper">
        <h1>HEXA SERVER MANAGER</h1>
        <h2>{userName ? `${userName} 님이 로그인중입니다.` : '로그인을 실패하였습니다 아래 버튼들을 통해 테이블 정보를 볼 수 있습니다.'}</h2>

        <!-- Navigation buttons -->
        <div class="button-group">
            <button on:click={navigateToHexaUsers}>헥사 등록된 유저 보기</button>
            <button on:click={navigateToHexaOrders}>헥사 Order 보기</button>
            <!-- <button on:click={navigateToRegister}>회원가입</button>
            <button on:click={navigateToAllUsers}>유저 정보 조회</button> -->
        </div>

        <!-- Tables section -->
        <div class="table-container">
            <!-- Hexa Session Users Table (Left) -->
            <div class="table-section">
                <h2>헥사 세션 유저 보기</h2>
                {#if users.length > 0}
                    <table>
                        <thead>
                            <tr>
                                <th>Peer</th>
                                <th>User Name</th>
                                <th>Session Time</th>
                                <th>Duplicated</th>
                            </tr>
                        </thead>
                        <tbody>
                            {#each users as user}
                                <tr>
                                    <td>{user.peer}</td>
                                    <td>{user.user_name}</td>
                                    <td>{user.session_time}</td>
                                    <td>{user.duplicated}</td>
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                {:else}
                    <p>No session user data available.</p>
                {/if}
            </div>

            <!-- Docker Images Table (Right) -->
            <div class="table-section">
                <h2>현재 실행 Docker 보기</h2>
                {#if dockerImages.length > 0}
                    <table>
                        <thead>
                            <tr>
                                <th>Container ID</th>
                                <th>Image</th>
                                <th>Status</th>
                                <th>Names</th>
                            </tr>
                        </thead>
                        <tbody>
                            {#each dockerImages as dockerImage}
                                <tr>
                                    <td>{dockerImage["Container ID"]}</td>
                                    <td>{dockerImage.Image}</td>
                                    <td>{dockerImage.Status}</td>
                                    <td>{dockerImage.Names}</td>
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                {:else}
                    <p>No Docker data available.</p>
                {/if}
            </div>
        </div>
    </div>
</section>

<style>
    .main-wrapper {
        text-align: center;
        padding: 20px;
    }

    /* .button-group {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-bottom: 20px;
    } */

    .button-group {
        display: flex;
        flex-direction: column; /* 세로 정렬 */
        align-items: center; /* 가운데 정렬 */
        gap: 10px; /* 버튼 간격 */
        margin-bottom: 20px;
    }

    .button-group button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
        background-color: #6A24FE;
        color: #fff;
        border: none;
    }

    .button-group button:hover {
        background-color: #8c52ff;
    }

    .table-container {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
        margin-top: 20px;
        padding: 0 10px;
    }

    .table-section {
        flex: 1;
        max-width: 45%;
        min-height: 300px;
        overflow-x: auto;
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 10px;
        border: 1px solid #ccc;
    }

    th {
        background-color: #6A24FE;
        color: white;
    }

    td {
        text-align: center;
    }
</style>