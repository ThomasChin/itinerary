import React from 'react';
import PropTypes from 'prop-types';

import TodoItem from './TodoItem';

class Todos extends React.Component {
  render() {
    return this.props.todos.map((todo) => (
      <TodoItem key={todo.id} todo={todo} delTodo={this.props.delTodo} markDone={this.props.markDone} />
    ));
  }
}

Todos.propTypes = {
  todos: PropTypes.array.isRequired,
  markDone: PropTypes.func.isRequired,
  delTodo: PropTypes.func.isRequired
}

export default Todos;
