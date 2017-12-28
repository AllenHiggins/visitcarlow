import React, { Component } from 'react';
import './App.css';
import ListingForm from './components/listingform';
import EditList from './components/editList';

export default class App extends Component {

  render(){
   return(
      <div>
    {/*   <ListingForm 
              edit={false}
              name=""
              address=""
              latitude=""
              longitude=""
              text=""
              phone=""
              email=""
              image=""
              type=""
              county=""
              btnText = 'Submit'
          />*/}
          <EditList />
       

      </div>
    );
  } 
}