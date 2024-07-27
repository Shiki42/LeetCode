// Toast.tsx
import React, { useEffect } from 'react';
import styled, { css, keyframes } from 'styled-components';

interface ToastProps {
  open: boolean;
  message: string;
  duration?: number;
  onClose: () => void;
  status?: 'success' | 'error' | 'info';
}

const toastIn = keyframes`
  from {
    opacity: 0;
    transform: translateY(-20%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
`;

const toastOut = keyframes`
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(-20%);
  }
`;

const ToastWrapper = styled.div<{ status?: 'success' | 'error' | 'info'; animateOut: boolean }>`
  position: fixed;
  top: 1rem;
  right: 1rem;
  padding: 1rem;
  background-color: ${({ status }) => {
    switch (status) {
      case 'success':
        return 'green';
      case 'error':
        return 'red';
      case 'info':
        return 'blue';
      default:
        return 'gray';
    }
  }};
  color: white;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  animation: ${({ animateOut }) => (animateOut ? css`${toastOut} 0.5s forwards` : css`${toastIn} 0.5s forwards`)};
`;

const CloseButton = styled.button`
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
`;

const Toast: React.FC<ToastProps> = ({ open, message, duration = 3000, onClose, status }) => {
  const [visible, setVisible] = React.useState(open);
  const [animateOut, setAnimateOut] = React.useState(false);

  useEffect(() => {
    let timer: ReturnType<typeof setTimeout>;
    if (open) {
      setVisible(true);
      setAnimateOut(false);
      timer = setTimeout(() => {
        setAnimateOut(true);
        setTimeout(onClose, 500); // Wait for animation to finish before closing
      }, duration);
    } else {
      setAnimateOut(true);
      setTimeout(() => setVisible(false), 500);
    }
    return () => clearTimeout(timer);
  }, [open, duration, onClose]);

  if (!visible) return null;

  return (
    <ToastWrapper status={status} animateOut={animateOut}>
      {message}
      <CloseButton onClick={onClose}>×</CloseButton>
    </ToastWrapper>
  );
};

export default Toast;