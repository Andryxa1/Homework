

s1 = square_figure.square(3)
s2 = square_figure.rectangle(2, 4)

import square_figure


result = s1 - s2

if result > 0:
    print('s1 > s2')
elif result < 0:
    print('s1 < s2')
else:
    print('s1 = s2')
