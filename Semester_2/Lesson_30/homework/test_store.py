import unittest
import store


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = store.Store

    # Tests for login method in Store class
    def test_store_login_success_user_exists(self):
        login_email = "behruz@gmail.com"
        login_password = "234fjfdsd"

        result = self.store.login(login_email, login_password)
        self.assertTrue(result.user_exists())

    def test_store_login_empty_password_error(self):
        login_email = "behruz@gmail.com"
        login_password = None

        result = self.store.login(login_email, login_password)
        self.assertEqual(result, "Empty values were given.")

    def test_store_login_empty_args(self):
        login_email = None
        login_password = None

        result = self.store.login(login_email, login_password)
        self.assertEqual(result, "Empty values were given.")

    def test_store_login_fail(self):
        login_email = "sdlfkjlkdfj@gmail.com"
        login_password = "2345lsdfj"

        result = self.store.login(login_email, login_password)
        self.assertEqual(result, "Wrong email or password")

    # Tests for register method in Store class
    def test_store_register_success_user_exists(self):
        name = "Emma"
        email = "emma@emma.com"
        password = "sldkfj345@kj"
        card_code = "8576854858685845"
        card_balance = 1000

        result = self.store.register(name, email, password, card_code, card_balance)
        self.assertTrue(result.user_exists())

    def test_store_register_exists_user_error(self):
        name = "John"
        email = "behruz@gmail.com"
        password = "234fjfdsd"
        card_code = "8576857689485768"
        card_balance = 10339

        result = self.store.register(name, email, password, card_code, card_balance)
        self.assertEqual(result, "User with this email or password is already exist.")

    def test_store_register_field_fail(self):
        name = "johj"
        email = "dlkjfskldjf@gmail.com"
        password = "slkdfjs23jsldf"
        card_code = "8697857475867324"
        card_balance = 10029

        result = self.store.register(name, email, password, card_code, card_balance)
        self.assertEqual(result, "Wrong credentials.")

    def test_store_register_empty_value(self):
        name = None
        email = "email@email.com"
        password = "sldkjf384@"
        card_code = "3948585849384859"
        card_balance = 12094

        result = self.store.register(name, email, password, card_code, card_balance)
        self.assertEqual(result, "Empty values were given.")

    # Tests for purchase method in Store class
    def test_store_purchase_success_with_login_available_product(self):
        user = self.store.login("behruz@gmail.com", "234fjfdsd")
        result = user.purchase("bag", 4)
        self.assertEqual(result, "Success.")

    def test_store_purchase_product_amount_error_with_login(self):
        user = self.store.login("behruz@gmail.com", "234fjfdsd")
        result = user.purchase("bag", "two")
        self.assertIsInstance(result, ValueError)

    def test_store_purchase_with_login_not_enough_balance_insufficient_funds(self):
        user = self.store.login("bob@bob.com", "bob345345@")

        result = user.purchase("sweater", 2)
        self.assertEqual(result, "Not enough money.")

    def test_store_purchase_product_invalid_with_login(self):
        user = self.store.login("behruz@gmail.com", "234fjfdsd")
        result = user.purchase("Jh", 2)
        self.assertEqual(result, "Not available.")

    def test_store_purchase_product_amount_not_given(self):
        user = self.store.login("behruz@gmail.com", "234fjfdsd")
        user.purchase("sweater")

        self.assertEqual(len(user.purchases), 1)

    def test_store_purchase_user_not_found(self):
        user = self.store(
            "Emma", "emma@emma.com", "ldskjf83#45", "8576857689878767", 300
        )
        result = user.purchase("bag", 1)

        self.assertEqual(result, "User not found.")

    def tearDown(self):
        self.store = None


if __name__ == "__main__":
    unittest.main()
