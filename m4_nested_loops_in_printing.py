"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler and his colleagues,
         and Jackie Xiangqing Zhang.  March, 2012.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_rectangle_of_stars()
    test_triangle_of_stars()
    test_triangle_same_number_in_each_row()
    test_triangle_all_numbers_in_each_row()
    test_triangle_right_justified()
    test_triangle_upside_down()
    test_numbers_constant_forward()
    test_numbers_constant_backwards()
    test_numbers_increasing_forward()


def test_rectangle_of_stars():
    """ Tests the    rectangle_of_stars    function. """
    print('\nTesting the   RECTANGLE_OF_STARS   function:')

    print('Test 1 of rectangle_of_stars: (3, 5)')
    rectangle_of_stars(3, 5)

    print('Test 2 of rectangle_of_stars: (4, 11)')
    rectangle_of_stars(4, 11)

    print('Test 3 of rectangle_of_stars: (6, 2)')
    rectangle_of_stars(6, 2)


def rectangle_of_stars(r, c):
    """
    Prints a rectangle of stars (asterisks), with r rows and c columns.
    For example, when r = 3 and c = 5:
       *****
       *****
       *****
    Preconditions:  r and c are non-negative integers.
    """
    for i in range(r):
        for j in range(c):
            print("*", end="")
        print()
    # DONE: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_triangle_of_stars():
    """ Tests the    triangle_of_stars    function. """
    print('\nTesting the   TRIANGLE_OF_STARS   function:')

    print('Test 1 of triangle_of_stars: (5)')
    triangle_of_stars(5)

    print('Test 2 of triangle_of_stars: (1)')
    triangle_of_stars(1)

    print('Test 3 of triangle_of_stars: (3)')
    triangle_of_stars(3)

    print('Test 4 of triangle_of_stars: (6)')
    triangle_of_stars(6)


def triangle_of_stars(r):
    """
    Prints a triangle of stars (asterisks), with r rows.
      -- The first row is 1 star,
         the second is 2 stars,
         the third is 3 stars, and so forth.
    For example, when r = 5:
       *
       **
       ***
       ****
       *****
    Precondition:  r is a non-negative integer.
    """
    for i in range(r):
        for j in range(i + 1):
            print("*", end='')
        print()
    # DONE: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_triangle_same_number_in_each_row():
    """ Tests the    triangle_same_number_in_each_row    function. """
    print()
    print('Testing the   TRIANGLE_SAME_NUMBER_IN_EACH_ROW   function:')

    print('Test 1 of triangle_same_number_in_each_row: (5)')
    triangle_same_number_in_each_row(5)

    print('Test 2 of triangle_same_number_in_each_row: (1)')
    triangle_same_number_in_each_row(1)

    print('Test 3 of triangle_same_number_in_each_row: (3)')
    triangle_same_number_in_each_row(3)

    print('Test 4 of triangle_same_number_in_each_row: (6)')
    triangle_same_number_in_each_row(6)


def triangle_same_number_in_each_row(r):
    """
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 22, the 3rd is 333, etc.
    For example, when r = 5:
       1
       22
       333
       4444
       55555
    Precondition:  r is a non-negative integer.
    """
    for i in range(r):
        for j in range(0, i + 1):
            print(i + 1, end='')
        print()
    # DONE: 4. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_triangle_all_numbers_in_each_row():
    """ Tests the    triangle_all_numbers_in_each_row    function. """
    print()
    print('Testing the   TRIANGLE_ALL_NUMBERS_IN_EACH_ROW   function:')

    print('Test 1 of triangle_all_numbers_in_each_row: (5)')
    triangle_all_numbers_in_each_row(5)

    print('Test 2 of triangle_all_numbers_in_each_row: (1)')
    triangle_all_numbers_in_each_row(1)

    print('Test 3 of triangle_all_numbers_in_each_row: (3)')
    triangle_all_numbers_in_each_row(3)

    print('Test 4 of triangle_all_numbers_in_each_row: (6)')
    triangle_all_numbers_in_each_row(6)


def triangle_all_numbers_in_each_row(r):
    """
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 12, the 3rd is 123, etc.
    For example, when r = 5:
       1
       12
       123
       1234
       12345
    Precondition:  r is a non-negative integer.
    """
    for i in range(r):
        for j in range(i + 1):
            print(j + 1, end='')
        print()
    # DONE: 5. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_triangle_right_justified():
    """ Tests the    triangle_right_justified    function. """
    print('\nTesting the   TRIANGLE_RIGHT_JUSTIFIED   function:')

    print('Test 1 of triangle_right_justified: (5)')
    triangle_right_justified(5)

    print('Test 2 of triangle_right_justified: (1)')
    triangle_right_justified(1)

    print('Test 3 of triangle_right_justified: (3)')
    triangle_right_justified(3)

    print('Test 4 of triangle_right_justified: (6)')
    triangle_right_justified(6)


def triangle_right_justified(r):
    """
    Prints a triangle of numbers, with r rows.
    It looks the same as the previous example, but right-justified.
    So the first row has some spaces, then a 1,
    the 2nd row has some spaces, then a 12,
    the 3rd row has some spaces, then a 123,
    and so forth, in such a way that the rightmost numbers line up.
    For example, when r = 5:
           1
          12
         123
        1234
       12345
    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    for i in range(r):
        for j in range(r - 1 - i):
            print(" ", end="")
        for j in range(0, i + 1):
            print(j + 1, end="")
        print()
    # DONE: 6. Implement and test this function.
    #          Some tests are already written for you (above).
    # HINT: Do this problem FIRST, then convert x's to spaces:
    #          xxxx1
    #          xxx12
    #          xx123
    #          x1234
    #          12345
    # HINT: One way to solve this problem is to have TWO inner loops,
    #       one after the other.
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_triangle_upside_down():
    """ Tests the    triangle_upside_down    function. """
    print('\nTesting the   TRIANGLE_UPSIDE_DOWN   function:')

    print('Test 1 of triangle_upside_down: (5)')
    triangle_upside_down(5)

    print('Test 2 of triangle_upside_down: (1)')
    triangle_upside_down(1)

    print('Test 3 of triangle_upside_down: (3)')
    triangle_upside_down(3)

    print('Test 4 of triangle_upside_down: (6)')
    triangle_upside_down(6)


def triangle_upside_down(r):
    """
    Prints a triangle of numbers, with r rows.
    It looks the same as the previous problem,
    but with rows in reversed order.  For example, when r = 5:
       12345
        1234
         123
          12
           1
    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    for i in range(r):
        for j in range(i):
            print(" ", end='')
        for j in range(r - i):
            print(j + 1, end='')
        print()
    # DONE: 7. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_numbers_constant_forward():
    """ Tests the    numbers_constant_forward    function. """
    print('\nTesting the   NUMBERS_CONSTANT_FORWARD   function:')

    print('Test 1 of numbers_constant_forward: (4, 7, 3)')
    numbers_constant_forward(4, 7, 3)

    print('Test 2 of numbers_constant_forward: (3, 5, 8)')
    numbers_constant_forward(3, 5, 8)

    print('Test 3 of numbers_constant_forward: (1, 5, 4)')
    numbers_constant_forward(1, 5, 4)

    print('Test 4 of numbers_constant_forward: (7, 3, 4)')
    numbers_constant_forward(7, 3, 4)


def numbers_constant_forward(r, maxnum, n):
    """
    Prints a rectangle of numbers, with r rows.
    Each row has n 1s, then n 2s, then n 3s, etc. up to n maxnum's.
    For example, when r = 4, maxnum = 7 and n = 3:
       111222333444555666777
       111222333444555666777
       111222333444555666777
       111222333444555666777
    Notice that there were r = 4 rows;
    each row had numbers that went from 1 to maxnum = 7; and
    there were n occurrences of each number on each row.
    Here is another example,
    when r = 3, maxnum = 5 and n = 8:
       1111111122222222333333334444444455555555
       1111111122222222333333334444444455555555
       1111111122222222333333334444444455555555
    Preconditions:  r, maxnum and n are positive integers.
    """
    for i in range(r):
        for j in range(maxnum):
            for k in range(n):
                print(j + 1, end='')
        print()
    # DONE: 8. Implement and test this function.
    #          Some tests are already written for you (above).
    # HINT: What loop structure do you need for this problem?
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_numbers_constant_backwards():
    """ Tests the    numbers_constant_backwards    function. """
    print('\nTesting the   NUMBERS_CONSTANT_BACKWARDS   function:')

    print('Test 1 of numbers_constant_backwards: (4, 7, 3)')
    numbers_constant_backwards(4, 7, 3)

    print('Test 2 of numbers_constant_backwards: (3, 5, 8)')
    numbers_constant_backwards(3, 5, 8)

    print('Test 3 of numbers_constant_backwards: (1, 5, 4)')
    numbers_constant_backwards(1, 5, 4)

    print('Test 4 of numbers_constant_backwards: (7, 3, 4)')
    numbers_constant_backwards(7, 3, 4)


def numbers_constant_backwards(r, maxnum, n):
    """
    Prints a rectangle of numbers, with r rows.
    It looks the same as the previous problem, but with
    numbers reversed. For example, when r = 4, maxnum = 7 and n = 3:
       777666555444333222111
       777666555444333222111
       777666555444333222111
       777666555444333222111
    Preconditions:  r, maxnum and n are positive integers.
    """
    for i in range(r):
        for j in range(maxnum, 0, -1):
            for k in range(n):
                print(j, end='')
        print()
    # DONE: 9. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.


def test_numbers_increasing_forward():
    """ Tests the    numbers_increasing_forward    function. """
    print('\nTesting the   NUMBERS_INCREASING_FORWARD   function:')

    print('Test 1 of numbers_increasing_forward: (4, 3)')
    numbers_increasing_forward(4, 3)

    print('Test 2 of numbers_increasing_forward: (2, 7)')
    numbers_increasing_forward(2, 7)

    print('Test 3 of numbers_increasing_forward: (5, 6)')
    numbers_increasing_forward(5, 6)

    print('Test 4 of numbers_increasing_forward: (1, 7)')
    numbers_increasing_forward(1, 7)

    print('Test 5 of numbers_increasing_forward: (2, 1)')
    numbers_increasing_forward(2, 1)


def numbers_increasing_forward(r, maxnum):
    """
    Prints a rectangle of numbers, with r rows, as in the previous
    two problems.  But now each row has one 1, two 2s, three 3s,
    four 4s, etc up to the given maxnum.
    For example, when r = 4 and maxnum = 3:
       122333
       122333
       122333
       122333
    Another example, when r = 2 and maxnum = 7:
       1223334444555556666667777777
       1223334444555556666667777777
    Preconditions:  r and maxnum are positive integers.
    """
    for i in range(r):
        for j in range(maxnum + 1):
            for k in range(j):
                print(j, end='')
        print()
    # DONE: 10. Implement and test this function.
    #          Some tests are already written for you (above).
    # IMPLEMENTATION RESTRICTION: You may NOT use string multiplication
    #                             in this or the following problems.

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
