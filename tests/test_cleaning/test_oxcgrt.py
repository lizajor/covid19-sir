#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
import pytest
from covsirphy import Term, SubsetNotFoundError


class TestOxCGRTData(object):
    def test_cleaning(self, oxcgrt_data):
        df = oxcgrt_data.cleaned()
        assert {Term.DATE, Term.ISO3, Term.COUNTRY, Term.PROVINCE}.issubset(df.columns)

    def test_subset(self, oxcgrt_data):
        with pytest.raises(SubsetNotFoundError):
            oxcgrt_data.subset("Moon")
        df = oxcgrt_data.subset("JPN")
        assert {Term.DATE}.issubset(df.columns)

    def test_total(self, oxcgrt_data):
        with pytest.raises(NotImplementedError):
            oxcgrt_data.total()

    def test_map(self, oxcgrt_data):
        warnings.filterwarnings("ignore", category=UserWarning)
        oxcgrt_data.map(country=None)
