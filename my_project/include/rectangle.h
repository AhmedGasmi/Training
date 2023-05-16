#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
public:
    Rectangle(int w, int h);
    int get_width();
    int get_height();
    int get_area();
    int get_perimeter();
private:
    int width;
    int height;
};

#endif
