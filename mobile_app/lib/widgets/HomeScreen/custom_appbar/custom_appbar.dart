import 'package:flutter/material.dart';
import 'package:mobile_app/widgets/HomeScreen/custom_appbar/profile_icon.dart';

class CustomAppBar extends StatelessWidget implements PreferredSizeWidget{
  const CustomAppBar({super.key, required this.title});

  final String title;

  @override
  Widget build(BuildContext context){
    return AppBar(
        toolbarHeight: 50,
        backgroundColor: Colors.blue,
        title: Text(title),
        actions: const [ProfileIcon()],
      );
  } 

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}