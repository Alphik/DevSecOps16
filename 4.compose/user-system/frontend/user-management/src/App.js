import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");

  const fetchUsers = async () => {
    const response = await axios.get("http://server:5050/users");
    setUsers(response.data);
  };

  const addUser = async (e) => {
    e.preventDefault();
    if (!name) return;

    await axios.post("http://server:5050/users", { name });
    setName("");
    fetchUsers(); // Reload users after adding
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className='app'>
      <h1>User Management</h1>
      <form onSubmit={addUser}>
        <input
          type='text'
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder='Enter user name'
          required
        />
        <button type='submit'>Add User</button>
      </form>
      <button onClick={fetchUsers}>Reload Users</button>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
