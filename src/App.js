import './App.css';
import React, { useState, useEffect } from 'react';
import LanguageCard from './components/LanguageCard';

const App = () => {
  const [languages, setLanguages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL + '/languages')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        const parsedData = data.body ? JSON.parse(data.body) : data;
        if (Array.isArray(parsedData)) {
          setLanguages(parsedData);
        } else {
          console.error('Invalid data format received:', parsedData);
        }
      })
      .catch(error => console.error('Error fetching data:', error))
      .finally(() => setLoading(false));
  }, []);

  const handleVote = language => {
    fetch(process.env.REACT_APP_API_URL + `/languages/${language}/vote`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        operation: 'update',
        payload: { language },
      }),
    })
      .then(response => response.json())
      .then(() => {
        fetch(process.env.REACT_APP_API_URL + '/languages')
          .then(response => response.json())
          .then(data => {
            const parsedData = data.body ? JSON.parse(data.body) : data;
            if (Array.isArray(parsedData)) {
              setLanguages(parsedData);
            } else {
              console.error('Invalid data format received:', parsedData);
            }
          })
          .catch(error => console.error('Error fetching data:', error));
      })
      .catch(error => console.error('Error updating vote:', error));
  };  

  return (
    <div className="container mx-auto">
      <div class="flex justify-center items-center h-full mt-8">
        <p class="font-bold text-3xl text-center">
          Vote for your 2024
          <span class="text-gray-700 mx-1 font-extrabold text-4xl relative inline-block stroke-current">
            Favourite
            <svg class="absolute -bottom-0.5 w-full max-h-1.5" viewBox="0 0 55 5" xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="none">
              <path d="M0.652466 4.00002C15.8925 2.66668 48.0351 0.400018 54.6853 2.00002" stroke-width="2"></path>
            </svg>
          </span>
          language!
        </p>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-0">
        {languages.map(language => (
          <LanguageCard key={language.Language} language={language} handleVote={handleVote} />
        ))}
      </div>
    </div>
  );
};

export default App;
