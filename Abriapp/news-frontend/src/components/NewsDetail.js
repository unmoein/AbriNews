import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const NewsDetail = () => {
  const { id } = useParams();
  const [news, setNews] = useState(null);
  const [comments, setComments] = useState([]);
  const [comment, setComment] = useState('');
  const [relatedNews, setRelatedNews] = useState([]);
  const { user } = useContext(AuthContext);

  const fetchNews = async () => {
    try {
      const response = await axios.get(`/api/news/${id}/`);
      setNews(response.data);
    } catch (error) {
      console.error('Error fetching news:', error);
    }
  };

  const fetchComments = async () => {
    try {
      const response = await axios.get(`/api/news/${id}/comments/`);
      setComments(response.data);
    } catch (error) {
      console.error('Error fetching comments:', error);
    }
  };

  const fetchRelatedNews = async () => {
    try {
      const response = await axios.get(`/api/news/?exclude=${id}&limit=5`);
      setRelatedNews(response.data);
    } catch (error) {
      console.error('Error fetching related news:', error);
    }
  };

  useEffect(() => {
    fetchNews();
    fetchComments();
    fetchRelatedNews();
  }, [id]);

  const handleAddComment = async () => {
    const accessToken = localStorage.getItem('access_token');
    try {
      await axios.post(
        `/api/news/${id}/comment/`,
        { comment },
        { headers: { Authorization: `Bearer ${accessToken}` } }
      );
      setComment('');
      fetchComments();
    } catch (error) {
      console.error('Error adding comment:', error);
    }
  };

  const handleLike = async () => {
    const accessToken = localStorage.getItem('access_token');
    try {
      await axios.post(
        `/api/news/${id}/like/`,
        {},
        { headers: { Authorization: `Bearer ${accessToken}` } }
      );
      fetchNews();
    } catch (error) {
      console.error('Error liking news:', error);
    }
  };

  if (!news) return <div>Loading...</div>;

  return (
    <div>
      <h2>{news.title}</h2>
      <p>{news.body}</p>
      <p>Published on: {new Date(news.publish_date).toLocaleString()}</p>
      <p>Publisher: {news.publisher}</p>
      <button onClick={handleLike}>
        {news.likes_count > 0 ? `Unlike (${news.likes_count})` : `Like`}
      </button>
      
      <h3>Comments ({news.comments_count})</h3>
      <ul>
        {comments.map((c) => (
          <li key={c.id}>
            <strong>{c.user}:</strong> {c.comment}
          </li>
        ))}
      </ul>
      
      <h3>Related News</h3>
      <ul>
        {relatedNews.map((n) => (
          <li key={n.id}>
            <Link to={`/news/${n.id}`}>{n.title}</Link>
          </li>
        ))}
      </ul>
      
      {user && (
        <div>
          <textarea
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            placeholder="Add a comment"
          ></textarea>
          <button onClick={handleAddComment}>Submit</button>
        </div>
      )}
    </div>
  );
};

export default NewsDetail;
