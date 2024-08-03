import unittest
import numpy as np
from my_model import predict_co2_emissions  # Assuming predict_co2_emissions is the function to be tested

class TestInvalidInput(unittest.TestCase):

    def test_negative_input(self):
        """Test handling of negative input values."""
        # Define negative input values
        negative_input = np.array([[-2.5, 4, 10.0]])  # Assuming engine size cannot be negative

        # Call the function with negative input
        with self.assertRaises(ValueError):
            predict_co2_emissions(negative_input)

if __name__ == '__main__':
    unittest.main()
