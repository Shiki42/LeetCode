import "./styles.css";

// .grid-container {
//     display: grid;
//     grid-template-columns: repeat(4, 1fr);
//     gap: 10px;
//     padding: 10px;
//   }
  
//   .grid-item {
//     border-radius: 8px;
//     border-color: black;
//     border-width: 1px;
//     padding: 10px;
//     background-color: beige;
//   }
  
//   @media (max-width: 900px) {
//     .grid-container {
//       grid-template-columns: repeat(3, 1fr);
//     }
//   }
  
//   @media (max-width: 600px) {
//     .grid-container {
//       grid-template-columns: repeat(2, 1fr);
//     }
//   }
  
//   @media (max-width: 300px) {
//     .grid-container {
//       grid-template-columns: repeat(1, 1fr);
//     }
//   }

  
const products = [
  { name: "Milk", price: "$3.49" },
  { name: "Bread", price: "$2.29" },
  { name: "Eggs", price: "$2.99" },
  { name: "Cheese", price: "$5.49" },
  { name: "Apples", price: "$1.99 per lb" },
  { name: "Bananas", price: "$0.59 per lb" },
  { name: "Tomatoes", price: "$2.99 per lb" },
  { name: "Potatoes", price: "$3.99 for 5lb" },
  { name: "Onions", price: "$1.50 for 3lb" },
  { name: "Carrots", price: "$2.00 for 2lb" },
  { name: "Cucumber", price: "$0.99" },
  { name: "Bell Peppers", price: "$1.49 each" },
  { name: "Oranges", price: "$4.99 for 4lb" },
  { name: "Grapes", price: "$2.99 per lb" },
  { name: "Chicken Breast", price: "$3.99 per lb" },
  { name: "Ground Beef", price: "$4.99 per lb" },
  { name: "Pork Chops", price: "$3.50 per lb" },
  { name: "Salmon Fillets", price: "$8.99 per lb" },
  { name: "Shrimp", price: "$12.00 per lb" },
  { name: "Tofu", price: "$2.50 per pack" },
  { name: "Yogurt", price: "$0.99 per cup" },
  { name: "Butter", price: "$3.99" },
  { name: "Ice Cream", price: "$4.50" },
  { name: "Coffee", price: "$7.99" },
  { name: "Tea", price: "$4.99" },
  { name: "Sugar", price: "$2.50 for 2lb" },
  { name: "Flour", price: "$2.00 for 2lb" },
  { name: "Rice", price: "$1.99 for 1lb" },
  { name: "Pasta", price: "$1.50" },
  { name: "Cereal", price: "$3.99" },
];

export default function App() {
  return (
    <ul className="grid-container">
      {products.map((product) => {
        return <div className="grid-item">{product.name}</div>;
      })}
    </ul>
  );
}
