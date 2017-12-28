
const GETOPTIONS ={

    getOptions : (link,data) => {
    let url = "http://127.0.0.1:5000/"+link;
    fetch(url)
    .then(res => res.json())
    .then(
      (result) => {
        let s = result +"."+ data;
        return s;
      },
      (error) => {
        this.setState({
          notLoaded: true,
          error
        });
      }
    )
  }

}
export default GETOPTIONS;