import { useEffect, useRef, useState } from "react";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL as string;

export type UserDataProps = {
    setUserToken: (userId: string | null) => void
}

export function LoginForm({ setUserToken }: UserDataProps) {
    const usernameRef = useRef<HTMLInputElement>(null);
    const passwordRef = useRef<HTMLInputElement>(null);

    return <div>
        <h2>Login</h2>
        <input type="text" name="username" placeholder="Username" ref={usernameRef} />
        <input type="password" name="password" placeholder="Password" ref={passwordRef} />
        <button onClick={() => {
            const username = usernameRef.current?.value || "";
            const password = passwordRef.current?.value || "";
            fetch(BACKEND_URL + "/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            })
                .then(response => response.json())
                .then(data => {
                    localStorage.setItem("access_token", data.access_token);
                    setUserToken(data.access_token);
                })
                .catch((error) => alert("Error logging in: " + error));
        }}>Login</button>
    </div>;
}

export function UserProfile({ setUserToken }: UserDataProps) {
    const [userData, setUserData] = useState<any>(null);
    useEffect(() => {
        fetch(BACKEND_URL + "/users/me", { headers: { "Authorization": "Bearer " + localStorage.getItem("access_token") } })
            .then(response => response.json())
            .then(data => setUserData(data))
    }, []);

    if (userData) {
        return <>
            <h2>Current User</h2>
            <p>Username: {userData.username}</p>
            <p>Email: {userData.email}</p>
            <p>Age: {userData.age}</p>
            <p>Role: {userData.role}</p>
            <p><button onClick={() => {
                localStorage.removeItem("access_token");
                setUserToken(null);
            }}>Logout</button></p>
        </>
    } else {
        return <h2>Loading...</h2>;
    }
}

export default function App() {
    const [userToken, setUserToken] = useState<string | null>(null);
    console.log("userToken", userToken);
    return <>
        <h1>Login example</h1>
        <p>If something is not working for you, try clearing local storage and reloading</p>
        <p>Token: {localStorage.getItem("access_token")}</p>
        {userToken ? <UserProfile setUserToken={setUserToken} /> : <LoginForm setUserToken={setUserToken} />}
    </>
}
