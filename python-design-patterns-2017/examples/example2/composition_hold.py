class Motor:
    def move_cylinder(self):
        print("Moving cylinder...")


class Car:
    def __init__(self, motor):
        self.motor = motor
    def turn_on(self):
        self.motor.move_cylinder()


motor = Motor()
car = Car(motor)
car.turn_on()
# or
car.motor.move_cylinder()


# Strong coupling
# Violation of the law of Demeter
"""
When applied to object-oriented programs, the Law of Demeter can be more
precisely called the “Law of Demeter for Functions/Methods” (LoD-F). In this
case, an object A can request a service (call a method) of an object instance
B, but object A should not "reach through" object B to access yet another
object, C, to request its services. Doing so would mean that object A
implicitly requires greater knowledge of object B's internal structure.
Instead, B's interface should be modified if necessary so it can directly serve
object A's request, propagating it to any relevant subcomponents.
Alternatively, A might have a direct reference to object C and make the request
directly to that. If the law is followed, only object B knows its own internal
structure.

https://en.wikipedia.org/wiki/Law_of_Demeter
"""
