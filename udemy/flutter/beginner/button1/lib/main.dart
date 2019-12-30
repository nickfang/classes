import 'package:flutter/material.dart';

void main() {
  runApp(new MaterialApp(
    home: new MyApp(),
  ));
}

class MyApp extends StatefulWidget {
  @override
  _State createState() => new _State();
}

class _State extends State<MyApp> {

  String _value = 'Hello World';
  String _value2 = 'Hello World';
  String _value3 = 'Hello World';
  int _value4 = 0;

  void _onClick() {
    setState((){
      _value = 'My name is Nick';
    });
  }

  void _onPressed(String value) {
    setState(() => _value2 = value);
  }

  void _onPressedDate() {
    setState(() => _value3 = new DateTime.now().toString());
  }

   void _add() {
    setState((){
      _value4++;
    });
  }

  void _subtract() {
    setState((){
      _value4--;
    });
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text('Name here'),
      ),
      body: new Container(
        padding: new EdgeInsets.all(32.0),
        child: new Center(
          child: new Column(
            children: <Widget>[
              new Text(_value),
              new RaisedButton(onPressed: _onClick, child: new Text('Click me'),),
              new Text(_value2),
              new RaisedButton(onPressed: () => _onPressed('Hello Nick'), child: new Text('Click me'),),
              new Text(_value3),
              new FlatButton(onPressed: _onPressedDate, child: new Text('Click me'),),
              new Text('value = $_value4'),
              new IconButton(icon: new Icon(Icons.add), onPressed: _add),
              new IconButton(icon: new Icon(Icons.remove), onPressed: _subtract),

            ],
          ),
        ),
      ),
    );
  }
}
