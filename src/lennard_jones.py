import numpy as np


def lj_potential(r, sigma, epsilon):
    return 4 * epsilon * ((sigma / r) ** 12 - (sigma / r) ** 6)


def compute_lj_force(r_vec, sigma, epsilon):
    r = np.linalg.norm(r_vec)
    if r == 0:
        return np.zeros_like(r_vec)
    force_magnitude = 24 * epsilon * (2 * (sigma**12) / (r**13) - (sigma**6) / (r**7))
    force_vector = force_magnitude * (r_vec / r)
    return force_vector
