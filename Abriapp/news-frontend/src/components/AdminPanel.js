import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdminPanel = () => {
  const [newsList, setNewsList] = useState([]);
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');

  const fetchNews = async () => {
    const response = await axios.get('/api/news/');
    setNewsList(response.data);
  };

  useEffect(() => {
    fetchNews();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const accessToken = localStorage.getItem('access_token');
    try {
      await axios.post(
        '/api/news/create/',
        { title, body },
        { headers: { Authorization: `Bearer ${accessToken}` } }
      );
      fetchNews();
    } catch (error) {
      console.error('Error creating news:', error);
    }
  };

  return (
    <div>
      <h2>Admin Panel</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <textarea
          placeholder="Body"
          value={body}
          onChange={(e) => setBody(e.target.value)}
          required
        ></textarea>
        <button type="submit">Publish News</button>
      </form>
      <h3>Published News</h3>
      <ul>
        {newsList.map((news) => (
          <li key={news.id}>{news.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default AdminPanel;
