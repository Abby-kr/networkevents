import React from 'react'
//import './navbar.css'

const NavBar=()=>{
    
    return (
        <nav className="navbar">
            <div className="container-fluid">
                <a className="navbar-brand" href="/">BigEvents</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/">Home</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/events">Events</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/about">About</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/contact">Contact Us</a>
                        </li>
                        <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="/signup">Sign up</a>
                        </li> 
                    </ul>
                </div>
            </div>
            </nav>
    )
}

export default NavBar