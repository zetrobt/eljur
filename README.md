## eljur
Eljur.ru diary API Wrapper

## Installing
You can install it using the command below:
```shell
pip install git+https://github.com/zetrobt/eljur.git
```
## How to use?
Now you need to get instance of Eljur class:
```python
from eljur import Eljur

eljur = Eljur(vendor*, login*, password*, devkey, domain)
```
After this you can use methods. At this time there are only two methods: call and getrules (under construction):
```python
eljur.call(method, dict_of_params)
eljur.get_rules()
```
