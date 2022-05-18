import {useEffect, useState} from "react";



export default function useFetch(baseUrl, token, url, method='GET', body, queryParams = '') {
    const [data, setData] = useState(null)
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        async function init() {
            try {
                const response = await fetch(baseUrl + url + "?token=" + token + queryParams,{method, body})
                if (response.ok) {
                    const json = await response.json()
                    // console.log('response data', json)
                    setData(json)
                }
                // else {
                //     throw response;
                // }
            } catch (e) {
                setError(e)
            } finally {
                setLoading(false)
            }
        }

        init();

    }, [queryParams, url])

    return {data, error, loading}
}
