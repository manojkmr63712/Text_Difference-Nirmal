# -*- coding: utf-8 -*-
import sys
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher
from pprint import pprint as _pprint
text1=',60125170993,2018-02-16 0:00:00,86000300257742,2018-01-26 0:00:00'
text2='2018-02-17 0:00:00,2018-02-17 0:00:00,2018-02-17 0:00:00,86000300159583,2018-01-26 0:00:00'
text3='20,60125170993,2018-02-18 0:00:00,86000300635552,2018-01-26 0:00:00'
s = SequenceMatcher(lambda x: x == " ",text1,text3)
print(round(s.ratio(),3))
if (round(s.ratio(),3)) >= 0.9:
    result = difflib.ndiff(text1.splitlines(),text3.splitlines())
    print('\n'.join(result))
    d = difflib.Differ()
    diff = d.compare(text1.splitlines(1),text2.splitlines(1))
    print '\n'.join(diff)
