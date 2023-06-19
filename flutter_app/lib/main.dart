import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Lung Cancer'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  File? selectedImage;
  String message = '';

  uploadImage() async {
    final request = http.MultipartRequest('POST',
        Uri.parse('https://00d8-103-163-171-241.ngrok-free.app/upload'));

    final headers = {'Content-type': 'multipart/form-data'};

    request.files.add(http.MultipartFile('image',
        selectedImage!.readAsBytes().asStream(), selectedImage!.lengthSync(),
        filename: selectedImage!.path.split('/').last));

    request.headers.addAll(headers);

    final res = await request.send();
    final responseText = await res.stream.bytesToString();
    final resJson = jsonDecode(responseText);
    print('Response: $resJson');

    // final response = await request.send();
    // http.Response res = await http.Response.fromStream(response);
    // final resJson = jsonDecode(res.body);
    // message = resJson['message'];
    setState(() {});
  }

  Future getImage() async {
    final pickedImage =
        await ImagePicker().getImage(source: ImageSource.gallery);
    selectedImage = File(pickedImage!.path);
    setState(() {});
  }

  // Future getImage() async {
  //   final pickedImage =
  //       await ImagePicker().getImage(source: ImageSource.gallery);
  //   if (pickedImage != null) {
  //     selectedImage = File(pickedImage!.path);
  //     print('Image Path: ${selectedImage?.path}');
  //     setState(() {});
  //   } else {
  //     print('No image picked');
  //   }
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            selectedImage == null
                ? const Text('Please pick a image')
                : Image.file(selectedImage!),
            TextButton.icon(
                onPressed: uploadImage,
                icon: const Icon(Icons.upload_file),
                label: const Text('upload'))
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: getImage,
        child: const Icon(Icons.add_a_photo),
      ),
    );
  }
}
