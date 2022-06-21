from utils.enumClass import RegexTypes
from utils.enumClass import DeclaredType
import re

class Types:
    @staticmethod
    def is_list(key):
        return isinstance(key, list)
    @staticmethod
    def what_type(key):
        for regex in RegexTypes:
            if re.search(regex.value[0], key):
                return regex.value[1]
        return None