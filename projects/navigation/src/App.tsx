
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import NavBar from './components/NavBar'
import AdminPage from './pages/AdminPage'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'
import SecondAdminPage from './pages/SecondAdminPage'

export default function App() {
    // <Link to="/"><button>Go to home page</button></Link>
    // <Link to="/login"><button>Go to login page</button></Link>
    // <Link to="/register"><button>Go to register page</button></Link>
    // <Link to="/admin"><button>Go to admin page</button></Link>

    return <>
        <BrowserRouter>
            <NavBar />
            <Routes>
                <Route path='/' element={<HomePage />} />
                <Route path='/home' element={<HomePage />} />
                <Route path='/login' element={<LoginPage />} />
                <Route path='/register' element={<RegisterPage />} />
                <Route path='/admin' element={<AdminPage />} />
                <Route path='/admin2' element={<SecondAdminPage />} />
            </Routes>
            <footer>This is a footer</footer>
        </BrowserRouter>
    </>
}