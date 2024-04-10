import { Link } from "react-router-dom";

export default function AdminPage() {
    return <>
        <h2>Admin Page</h2>
        <Link to="/admin2"><button>Go to the second admin page</button></Link>
    </>
}
