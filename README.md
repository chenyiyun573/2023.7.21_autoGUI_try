please use python3.9 or 3.6~3.9

```
python3.9 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
```










Issue Fixing:
1. if tuple(PIL__version__) < (6, 2, 1):
TypeError: '<' not supported between instances of 'str' and 'int'

/Users/chenyiyun/Desktop/2023.7.21_autoGUI_try/.venv/lib/python3.9/site-packages/pyscreeze/\__init\__.py. line 527
replace it with:
```
if tuple(map(int, PIL__version__.split('.'))) < (6, 2, 1):
```


