# -*- coding: utf-8 -*-
import pytest

import pymince.text


def test_replace_all_with_one_old_values():
    ini = "No, woman, no cry"
    end = "No; woman; no cry"
    assert pymince.text.replace(ini, [","], ";") == end


def test_replace_all_with_two_old_values():
    ini = "No, woman, no cry"
    end = "Nowomannocry"
    assert pymince.text.replace(ini, [",", " "], "") == end


def test_replace_first_with_one_old_values():
    ini = "No, woman, no cry"
    end = "No; woman, no cry"
    assert pymince.text.replace(ini, [","], ";", count=1) == end


def test_replace_first_with_two_old_values():
    ini = "No, woman, no cry"
    end = "Nowoman, no cry"
    assert pymince.text.replace(ini, [",", " "], "", count=1) == end


def test_replace_not_ignore_case():
    ini = "No, woman, no cry"
    end = "Ok, woman, no cry"
    assert pymince.text.replace(ini, ["No"], "Ok") == end


def test_replace_with_type_error():
    with pytest.raises(TypeError):
        assert pymince.text.replace("No, woman, no cry", [","], 1)
