import React, { Component } from 'react'
import SelectBox from './selectbox'

export default class ListformElements extends Component{
    render(){

        const { 
            listname, address, latitude, longitude, 
            text, phone, email, type, county, website, facebook, 
            twitter, instagram, handleChange, countyList, listType
          } = this.props;

        return(
            <div>
                <div>
                
                    <label htmlFor='name'> Name:</label>
                    <input 
                        id='name'
                        type='text' 
                        name='name' 
                        value={listname || ''}
                        onChange={handleChange}
                        placeholder='Name'
                        required
                    />

                    <label htmlFor='address'> Address:</label>
                    <input 
                        id='address'
                        type='text' 
                        name='address' 
                        value={address || ''}
                        onChange={handleChange}
                        placeholder='Address'
                        required
                    />

                    <label htmlFor='latitude'> Latitude:</label>
                    <input
                        id='latitude' 
                        type='text' 
                        name='latitude' 
                        value={latitude || ''}
                        onChange={handleChange}
                        placeholder='Latitude'
                        required
                    />

                    <label htmlFor='longitude'> Longitude:</label>
                    <input 
                        id='longitude'
                        type='text' 
                        name='longitude' 
                        value={longitude || ''}
                        onChange={handleChange}
                        placeholder='Longitude'
                        required
                    />

                    <label htmlFor='phone'> Phone:</label>
                    <input 
                        id='phone'
                        type='text' 
                        name='phone' 
                        value={phone || ''}
                        onChange={handleChange}
                        placeholder='Phone Number'
                        //required
                    />

                    <label htmlFor='email'> Email:</label>
                    <input 
                        id='email'
                        type='email' 
                        name='email' 
                        value={email || ''}
                        onChange={handleChange}
                        placeholder='Email'
                        //required
                    />

                    <label htmlFor='type'> Type:</label>
                    <SelectBox 
                        id='type'
                        data={listType} 
                        onChange={handleChange}
                        name={'type'}
                        index={type || ''}
                    />

                    <label htmlFor='county'> County:</label>
                    <SelectBox 
                        id='county'
                        data={countyList} 
                        onChange={handleChange}
                        name={'county'}
                        index={county || ''}
                    />
                    </div>

                    <div id='media'>
                    <h3>Media Links:</h3>
                
                    <label htmlFor='website'> Website:</label>
                    <input 
                        id='website'
                        type='url' 
                        name='website' 
                        value={website || ''}
                        onChange={handleChange}
                        placeholder='Website'
                    />

                    <label htmlFor='facebook'> Facebook:</label>
                    <input 
                        id='facebook'
                        type='url' 
                        name='facebook' 
                        value={facebook || ''}
                        onChange={handleChange}
                        placeholder='Facebook'
                    />

                    <label htmlFor='twitter'> Twitter:</label>
                    <input 
                        id='twitter'
                        type='url' 
                        name='twitter' 
                        value={twitter || ''}
                        onChange={handleChange}
                        placeholder='Twitter'
                    />

                    <label htmlFor='instagram'> Instagram:</label>
                    <input 
                        id='instagram'
                        type='url' 
                        name='instagram' 
                        value={instagram || ''}
                        onChange={handleChange}
                        placeholder='Instagram'
                    />
                    </div>

                    <div id='info'>
                    <h3>Informational Context</h3>

                    <label htmlFor='text'> Text:</label>
                    <textarea 
                        id='text'
                        name='text' 
                        value={text || ''}
                        onChange={handleChange}
                        placeholder='Info'
                        required
                    />

                </div>  
            </div>
        );
    }
}