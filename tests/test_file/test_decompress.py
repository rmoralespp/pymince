import gzip
import json
import os
import tempfile

import pymince.file
import pymince.json


def test_decompress_txt():
    text = "foo, var, baz, ño"
    encoding = "utf-8"
    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, "src.txt.gz")
        dst_path = os.path.join(tmpdir, "dst.txt")
        with open(src_path, mode='wb') as f:
            compressed = gzip.compress(text.encode(encoding))
            f.write(compressed)

        res_path = pymince.file.decompress(src_path, dst_path)
        assert res_path == dst_path

        with open(dst_path, encoding=encoding) as dst:
            assert dst.read() == text


def test_decompress_json():
    data = {
        'foo': 'var',
        'baz': 'ño',
        "nested": [
            "á", 1,
            {"date": "2019-01-22T17:27:22+08:00"}
        ],
    }
    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, "src.json.gz")
        dst_path = os.path.join(tmpdir, "dst.json")

        dumped = json.dumps(data).encode(pymince.json.ENCODING)
        compressed = gzip.compress(dumped)
        with open(src_path, 'wb') as f:
            f.write(compressed)

        res_path = pymince.file.decompress(src_path, dst_path)
        assert res_path == dst_path
        assert pymince.json.load_from(dst_path) == data
