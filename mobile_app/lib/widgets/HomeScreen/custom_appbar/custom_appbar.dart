import 'package:flutter/material.dart';
import 'package:mobile_app/widgets/HomeScreen/custom_appbar/profile_icon.dart';

class CustomAppBar extends StatelessWidget implements PreferredSizeWidget{
  const CustomAppBar({super.key});

  @override
  Widget build(BuildContext context){
    return AppBar(
        toolbarHeight: 50,
        backgroundColor: Colors.blue,
        title: const Text("Smart Mirror"),
        actions: const [ProfileIcon()],
      );
  } 

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}