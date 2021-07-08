import os

for _var in os.environ:
    _value = os.getenv(_var)
    print(f'{_var}={_value}')
