from typing import Optional, List


def find_consecutive_runs(input_numbers: List) -> Optional[List[int]]:
    """
    Checks for all runs of 3 consecutive numbers that increase or decrease by 1.
    Returns the list indices of the first element of each run.
    If there are no consecutive runs it should return None.

    Args:
        input_numbers (): List

    Returns: Optional[List[int]]

    """
    first_elements_in_consecutive_runs = []

    # This can be modified to be a parameter to change count of numbers
    # in a consecutive run to make the code reusable/scalable
    count_of_numbers_in_run = 3
    min_index_for_run = _count_of_numbers_in_run - 1

    # Loop over the input to find indices of the first element of consecutive run
    for index, number in enumerate(input_numbers):
        if index >= min_index_for_run:

            # Slice the input_numbers to get the run
            run = slice_input_numbers(input_numbers, index, count_of_numbers_in_run)

            # Check if the numbers in the run are consecutive that increase or decrease by 1
            is_consecutive = is_run_consecutive(_run)

            # Add list indices of the first element of each consecutive run
            if is_consecutive:
                index_of_first_number_in_run = index - 2
                first_elements_in_consecutive_runs.append(index_of_first_number_in_run)

    # Results in returning None if there are no consecutive runs
    if first_elements_in_consecutive_runs:
        return first_elements_in_consecutive_runs


def slice_input_numbers(input_numbers: List, index: int, count_of_numbers_in_run: int) -> List[int]:
    """
    Slice _count_of_numbers_in_run of input_numbers ending at index: _index
    Args:
        input_numbers (): List
        _index (): int
        _count_of_numbers_in_run (): int

    Returns: List[int]

    """
    end = index + 1
    start = end - count_of_numbers_in_run

    return input_numbers[start:end]


def is_run_consecutive_with_direction(numbers_in_run: List, direction: int) -> bool:
    """
    Checks if the numbers in the run are consecutive in the given direction
    Args:
        numbers_in_run (): List
        _direction (): int

    Returns: bool

    """
    prev_number = None

    for number in numbers_in_run:
        if prev_number is None:
            prev_number = number
        elif number == prev_number + direction:
            prev_number = number
        else:
            # prev_number and number are not consecutive
            return False

    return True


def is_run_positive_consecutive(numbers_in_run: List) -> bool:
    """
    Checks if the numbers in the run are consecutive in the positive direction
    Args:
        numbers_in_run (): List

    Returns: bool

    """
    return is_run_consecutive_with_direction(numbers_in_run, 1)


def is_run_negative_consecutive(numbers_in_run: List) -> bool:
    """
    Checks if the numbers in the run are consecutive in the negative direction
    Args:
        numbers_in_run (): List

    Returns: bool

    """
    return is_run_consecutive_with_direction(numbers_in_run, -1)


def is_run_consecutive(numbers_in_run: List) -> bool:
    """
    Checks if the numbers in the run are consecutive
    Args:
        numbers_in_run (): List

    Returns: bool

    """
    if is_run_positive_consecutive(numbers_in_run):
        return True
    elif is_run_negative_consecutive(numbers_in_run):
        return True
    else:
        return False
