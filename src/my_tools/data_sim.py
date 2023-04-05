import numpy as np

def noisy_polynomial(x, k, sign=1):
    """Simulate noisy degree-k polynomial function of x.

    """
    x = x.squeeze()
    n = len(x)
    running_sum = 0.0
    
    for k_ in range(1, k + 1):
        beta_k_ = np.random.uniform(low=0.25, size=1)
        running_sum += ( np.power(x, k_) * beta_k_)
    eps = np.random.normal(scale=1, size=(n,))
    running_sum += eps

    return running_sum * sign
