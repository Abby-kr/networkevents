import Home from "./home"
import About from "./about";
import NavBar from './navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Router>
        <Routes>
          <Route path={"/"} element={<Home/>} />
          <Route path={"/about"} element={<About/>} />
          {/* <Route path={"/counsellors"} element={<Counsellors/>} />
          <Route path={"/signup"} element={<SignupForm />} />
           <Route path={"/events"} element={<EventsList />} />
             <Route path={"/contact"} element={<Contact />} /> */}
        </Routes>
      </Router>
    </div>
  );
}

export default App;

