// import React from 'react';
// import { Routes, Route, Link } from 'react-router-dom';
// import Home from './pages/Home';
// import AboutUs from './pages/AboutUs';
// import Contact from './pages/Contact';
// import Predict from './pages/Predict';
// import './App.css';

// function App() {
//   return (
//     <div>
//       {/* Header */}
//       <header className="header">
//         <div className="logo">PlantCare</div>
//         <nav className="navbar">
//           <Link to="/" className="nav-link">Home</Link>
//           <Link to="/about" className="nav-link">About Us</Link>
//           <Link to="/contact" className="nav-link">Contact</Link>
//           <Link to="/predict" className="nav-link">Predict</Link>
//         </nav>
//       </header>

//       {/* Main Content */}
//       <main>
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/about" element={<AboutUs />} />
//           <Route path="/contact" element={<Contact />} />
//           <Route path="/predict" element={<Predict />} />
//         </Routes>
//       </main>

//       {/* Footer */}
//       <footer>
//         <p>© 2025 PlantCare. All Rights Reserved.</p>
        
//       </footer>
//     </div>
//   );
// }

// import React from 'react';
// import { Routes, Route, Link } from 'react-router-dom';
// import Home from './pages/Home';
// import AboutUs from './pages/AboutUs';
// import Contact from './pages/Contact';
// import Predict from './pages/Predict';
// import './App.css';

// function App() {
//   return (
//     <div className="app-container">
//       {/* Header */}
//       <header className="header">
//         <div className="logo">PlantCare</div>
//         <nav className="navbar">
//           <Link to="/" className="nav-link">Home</Link>
//           <Link to="/about" className="nav-link">About Us</Link>
//           <Link to="/contact" className="nav-link">Contact</Link>
//           <Link to="/predict" className="nav-link btn-primary">Predict</Link>
//         </nav>
//       </header>

//       {/* Main Content */}
//       <main className="main-content">
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/about" element={<AboutUs />} />
//           <Route path="/contact" element={<Contact />} />
//           <Route path="/predict" element={<Predict />} />
//         </Routes>
//       </main>

//       {/* Footer */}
//       <footer className="footer">
//         <p>© 2025 PlantCare. All Rights Reserved.</p>
//       </footer>
//     </div>
//   );
// }

// export default App;


import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import AboutUs from './pages/AboutUs';
import Contact from './pages/Contact';
import Predict from './pages/Predict';
import './App.css';

function App() {
  return (
    <div className="app-container">
      {/* Wavy Background */}
      <div className="wavy-bg"></div>

      {/* Header */}
      <header className="header">
        <div className="logo">PlantCare</div>
        <nav className="navbar">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/about" className="nav-link">About Us</Link>
          <Link to="/contact" className="nav-link">Contact</Link>
          <Link to="/predict" className="nav-link">Predict</Link>
        </nav>
      </header>

      {/* Main Content */}
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<AboutUs />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/predict" element={<Predict />} />
        </Routes>
      </main>

      {/* Footer */}
      <footer>
        <p>© 2025 PlantCare. All Rights Reserved.</p>
      </footer>
    </div>
  );
}


export default App;

