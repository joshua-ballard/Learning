# LS_to_CCon
A tool for converting Lakeshore Cernox curves to CryoCon curves.  

Lakeshore curves should be the .dat format.
CryoCon curve will be in .crv format.

## USAGE

python LS_to_CCon -i <filename.dat>

currently, this will have to be done one file at a time.

Presumably, you could write another script to recursively walk through the directory and subdirectories and call this module:

```
import LS_to_CCon

LC_to_CCon.main(argument)  
```
