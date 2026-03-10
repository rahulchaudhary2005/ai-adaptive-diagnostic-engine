import math

def irt_probability(theta, difficulty):
    """
    Calculate probability of correct answer using IRT model
    """
    return 1 / (1 + math.exp(-(theta - difficulty)))


def update_ability(theta, difficulty, correct, learning_rate=0.1):
    """
    Update ability score using gradient update
    """

    p = irt_probability(theta, difficulty)

    if correct:
        theta = theta + learning_rate * (1 - p)
    else:
        theta = theta - learning_rate * (p)

    # clamp ability between 0.1 and 1.0
    theta = max(0.1, min(1.0, theta))

    return theta