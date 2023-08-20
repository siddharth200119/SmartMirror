import 'package:flutter/material.dart';
import 'package:mobile_app/widgets/HomeScreen/home_screen.dart';

void main(){
  runApp(MaterialApp(
    theme: ThemeData(useMaterial3: true),
    home: const HomeScreen(),
  ));
}