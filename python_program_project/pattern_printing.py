def inverse_right_angle_pyramid(n):
    for i in range(n + 1):
        for j in range(i):
            print("*", end="")
        print()

    for i in range(n - 1, 0, -1):
        space = n - i
        print(" " * space, end="")
        for j in range(i):
            print("*", end="")
        print()


# Example usage with n = 4
inverse_right_angle_pyramid(4)
