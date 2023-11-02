import unittest
from client3 import get_data_point
from client3 import get_ratio


class ClientTest(unittest.TestCase):
    def test_get_data_point_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(
            get_data_point(quotes[0]),
            (
                quotes[0]["stock"],
                quotes[0]["top_bid"]["price"],
                quotes[0]["top_ask"]["price"],
                (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2,
            ),
        )

    def test_get_data_point_calculate_price_bid_greater_than_ask(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(
            get_data_point(quotes[0]),
            (
                quotes[0]["stock"],
                quotes[0]["top_bid"]["price"],
                quotes[0]["top_ask"]["price"],
                (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2,
            ),
        )

    def test_get_ratio_calculate_ratio(self):
        price_a = 120.48
        price_b = 117.87

        self.assertEqual(get_ratio(price_a, price_b), 1.0221430389412065)

    def test_get_ratio_calculate_ratio_bid_less_than_ask(self):
        price_a = 119.2
        price_b = 120.48

        self.assertLess(get_ratio(price_a, price_b), 1.17)


if __name__ == "__main__":
    unittest.main()
