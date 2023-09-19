import 'package:flutter/material.dart';
import 'package:mobile_app/widgets/HomeScreen/custom_appbar/custom_appbar.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int index = 1;
  var pages = [const Center(child: Text("Live Feed")), const Center(child: Text("Home")), const Center(child: Text("To-Do"))];
  var titles = ["Live Feed", "Smart Mirror", "To-Do List"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: CustomAppBar(title: titles[index]),
      body: pages[index],
      bottomNavigationBar: NavigationBar(
        height: 60,
        selectedIndex: index,
        onDestinationSelected: (index) => setState(() => this.index = index),
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.camera_alt),
            label: "Live Feed",
          ),
          NavigationDestination(
            icon: Icon(Icons.home),
            label: "Home",
          ),
          NavigationDestination(
            icon: Icon(Icons.list_alt),
            label: "To-Do",
          ),
        ],
      ),
    );
  }
}
