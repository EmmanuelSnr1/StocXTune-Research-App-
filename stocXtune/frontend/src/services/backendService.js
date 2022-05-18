import { backendBaseUrl } from "../core/constants";


/*
Register a new User account
 */
async function register({first_name, last_name, user_name, email, password}) {
    const response = await fetch(backendBaseUrl + "user/register/", {
        method: 'POST',
        body: JSON.stringify(arguments[0]),
        headers: {
            "Content-Type":"application/json"
        }
    })
    if (response.ok) {
        return response.json()
    }
    throw response;
}


export  const BackendService = {
    register
}