import React from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import GridLayout from 'react-grid-layout'

import './App.css';
import Grid from './components/Grid';
import Todos from './components/Todos';
import Header from './components/layout/Header';
import AddTodo from './components/AddTodo';
import About from './components/pages/About';

class App extends React.Component {
  state = {
    todos: []
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/v1/todo/list')
      .then(res => this.setState({ todos: res.data }))
  }

  // Toggle Complete
  markDone = (todo) => {
    const { id, description, notes, deadline, done } = todo;
    axios.put(`http://localhost:8000/api/v1/todo/${id}`, {
      description,
      notes,
      deadline,
      done: !done
    });
    this.setState({
      todos: this.state.todos.map(todo => {
        if (todo.id === id) {
          todo.done = !todo.done;
        }
        return todo;
      })
    })
  }

  addTodo = (description, notes) => {
    axios.post('http://localhost:8000/api/v1/todo/list', {
      description,
      notes,
      deadline: null,
      done: false
    }).then(res => this.setState({ todos: [...this.state.todos, res.data] }))
  }

  delTodo = (id) => {
    axios.delete(`http://localhost:8000/api/v1/todo/${id}`)
      .then(res => this.setState({
        todos: [...this.state.todos.filter(todo => todo.id !== id)]
      }));
  }

  render() {
    const layout = [
      { i: 'a', x: 0, y: 0, w: 10, h: 16 },
      { i: 'b', x: 10, y: 10, w: 10, h: 16 },
    ];

    return (
      <Router>
        <div className="App" >
          <div className="container">
            <Header />
            <AddTodo addTodo={this.addTodo} />
            <GridLayout className="layout" layout={layout} cols={12} rowHeight={30} width={1200}>
              <div key="a"><Todos todos={this.state.todos} delTodo={this.delTodo} markDone={this.markDone} /></div>
              <div key="b"><Todos todos={this.state.todos} delTodo={this.delTodo} markDone={this.markDone} /></div>
            </GridLayout>
            {/* <Route exact path="/" render={props => (
              <React.Fragment>
              </React.Fragment>
            )} />
            <Route path="/about" component={About} /> */}
          </div>
        </div>
      </Router>
    );
  }
}

export default App;
