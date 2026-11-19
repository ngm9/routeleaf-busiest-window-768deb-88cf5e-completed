from solution import busiest_window


def test_example_window_of_two():
    assert busiest_window([4, 2, 7, 1, 8, 3], 2) == 11


def test_example_window_of_three():
    assert busiest_window([4, 2, 7, 1, 8, 3], 3) == 16


def test_single_element_list():
    assert busiest_window([5], 1) == 5


def test_all_zero_days():
    assert busiest_window([0, 0, 0], 3) == 0


def test_k_equals_one_picks_largest_single_day():
    assert busiest_window([4, 2, 7, 1, 8, 3], 1) == 8


def test_k_equals_length_sums_everything():
    assert busiest_window([4, 2, 7, 1, 8, 3], 6) == 25


def test_busiest_window_at_the_start():
    assert busiest_window([9, 9, 1, 1, 1], 2) == 18


def test_busiest_window_at_the_end():
    assert busiest_window([1, 1, 1, 9, 9], 2) == 18


def test_all_equal_values():
    assert busiest_window([5, 5, 5, 5, 5], 3) == 15


def test_large_uniform_input():
    # 10^5 days each with 7 deliveries; any window of 50000 days sums to 350000.
    deliveries = [7] * 100000
    assert busiest_window(deliveries, 50000) == 350000


def test_large_input_peak_at_end():
    # 99999 days of 0 followed by one day of 10000; window of 1 is 10000.
    deliveries = [0] * 99999 + [10000]
    assert busiest_window(deliveries, 1) == 10000


def test_large_input_full_window():
    # 100000 days each with 3 deliveries; the whole-array window sums to 300000.
    deliveries = [3] * 100000
    assert busiest_window(deliveries, 100000) == 300000
