import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");

  const askAI = async () => {
    try {
      const res = await axios.post("http://localhost:8000/chat", {
        message: message,
      });

      setAnswer(res.data.answer);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Interview Coach</h1>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />

      <button
        className="border rounded bg-blue-600 p-2 text-white cursor-pointer"
        onClick={askAI}
      >
        Ask
      </button>

      <hr />

      <h3>Response</h3>

      <p>{answer}</p>
    </div>
  );
}

export default App;
