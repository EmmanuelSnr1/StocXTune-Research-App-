import React from 'react'

const ListItem = ({ watchlist }) => {
  return (
    <div>
        <h3>
            {watchlist.body}
        </h3>

    </div>
  )
}

export default ListItem