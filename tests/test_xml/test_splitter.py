import os
import tempfile

import pytest

import pymince.xml
import tests


@pytest.fixture(scope='module')
def xml_string():
    lines = (
        "<?xml version='1.0' encoding='UTF-8'?>",
        "<countries>",
        "  <country code='af' handle='afghanistan' continent='asia' iso='4'>Afghanistan</country>",
        "  <country code='al' handle='albania' continent='europe' iso='8'>Albania</country>",
        "</countries>"
    )
    return "\n".join(lines)


def test_splitter_files(xml_string):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "countries.xml")
        tests.make_file(filename, content=xml_string)
        result = pymince.xml.splitter(filename, "country")
        assert list(result) == [
            os.path.join(tmpdir, "countries0.xml"),
            os.path.join(tmpdir, "countries1.xml")
        ]


def test_splitter_content_file(xml_string):
    with tempfile.TemporaryDirectory() as tmpdir:
        filename = os.path.join(tmpdir, "countries.xml")
        tests.make_file(filename, content=xml_string)
        result = pymince.xml.splitter(filename, "country")

        next(iter(result))
        expected = "  <country code='af' handle='afghanistan' continent='asia' iso='4'>Afghanistan</country>"
        outfile = os.path.join(tmpdir, "countries0.xml")
        with open(outfile) as f:
            assert f.read().replace("\n", "") == expected
