import {usePromiseTracker} from "react-promise-tracker";
import {useState} from "react";


export const LoadingIndicator = props => {
    let [color, setColor] = useState("#ffffff");
    const {promiseInProgress} = usePromiseTracker()

    return <div>Loading</div>
}