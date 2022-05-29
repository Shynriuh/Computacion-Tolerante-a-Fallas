import React from 'react';
import ReactDOM from 'react-dom';
import './css/reset.css';
import './css/index.css';
import App from './components/App';
import * as serviceWorker from './components/serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

serviceWorker.register();
