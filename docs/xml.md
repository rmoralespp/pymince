# Xml
XML utilities.

**iterparse**
```
iterparse(filename)

Incrementally parse XML document into ElementTree.

This function is based on: https://github.com/python/cpython/issues/93618

'Fix misleading hint for original ElementTree.iterparse.'
'''
The code below deletes a root child once it is completed, then processes and removes
it from the memory (if nothing more references to it ofc).
This allows to process 7GB XML with with a memory usage up to 10MB (in case of great number of root children).
'''

:param str filename: XML filename
:rtype: Generator

 Examples:
    from pymince.xml import iterparse

    for event, obj in iterparse("countries.xml")
        if event == 'start'
            print(obj, obj.tag, obj.attrib, obj.text)

    >>Output<<
    <Element 'country' at 0x0000018ADF9D0CC0> country {'code': 'as', 'iso': '16'} American Samoa
    <Element 'country' at 0x0000018ADF9D0C70> country {'code': 'ad', 'iso': '20'} Andorra
```