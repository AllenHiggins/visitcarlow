import React, { Component } from 'react';
import SelectBox from './selectbox';

export default class ListingForm extends Component{
    constructor(props) {
        super(props);
        
        const { 
          name, address, latitude, longitude, edit, id,
          text, phone, email, type, county, image, onChange
        } = this.props;

        this.state = {
          edit: edit,
          notLoaded: false,
          id: id,
          name: name,
          address: address,
          latitude: latitude,
          longitude: longitude,
          text: text,
          phone: phone,
          email: email,
          image:{},
          listType: [],
          type: type,
          countyList: [],
          county: county,
          website:'',
          facebook:'',
          twitter:'',
          instagram:'',
          files:""
        };

        this.handleChange = this.handleChange.bind(this);
       
      }
 
      componentDidMount() {

        fetch("http://127.0.0.1:5000/types/all")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              listType: result.types,
            });
          },
          (error) => {
            this.setState({
              notLoaded: true,
              error
            });
          }
        )

        fetch("http://127.0.0.1:5000/counties")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              countyList: result.County,
            });
          },
          (error) => {
            this.setState({
              notLoaded: true,
              error
            });
          }
        )

      }

      handleChange = (e) => {
        switch(e.target.name){
          case 'type':
            this.setState({
              type: e.target.value,
            });
          break;
          case 'county':
            this.setState({
              county: e.target.value
            });
          break;
          case 'name':
            this.setState({
              name: e.target.value
            });
          break;
          case 'address':
          this.setState({
            address: e.target.value
          });
          break;
          case 'longitude':
          this.setState({
            longitude: e.target.value
          });
          break;
          case 'latitude':
          this.setState({
            latitude: e.target.value
          });
          break;
          case 'phone':
          this.setState({
            phone: e.target.value
          });
          break;
          case 'text':
          this.setState({
            text: e.target.value
          });
          break;
          case 'email':
          this.setState({
            email: e.target.value
          });
          break;
          case 'website':
          this.setState({
            website: e.target.value
          });
          break;
          case 'facebook':
          this.setState({
            facebook: e.target.value
          });
          break;
          case 'twitter':
          this.setState({
            twitter: e.target.value
          });
          break;
          case 'instagram':
          this.setState({
            instagram: e.target.value
          });
          break;
          case 'file':
          this.setState({
            image: e.target.files
          });
          break;
          default:

        } 
      }

      handleSubmit = (e) => {
        // check type cat and county are !== null


        // to do
        // alert box warning to confrim contuining to update listing
        // if no reset values to old values else submit and reset all to null



        e.preventDefault();
        let URL = ''
        this.state.edit ? URL = 'http://127.0.0.1:5000/listing/details/edit' : URL = 'http://127.0.0.1:5000/listing/add'
        // POST data
        fetch(URL,{
          method: 'POST',
          headers:{
            'Accept':'application/json',
            'Content-Type':'application/json',
          },body: JSON.stringify({
            'typeID': this.state.type,
            'countID': this.state.county,
            'name': this.state.name,
            'address': this.state.address,
            'latitude': this.state.latitude,
            'longitude': this.state.longitude,
            'text': this.state.text,
            'phone': this.state.phone,
            'email': this.state.email,
            'website': this.state.website,
            'facebook': this.state.facebook,
            'twitter': this.state.twitter,
            'instagram': this.state.instagram
          })
        })
        .then(res => res.json())
        .then((result) => {
            //Success - returns id of last inserted listing
            console.log(result);
    /*
    
            // to do
            // if image value has changed else do not run this part

    
            // Post listing image to server
            let request = new XMLHttpRequest();
            request.open('POST', 'http://127.0.0.1:5000/image/upload/' + this.state.id); //need to insert list id here
            const myForm = this.refs.image;
            const formData = new FormData(myForm);
            formData.append('image', this.refs.image.files[0]); 
            request.send(formData);
    
    
    
    */
         },(error) => {
            console.log(error);
          }
        )  
      }

      render(){
        
        const { listType, countyList, notLoaded } = this.state;
        const { btnText, id } = this.props;

        if(notLoaded){
          return(
            <div>Connection Faild...</div>
          );
        }else{
          return(
          
            <form onSubmit={this.handleSubmit} encType="multipart/form-data" method="POST">
        
              <div id='gen'>

                <label for='name'> Name:</label>
                <input 
                  id='name'
                  type='text' 
                  name='name' 
                  value={this.state.name}
                  onChange={this.handleChange}
                  placeholder='Name'
               //   required
                />

                <label for='address'> Address:</label>
                <input 
                  id='address'
                  type='text' 
                  name='address' 
                  value={this.state.address}
                  onChange={this.handleChange}
                  placeholder='Address'
              //    required
                />

                <label for='latitude'> Latitude:</label>
                <input
                  id='latitude' 
                  type='text' 
                  name='latitude' 
                  value={this.state.latitude}
                  onChange={this.handleChange}
                  placeholder='Latitude'
            //      required
                />

                <label for='longitude'> Longitude:</label>
                <input 
                  id='longitude'
                  type='text' 
                  name='longitude' 
                  value={this.state.longitude}
                  onChange={this.handleChange}
                  placeholder='Longitude'
             //     required
                />

                <label for='phone'> Phone:</label>
                <input 
                  id='phone'
                  type='text' 
                  name='phone' 
                  value={this.state.phone}
                  onChange={this.handleChange}
                  placeholder='Phone Number'
           //       required
                />

                <label for='email'> Email:</label>
                <input 
                  id='email'
                  type='email' 
                  name='email' 
                  value={this.state.email}
                  onChange={this.handleChange}
                  placeholder='Email'
             //     required
                />

               <label for='image'> Image:</label>
               <input 
                  accept="image/*"
                  id='image'
                  ref = 'image'
                  type='file' 
                  name='file' 
                  onChange={this.handleChange}
                  multiple="true"
              //    required
                />
          
                <label for='type'> Type:</label>
                <SelectBox 
                  id='type'
                  data={listType} 
                  onChange={this.handleChange}
                  name={'type'}
                />

                <label for='county'> County:</label>
                <SelectBox 
                  id='county'
                  data={countyList} 
                  onChange={this.handleChange}
                  name={'county'}
                />
              </div>

              <div id='media'>
                <h3>Media Links:</h3>
          
                <label for='website'> Website:</label>
                <input 
                  id='website'
                  type='url' 
                  name='website' 
                  value={this.state.website}
                  onChange={this.handleChange}
                  placeholder='Website'
                />


                <label for='facebook'> Facebook:</label>
                <input 
                  id='facebook'
                  type='url' 
                  name='facebook' 
                  value={this.state.facebook}
                  onChange={this.handleChange}
                  placeholder='Facebook'
                />

                <label for='twitter'> Twitter:</label>
                <input 
                  id='twitter'
                  type='url' 
                  name='twitter' 
                  value={this.state.twitter}
                  onChange={this.handleChange}
                  placeholder='Twitter'
                />

                <label for='instagram'> Instagram:</label>
                <input 
                  id='instagram'
                  type='url' 
                  name='instagram' 
                  value={this.state.instagram}
                  onChange={this.handleChange}
                  placeholder='Instagram'
                />
              </div>

              <div id='info'>
                <h3>Informational Context</h3>

                <label for='text'> Text:</label>
                <textarea 
                  id='text'
                  name='text' 
                  value={this.state.text}
                  onChange={this.handleChange}
                  placeholder='Info'
          //        required
                />
              </div>

              <button type='submit'>{btnText}</button>



              {this.state.type}
              {this.state.county}
            
            
            
            
            </form>
          );
        } 
      } 
      
}
