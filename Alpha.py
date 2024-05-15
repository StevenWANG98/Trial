import pandas as pd

df = pd.DataFrame({'a': [1, 2] * 3,
                   'b': [True, False] * 3,
                   'c': [1.0, 2.0] * 3,
                   'd': ['x', 'y']*3,
                   'e': ['x', 'y']*3})

print(df)

df['new'] = df.apply(lambda X: 1 if (X.b and X.c == 1) else 0, axis=1)
print(df)





