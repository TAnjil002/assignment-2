// Abstract class Vehicle
abstract class Vehicle {
  int _speed = 0; // Protected variable using underscore for encapsulation

  // Abstract method
  void move();

  // Non-abstract method to set speed
  void setSpeed(int speed) {
    _speed = speed;
  }

  // Getter to access speed safely (encapsulation)
  int get speed => _speed;
}

// Subclass Car extending Vehicle
class Car extends Vehicle {
  @override
  void move() {
    print("The car is moving at ${speed} km/h");
  }
}

// Main function
void main() {
  Car myCar = Car();         // Create Car object
  myCar.setSpeed(80);        // Set speed using method
  myCar.move();              // Call move method
}
