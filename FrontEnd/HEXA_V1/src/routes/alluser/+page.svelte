<script>
    import { goto } from '$app/navigation';
    import apiEx from '../../api/apiEx'
    import { count, accessToken } from '../../store';

    // let email = "";
    // let password = "";

    // const onLogin = async (event) => {
    //     event.preventDefault(); // 기본 폼 제출 동작을 막아줍니다
    //     console.log("email: ", email);
    //     console.log("password: ", password);

    //     const url = "/auths/login/";

    //     try {
    //         const { data } = await apiEx.post(url, { email, password });
    //         accessToken.set(data.access); // store에 token을 저장하여 localStorage에도 반영
    //         console.log("access: ", $accessToken);
    //         goto("/mainPage")
    //         // 로그인 성공 시 다음 페이지로 리다이렉트 로직 추가 가능
    //     } catch (error) {
    //         console.error("로그인 실패", error);
    //     }
    //     console.log("access: ", $accessToken);
    // }

    const navigateToAdminPage = () => {
        goto('/adminpage');
    };

    let users = [];
    let selectedUsers = new Set(); // 선택된 유저를 저장하는 Set 선언

    const getAllUser = async (event) => {
        event.preventDefault();
        const headers = {
            "Authorization": `Bearer ${$accessToken}`
        }
        const url = "/auths/users/"

        try {
            const {data} = await apiEx.get(url, { headers } );
            users = data;
            console.log(data);
        } catch (error) {
            console.error("에러: ", error)
            console.log("로그인 세션이 만료 됨")
            goto('/login');
        }
    }

        // 유저 수정 페이지로 이동
        const navigateToEditUser = (user) => {
        goto(`/edituser/${user.id}`);
    };

    // 유저 선택/해제 함수
    const toggleUserSelection = (user) => {
        if (selectedUsers.has(user)) {
            selectedUsers.delete(user);
        } else {
            selectedUsers.add(user);
        }
    };

    // 선택된 유저 삭제 함수
    const deleteSelectedUsers = async (event) => {
        event.preventDefault();

        const headers = {
            "Authorization": `Bearer ${$accessToken}`
        }
        const url = "/auths/userdelete/";

        // 선택된 유저가 없을 경우 경고
        if (selectedUsers.size === 0) {
            alert("삭제할 유저를 선택하세요.");
            return;
        }

        // 삭제 확인
        const confirmDelete = confirm("선택한 유저들을 삭제하시겠습니까?");
        if (!confirmDelete) return;

        try {
            // 선택된 유저 ID를 배열로 변환하여 삭제 요청
            for (const userId of selectedUsers) {
                const user = { user: userId }; // 삭제 요청에 필요한 유저 데이터 구성
                // DELETE 요청 보내기
                const res = await apiEx.delete(url, {
                    headers,
                    data: user
                });

                console.log('삭제 응답:', res);
            }

            // 성공적으로 삭제되면, 로컬 상태에서 해당 유저들을 제거
            users = users.filter(user => !selectedUsers.has(user.id));
            selectedUsers.clear(); // 선택 목록 초기화
            alert("선택된 유저들이 삭제되었습니다.");
        } catch (error) {
            console.error('삭제 오류:', error);
            alert("삭제 중 오류가 발생했습니다.");
        }
    };
</script>

<svelte:head>
	<title>All User</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
    <h1>유저 정보 가져오기</h1>
    <button on:click={getAllUser}>Get All User</button>

    <!-- 유저 정보 테이블 -->
    {#if users.length > 0}
        <table>
            <thead>
                <tr>
                    <th>Select</th>
                    <th>Email</th>
                    <th>Username</th>
                    <th>Phone</th>
                    <th>Gender</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {#each users as user}
                    <tr>
                        <td>
                            <input type="checkbox" on:change={() => toggleUserSelection(user.email)} />
                        </td>
                        <td>{user.email}</td>
                        <td>{user.username}</td>
                        <td>{user.phone ? user.phone : 'N/A'}</td>
                        <td>{user.gender ? user.gender : 'N/A'}</td>
                        <td>
                            <button on:click={() => navigateToEditUser(user)}>수정</button>
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
    {:else}
        <p>No user data available.</p>
    {/if}

    <!-- 선택된 유저 삭제 버튼 -->
    <button on:click={deleteSelectedUsers}>선택된 유저 삭제</button>
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
</style>
