import { useState } from "react";
import axios from "axios";
import "./VeriFact.css";

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
        relevance: 0,
        summary: "",
      },
    ],
    articles: [
      {
        id: 0,
        title: "",
        reliability: 0,
        bias: 0,
        relevance: 0,
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
        <h1 className="header">VeriFact</h1>
        <h2>Trusted Credibility Report</h2>
        <div id="bias-stat">
          <progress
            id={summary.average < 0 ? "democrat" : "republican"}
            className="bias-bar"
            value={Math.abs(summary.average)}
            max="84"
            style={{
              transform: summary.average < 0 ? "scale(-1, 1)" : "scale(1, 1)",
            }}
          >
            {" "}
            {summary.average}%{" "}
          </progress>
          <div className="bar-labels">
            <div className="left">L</div>
            <div className="right">R</div>
          </div>
          <div className="bar-text">Bias</div>
        </div>
        <div id="reliability-stat">
          <progress
            className="reliability-bar"
            value={summary.reliability}
            max="100"
          >
            {" "}
            {summary.reliability}%{" "}
          </progress>
          <div className="bar-labels">
            <div className="left">0</div>
            <div className="right">100</div>
          </div>
          <div className="bar-text">Reliability</div>
        </div>
        <div className="head-article-list">
          {summary.headArticles.map(
            ({ id, title, reliability, bias, relevance, summary }) => (
              <div key={id} className="head-article">
                <div className="head-article-header">
                  <div className="article-title">"{title}"</div>
                  <div className="head-reliability">
                    Reliability: {reliability}%
                  </div>
                  <div className="head-bias">Bias: {bias}%</div>
                  <div className="head-relevance">Relevance: {relevance}%</div>
                </div>
                <div className="head-summary">{summary}</div>
              </div>
            )
          )}
        </div>
        <div className="article-list">
          {summary.articles.map(
            ({ id, title, reliability, bias, relevance }) => (
              <div key={id} className="article">
                <div className="article-title">"{title}"</div>
                <div className="article-reliability">
                  Reliability: {reliability}%
                </div>
                <div className="article-bias">Bias: {bias}%</div>
                <div className="head-relevance">Relevance: {relevance}%</div>
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );

  let formPage = (
    <div className="form-container">
      <div id="form">
        <img src="/public/BANNER_NO_BACKY.png"></img>
        <h2>Input Verifact:</h2>
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
