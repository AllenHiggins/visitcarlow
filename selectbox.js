import React, { Component } from 'react';

export default class SelectBox extends Component{
    render() {
        const { data, onChange, name } = this.props;
            
            return (
                <div className="App">
                <select onChange = {onChange} name={name}>
                    <option value=''></option>
                    {data.map(item => (
                    <option key={item.id} value={item.id}>
                        {item.title}
                    </option>
                    ))}
                </select>
                </div>
            );
        }   
}