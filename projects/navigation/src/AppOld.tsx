
import { useState } from 'react'
import './App.css'
import AdminPage from './pages/AdminPage'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'

export default function App() {

    // window.history.pushState(null, "", "/login")

    const lastPage = localStorage.getItem("lastPage") || "home";
    let defaultPage;
    if (lastPage === "home") {
        defaultPage = <HomePage />
    } else if (lastPage === "login") {
        defaultPage = <LoginPage />
    } else if (lastPage === "register") {
        defaultPage = <RegisterPage />
    // } else if (lastPage === "/admin") {
    //     defaultPage = <AdminPage setCurrentPage={setCurrentPage} />/>
    } else {
        defaultPage = <HomePage />
    }

    const [currentPage, setCurrentPage] = useState(defaultPage);

    function changePage(page: JSX.Element, pageName: string) {
        setCurrentPage(page);
        // localStorage.setItem("lastPage", pageName);
        window.history.pushState(null, "", "/" + pageName)
    }
    console.log("we are here")
    return <>
        {currentPage}
        <button onClick={() => changePage(<HomePage />, "home")}>Go to home page</button>
        <button onClick={() => changePage(<LoginPage />, "login")}>Go to login page</button>
        <button onClick={() => changePage(<RegisterPage />, "register")}>Go to register page</button>
        <button onClick={() => changePage(<AdminPage setCurrentPage={setCurrentPage} />, "admin")}>Go to admin page</button>
    </>

    // if (window.location.pathname === "/") {
    //     return 
    // } else if (window.location.pathname === "/login") {
    //     return <LoginPage />
    // } else if (window.location.pathname === "/register") {
    //     return <RegisterPage />
    // } else if (window.location.pathname === "/admin") {
    //     return <AdminPage />
    // } else {
    //     return <HomePage />
    // }
}
