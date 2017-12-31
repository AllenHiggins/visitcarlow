import React, { Component } from 'react';

export default class ListInfo extends Component{
    constructor(props){
        super(props)

        this.state ={
            search:''
        }

    }
    
    updateSearch = (e) => {
        this.setState({
            search: e.target.value
        })
    }

    render(){
        
        const { onClick } = this.props;
       
        let filterList = this.props.list.filter(
            (listing) => { 
                return listing.name.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1;
            }
        );

        return(
            <div>
               <label htmlFor='search'>Search</label>
               <input 
                id='search'
                type='text' 
                value={this.state.search} 
                onChange={this.updateSearch.bind(this)} 
               />
                {
                    filterList.map( (listing, index) => {
                        return (
                            <li key={listing.id} > 
                                {listing.name} 
                                {listing.address}
                                {listing.county}
                                <button onClick={onClick} value={listing.id}>Edit</button>
                            </li>
                        )
                    })
                }
            </div>
        );
    }
}