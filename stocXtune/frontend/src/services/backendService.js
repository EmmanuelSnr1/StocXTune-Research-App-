import { backendBaseUrl } from "../core/constants";

const baseUrl = 'https://cloud.iexapis.com/'
const token = 'pk_d0153e3e12ee4a9f83ae3a1c3c38a8cd';

/*
Register a new User account
 */
export async function register(paylaod) {
    const response = await fetch(backendBaseUrl + "/user/register", {method: 'POST'})
    if (response.ok) {
        return response.json()
    }
    throw response;
}
