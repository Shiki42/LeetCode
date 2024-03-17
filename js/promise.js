function promiseAll(iterable) {
    return new Promise((resolve, reject) => {
      const results = new Array(iterable.length);
      let unresolved = iterable.length;
  
      if (unresolved === 0) {
        resolve(results);
        return;
      }
  
      iterable.forEach(async (item, index) => {
        try {
          console.log('item', item, 'index', index)
          const value = await item;
          results[index] = value;
          unresolved -= 1;
  
          if (unresolved === 0) {
            resolve(results);
          }
        } catch (err) {
          reject(err);
        }
      });
    });
  }
promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('promise1');
    }, 3000);
});
promise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('promise2');
    }, 3000);
});
promise3 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('promise3');
    }, 3000);
});

test_data = [promise1, promise2, promise3]

promiseAll(test_data).then((values) => {
    console.log(values);
});