import React from 'react';
import logo from './logo.svg';
import './App.css';

import Products from "./admin/Products";
import ProductsCreate from "./admin/ProductsCreate";
import ProductsEdit from "./admin/ProductsEdit";
import Main from "./main/Main";
import {BrowserRouter, Route} from "react-router-dom";

function App() {
  return (
    <div className="App">

            <BrowserRouter>
              <Route path = '/' exact component={Main}/>
              <Route path = '/admin/products' exact component={Products}/>
              <Route path = '/admin/products/create' component={ProductsCreate}/>
              <Route path = '/admin/products/:id/edit' component={ProductsEdit}/>
            </BrowserRouter>
       

    </div>
  );
}

export default App;
