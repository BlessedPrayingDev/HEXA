<script>
    import { goto } from '$app/navigation';
    import apiEx from '../../api/apiEx';
    import { count, accessToken } from '../../store';
    import { onMount, onDestroy } from 'svelte';
    import UserModal from './UserModal.svelte';

    let users = [];
    let loginUsers = [];
    let selectedUser = null;
    let isModalOpen = false;
    let interval;
    let token;

    // accessToken을 구독하여 token에 저장
    accessToken.subscribe(value => {
        token = value;
    });

    // 모달 열기
    const openModal = (user) => {
        selectedUser = user;
        isModalOpen = true;
    };

    // 모달 닫기
    const closeModal = () => {
        isModalOpen = false;
        selectedUser = null;
    };

    const saveUserChanges = async (event) => {
        const updatedUser = event.detail;
        // API 호출로 유저 정보 업데이트
        closeModal();
    };

    const deleteUser = async (event) => {
        const userToDelete = event.detail;
        // API 호출로 유저 삭제
        users = users.filter(u => u.user !== userToDelete.user);
        closeModal();
    };

    const getAllHexaUser = async () => {
        const headers = {
            "Authorization": `Bearer ${token}`
        };
        const url = "/dashboard/hexausers/";

        try {
            const { data } = await apiEx.get(url, { headers });
            users = data;
            console.log(data);
        } catch (error) {
            console.error("Error fetching users: ", error);
            alert("로그인 세션이 만료되었습니다. 로그인 페이지로 이동합니다."); // Alert 창 추가
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    };

    const fetchHexaSessionUsers = async () => {
        const headers = { "Authorization": `Bearer ${token}` };
        const url = "/dashboard/hexasessionuser/";

        try {
            const { data } = await apiEx.get(url, { headers });
            loginUsers = data;
            console.log(loginUsers);
        } catch (error) {
            console.error("Error fetching session users: ", error);
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    };

    // 로그인한 유저인지 확인하는 함수
    const isUserLoggedIn = (user) => {
        return loginUsers.some(loginUser => loginUser.user_name === user.user);
    };

    // Function to fetch data
    const fetchData = () => {
        getAllHexaUser();
        fetchHexaSessionUsers();
    };

    // Set up interval on mount and clear on destroy
    onMount(() => {
        fetchData();
        interval = setInterval(fetchData, 5000);
    });

    onDestroy(() => {
        clearInterval(interval);
    });

    const navigateToRegisterHexaUser = () => goto('/registerhexauser');
    const navigateToAdminPage = () => goto('/adminpage');
</script>

<svelte:head>
	<title>Hexa User</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <h1>헥사 유저 정보</h1>

    {#if users.length > 0}
        <table>
            <thead>
                <tr>
                    <th>User</th>
                    <th>Level</th>
                    <th>Serial Number</th>
                    <th>Expired Date</th>
                    <th>Login</th>
                </tr>
            </thead>
            <tbody>
                {#each users as user}
                    <tr>
                        <td>
                            <button on:click={() => openModal(user)} style="background: none; border: none; color: blue; cursor: pointer; text-decoration: underline;">
                                {user.user}
                            </button>
                        </td>
                        <td>{user.level}</td>
                        <td>{user.serial_number}</td>
                        <td>{user.expired_date}</td>
                        <td>
                            {#if isUserLoggedIn(user)}
                                <span class="status-icon">✔</span>
                            {/if}
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {:else}
        <p>No user data available.</p>
    {/if}

    {#if isModalOpen}
        <UserModal user={selectedUser} on:close={closeModal} on:save={saveUserChanges} on:delete={deleteUser} />
    {/if}

    <button on:click={navigateToRegisterHexaUser}>헥사 유저 추가</button>
    <button on:click={navigateToAdminPage}>메인 페이지</button>
</section>

<style>
    section {
        text-align: center;
    }

    table {
        width: 80%;
        margin: 20px auto;
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

    /* 로그인 상태 표시 아이콘 */
    .status-icon {
        color: green;
        font-size: 1.5em;
        font-weight: bold;
    }
</style>