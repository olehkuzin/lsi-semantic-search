import React, { useState, useEffect } from "react";
import "./home.css";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]); // State to store search results
  const [currentIndex, setCurrentIndex] = useState(0); // State to track the current visible item
  useEffect(() => {
    document.title = "Vector LSI Search"; // Set tab title
  }, []);
  const handleInputChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Sending request to the server
    try {
      const response = await fetch("http://127.0.0.1:5000/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      if (!response.ok) {
        throw new Error("Network error");
      }

      const data = await response.json();
      console.log("Server response:", data);
      setResults(data.results); // Save results in state
      setCurrentIndex(0); // Reset to the first item when new results arrive
    } catch (error) {
      console.error("Request sending error:", error);
    }

    // Clear the input field
    setQuery("");
  };

  // Function to navigate to the previous item
  const showPrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex > 0 ? prevIndex - 1 : prevIndex
    );
  };

  // Function to navigate to the next item
  const showNext = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex < results.length - 1 ? prevIndex + 1 : prevIndex
    );
  };

  return (
    <div className="container">
      <h1 className="title">Enter your query</h1>
      <form onSubmit={handleSubmit} className="input-container">
        <input
          type="text"
          className="input"
          placeholder="Write your query here..."
          value={query}
          onChange={handleInputChange}
        />
        <button type="submit" className="button">
          Submit
        </button>
      </form>

      {/* Display results in a carousel */}
      {results.length === 5 && (
        <div className="carousel-container">
          <h2>Search result for your request: "{results[currentIndex].quer}"</h2>
          <div className="carousel-wrapper">

            <button className="carousel-button left" onClick={showPrevious}>
              &#10094; {/* Left arrow */}
            </button>
            <div className="carousel-item">
              <h3>Topic: {results[currentIndex].tit}</h3> {/* Document Title */}
              <div className="content">
                {results[currentIndex].con} {/* Document Content */}
              </div>
                <p>{currentIndex === 0
                  ? "Source article"
                  : `Match score: ${results[currentIndex].sc}%`}
                </p>
            </div>
            <button className="carousel-button right" onClick={showNext}>
              &#10095; {/* Right arrow */}
            </button>
          </div>
          <div className="carousel-indicator">
            {currentIndex + 1} / {results.length} {/* Current position indicator */}
          </div>
        </div>
      )}

      {results.length === 1 && (
        <div>
          <h2>No matches found for your request: "{results[currentIndex].quer}"</h2>
        </div>
      )}
    </div>
  );
}