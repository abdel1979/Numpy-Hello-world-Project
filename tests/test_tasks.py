# Importing libraries
import pytest
from .utils import get_calls, get_assignments
from tasks import solution

# -------------------------------------------------
# Pytest for Task 1
# Importing the `numpy` library with an alias `np`

@pytest.mark.test_task1
def test_task1():
    assert 'np' in dir(solution), 'Have you imported the `numpy` library with an alias as `np`?'
    
# -------------------------------------------------
# Pytest for Task 2
# Loading the TXT file in a variable `score_data` using the `np.genfromtxt()` method.

@pytest.mark.test_task2
def test_task2():
    assert get_calls(solution)[0] == 'np:genfromtxt:data/scores.txt:delimiter:,', 'Have you loaded the TXT file using the `np.genfromtxt` method with 'delimiter' arguments?'
    assert get_assignments(solution)[0][:10] == 'score_data', 'Has the `score_data` DataFrame been created?'

# -------------------------------------------------
# Pytest for Task 3
# Finding the Maximum score value and store it in `score_max` variable.

@pytest.mark.test_task3
def test_task3():    
    assert get_assignments(solution)[1][:9] == 'score_max', 'Has the `score_max` variable been created?'
    assert solution.score_max == 8, 'You can use the `np.max(score_data)` call to calculate the maximum value.'

# -------------------------------------------------
# Pytest for Task 4
# Finding the Maximum score value and store it in `score_min` variable.

@pytest.mark.test_task4
def test_task4():    
    assert get_assignments(solution)[2][:9] == 'score_min', 'Has the `score_min` variable been created?'
    assert solution.score_min == 1, 'You can use the `np.min(score_data)` call to calculate the minimum value.'
