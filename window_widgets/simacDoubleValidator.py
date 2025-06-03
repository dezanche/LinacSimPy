# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: views\simacDoubleValidator.pyc
# Compiled at: 2016-07-29 10:54:06
from PyQt5.QtGui import QDoubleValidator, QValidator
from sys import float_info

class SimacDoubleValidator(QDoubleValidator):
    """
    Fix for strange behavior of default QDoubleValidator
    """

    def __init__(self, bottom=float_info.min, top=float_info.max, decimals=float_info.dig, parent=None):
        super(SimacDoubleValidator, self).__init__(bottom, top, decimals, parent)

    def validate(self, input, pos):
        state, pos = QDoubleValidator.validate(self, input, pos)
        if state == QValidator.Intermediate and input.toDouble() > bottom() and input.toDouble() < top():
            return (QValidator.Acceptable, pos)
        else:
            return (
             QValidator.Invalid, pos)

        return (state, pos)
# okay decompiling simacDoubleValidator.pyc
