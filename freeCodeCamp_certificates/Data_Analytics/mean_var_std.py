import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)
    axis1 = np.array([arr[:, 0], arr[:, 1], arr[:, 2]])
    axis2 = np.array([arr[0, :], arr[1, :], arr[2, :]])
    flattened = arr.flatten()

    mean_c = [[n.mean() for n in axis1], [n.mean() for n in axis2], flattened.mean()]
    var_c = [[n.var() for n in axis1], [n.var() for n in axis2], flattened.var()]
    std_c = [[n.std() for n in axis1], [n.std() for n in axis2], flattened.std()]
    max_c = [[n.max() for n in axis1], [n.max() for n in axis2], flattened.max()]
    min_c = [[n.min() for n in axis1], [n.min() for n in axis2], flattened.min()]
    sum_c = [[n.sum() for n in axis1], [n.sum() for n in axis2], flattened.sum()]

    calculations = {
        'mean': mean_c,
        'variance': var_c,
        'standard deviation': std_c,
        'max': max_c,
        'min': min_c,
        'sum': sum_c
    }

    return calculations

