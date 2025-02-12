from window import Window
from shapes import Square, Point

def main():
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    square = Square(Point(100, 100), 100)
    win.draw_square(square)
  
    win.wait_for_close()

if __name__ == "__main__":
    main()