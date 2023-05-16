CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17
SRCDIR = src
INCDIR = include

all: main

$(SRCDIR)/rectangle.o: $(SRCDIR)/rectangle.cpp $(INCDIR)/rectangle.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: main.cpp $(INCDIR)/rectangle.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

main: $(SRCDIR)/rectangle.o main.o
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	rm -f $(SRCDIR)/*.o main main.o
