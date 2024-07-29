import react, {useState, useEffect} from "react";

interface ToastProps {
    open: boolean;
}

const Toast: React.FC<ToastProps> = (props) => { 
    if (!props.open) return null;
    return (
        <div>
            <p>Toast</p>
        </div>
    )

}

export default Toast;