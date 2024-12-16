import axios from "axios";

const baseURL = 'http://172.30.1.165:8000/';
const timeout = 10000;
const headers = {'Content-Type': 'application/json'};

const apiEx = axios.create({baseURL, timeout, headers});

export default apiEx;