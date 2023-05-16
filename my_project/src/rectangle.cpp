#include "../include/rectangle.h"

Rectangle::Rectangle(int w, int h) {
    width = w;
    height = h;
}

int Rectangle::get_width() {
    return width;
}

int Rectangle::get_height() {
    return height;
}

int Rectangle::get_area() {
    return width * height;
}

int Rectangle::get_perimeter() {
    return 2 * (width + height);
}
