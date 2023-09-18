import 'package:flutter/material.dart';
import 'package:google_nav_bar/google_nav_bar.dart';

class CustomNavigationBar extends StatefulWidget {
  const CustomNavigationBar({super.key});

  @override
  State<CustomNavigationBar> createState() => _CustomNavigationBarState();
}

class _CustomNavigationBarState extends State<CustomNavigationBar> {
  int index = 1;

  @override
  Widget build(BuildContext context) {
    return NavigationBar(
      height: 60,
      selectedIndex: index,
      onDestinationSelected: (index) => setState(() => this.index = index),
      destinations: const [
        NavigationDestination(icon: Icon(Icons.camera_alt), label: "Live Feed"),
        NavigationDestination(icon: Icon(Icons.home), label: "Home"),
        NavigationDestination(icon: Icon(Icons.list_alt), label: "To-Do")
      ],
    );
  }
}
