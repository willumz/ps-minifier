[![PyPI](https://img.shields.io/pypi/v/ps-minifier.svg)](https://pypi.org/project/ps-minifier)
[![CircleCI](https://circleci.com/gh/Willumz/ps-minifier.svg?style=shield)](https://circleci.com/gh/Willumz/ps-minifier)
[![codecov](https://codecov.io/gh/Willumz/ps-minifier/branch/master/graph/badge.svg)](https://codecov.io/gh/Willumz/ps-minifier)

# ps-minifier
A very basic minifier for PowerShell scripts.

Currently, a semicolon (`;`) is required at the end of each line in the script it is given.

NOTE: This minifier is currently not very complex, and (while it works with programs I have tested it on) may not output functioning code for all programs it is given.

## Installation
```$ pip install ps-minifier```

## Usage
To display the help menu:

```$ psminifier -h```


```
usage: psminifier [-h] [-f FILE] [-o OUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path to file to minify
  -o OUT_FILE, --out-file OUT_FILE
                        path to save the result
```

Pass the path to the file:

```$ psminifier -f FILE_PATH```

Pass the path to save the result to:

```$ psminifier -o OUTPUT_PATH```

If `psminifier` is run without `-f` it will prompt the user to enter code via the standard input.
If it is run without `-o` it will output the result to the standard output.

The psminifier module can be imported from python script as follows.
```python
from ps_minifier.psminifier import minify

script = "[Some Powershell Scripts]"
minified_script = minify(script)
print(minified_script)
```
