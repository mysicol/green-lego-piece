import { useState, useEffect } from "react";
import axios from "axios";

export default function Example() {
  let fetchExample = async () => {
    let response = await axios.get("/api/example");
    console.log(response);
  };

  useEffect(() => {
    fetchExample();
  }, []);

  return <></>;
}
