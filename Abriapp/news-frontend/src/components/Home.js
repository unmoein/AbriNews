import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [newsList, setNewsList] = useState([]);

  const fetchNews = async () => {
    const response = await axios.get('/api/news/');
    setNewsList(response.data);
  };

  useEffect(() => {
    fetchNews();
  }, []);

  return (
    <div>
      <h2>Latest News</h2>
      <ul>
        {newsList.map((news) => (
          <li key={news.id}>
            <Link to={`/news/${news.id}`}>{news.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
