import pytest

import pymince.text

int_positives = (
    "10",
    "10.",
    "10.0",
    "+10",
    "+10.",
    "+10.0",
)

int_negatives = (
    "-10",
    "-10.",
    "-10.0",
)

not_int = (
    "" "0",
    "+0",
    "-0",
    "0.0",
    "+0.0",
    "-0.0",
    "01",
    "foo",
    "foo123",
    "1.0001",
    "1.0.00",
    "10,",
    "10,0",
)


class TestIsAnyInt:
    @pytest.mark.parametrize("numb", int_positives + int_negatives)
    def test_true(self, numb):
        assert pymince.text.fullstr(numb).is_int()

    @pytest.mark.parametrize("numb", not_int)
    def test_false(self, numb):
        assert not pymince.text.fullstr(numb).is_int()


class TestIsPositiveInt:
    @pytest.mark.parametrize("param", int_positives)
    def test_true(self, param):
        assert pymince.text.fullstr(param).is_positive_int()

    @pytest.mark.parametrize("param", not_int + int_negatives)
    def test_false(self, param):
        assert not pymince.text.fullstr(param).is_positive_int()


class TestIsNegativeInt:
    @pytest.mark.parametrize("param", int_negatives)
    def test_true(self, param):
        assert pymince.text.fullstr(param).is_negative_int()

    @pytest.mark.parametrize("param", not_int + int_positives)
    def test_false(self, param):
        assert not pymince.text.fullstr(param).is_negative_int()


class TestIsUrl:
    schemes = ("http", "https", "ftp", "ftps", "mongodb", "file", "postgres")
    hostnames = ("example.org", "example.com", "localhost", "www.example.com")

    @pytest.mark.parametrize(
        "param",
        [
            "" "foo",
            "example.com",
            "http:///example.com/",
            "http://.example.com:8000/foo",
            "https://example.org\\",
            "https://exampl$e.org",
            "http://??",
            "http://.",
            "$https://example.org",
            "ht*tp://example.com/",
            "http://2001:db8::ff00:42:8329",
            "http://example.com:99999",
            "http://example/##",
            "ht*tp://example.com/",
            "+http://example.com/",
            "/",
            "..",
            "../icons/logo.gif",
        ],
    )
    def test_false(self, param):
        assert not pymince.text.fullstr(param).is_url(
            schemes=self.schemes, hostnames=self.hostnames
        )

    @pytest.mark.parametrize(
        "param",
        [
            "http://example.com",
            "http://localhost",
            "https://example.org/foo/next/",
            "postgres://username:password@localhost:5432/app",
            "mongodb://username:password@localhost:5432/foo?replicaSet=myrs"
            "ftp://example.org",
            "http://андрей@example.com",
            "https://www.example.com/",
            "https://example.com/",
            "http://example.com/@handle/",
            "http://example.com/#fragment",
            "http://example.com#/?#",
            "file://localhost/foo/bar",
        ],
    )
    def test_true(self, param):
        assert pymince.text.fullstr(param).is_url(
            schemes=self.schemes, hostnames=self.hostnames
        )


class TestIsPaymentCard:
    @pytest.mark.parametrize(
        "card_numb",
        [
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
        ],
    )
    def test_true(self, card_numb):
        assert pymince.text.fullstr(card_numb).is_payment_card()

    @pytest.mark.parametrize(
        "card_numb",
        [
            "" "3710293",
            "5190990281925290",
            "37168200192719989",
            "8102966371298364",
            "1234567890123456",
        ],
    )
    def test_false(self, card_numb):
        assert not pymince.text.fullstr(card_numb).is_payment_card()


class TestIsBinary:
    @pytest.mark.parametrize(
        "v",
        [
            "00",
            "0",
            "1",
            "01",
            "10",
            "101010000111",
        ],
    )
    def test_true(self, v):
        assert pymince.text.fullstr(v).is_binary()

    @pytest.mark.parametrize("v", ["" "02", "12", "21", "20", "012", "foo"])
    def test_false(self, v):
        assert not pymince.text.fullstr(v).is_binary()


class TestIsPercentage:
    @pytest.mark.parametrize(
        "v",
        [
            "0%",
            "0 %",
            "0.0%",
            "0.0 %",
            "0&nbsp;%",
            "1234.000 %",
            "1%",
        ],
    )
    def test_true(self, v):
        assert pymince.text.fullstr(v).is_percentage()

    @pytest.mark.parametrize(
        "v", ["", "foo", "-1%", "0.%", "1  %", "01.000 %", "00 %", "90"]
    )
    def test_false(self, v):
        assert not pymince.text.fullstr(v).is_percentage()


class TestIsPalindrome:
    @pytest.mark.parametrize(
        "v",
        [
            "",
            "a",
            "aa",
            "aba",
            "abcba",
            "abcdcba",
            "111",
            "123454321",
        ],
    )
    def test_true(self, v):
        assert pymince.text.fullstr(v).is_palindrome()

    @pytest.mark.parametrize(
        "v",
        [
            "ab",
            "aab",
            "012",
        ],
    )
    def test_false(self, v):
        assert not pymince.text.fullstr(v).is_palindrome()


class TestIsEmailAddress:
    @pytest.mark.parametrize(
        "v",
        [
            "foo@example.org",
            "foo.123@testing-example.com",
            "!#$%&'*+-/=?^_`.{|}~@example.org",
            "ñó@example.org",
            "foo@..twodots.com",
            "my@foo..com",
            "my@baddash.-a.com",
            ".leadingdot@domain.com",
            "123456789@example.com",
            "123456789@ñó",
        ],
    )
    def test_true(self, v):
        assert pymince.text.fullstr(v).is_email_address()

    @pytest.mark.parametrize(
        "v",
        [
            "",
            "@",
            "foo",
            "@foo",
            "foo@",
            "\nmy@example.com",
            "m\ny@example.com",
            "my\n@example.com",
            "foo@ ab",
            "foo @ab",
        ],
    )
    def test_false(self, v):
        assert not pymince.text.fullstr(v).is_email_address()


class TestIsRoman:
    @pytest.mark.parametrize(
        "v",
        [
            "I",
            "IV",
            "V",
            "IX",
            "X",
            "XL",
            "L",
            "XC",
            "C",
            "CD",
            "D",
            "CM",
            "M",
            "MMMDCCXXIV",
            "XLIX",
        ],
    )
    def test_true(self, v):
        assert pymince.text.fullstr(v).is_roman()

    @pytest.mark.parametrize(
        "v",
        [
            "XIIIIII",
            "VVVI",
            "IIIIIIIIIIIIIIII",
            "XIIIIIIIII",
            "MCCCCCCVI",
            "CCCCC",
            "IL",
            "XLVIIII",
            "XXXXVIIII",
            "XLIIIIIIIII",
            "XXXXX",
            "XXXXVIIII",
            "VX",
            "VL",
            "VC",
            "VD",
            "VM",
            "LC",
            "LD",
            "LM",
            "DM",
        ],
    )
    def test_false(self, v):
        assert not pymince.text.fullstr(v).is_roman()
