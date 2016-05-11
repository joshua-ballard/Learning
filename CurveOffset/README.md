### CurveOffset
A Python script that, when called, takes a CryoCon .crv file and an offset and writes a new .crv file with the resistance offset by 'offset'.

```shell
  python CurveOffset.py <filename.crv> <offset>
```

Written such that it can be imported and used en-masse:

```python
import CurveOffset

CurveOffset.main(argument1, argument2)
```
