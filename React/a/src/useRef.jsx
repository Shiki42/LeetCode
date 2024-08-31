import "./styles.css";
import { useRef, useState, useEffect } from "react";
export default function App() {
  const [isVisible, setIsvisible] = useState(false);
  const alertRef = useRef(null);
  useEffect(() => {
    if (isVisible && alertRef.current) {
      alertRef.current.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }, [isVisible]);
  return (
    <div className="App">
      <button
        onClick={() => {
          setIsvisible(!isVisible);
        }}
      >
        ALERT
      </button>
      <div className="a">space </div>
      {isVisible && <p ref={alertRef}>Alert Message</p>}

      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
}
