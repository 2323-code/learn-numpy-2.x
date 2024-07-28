# https://qiita.com/mo256man/items/3578f374cd775ce54cb8
import datetime

import numpy as np

print("ver", np.__version__)
# 2.0.1


now1 = datetime.datetime.now()
l = np.strings.add(["num", "doc"], ["py", "umentation"])
# l = np.char.add(["num", "doc"], ["py", "umentation"]) # ver 1.x まで
print(l.dtype)
print(l)
now2 = datetime.datetime.now()

print(now2 - now1)