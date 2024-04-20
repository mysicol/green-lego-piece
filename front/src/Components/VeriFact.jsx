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
        id: 0,
        title: "",
        reliability: 0,
        bias: 0,
        summary: "",
      },
    ],
    articles: [
      {
        id: 0,
        title: "",
        reliability: 0,
        bias: 0,
      },
    ],
  }); // default data

  let sendForm = async function () {
    let result = await axios.post("/api/input", form);
    console.log(result.data.summary);
    setSummary(result.data.summary);
    setForm({ verifact: "" });
    setFormSent(true);
  };

  let summaryPage = (
    <div className="summary-container">
      <div id="summary">
        <h1>Bias Bar: {summary.average}</h1>
        <h1>Reliability Bar: {summary.reliability}</h1>
        <div className="head-article-list">
          {summary.headArticles.map(
            ({ id, title, reliability, bias, summary }) => (
              <div key={id} className="head-article">
                <div className="head-title">{title}</div>
                <div className="head-reliability">{reliability}</div>
                <div className="head-bias">{bias}</div>
                <div className="head-summary">{summary}</div>
              </div>
            )
          )}
        </div>
        <div className="article-list">
          {summary.articles.map(({ id, title, reliability, bias }) => (
            <div key={id} className="article">
              <div className="article-title">{title}</div>
              <div className="article-reliability">{reliability}</div>
              <div className="article-bias">{bias}</div>
            </div>
          ))}
        </div>
        <div className="article-list"></div>
      </div>
    </div>
  );

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
