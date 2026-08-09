import { useState, useEffect } from 'react';
import './App.css';

function App ()
{
const [books, setBooks] = useState([]);

useEffect(() => {
  fetch('http://localhost:8000/api/books/')
  .then(res => res.json())
  .then(data => setBooks(data));
 }, []);

return (
  <div className="App">

  <header className="App-header">
    <h1>My Book Log</h1>
    <ul>
      {books.map(book => (
        <li key={book.id}>{book.title}</li>
       ))}

  </ul>


  </header>

  </div>
);
}
export default App;







