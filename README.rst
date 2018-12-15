PyXMP
======
An XMP reader written in pure python

Install
-------

'easy_install'::

    $ easy_install piexif

or 'pip'::

    $ pip install pyxmp

or download .zip, extract it. Put 'pyxmp' directory into your environment.

Why Choose PyXMP
-----------------

- Pure Python. So, it runs everywhere where Python runs.
- Documented. http://pyxmp.readthedocs.org/en/latest/

How to Use
----------
```python
from pyxmp import XMP

xmp_data = XMP(filepath="file_path", NS="https://namespace_url.org/1.0/")
try:
  value = xmp_data.NS.property
except AttributeError:
  pass
```

Example
-------


Environment
-----------

Tested on Python 2.7, 3.3, 3.4, 3.5, 3.6 and pypy3. Piexif would run even on IronPython. Piexif is OS independent and can run on Google App Engine.

License
-------

This software is released under the MIT license, see LICENSE.txt.

