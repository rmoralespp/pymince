import pytest

import pymince.text


class TestIsAnyInt:

    @pytest.mark.parametrize('numb', ["10", "-10", "999", "10.", "10.0", "10.0000"])
    def test_true(self, numb):
        assert pymince.text.fullstr(numb).is_int()

    @pytest.mark.parametrize('numb', ["0", "-10.50", "10.50", "0.0", "foo", "01", "-01", "10.0001"])
    def test_false(self, numb):
        assert not pymince.text.fullstr(numb).is_int()


class TestIsPositiveInt:

    @pytest.mark.parametrize("param", ["1", "10", "2", "345678921", "1.000", "1."])
    def test_true(self, param):
        assert pymince.text.fullstr(param).is_positive_int()

    @pytest.mark.parametrize("param", ["0", "-1", "01", "asdf123", "1.0001"])
    def test_false(self, param):
        assert not pymince.text.fullstr(param).is_positive_int()


class TestIsNegativeInt:

    @pytest.mark.parametrize("param", ["-1", "-10", "-2", "-345678921", "-2.", "-1.0000"])
    def test_true(self, param):
        assert pymince.text.fullstr(param).is_negative_int()

    @pytest.mark.parametrize("param", ["0", "1", "-01", "asdf123", "-0.1", "-1.0001"])
    def test_false(self, param):
        assert not pymince.text.fullstr(param).is_negative_int()


class TestIsUrl:
    schemes = ('http', 'https', 'ftp', 'ftps', 'mongodb', 'file', 'postgres')
    hostnames = ("example.org", "example.com", 'localhost', "www.example.com")

    @pytest.mark.parametrize("param", [
        "foo",
        "example.com",
        'http:///example.com/',
        'http://.example.com:8000/foo',
        'https://example.org\\',
        'https://exampl$e.org',
        'http://??',
        'http://.',
        '$https://example.org',
        'ht*tp://example.com/',
        'http://2001:db8::ff00:42:8329',
        'http://example.com:99999',
        'http://example/##',
        'ht*tp://example.com/',
        '+http://example.com/',
        '/',
        '..',
        '../icons/logo.gif',
    ])
    def test_false(self, param):
        assert not pymince.text.fullstr(param).is_url(schemes=self.schemes, hostnames=self.hostnames)

    @pytest.mark.parametrize("param", [
        'http://example.com',
        'http://localhost',
        'https://example.org/foo/next/',
        'postgres://username:password@localhost:5432/app',
        'mongodb://username:password@localhost:5432/foo?replicaSet=myrs'
        'ftp://example.org',
        'http://андрей@example.com',
        'https://www.example.com/',
        'https://example.com/',
        'http://example.com/@handle/',
        'http://example.com/#fragment',
        'http://example.com#/?#',
        'file://localhost/foo/bar',
    ])
    def test_true(self, param):
        assert pymince.text.fullstr(param).is_url(schemes=self.schemes, hostnames=self.hostnames)


class TestIsCardNumber:

    @pytest.mark.parametrize("card_numb", [
        "371449635398431",  # AMEX
        "3714 4963 539 8431",  # AMEX
        "6823 1198 3424 8189",
        "370000000000002",
        "5401683100112371",  # MasterCard
        "370000000000002",  # AMEX
        "5424000000000015",  # Discover
        "6011000000000012",  # MasterCard
        "4007000000027",  # VISA
        "4050000000001",  # VISA
    ])
    def test_true(self, card_numb):
        assert pymince.text.fullstr(card_numb).is_payment_card_num()

    @pytest.mark.parametrize("card_numb", [
        "3710293",
        "5190990281925290",
        "37168200192719989",
        "8102966371298364",
        "1234567890123456",
    ])
    def test_false(self, card_numb):
        assert not pymince.text.fullstr(card_numb).is_payment_card_num()
