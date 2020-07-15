#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/29/20 3:19 PM
# @Author  : lingxiangxiang
# @File    : acrossbackendPyquil.py

import transitionBackend.Pyquilbackend as Pb
import re


def generate(address: str, name: str):
    simup = re.compile("Simulator_pyquil")
    qcp = re.compile("QC_pyquil")
    classcp = re.compile("Classical_pyquil")

    if simup.match(name):
        return Pb.simulator_to_qc(address), Pb.simulator_to_state_vector(address)

    if qcp.match(name):
        return Pb.qc_to_simulator(address), Pb.qc_to_state_vector(address)

    if classcp.match(name):
        return Pb.state_vector_to_qc(address), Pb.state_vector_to_qc(address)