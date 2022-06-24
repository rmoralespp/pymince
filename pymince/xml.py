import xml.etree.ElementTree as etree


def iterparse(filename):
    """
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

    """

    parser = etree.XMLPullParser(['start', 'end'])  # can be replaced with iterparse as well
    root = None
    with open(filename, encoding="utf-8") as f:
        for line in f:
            parser.feed(line)
            for event, obj in parser.read_events():
                if event == 'start':
                    if root is None:
                        root = obj
                elif event == 'end':
                    if len(root) > 0 and obj == root[0]:
                        del root[0]
                        # process obj

                yield event, obj

    parser.close()
