import { useEffect, useRef, useState } from "react"

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL as string;

export type User = {
  id: number
  username: string
  password: string
  email: string | null
  age: number | null
}

export type PublicUser = {
  id: number
  username: string
  email: string | null
  age: number | null
}

export type NewUser = {
  username: string
  password: string
  email: string | null
  age: number | null
}

export function userRow(user: PublicUser) {
  // TODO: Refresh the table when a user is deleted
  function deleteUser() {
    fetch(BACKEND_URL + "/users/" + user.id, {
      method: "DELETE"
    }).then(() => { console.log("User deleted: ", user.id); })
      .catch((error) => alert("Error deleting user: " + error));
  }

  return (
    <tr key={user.id}>
      <td>{user.id}</td>
      <td>{user.username}</td>
      <td>{user.email}</td>
      <td>{user.age}</td>
      <td><button onClick={deleteUser}>Delete</button></td>
    </tr>
  );
}


export function UserTable({ refresh }: { refresh: boolean }) {
  const [users, setUsers] = useState<PublicUser[]>([]);

  useEffect(() => {
    const url = BACKEND_URL + "/users";
    fetch(url)
      .then(response => response.json())
      .then((users: PublicUser[]) => setUsers(users))
  }, [refresh]);

  // TODO: Add validation for users - if the user is not valid, don't display it or display an error message
  // TODO: Add a loading spinner animation while the users are being fetched

  return <table>
    <thead>
      <tr>
        <th>Id</th>
        <th>Username</th>
        <th>Email</th>
        <th>Age</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      {users.map(userRow)}
    </tbody>
  </table>;
}


type CreateUserFormProps = { setRefresh: React.Dispatch<React.SetStateAction<boolean>> }

export function CreateUserForm({ setRefresh }: CreateUserFormProps) {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const emailRef = useRef<HTMLInputElement>(null);
  const ageRef = useRef<HTMLInputElement>(null);

  function createUser() {
    const userData: NewUser = {
      username: usernameRef.current?.value || "",
      password: passwordRef.current?.value || "",
      email: emailRef.current!.value || null,
      age: Number(ageRef.current?.value) || null
    };
    fetch(BACKEND_URL + "/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData)
    }).then(() => { setRefresh(prev => !prev) })
      .catch((error) => alert("Error creating user: " + error));
  }

  return <>
    <input type="text" name="username" placeholder="Username" ref={usernameRef} />
    <input type="password" name="password" placeholder="Password" ref={passwordRef} />
    <input type="email" name="email" ref={emailRef} />
    <input type="number" name="age" ref={ageRef} />
    <button onClick={createUser}>Add User</button>
    {import.meta.env.DEV && <button onClick={() => setRefresh(prev => !prev)}>Refresh Table</button>}
  </>;
}

export default function App() {
  const [refresh, setRefresh] = useState<boolean>(false);
  return <>
    <CreateUserForm setRefresh={setRefresh} />
    <UserTable refresh={refresh} />
  </>
}
