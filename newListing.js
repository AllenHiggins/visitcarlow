import React, { Component } from 'react'
import ListformElements from './listeditcom'

export default class NewListing extends Component{
    render(){

        const { 
            handleChange,countyList,listType,listname,address,
            latitude,longitude,text,phone,email,type,county,
            website,facebook,twitter,instagram
        } = this.props
        return(
            <div>
        
                <ListformElements 
                    listname={listname}
                    address={address} 
                    latitude={latitude}
                    longitude={longitude}
                    text={text}
                    phone={phone} 
                    email={email}
                    type={type}
                    county={county}
                    website={website}
                    facebook={facebook} 
                    twitter={twitter}
                    instagram={instagram}
                    handleChange={handleChange}
                    countyList={countyList}
                    listType={listType}
                />
        
            </div>
        )
    }
}