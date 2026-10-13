class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1 = Point()
Point1.x = 20
Point1.y = 90
print(Point1.x)
Point1.draw()
