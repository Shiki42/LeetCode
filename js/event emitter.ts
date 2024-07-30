type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    cache = {}
    subscribe(eventName: string, callback: Callback): Subscription {
        this.cache[eventName] = this.cache[eventName] ?? [];
        this.cache[eventName].push(callback)
        return {
            unsubscribe: () => {
                this.cache[eventName] = this.cache[eventName].filter((cb)=>cb != callback);
                if (this.cache[eventName].length == 0) delete this.cache[eventName];
            }
        };
    }
    
    emit(eventName: string, args: any[] = []): any[] {
        if(this.cache[eventName] != undefined){
            return this.cache[eventName].map((cb)=>{return cb(...args)});
        }
        return [];
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */