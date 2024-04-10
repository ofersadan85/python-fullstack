import { useNavigate } from "react-router-dom";

export default function LoginPage() {
    const navigate = useNavigate();

    function doLogin(goHome: boolean) {
        if (goHome) {
            console.log("Navigating home");
            navigate("/");
        } else {
            console.log("Doing nothing")
        }
    }

    return <>
        <h2>Login Page</h2>
        <button onClick={() => doLogin(true)}>Login NOW</button>
    </>
}
