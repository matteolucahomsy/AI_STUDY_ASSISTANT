import {useEffect,useState} from "react";
function App() {
  const [message,setMessage] = useState("");
  useEffect(()=>{
    fetch("http://127.0.0.1:8000/chat")
    .then((response)=> response.json())
    .then((data)=> {
      setMessage(data.response);
    })
    .catch((error)=>{
      console.error("Error:",error);
    });
  }, []);
  return(
    <div>
      <h1>AI Study Assistant</h1>
      <h2>{message}</h2>
    </div>
  );
}
export default App;