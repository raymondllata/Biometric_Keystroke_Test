from scipy import stats
import numpy as np
import math
SAMPLE_VEC = [(97, 0), (32, 0.1), (98, 0.5), (32, 0.7), (99, 0.9999999999999999), (32, 1.3), (100, 1.7000000000000004), (32, 1.8000000000000005), (101, 2.0000000000000004), (32, 2.1000000000000005), (102, 2.3000000000000007), (32, 2.500000000000001), (103, 2.700000000000001), (32, 2.800000000000001), (104, 3.1000000000000014), (32, 3.2000000000000015), (105, 3.4000000000000017), (32, 3.600000000000002), (106, 3.700000000000002), (32, 3.900000000000002), (107, 4.100000000000001), (32, 4.300000000000001), (108, 4.4), (109, 4.5), (110, 4.699999999999999), (111, 4.799999999999999), (112, 4.999999999999998)]

#uses gaussian random variables to estimate approximation
def compute_likelihood_stats(person_A, person_B, mystery_Person):
    person_A_vec = difference_vector(person_A)
    personA_mean = np.mean(person_A_vec)
    personA_var = np.var(person_A_vec)
    person_B_vec = difference_vector(person_B)
    personB_mean = np.mean(person_B_vec)
    personB_var = np.var(person_B_vec)
    person_C_vec = difference_vector(mystery_Person)

    return(compute_likelihood(person_C_vec, personA_mean, personA_var, personB_mean, personB_var))


#code written for vector of tuples of form (key name, timing)
def difference_vector(vector):
    new_vec = []
    for i in range(len(vector) - 1):
        new_vec.append(vector[len(vector) - 1 - i][1] - vector[len(vector) - 2 - i][1])
    return new_vec

def compute_likelihood(mystery, mean_a, variance_a, mean_b, variance_b):
    likelihoodAoverB = 1
    likelihoodBoverA = 1

    for i in mystery:
        p_A = stats.norm.pdf(i, mean_a, math.sqrt(variance_a))
        p_B = stats.norm.pdf(i, mean_b, math.sqrt(variance_b))
        likelihoodAoverB *= p_A / p_B
        likelihoodBoverA *= p_B / p_A
    return (likelihoodAoverB, likelihoodBoverA)


#difference_vector(SAMPLE_VEC)