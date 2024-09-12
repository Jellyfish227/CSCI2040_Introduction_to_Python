# recursion
def print_triangle(height):
    space = ' '
    underline = '_'
    left_boarder = '/'
    right_boarder = '\\'
    # divide
    if height < 2:
        print(left_boarder + underline * (2 * (int(h)- 1)) + right_boarder)
        return
    # conquer
    print(space * (height - 1) + left_boarder + space * (2 * (int(h) - height)) + right_boarder)
    return print_triangle(height - 1)

h = input("Enter h: ")
while not(1 < int(h) < 30):
    print("Invalid input for h!")
    h = input("Enter h: ")

print_triangle(int(h))