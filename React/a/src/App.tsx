import { useState } from 'react'

import './App.css'
import Toast from './toast'
import MyToast from './my-toast';
import Styled_button from './styled_component';
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
      <Styled_button />
      <MyToast open={toastOpen}
      onclose={() => setToastOpen(false)}
      />
    </div>
  );
};


export default App
