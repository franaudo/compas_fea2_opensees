from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.problem import QuasiStaticStep
from compas_fea2.problem import DirectCyclicStep


class OpenseesQuasiStaticStep(QuasiStaticStep):
    def __init__(self, **kwargs):
        super(OpenseesQuasiStaticStep, self).__init__(**kwargs)
        raise NotImplementedError


class OpenseesDirectCyclicStep(DirectCyclicStep):
    def __init__(self, **kwargs):
        super(OpenseesDirectCyclicStep, self).__init__(**kwargs)
        raise NotImplementedError
