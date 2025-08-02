import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // Hides the "DEBUG" banner
      title: 'Greeting App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Greeting App'),
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  // This method will display a SnackBar with a message
  void _showSnackBar(BuildContext context) {
    final snackBar = SnackBar(
      content: const Text('Button Pressed!'),
      action: SnackBarAction(
        label: 'Dismiss',
        onPressed: () {
          // You can add an action here, like closing the snackbar.
          // In this case, the snackbar will simply disappear.
        },
      ),
    );

    // Find the ScaffoldMessenger in the widget tree
    // and use it to show a SnackBar.
    ScaffoldMessenger.of(context).showSnackBar(snackBar);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Center(
        // Use a Column to place widgets vertically
        child: Column(
          // Align widgets in the center of the column
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            // 1. "Hello, World!" text with custom styling
            const Text(
              'Hello, World!',
              style: TextStyle(
                color: Colors.red, // Change text color to red
                fontWeight: FontWeight.bold, // Make text bold
                fontSize: 24,
              ),
            ),
            // Add some spacing between widgets
            const SizedBox(height: 16),

            // 2. Additional "Welcome to Flutter!" text
            const Text(
              'Welcome to Flutter!',
              style: TextStyle(
                fontSize: 18,
              ),
            ),
            // Add some spacing between widgets
            const SizedBox(height: 24),

            // 3. Image from a network URL
            Image.network(
              'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flutter_logo.svg/1024px-Flutter_logo.svg.png',
              width: 150, // Set a specific width for the image
            ),
            // Add some spacing between widgets
            const SizedBox(height: 32),

            // 4. Interactive button with custom styling
            ElevatedButton(
              onPressed: () => _showSnackBar(context),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green, // Change button color to green
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(20.0),
                ),
              ),
              child: const Text(
                'Press Me',
                style: TextStyle(color: Colors.white),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
