import unittest
from main import calculate_response_time

test_data1 = [
    {"create_time": "10:15", "response_time": "10:20"},
    {"create_time": "13:00", "response_time": "13:02"},
    {"create_time": "09:12", "response_time": "09:55"},
]

test_data2 = [
    {"create_time": "10:15", "response_time": "10:20"},
]


class hotel_accommodation_cost(unittest.TestCase):
    def test_calculate_response_time(self):
        self.assertEqual(calculate_response_time(test_data1), 16.67)
        self.assertEqual(calculate_response_time(test_data2), 5.00)


if __name__ == "__main__":
    unittest.main()
