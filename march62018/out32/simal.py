import re
from simhash import Simhash
def get_features(s):
    width = 2
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

print '%x' % Simhash(get_features('20,60125170993,2018-02-18 0:00:00,86000300635552,2018-01-26 0:00:00')).value
print '%x' % Simhash(get_features('2018-02-18,60125170993,2018-02-18 0:00:00,86000300635552,2018-01-26 0:00:00')).value
print '%x' % Simhash(get_features('2018-02-13 0:00:00,60125170993,2018-02-13 0:00:00,86000300420496,2018-01-26 0:00:00')).value
