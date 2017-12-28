import React, { Component } from 'react';

export default class ListInfo extends Component{
    render(){
        const { name, address, county, onClick } = this.props;
        return(
            <div>
                {name}
                {address}
                {county}
                <button onClick = {onClick} >Edit</button>    
            </div>
        );
    }
}