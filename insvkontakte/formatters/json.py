'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import Formatter
from json import loads
import re

class RawJSON(Formatter):
    
    _format = '.json'

    
class JSON(RawJSON):
    
    _json_fixer = re.compile('(\{|\,)( *)(\d+)( *)(:)')
    
    def format(self, data):
        data = self._json_fixer.sub(r'\1"\3":', data)
        return loads(data, encoding='utf-8', strict=False)