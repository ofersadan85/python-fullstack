import { Link } from "react-router-dom"
import "./NavBar.css"

export default function NavBar() {
    return <nav>
        <ul>
        <li className="navLink"><Link to="/">Home</Link></li>
        <li className="navLink"><Link to="/login">Login</Link></li>
        <li className="navLink"><Link to="/register">Register</Link></li>
        <li className="navLink"><Link to="/admin">Admin</Link></li>
        </ul>
    </nav>
}
