import React from 'react';
import PropTypes from 'prop-types';

class AddTodo extends React.Component {
  state = {
    description: '',
    notes: ''
  }

  onSubmit = (e) => {
    e.preventDefault();
    this.props.addTodo(this.state.description, this.state.notes);
    this.setState({ description: '', notes: '' });
  }

  onChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    });
  }

  render() {
    return (
      <form onSubmit={this.onSubmit} style={{ display: 'flex' }}>
        <input
          type="text"
          name="description"
          placeholder="Add Todo..."
          style={{ flex: '10', padding: '5px' }}
          value={this.state.description}
          onChange={this.onChange}
        />
        <input
          type="text"
          name="notes"
          placeholder="Notes..."
          style={{ flex: '10', padding: '5px' }}
          value={this.state.notes}
          onChange={this.onChange}
        />
        <input
          type="submit"
          value="Submit"
          className="btn"
          style={{ flex: '1' }}
        />
      </form>
    )
  }
}

AddTodo.propTypes = {
  addTodo: PropTypes.func.isRequired,
}

export default AddTodo;
