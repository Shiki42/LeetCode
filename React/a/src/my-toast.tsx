import react, {useState, useEffect} from "react";

import styled from "styled-components";


interface ToastProps {
    open: boolean;
    onclose: () => void;
}

const ToastWrapper = styled.div`
    position: fixed;
    top: 1rem;
    right: 1rem;
    padding: 1rem;
    background-color: green;
    color: white;
    border-radius: 5px;
`

const Toast: React.FC<ToastProps> = (props) => { 
    useEffect(() => {
        const timer = setTimeout(() => {
            props.onclose();
        }, 1000);
        return () => {
            clearTimeout(timer);
        };
    }, [props.open]);

    if (!props.open) return null;

    return (
        <ToastWrapper>
            <p>Toast</p>
        </ToastWrapper>
    )

}

export default Toast;