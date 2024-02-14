# Perform trigonometric calculations
import math 

def perform_trigonometric_calculations(angle):
    """
    Performs trigonometric calculations for a given angle in degrees.

    Args:
        angle (float): The angle in degrees.

    Returns:
        tuple: A tuple containing the sine, cosine, and tangent of the angle.
    """
    return math.sin(angle), math.cos(angle), math.tan(angle)
print(perform_trigonometric_calculations(math.pi/4))