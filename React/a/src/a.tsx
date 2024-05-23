import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

const style = {
  table: {
    borderCollapse: 'collapse'
  },
  tableCell: {
    border: '1px solid gray',
    margin: 0,
    padding: '5px 10px',
    width: 'max-content',
    minWidth: '150px'
  },
  form: {
    container: {
      padding: '20px',
      border: '1px solid #F0F8FF',
      borderRadius: '15px',
      width: 'max-content',
      marginBottom: '40px'
    },
    inputs: {
      marginBottom: '5px'
    },
    submitBtn: {
      marginTop: '10px',
      padding: '10px 15px',
      border:'none',
      backgroundColor: 'lightseagreen',
      fontSize: '14px',
      borderRadius: '5px'
    }
  }
}

function PhoneBookForm({ addEntryToPhoneBook }) {

  const [firstName, setFirstName] = useState('Code');
  const [lastName, setLastName] = useState('Byte');
  const [phone, setPhone] = useState('8885559999');

  function onFormSubmit(e) {
    e.preventDefault();
    const newEntry = {firstName, lastName, phone};
    addEntryToPhoneBook(newEntry);

    setFirstName('');
    setLastName('');
    setPhone('');
  }

  return (
    <form onSubmit={e => { onFormSubmit(e) }} style={style.form.container}>
      <label>First name:</label>
      <br />
      <input
        value={firstName}
        style={style.form.inputs}
        className='userFirstname'
        name='userFirstname' 
        type='text'
        onChange={e => setFirstName(e.target.value)}
      />
      <br/>
      <label>Last name:</label>
      <br />
      <input 
        value={lastName}
        style={style.form.inputs}
        className='userLastname'
        name='userLastname' 
        type='text'
        onChange={e => setLastName(e.target.value)}
      />
      <br />
      <label>Phone:</label>
      <br />
      <input
        value={phone}
        style={style.form.inputs}
        className='userPhone' 
        name='userPhone' 
        type='text'
        onChange={e => setPhone(e.target.value)}
      />
      <br/>
      <input 
        style={style.form.submitBtn} 
        className='submitButton'
        type='submit' 
        value='Add User' 
      />
    </form>
  )
}

function InformationTable(props) {
  return (
    <table style={style.table} className='informationTable'>
      <thead> 
        <tr>
          <th style={style.tableCell}>First name</th>
          <th style={style.tableCell}>Last name</th>
          <th style={style.tableCell}>Phone</th>
        </tr>
      </thead> 
      <tbody>
        {props.phoneList.map((row, index) => (
          <tr key={index}>
          <td style={style.tableCell}>{row.firstName}</td>
          <td style={style.tableCell}>{row.lastName}</td>
          <td style={style.tableCell}>{row.phone}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

function Application(props) {
  const [phoneList,setPhoneList] = useState([]);
  function addEntryToPhoneBook(newEntry){
    const updatedPhoneList = [...phoneList, newEntry];
    updatedPhoneList.sort((a,b) => a.lastName.localeCompare(b.lastName));
    setPhoneList(updatedPhoneList);
  }
  return (
    <section>
      <PhoneBookForm addEntryToPhoneBook={addEntryToPhoneBook}/>
      <InformationTable phoneList={phoneList}/>
    </section>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<Application />);