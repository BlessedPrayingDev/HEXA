<script>
	import Header from './Header.svelte';
	import '../app.css';
	import { onMount } from 'svelte';
	import { get } from 'svelte/store';
	import { accessToken, refreshToken, lastAccessTokenUpdate } from '../store';
	import apiEx from '../api/apiEx';


	let { children } = $props();

	let interval;
	let userName = "";

	// API functions
	const getUserInfo = async () => {
        const headers = { "Authorization": `Bearer ${$accessToken}` };
        const url = "/auths/userinfo/";

        try {
            const { data } = await apiEx.post(url, {}, { headers });
            userName = data.data.username;
			// 상단에 토큰 남은 시간, 연장 버튼, 로그아웃 버튼
			
        } catch (error) {
            console.error("Failed to retrieve user info", error);
            console.log("로그인 세션이 만료 됨")
            // goto('/login');
        }
    };

	onMount(() => {
		const unsubscribe = accessToken.subscribe(token => {
			if (token) {
				console.log("업데이트된 토큰:", token);
				getUserInfo(); // 토큰이 업데이트된 후 호출
			}
		});

		return () => {
			unsubscribe(); // 컴포넌트 언마운트 시 구독 해제
		};
	});
</script>

<div class="app">
	<Header />

	<main>
		{@render children()}
	</main>

	<footer>
		<p>
			<!-- visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to learn about SvelteKit -->
		</p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	/* footer a {
		font-weight: bold;
	} */

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
