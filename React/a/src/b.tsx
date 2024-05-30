import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

const style = {
  container: {
    padding: '20px',
    border: '1px solid #E0E0E0',
    borderRadius: '15px',
    width: 'max-content',
    marginBottom: '40px',
  },
  question: {
    fontWeight: 'bold',
    marginBottom: '10px',
  },
  options: {
    marginBottom: '5px',
  },
  button: {
    marginTop: '10px',
    padding: '10px 15px',
    border: 'none',
    backgroundColor: '#007BFF',
    color: '#FFF',
    fontSize: '14px',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  feedback: {
    marginTop: '10px',
    fontSize: '14px',
  },
};

function QuizApp() {
  // do not modify the questions or answers below
  const questions = [
    {
      question: 'What is the capital of France?',
      options: ['London', 'Paris', 'Berlin', 'Madrid'],
      correct: 'Paris',
    },
    {
      question: 'What is the capital of Germany?',
      options: ['Berlin', 'Munich', 'Frankfurt', 'Hamburg'],
      correct: 'Berlin',
    },
  ];

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [userAns, setUserAns] = useState('');
  const [feedback, setFeedback] = useState('');
  const [complete, setComplete] = useState(false);

  function onAnsChange(e) {
    setUserAns(e.target.value);
  }

  function onSubmit(e) {

    e.preventDefault();

    if (complete) return;

    if (userAns === questions[currentQuestion].correct) {
      setFeedback('Correct!');
      setScore(score + 1);
    } else {
      setFeedback('Incorrect!');
    }
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else if(currentQuestion == questions.length - 1) {
      setFeedback(`Quiz Complete! You scored ${score + (userAns === questions[currentQuestion].correct ? 1 : 0)} out of ${questions.length}!`);
      setComplete(true);
    } 
  };
  return (
    <div style={style.container}>
      <div id="question" style={style.question}>
        {questions[currentQuestion].question}</div>
      <form onSubmit={onSubmit}>
        <div style={style.options}>
          {questions[currentQuestion].options.map((option,index) => (
            <div key={index}>
             <input
                type='radio'
                id={`input${index +1}`}
                value={option}
                checked={userAns === option}
                onChange={onAnsChange}
              />
              <label htmlFor={`input${index +1}`}>{option}</label>
            </div>
          ))}
        </div>
      <button style={style.button} id="submitBtn">
        Submit
      </button>
      </form>
      <div id="feedback" style={style.feedback}>{feedback}</div>
    </div>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<QuizApp />);