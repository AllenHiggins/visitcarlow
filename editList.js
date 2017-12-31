import React, { Component } from 'react'
import ListInfo from './listinfo'
import ListformElements from './listeditcom'
import NewListing from './newListing'

export default class EditList extends Component {
    constructor(props) {
        super(props);

        this.state = {
            success:false,
            createList: true,
            editOption: false,
            imgRef:'image',
            edit: false,
            list: [],
            editList: [],
            imagePath:'',
            btnText: '',
            editImage: false,
            notLoaded: false,
            id: '',
            listname: '',
            address: '',
            latitude: '',
            longitude: '',
            text: '',
            phone: '',
            email: '',
            image:{},
            imageEdit:{},
            listType: [],
            type: '',
            countyList: [],
            county: '',
            website: '',
            facebook: '',
            twitter: '',
            instagram:'',
            files:''
        }

        this.handleEdit = this.handleEdit.bind(this)
        this.habdleCancel = this.habdleCancel.bind(this)
        this.table = this.table.bind(this)    
        this.edit = this.edit.bind(this)
        this.handleChange = this.handleChange.bind(this)
        this.editImage = this.editImage.bind(this)
        this.newImageUpload = this.newImageUpload.bind(this)
        this.handleOption = this.handleOption.bind(this)
        this.successMSG = this.successMSG.bind(this)
        this.getAdminListOfListings = this.getAdminListOfListings.bind(this)

    }

    reset = () => {
        this.setState({
            edit: false,
            editList: [],
            imagePath:'',
            btnText: '',
            editImage: false,
            notLoaded: false,
            id: '',
            listname: '',
            address: '',
            latitude: '',
            longitude: '',
            text: '',
            phone: '',
            email: '',
            image:{},
            imageEdit:{},
            type: '',
            county: '',
            website: '',
            facebook: '',
            twitter: '',
            instagram:'',
            files:''
        })
    }

    getAdminListOfListings = () => {
        fetch("http://127.0.0.1:5000/listing/admin/display")
        .then(res => res.json())
        .then(
        (result) => {   
            this.setState({
                list: result.listings,
            });
        },
        (error) => {
            
        })
    }

    componentDidMount() {

        this.getAdminListOfListings()

        fetch("http://127.0.0.1:5000/types/all")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              listType: result.types,
            });

            fetch("http://127.0.0.1:5000/listing/image/"+this.state.list[0].id)
            .then(res => res.json())
            .then(
              (result) => {
                this.setState({
                  imagePath: result.imagePath
                })
                console.log(this.state.imagePath)
              },
              (error) => {
                console.log(error)
              }
            )
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

    onSuccess = () => {
        this.setState({
            success:true
        })
    }
    
    successMSG = () => {
        if(this.state.success){
          return <div><h3>Listing was successful!</h3></div>
        }
    }

    handleEdit = (e) => {

        let id = e.target.value

        fetch("http://127.0.0.1:5000/listing/choice/"+id)
        .then(res => res.json())
        .then(
        (result) => {   
            this.setState({
                editList: result.Listing
            });

            fetch("http://127.0.0.1:5000/listings/media/"+id)
            .then(res => res.json())
            .then(
            (result) => {  
                try {
                    // set the state
                    this.state.editList[0]['website'] = result.Media[0].website
                    this.state.editList[0]['facebook'] = result.Media[0].facebook
                    this.state.editList[0]['twitter'] = result.Media[0].twitter
                    this.state.editList[0]['instagram'] = result.Media[0].instagram
                    // update the the state
                    this.setState({
                        editList: this.state.editList,
                        edit:true,
                        id:this.state.editList[0].id,
                        listname:this.state.editList[0].name,
                        address:this.state.editList[0].address,
                        latitude:this.state.editList[0].latitude,
                        longitude:this.state.editList[0].longitude,
                        text:this.state.editList[0].text,
                        phone:this.state.editList[0].phone,
                        email:this.state.editList[0].email,
                        type:this.state.editList[0].listTypeID,
                        county:this.state.editList[0].countyID,
                        website:this.state.editList[0].website,
                        facebook:this.state.editList[0].facebook,
                        twitter:this.state.editList[0].twitter,
                        instagram:this.state.editList[0].instagram
                    });
                } catch (error) {
                    this.setState({
                        edit:true
                    });
                }
            },
            (error) => {
                console.log(error)
            })
        },
        (error) => {
            console.log(error)
        }) 
    }
    
    habdleCancel = () => {
      
        this.reset()
    }

    handleChange = (e) => {
        console.log("here", e.target.name)
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
                listname: e.target.value
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

        // to do
        // component alert box warning to confrim contuining to update listing 
       


        e.preventDefault();
        let URL = ''
        this.state.edit ? URL = 'http://127.0.0.1:5000/listing/details/edit/'+this.state.id : URL = 'http://127.0.0.1:5000/listing/add'

        // POST data
        fetch(URL,{
          method: 'POST',
          headers:{
            'Accept':'application/json',
            'Content-Type':'application/json',
          },body: JSON.stringify({
            'typeID': this.state.type,
            'countID': this.state.county,
            'name': this.state.listname,
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
            this.setState({
              id: result.result
            })
            
            // HAS THE IMAGE CHANGED
            if(this.state.editImage){
              // Post listing image to server
              this.imageSend(this.refs.newImage, this.refs.newImage.files[0]) 
            }
            
            // If creadting a new listing
            if(!this.state.edit){
              // Post listing image to server  
              console.log(this.refs.image.files[0])
              this.imageSend(this.refs.image, this.refs.image.files[0])
            }   
            
            //get back to not edit
            this.reset()
            
            // to do
            // success msg + time out and reset to false
            this.onSuccess()

            console.log('SAVED!');
         },(error) => {
            console.log(error);
          }
        )  
      }

      imageSend = (theRef, theRefFile) => {
        let request = new XMLHttpRequest();
        request.open('POST', 'http://127.0.0.1:5000/image/upload/'+this.state.id);
        const myForm = theRef
        const formData = new FormData(myForm);
        formData.append('image', theRefFile); 
        request.send(formData);
      }

      handleEditImageChange = (e) => {
        this.setState({
          imageEdit: e.target.files
        });
      }

      newImageUpload = () => {
        this.setState({
          editImage: true
        })
      }

      editImage = () => {
        const { editImage } = this.state
        if(editImage){
          return(
            <div>
              <label htmlFor='image'> Image:</label>
              <input 
              accept="image/*"
              id='image'
              ref ='newImage'
              type='file' 
              name='file' 
              onChange={this.handleEditImageChange}
              multiple="true"
              required
              />
          </div>
          );
        }else{   
          return(
            <div>
              <h3>Upload New Image</h3>
              <div>





              {/*  
                GET IMAGE AND DISPLAY  
                <img src={this.state.imagePath} alt='image' />
              */}





              </div>
              <button onClick={this.newImageUpload}>Change Image</button>
            </div>
          );
        }
      }

    edit = () => {
        
        const { listType, countyList, notLoaded, listname, address, 
            latitude, longitude, text, phone, email, type, edit,
            county, website, facebook, twitter, instagram
          } = this.state;

        if(notLoaded){
            return(
              <div>Connection Faild...</div>
            );
          }else if(edit){
        return(
            <div>
                <h1>Edit</h1>

                {/*BLOCK LISTING COMPONENT*/}

                <form  encType="multipart/form-data" onSubmit={this.handleSubmit} method="POST">
        
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
                        handleChange={this.handleChange}
                        countyList={this.state.countyList}
                        listType={this.state.listType}
                    />

                    { this.editImage() }

                    <button type='submit'>Save Changes</button>
                </form> 
        
                <button value='cancel' onClick={this.habdleCancel}>Cancel</button>
            </div>
            );
        }          
    }

    table = () => { 
        return(
            <div>
                <h1>Listings</h1>
                {this.successMSG()}
                <ListInfo 
                    list={this.state.list}
                    onClick = {this.handleEdit}  
                />
            </div>
            ); 
    }

    handleBlock = (e) => {
        console.log(e.target.value)
    }

    newList = () => {
        const { 
            listname,address,latitude,longitude,text,phone,imgRef,
            email,type,county,website,facebook,twitter, instagram
        } = this.state
        return(
            <div>
                <h1>Create a New Listing</h1>

                <form  encType="multipart/form-data" onSubmit={this.handleSubmit} method="POST">
                <NewListing 
                    handleChange={this.handleChange}
                    countyList={this.state.countyList}
                    listType={this.state.listType}
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
                />

            <label htmlFor='image'> Image:</label>
            <input 
                accept="image/*"
                id='image'
                ref ={imgRef}
                type='file' 
                name='file' 
                onChange={this.handleEditImageChange}
                multiple="true"
                required
            />
            <button type='submit'>Save</button>
            </form> 
        </div>
        )
    }

    options = () => {
        const { edit,createList,editOption } = this.state
        
        if(createList){
            return <div>{this.newList()}</div>
        }
        
        if(editOption){
            return <div>{edit ? this.edit() : this.table()}</div> 
        }
    }

    handleOption = (e) => {
        this.reset()
       
        if(e.target.value === 'newListingOption'){
            this.setState({
                createList:true,
                editOption: false
            })
        }
        if(e.target.value === 'editListingOption'){
            this.getAdminListOfListings()
            this.setState({
                editOption:true,
                createList:false
            }) 
        }
    }

    render(){

        return(
            <div>
                <button onClick={this.handleOption} value='newListingOption'>Create New Listing</button>
                <button onClick={this.handleOption} value='editListingOption'>Edit a Listing</button>
                {this.options()}
            </div>
        )   
    } 
}