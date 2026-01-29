class Car:
    def turn_on(self):
        print("You turn on the engine")
        return self

    def drive(self):
        print("You are drving")
        return self

    def brake(self):
        print("You are stepping on the brake")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

#car.turn_on()
#car.turn_off()

# instead of using this 2 lines of code we can use it in just 1 line

(car.turn_on()
 .drive()
 .brake()
 .turn_off())
