import { useState } from 'react'

import './App.css'
import Toast from './toast'
const App: React.FC = () => {
  const [toastOpen, setToastOpen] = useState(false);

  return (
    <div>
      <button onClick={() => setToastOpen(true)}>Show Toast</button>
      <Toast
        open={toastOpen}
        message="This is a toast message"
        duration={5000}
        onClose={() => setToastOpen(false)}
        status="success"
      />
    </div>
  );
};


export default App
