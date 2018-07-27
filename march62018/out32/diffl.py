import difflib
from difflib_data import *
text1="2018-02-17 0:00:00,2018-02-17 0:00:00,2018-02-17 0:00:00,86000300159583,2018-01-26 0:00:00"
text2="2018-02-17 0:00:00,2018-03-17 0:00:00,2018-02-17 0:00:00,86000300159583,2018-01-26 0:00:00"
diff = ndiff(text1.splitlines(), text2.splitlines())
print '\n'.join(diff)
