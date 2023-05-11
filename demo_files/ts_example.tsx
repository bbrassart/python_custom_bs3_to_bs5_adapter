// @ts-expect-error
import React from 'react';

const Demo: React.FC = () => {
  return (
    <div className='do-not-touch margin-top-small'>
      <h1>React Demo</h1>
      </div>
  );
};

export default Demo;