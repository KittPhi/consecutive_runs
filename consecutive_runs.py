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
    _first_elements_in_consecutive_runs = []

    # This can be modified to be a parameter to change count of numbers
    # in a consecutive run to make the code reusable/scalable
    _count_of_numbers_in_run = 3
    _min_index_for_run = _count_of_numbers_in_run - 1

    # Loop over the input to find indices of the first element of consecutive run
    for _index, _number in enumerate(input_numbers):
        if _index >= _min_index_for_run:

            # Slice the input_numbers to get the run
            _run = _slice_input_numbers(input_numbers, _index, _count_of_numbers_in_run)

            # Check if the numbers in the run are consecutive that increase or decrease by 1
            _is_consecutive = _is_run_consecutive(_run)

            # Add list indices of the first element of each consecutive run
            if _is_consecutive:
                _index_of_first_number_in_run = _index - 2
                _first_elements_in_consecutive_runs.append(_index_of_first_number_in_run)

    # Results in returning None if there are no consecutive runs
    if _first_elements_in_consecutive_runs:
        return _first_elements_in_consecutive_runs


def _slice_input_numbers(input_numbers: List, _index: int, _count_of_numbers_in_run: int) -> List[int]:
    """
    Slice _count_of_numbers_in_run of input_numbers ending at index: _index
    Args:
        input_numbers (): List
        _index (): int
        _count_of_numbers_in_run (): int

    Returns: List[int]

    """
    _end = _index + 1
    _start_index = _end - _count_of_numbers_in_run

    return input_numbers[_start_index:_end]


def _is_run_consecutive_with_direction(numbers_in_run: List, _direction: int) -> bool:
    """
    Checks if the numbers in the run are consecutive in the given direction
    Args:
        numbers_in_run (): List
        _direction (): int

    Returns: bool

    """
    _prev_number = None

    for _number in numbers_in_run:
        if _prev_number is None:
            _prev_number = _number
        elif _number == _prev_number + _direction:
            _prev_number = _number
        else:
            # _prev_number and _number are not consecutive
            return False

    return True


def _is_run_positive_consecutive(numbers_in_run: List) -> bool:
    """
    Checks if the numbers in the run are consecutive in the positive direction
    Args:
        numbers_in_run (): List

    Returns: bool

    """
    return _is_run_consecutive_with_direction(numbers_in_run, 1)


def _is_run_negative_consecutive(numbers_in_run: List) -> bool:
    """
    Checks if the numbers in the run are consecutive in the negative direction
    Args:
        numbers_in_run (): List

    Returns: bool

    """
    return _is_run_consecutive_with_direction(numbers_in_run, -1)


def _is_run_consecutive(numbers_in_run: List) -> bool:
    """
    Checks if the numbers in the run are consecutive
    Args:
        numbers_in_run (): List

    Returns: bool

    """
    if _is_run_positive_consecutive(numbers_in_run):
        return True
    elif _is_run_negative_consecutive(numbers_in_run):
        return True
    else:
        return False
