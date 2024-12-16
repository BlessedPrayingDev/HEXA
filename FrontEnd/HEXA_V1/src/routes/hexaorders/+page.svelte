<script>
    import { goto } from '$app/navigation';
    import apiEx from '../../api/apiEx'
    import { count, accessToken } from '../../store';
    import { onMount, onDestroy } from 'svelte';

    const navigateToAdminPage = () => {
        goto('/adminpage');
    };

    let orders = [];
    let username = "";

    // const getAllHexaOrders = async (event) => {
    //     event.preventDefault();

    //     const headers = {
    //         "Authorization": `Bearer ${$accessToken}`
    //     }
    //     const url = "/dashboard/hexaorders/"

    //     // 요청 본문에 username을 포함하여 서버로 보냅니다.
    //     const body = username ? { username } : {};

    //     try {
    //         const {data} = await apiEx.get(url, { headers, params: body } );
    //         orders = data;
    //         console.log(data);
    //     } catch (error) {
    //         console.error("에러: ", error)
    //     }
    // };

    const getAllHexaOrders = async (event) => {
        if (event) event.preventDefault();

        const headers = {
            "Authorization": `Bearer ${$accessToken}`
        };
        const url = "/dashboard/hexaorders/";

        // 요청 본문 대신 params로 username을 전달합니다.
        const params = username ? { username } : {};

        try {
            const { data } = await apiEx.get(url, { headers, params });
            orders = data;
            console.log(data);
        } catch (error) {
            console.error("에러: ", error);
            alert("로그인 세션이 만료되었습니다. 로그인 페이지로 이동합니다."); // Alert 창 추가
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    };

    onMount(() => {
        getAllHexaOrders();
    });
</script>

<svelte:head>
	<title>Hexa Orders</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <h1>헥사 Order 정보 가져오기</h1>
    <button on:click={navigateToAdminPage}>메인 페이지</button>
    <!-- 검색 조건 입력 -->
    <form on:submit={getAllHexaOrders}>
        <input 
            type="text" 
            bind:value={username} 
            placeholder="Enter username" 
        />
        <button type="submit">Search</button>
    </form>


    <!-- <button on:click={getAllHexaOrders}>Get All Hexa Orders</button> -->

    <!-- 유저 정보 테이블 -->
    {#if orders.length > 0}
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>User Name</th>
                    <th>Project Name</th>
                    <th>Date Time</th>
                    <th>Algorithm</th>
                    <th>Success</th>
                </tr>
            </thead>
            <tbody>
                {#each orders as order}
                    <tr>
                        <td>{order.id}</td>
                        <td>{order.username}</td>
                        <td>{order.project_name}</td>
                        <td>{order.datetime}</td>
                        <td>{order.algorithms}</td>
                        <td>{order.success}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {:else}
        <p>No order data available.</p>
    {/if}
</section>

<style>
    section {
        text-align: center;
    }

    form {
        margin: 20px;
    }

    input {
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 4px;
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
</style>
