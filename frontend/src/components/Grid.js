import React from 'react'
import GridLayout from 'react-grid-layout'

import Todos from './Todos';

class Grid extends React.Component {
  state = {
    todos: []
  };

  render() {
    const layout = [
      { i: 'a', x: 0, y: 0, w: 10, h: 16 },
    ];

    return (
      <GridLayout className="layout" layout={layout} cols={12} rowHeight={30} width={1200}>
        <div key="a"><Todos todos={this.state.todos} /></div>
      </GridLayout>
    )
  }
}

export default Grid;
