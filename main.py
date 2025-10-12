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

# 在文件末尾添加不规范代码
def bad_function  ():
    x=1
    print("This line is way too long and should trigger flake8 error because it exceeds the maximum line length limit of 79 characters")