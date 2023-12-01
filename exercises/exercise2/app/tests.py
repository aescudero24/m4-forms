from django.test import SimpleTestCase


# Create your tests here.
class TestFrontTimesView(SimpleTestCase):
    def test_Chocolate_2(self):
        url = "/warmup-2/front-times/"
        data = {"string": "Chocolate", "number": 2}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ChoCho")

    def test_Chocolate_3(self):
        url = "/warmup-2/front-times/"
        data = {"string": "Chocolate", "number": 3}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ChoChoCho")

    def test_Abc_3(self):
        url = "/warmup-2/front-times/"
        data = {"string": "Abc", "number": 3}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AbcAbcAbc")


class TestNoTeenSumView(SimpleTestCase):
    def test_1_2_3(self):
        url = "/logic-2/no-teen-sum/"
        data = {"a": 1, "b": 2, "c": 3}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "6")

    def test_2_13_1(self):
        url = "/logic-2/no-teen-sum/"
        data = {"a": 2, "b": 13, "c": 1}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")

    def test_2_1_14(self):
        url = "/logic-2/no-teen-sum/"
        data = {"a": 2, "b": 1, "c": 14}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")


class TestXyzThereView(SimpleTestCase):
    def test_abcxyz(self):
        url = "/string-2/xyz-there/"
        data = {"string": "abcxyz"}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "True")

    def test_abc_period_xyz(self):
        url = "/string-2/xyz-there/"
        data = {"string": "abc.xyz"}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "False")

    def test_xyz_period_abc(self):
        url = "/string-2/xyz-there/"
        data = {"string": "xyz.abc"}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "True")


class TestCenteredAverageView(SimpleTestCase):
    def test_1_2_3_4_100(self):
        url = "/list-2/centered-average/"
        data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 100}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")

    def test_1_1_5_5_10_8_7(self):
        url = "/list-2/centered-average/"
        data = {"a": 1, "b": 1, "c": 5, "d": 5, "e": 10, "f": 8, "g": 7}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "5")

    def test__10__4__2__4__2_0(self):
        url = "/list-2/centered-average/"
        data = {"a": -10, "b": -4, "c": -2, "d": -4, "e": -2, "f": 0}

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "-3")
