import full_calc as fc
import simplified_cals as sc


def compare(a_set, b_set, c_set, universal_set):
    """compares calculation result of starting and given expressions"""
    a = fc.FullCalculation(a_set, b_set, c_set, universal_set)
    b = sc.SimplifiedCalculation(a_set, b_set, c_set, universal_set)
    if a.step_5_d_final() == b.step_2():
        return True
    else:
        return False
