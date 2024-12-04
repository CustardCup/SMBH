'''
This file contains the tester functions for each function used in the notebook. 
'''

from typing import List, Callable, Optional
import numpy as np
import functions as fn
from astropy.constants import G

def create_test_cases(name: str, test_cases: List,
                      original_func: Callable, student_func: Callable,
                      message_formatter: Optional[Callable] = None):
    """
    Tests a student's function against an original function using a set of test cases. 
    It evaluates whether the student's function behaves as expected by comparing its output 
    with the original function's output for the same arguments. If discrepancies occur,
    formatted error messages are generated. The function can optionally use a custom 
    message formatter for error messages.

    Parameters:
    - name (str): Name for the test suite, used for identifying the test cases.
    - test_cases (List[Tuple[str, List]]): A list of test case tuples, each containing a scenario description and a list of arguments.
    - original_func (Callable): The reference function to produce the correct output for the provided arguments.
    - student_func (Callable): The student's function to be tested against the original function.
    - message_formatter (Optional[Callable]): An optional function to format error messages, accepts the test case, expected result, and actual result.

    Returns:
    - str: A single string indicating all tests passed, or concatenated error messages for each failing test case.
          If the student function is not implemented, it returns a message indicating this and skips the tests.
    """
    messages = []
    
    for case in test_cases:
        scenario, args = case
        expected = original_func(*args)
        try:
            result = student_func(*args)
            if result is None:
                return f"{name} function not implemented. Skipping tests."
            
            if not np.isclose(result, expected, rtol=1e-5, atol=0):
                raise ValueError
            
        except ValueError:
            if message_formatter is None:
                msg = f"Scenario {scenario} failed. Expected result was close to {expected:.2e}, but got {result:.2e}."
            else:
                msg = message_formatter(case, expected, result)
            messages.append(msg)
    
    if not messages:
        return "All tests passed! Your implementation appears to be correct."
    else:
        return "\n\n".join(messages)


def test_mass_bh(student_func):
    """
    Tests the student's implementation of the Kepler's formula.
    """
    test_cases = [
        ("Testing for the star S4714", (1.19680e+14, 3.627100e+08)),
        ("Testing for the star S14", (1.19680e+14, 3.627100e+08))
    ]

    def formatter(case, expected, result):
        scenario, (sem_axis, period) = case
        return(f"Scenario {scenario} failed:\nSemi-Major Axis={sem_axis} m and Period={period} s.\n" +
                                    f"Expected result was close to {expected:.2e} kg, but got {result:.2e}.")

    # Run standard tests
    output = create_test_cases('Blackhole Mass', test_cases,
                                fn.mass_bh_advanced, student_func, formatter)
    
    return f"{output}"
            
def test_line(student_func):
    """
    Tests the student's implmenetation of linear function'
    """
    test_cases = [
        ("Testing for x = 1, m = 2, b = 3", (1, 2, 3)),
        ("Testing for x = 4, m = 5, b = 6", (4, 5, 6))
    ]

    def formatter(case, expected, result):
        scenario, (x, m, b) = case
        return(f"Scenario {scenario} failed:\n x={x} ; m={m} ; b = {b}\n" +
                                    f"Expected result was close to {expected:.2e} kg, but got {result:.2e}.")

    # Run standard tests
    output = create_test_cases('Line Function', test_cases,
                                fn.line, student_func, formatter)
    
    return f"{output}"


#function to test if the functions are imported into the functions file
def printer():
    print('works')













