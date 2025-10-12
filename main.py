def   calculate_sum  (  a,  b  ):
    result=a+b
    print(f"The sum of {a} and {b} is: {result}")
    return result

def very_long_function_name_that_exceeds_pep8_line_length_limit_and_should_be_refactored(x,y,z):
    total = x + y + z
    print(f"This is a very long line that definitely exceeds the recommended 79 characters limit in PEP8 style guide and should be broken into multiple lines")
    return total

if __name__ == "__main__"  :
    calculate_sum(5,10)
    very_long_function_name_that_exceeds_pep8_line_length_limit_and_should_be_refactored(1,2,3)
