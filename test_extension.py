#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 AUTHORNAME

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Unit tests, to be run using pytest."""


__author__ = "AUTHORNAME"
__copyright__ = "Copyright (C) YEAR AUTHORNAME"
__email__ = "AUTHOREMAIL"
__license__ = "Apache 2.0"


import sys
import os
import kineticstoolkit as ktk
import numpy as np


# Add this extension to the path, for testing before the extension is
# distributed and installed via pip.
if os.path.dirname(__file__) not in sys.path:
    sys.path.append(os.path.dirname(__file__))

ktk.import_extensions()


def test_read_n3d():
    """Regression test."""
    markers = ktk.ext.n3d.read_n3d("data/kinematics_sample_optotrak.n3d")

    tol = 1e-4
    assert np.abs(np.sum(markers.data["Marker0"]) - 172.3365) < tol
    assert np.abs(np.sum(markers.data["Marker40"]) + 45.3753) < tol
    assert markers.time_info["Unit"] == "s"
    assert markers.data_info["Marker40"]["Unit"] == "m"

    labels = [
        "Probe1",
        "Probe2",
        "Probe3",
        "Probe4",
        "Probe5",
        "Probe6",
        "FRArrD",
        "FRArrG",
        "FRav",
        "ScapulaG1",
        "ScapulaG2",
        "ScapulaG3",
        "ScapulaD1",
        "ScapulaD2",
        "ScapulaD3",
        "Tete1",
        "Tete2",
        "Tete3",
        "Sternum",
        "BrasG1",
        "BrasG2",
        "BrasG3",
        "EpicondyleLatG",
        "AvBrasG1",
        "AvBrasG2",
        "AvBrasG3",
        "NAG",
        "GantG1",
        "GantG2",
        "GantG3",
        "BrasD1",
        "BrasD2",
        "BrasD3",
        "EpicondyleLatD",
        "AvBrasD1",
        "AvBrasD2",
        "AvBrasD3",
        "NAD",
        "GantD1",
        "GantD2",
        "GantD3",
    ]

    markers = ktk.ext.n3d.read_n3d(
        "data/kinematics_sample_optotrak.n3d",
        labels=labels,
    )

    assert np.abs(np.sum(markers.data["Probe1"]) - 172.3365) < tol
    assert np.abs(np.sum(markers.data["GantD3"]) + 45.3753) < tol
    assert markers.time_info["Unit"] == "s"
    assert markers.data_info["GantD3"]["Unit"] == "m"


if __name__ == "__main__":
    # You can either run this file directly, or run 'pytest test_extension.py' in
    # a terminal.
    import pytest

    pytest.main([__file__])
