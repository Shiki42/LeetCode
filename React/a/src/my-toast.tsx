import react, {useState, useEffect} from "react";

interface ToastProps = {
    open: boolean;
}

export default function MyToast({open}) { 
    if (!open) return null;
    return (
        <div>
            <p>Toast</p>
        </div>
    )

}