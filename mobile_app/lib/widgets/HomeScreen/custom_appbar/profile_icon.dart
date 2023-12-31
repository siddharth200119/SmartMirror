import 'package:flutter/material.dart';

class ProfileIcon extends StatelessWidget{
  const ProfileIcon({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(0, 0, 12, 0),
      child: CircleAvatar(
          backgroundColor: Colors.white,
          radius: 18,
          child: IconButton(
            icon: const Icon(
              Icons.person,
              color: Colors.blueAccent,
              size: 20,
            ),
            onPressed: () {},
          ),
        ),
    );
  }
}