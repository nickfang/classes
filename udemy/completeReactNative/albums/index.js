// Import a library to help create a component
import React from 'react';
import { AppRegistry } from 'react-native';
import Header from './src/components/header';

// create a component
const App = () => {
  return (
    <Header title="Albums!" />
  );
};

// render it to a device
AppRegistry.registerComponent('albums', () => App);
