import React from 'react';
import PropTypes from 'prop-types';

class TodoItem extends React.Component {
  getStyle = () => {
    return {
      background: '#f4f4f4',
      padding: '10px',
      borderBottom: '1px #ccc dotted',
      textDecoration: this.props.todo.done ? 'line-through' : 'none'
    }
  }

  render() {
    const { id, description, notes, deadline, done } = this.props.todo;
    const renderDone = () => {
      if (done === false) {
        return <input type="checkbox" onChange={this.props.markDone.bind(this, this.props.todo)} />
      }
      return;
    }
    return (
      <div style={this.getStyle()}>
        <p>
          {renderDone()} {' '}
          <b>Description:</b> {description} {' '}
          <b>Notes:</b> {notes} {' '}
          <b>Deadline:</b> {deadline}{' '}
          <button onClick={this.props.delTodo.bind(this, id)} style={btnStyle}>x</button>
        </p>
      </div>
    )
  }
}

TodoItem.propTypes = {
  markComplete: PropTypes.func.isRequired,
  delTodo: PropTypes.func.isRequired
}

const btnStyle = {
  background: '#ff0000',
  color: '#fff',
  border: 'none',
  padding: '5px 9px',
  borderRadius: '50%',
  float: 'right'
}

export default TodoItem;
