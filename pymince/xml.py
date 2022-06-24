import os
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

        for raw_line, event, obj in iterparse("countries.xml")
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

                yield line, event, obj

    parser.close()


class chunker:
    """
    Separate content of given xml file into chunk files
    according to bounded tag.

    :param filename:
    :param sep: tag name delimiter
    :param outdir:
        Directory to write the output fragments.
        If not specified, the generated fragments are saved in the directory of given "filename"
    """

    def __init__(self, filename, sep, outdir=None):
        self._filename = filename
        self._sep = sep
        self._outdir = outdir or os.path.dirname(self._filename)
        self._filetext = os.path.splitext(self._filename)[0]

    def __iter__(self):
        counter = 0
        writing = False
        for raw_line, event, obj in iterparse(self._filename):
            if event == "start" and obj.tag == self._sep:
                onlyone = True
                writing = True
                outname = os.path.join(self._outdir, f"{self._filetext}{counter}.xml")
                outfile = open(outname, mode="wt", encoding="utf-8")
                print(raw_line, file=outfile)
            elif event == "end" and obj.tag == self._sep:
                if not onlyone:
                    print(raw_line, file=outfile)
                outfile.close()
                writing = False
                counter += 1
                yield outname  # yield split filename
            elif event == "start" and writing:
                print(raw_line, file=outfile)
                onlyone = False
