class Motor:
    def move_cylinder(self):
        print("Moving cylinder...")


class Car(Motor):
    def turn_on(self):
        self.move_cylinder()


car = Car()
car.turn_on()
# or
car.move_cylinder()


# Strong coupling
# Semantically incorrect (in this case)
# Often less work (because inherited methods work out of the box)
