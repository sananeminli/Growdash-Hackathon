
import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Home from "./Components/Home";
import BranchDetails from "./Components/BranchDetails";

function App() {


  return (
    <>
      <Router >
        <Routes>
          <Route path="/branchdetails/:id" Component={BranchDetails} />
          <Route path="/" Component={Home} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
