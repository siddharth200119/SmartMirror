import React, { useState, useEffect } from "react";
import "./News.css"

//7ae23b4eb7f44561866b51a3b4493b90

function News(props) {

  let preferences = props.preferences
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetch(`https://newsapi.org/v2/top-headlines?q=${preferences}&pageSize=100&sortBy=publishedAt&apiKey=7ae23b4eb7f44561866b51a3b4493b90`, {
      method: "GET"
    })
      .then((response) => response.json())
      .then((data) => {
        setNews(data.articles);
        console.log(data.articles);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div className='News_widget'>
      <h3>News</h3>
      <hr></hr>
        {news?.map((article) =>
          <p>{article.title}</p>
        )}
    </div>
  );
}

export default News;
