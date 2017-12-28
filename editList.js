import React, { Component } from 'react';
import ListInfo from './listinfo';
import ListingForm from './listingform';

export default class EditList extends Component {
    constructor(props) {
        super(props);

      this.state = {
        edit: false,
        list: [],
        editList: [],
        mediaList: []
        }

        this.handleEdit = this.handleEdit.bind(this);
        this.habdleCancel = this.habdleCancel.bind(this);
        this.table = this.table.bind(this);    
        this.edit = this.edit.bind(this);

    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/listing/admin/display")
        .then(res => res.json())
        .then(
        (result) => {   
            this.setState({
                list: result.listings
            });
        },
        (error) => {
            this.setState({
            error
            });
        })
    }

    handleEdit = (id) => {
        fetch("http://127.0.0.1:5000/listing/choice/"+id)
        .then(res => res.json())
        .then(
        (result) => {   
            this.setState({
                edit:true,
                editList: result.Listing
            });
            console.log("Listing: ",this.state.editList);
            fetch("http://127.0.0.1:5000/listings/media/"+id)
            .then(res => res.json())
            .then(
            (result) => {   
                this.setState({
                    edit:true,
                    mediaList: result.Media
                });
                console.log("Media: ",this.state.mediaList);
            },
            (error) => {
                this.setState({
                error
                });
            })
        },
        (error) => {
            this.setState({
            error
            });
        })
    }
    
    habdleCancel = () => {
        this.setState({
            edit:false,
            editList:[]
        });
    }

    edit = () =>{
        return(
            <div>
                <h1>Edit</h1>
                {this.state.editList.map((item, index) => (   
                    <div key={index}>
                        <ListingForm 
                            edit={true}
                            id={item.id}
                            name={item.name}
                            address={item.address}
                            latitude={item.latitude}
                            longitude={item.longitude}
                            text={item.text}
                            phone={item.phone}
                            email={item.email}
                            image={item.image}
                            type={item.listTypeID}
                            county={item.countyID}
                            btnText = 'Update'

                            // mediaList ???? 
                            // How to set index pos of select box
                        />
                        <button value='cancel' onClick={this.habdleCancel}>Cancel</button>
                    </div>
                ))}
            </div>
        );
    }

    table = () => { 
        return(
            <div>
                <h1>Listings</h1>
                <table>
                    <tbody>
                        {this.state.list.map((item, index) => (
                            <tr key={index}
                                onClick = {this.handleEdit.bind(this,item.id)}>
                                <td>
                                    <ListInfo 
                                        name = {item.name}
                                        address = {item.address}
                                        county = {item.county}
                                        onClick = {this.handleEdit.bind(this,item.id)}
                                    />
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table> 
            </div>
            ); 
        }

    render(){
        const { edit, loaded } = this.state;
            return(   
                <div>
                    {edit ? this.edit() : this.table() }
                </div>
            );  
        
    } 
}