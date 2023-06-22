import unittest
import lesson_34
import hashlib


from requests.exceptions import HTTPError


class TestPwnedPasswords(unittest.TestCase):
    def setUp(self):
        self.sha1_password = (
            hashlib.sha1("password".encode("utf-8")).hexdigest().upper()
        )

    def test_status_code_ok_request_api_data(self):
        first5_param = self.sha1_password[:5]
        status_code = lesson_34.request_api_data(first5_param).status_code
        self.assertEqual(status_code, 200)

    def test_bad_status_code_request_api_data(self):
        incorrect_sha1 = "KJFDS"

        with self.assertRaises(HTTPError):
            lesson_34.request_api_data(incorrect_sha1)

    def tearDown(self):
        del self.sha1_password


if __name__ == "__main__":
    unittest.main()
