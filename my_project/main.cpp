#include <iostream>
#include "include/rectangle.h"

int main() {
    Rectangle r(5, 10);
    std::cout << "Width: " << r.get_width() << std::endl;
    std::cout << "Height: " << r.get_height() << std::endl;
    std::cout << "Area: " << r.get_area() << std::endl;
    std::cout << "Perimeter: " << r.get_perimeter() << std::endl;
    return 0;
}
