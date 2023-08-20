import 'package:flutter/material.dart';
import 'package:mobile_app/widgets/HomeScreen/profile_icon.dart';

class HomeScreen extends StatelessWidget{
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 120,
        title: const Text("Smart Mirror"),
        actions: const [
          ProfileIcon()
        ],
      ),
      body: const Center(child: Text("App")),
    );
  }
}