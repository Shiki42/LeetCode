import react, {useState, useEffect} from "react";

interface ToastProps {
    open: boolean;
    onclose: () => void;
}

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
        <div>
            <p>Toast</p>
        </div>
    )

}

export default Toast;