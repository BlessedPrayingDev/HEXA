import { writable } from "svelte/store";

export const count = writable(3);

let initialToken = '';
let initialRefreshToken = '';
let initialUpdateTime = null; // 마지막 업데이트 시간

if (typeof window !== 'undefined') {
    initialToken = localStorage.getItem('accessToken') || '';
    initialRefreshToken = localStorage.getItem('refreshToken') || '';
    initialUpdateTime = localStorage.getItem('lastAccessTokenUpdate') || null;
}

export const accessToken = writable(initialToken);
export const refreshToken = writable(initialRefreshToken);
export const lastAccessTokenUpdate = writable(initialUpdateTime);

// 업데이트 시 localStorage 동기화
accessToken.subscribe(value => {
    if (typeof window !== 'undefined') {
        if (value) {
            localStorage.setItem('accessToken', value);
            localStorage.setItem('lastAccessTokenUpdate', Date.now());
            lastAccessTokenUpdate.set(Date.now());
        } else {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('lastAccessTokenUpdate');
        }
    }
});

refreshToken.subscribe(value => {
    if (typeof window !== 'undefined') {
        if (value) {
            localStorage.setItem('refreshToken', value);
        } else {
            localStorage.removeItem('refreshToken');
        }
    }
});