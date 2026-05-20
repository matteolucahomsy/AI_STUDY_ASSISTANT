import {useEffect,useState} from "react";
import axios from "axios";
function App() {
  const [message,setMessage] = useState("");
  const[chat, setChat]= useState([]);
  const sendMessage= async() => {
    if (!message) return ;
    const userMsg= message;
    setChat((prev) => [...prev,{role: "user", text: userMsg}]);
    setMessage("");
    const res = await axios.post("http://127.0.0.1:8000/chat",{
      message: userMsg,
    });
    setChat((prev) => [
      ...prev,
      {role: "ai", text: res.data.response},
    ]);
  };
  return(
    <div style={{padding: 20}}>
      <h1>AI Study Assistant</h1>
      
      <div>
        {chat.map((c, i)=> (
          <p key={i}>
            <b>{c.role}:</b> {c.text}
          </p>
        ))}
      </div>
      <input 
      value={message}
      onChange={(e) => setMessage(e.target.value)}
      placeholder="Type message ..." />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
export default App;