class Motor:
    def move_cylinder(self):
        print("Moving cylinder...")


class Car:
    def __init__(self, motor):
        self._motor = motor
    def turn_on(self):
        self._motor.move_cylinder()
    def move_cylinder(self):
        self._motor.move_cylinder()

motor = Motor()
car = Car(motor)
car.turn_on()
# or
car.move_cylinder()


# Good coupling
# More work

# Can be automated with __getattr__
# Can be used to "limit access"
