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

  String _value = '';
  bool _value2 = false;
  bool _value3 = false;

  int _radioValue1 = 0;
  int _radioValue2 = 0;

  void _onChange(String value) {
    setState(() => _value = 'Change: ${value}');
  }

  void _onSubmit(String value) {
    setState(() => _value = 'Submit: ${value}');
  }

  void _value2Changed(bool value) => setState(() => _value2 = value);
  void _value3Changed(bool value) => setState(() => _value3 = value);

  void _setValue1(int value) => setState(() => _radioValue1 = value);
  void _setValue2(int value) => setState(() => _radioValue2 = value);

  Widget makeRadios() {
    List list1 = new List<Widget>();

    for (int i = 0; i < 3; i++) {
      list1.add(new Radio(value: i, groupValue: _radioValue1, onChanged: _setValue1));
    }

    Column column = new Column(children: list1,);
    return column;
  }

  Widget makeRadioTiles() {
    List list2 = new List<Widget>();

    for (int i = 0; i < 3; i++) {
      list2.add(new RadioListTile(
        value: i,
        groupValue: _radioValue2,
        onChanged: _setValue2,
        activeColor: Colors.green,
        controlAffinity: ListTileControlAffinity.trailing,
        title: new Text('Item: ${i}'),
        subtitle: new Text('sub title'),

      ));
    }

    Column column = new Column(children: list2,);
    return column;
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
              new TextField(
                decoration: new InputDecoration(
                  labelText: 'Hello',
                  hintText: 'Hint',
                  icon: new Icon(Icons.people)
                ),
                autocorrect: true,
                autofocus: true,
                keyboardType: TextInputType.text,
                onChanged: _onChange,
                onSubmitted: _onSubmit,
              ),
              new Checkbox(value: _value2, onChanged: _value2Changed),
              new CheckboxListTile(
                value: _value3,
                onChanged: _value3Changed,
                title: new Text('Hello World'),
                controlAffinity: ListTileControlAffinity.leading,
                subtitle: new Text('Subtitle'),
                secondary: new Icon(Icons.archive),
                activeColor: Colors.red,
              ),
              makeRadios(),
              makeRadioTiles(),
            ],
          ),
        ),
      ),
    );
  }
}
