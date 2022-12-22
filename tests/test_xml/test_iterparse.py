import os
import tempfile
import types

import pytest

import pymince.xml
import tests


@pytest.fixture(scope="module")
def xml_string():
    lines = (
        "<?xml version='1.0' encoding='UTF-8'?>",
        "<countries>",
        "  <country code='af' handle='afghanistan' continent='asia' iso='4'>Afghanistan</country>",
        "  <country code='al' handle='albania' continent='europe' iso='8'>Albania</country>",
        "  <country code='dz' handle='algeria' continent='africa' iso='12'>Algeria</country>",
        "  <country code='as' handle='american-samoa' continent='polynesia' iso='16'>American Samoa</country>",
        "  <country code='ad' handle='andorra' continent='europe' iso='20'>Andorra</country>",
        "</countries>",
    )
    return "\n".join(lines)


def test_type(xml_string):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "countries.xml")
        tests.make_file(filename, content=xml_string)
        result = pymince.xml.iterparse(filename)
        assert isinstance(result, types.GeneratorType)


def test_items(xml_string):
    with tempfile.TemporaryDirectory() as tmpdir:
        expected = [
            ["countries", {}, None],
            [
                "country",
                {
                    "code": "af",
                    "handle": "afghanistan",
                    "continent": "asia",
                    "iso": "4",
                },
                "Afghanistan",
            ],
            [
                "country",
                {"code": "al", "handle": "albania", "continent": "europe", "iso": "8"},
                "Albania",
            ],
            [
                "country",
                {"code": "dz", "handle": "algeria", "continent": "africa", "iso": "12"},
                "Algeria",
            ],
            [
                "country",
                {
                    "code": "as",
                    "handle": "american-samoa",
                    "continent": "polynesia",
                    "iso": "16",
                },
                "American Samoa",
            ],
            [
                "country",
                {"code": "ad", "handle": "andorra", "continent": "europe", "iso": "20"},
                "Andorra",
            ],
        ]
        filename = os.path.join(tmpdir, "countries.xml")
        tests.make_file(filename, content=xml_string)
        result = pymince.xml.iterparse(filename)
        result = [
            [obj.tag, obj.attrib, obj.text] for event, obj in result if event == "start"
        ]
        assert result == expected
