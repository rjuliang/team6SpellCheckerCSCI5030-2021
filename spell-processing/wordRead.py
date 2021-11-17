
"""
Special thanks to Peter Norvig for providing this amazing solution.

Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

import re

def words(text): return re.findall(r'\w+', text)