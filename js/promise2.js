async function fn (n) { await new Promise(res => setTimeout(res, 100)); return n * n; }
async function d(){
    var a = new Promise((resolve, reject) => {
        setTimeout(() => {
            reject('promise1');
        }, 300);
    });
    
    c = await a;
    console.log(c);
}

d();