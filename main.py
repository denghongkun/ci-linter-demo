def calculate_sum(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result


def calculate_total(x, y, z):
    total = x + y + z
    print(
        "This is a very long line that definitely exceeds the recommended "
        "79 characters limit in PEP8 style guide and should be broken into "
        "multiple lines"
    )
    return total


if __name__ == "__main__":
    calculate_sum(5, 10)
    calculate_total(1, 2, 3)
