import unittest
import requests


class GetUserAPITest(unittest.TestCase):
    def test_get_user(self):
        response = requests.get("https://reqres.in/api/users/2")
        print(response.json())  # Print the response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Add your assertions or validations here
        self.assertEqual(data['data']['id'], 2)
        self.assertEqual(data['data']['email'], 'janet.weaver@reqres.in')
        self.assertEqual(data['data']['first_name'], 'Janet')
        self.assertEqual(data['data']['last_name'], 'Weaver')

        # Validate response time is less than 2000 milliseconds (2 seconds)
        response_time_ms = response.elapsed.total_seconds() * 1000
        print(f"Response time: {response_time_ms} ms")  # Print the response time
        self.assertLess(response_time_ms, 2000)


if __name__ == '__main__':
    unittest.main()
