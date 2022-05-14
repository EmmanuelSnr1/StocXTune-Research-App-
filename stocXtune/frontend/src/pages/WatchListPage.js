import React, {useState, useEffect} from 'react'
import ListItem from '../components/ListItem'

const WatchListPage = () => {

    let [watchlists,setWatchlists] = useState([])

    let getWatchlists = async ()=> {
        let response = await fetch('http://127.0.0.1:8000/api/watchlistlist/')
        let data = await response.json()
        console.log('DATA', data)
        setWatchlists(data)
        
    }

    useEffect(() =>{
        getWatchlists()
    },[])

    

    return (
        

        <div>
            So these are the watchlists
            
                <div className="watchlist-list">
                    {watchlists.map((watchlist,index) =>(
                        <ListItem key={index} watchlist = {watchlist} />
                    ))}
                    
                </div>
            
        </div>
        )

}

export default WatchListPage