import { Container } from "react-bootstrap";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";

import ToolScreen from "./screens/ToolScreen";
import ToolDetailScreen from "./screens/ToolDetailScreen";
import ResultsScreen from "./screens/ResultsScreen";
import ResultDetailScreen from "./screens/ResultDetailScreen";

function App() {
  return (
    <Router>
      <Header />
      <main className="py-3">
        <Container>
          <Route path="/" component={ToolScreen} exact />
          <Route path="/tools/:id" component={ToolDetailScreen} />
          <Route path="/results/" component={ResultsScreen} exact />
          <Route path="/results/:id" component={ResultDetailScreen} />
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
