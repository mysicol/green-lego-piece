import { useState } from "react";
import axios from "axios";

export default function VeriFact() {
  let [form, setForm] = useState({ verifact: "" });
  let [formSent, setFormSent] = useState(false);
  let [summary, setSummary] = useState({
    average: 0,
    reliability: 0,
    headArticles: [
      {
        title: "",
        reliability: 0,
        bias: 0,
        summary: "",
      },
    ],
    articles: [
      {
        title: "",
        reliability: 0,
        bias: 0,
      },
    ],
  });

  let sendForm = async function () {
    let result = await axios.post("/api/input", form);
    console.log(result.data.summary);
    setSummary(result.data.summary);
    setForm({ verifact: "" });
    setFormSent(true);
  };

  let summaryPage = <div>Summary</div>;

  let formPage = (
    <div className="form-container">
      <div id="form">
        <h1>Input Verifact:</h1>
        <div className="input-box">
          <input
            id="verifact"
            value={form.verifact}
            onChange={(e) => {
              setForm({ [e.target.id]: e.target.value });
            }}
            placeholder="Verifact"
          ></input>
        </div>
        <button className="submit-button" onClick={sendForm}>
          Submit
        </button>
      </div>
    </div>
  );

  return <>{formSent ? summaryPage : formPage}</>;
}
