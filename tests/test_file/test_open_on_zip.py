import os
import shutil
import tempfile
import zipfile

import pymince.file
import tests.test_file


def test_open_on_zip():
    with tempfile.TemporaryDirectory() as tmpdir:
        basename1, content1 = "file1.log", "contentOfFile1"
        basename2, content2 = "file2.log", "contentOfFile2"
        filename1 = os.path.join(tmpdir, basename1)
        filename2 = os.path.join(tmpdir, basename2)
        tests.test_file.make_file(filename1, content=content1)
        tests.test_file.make_file(filename2, content=content2)

        zip_path = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        with zipfile.ZipFile(zip_path) as zp:
            with pymince.file.open_on_zip(zp, basename1) as file1:
                assert file1.read() == content1
            with pymince.file.open_on_zip(zp, basename2) as file2:
                assert file2.read() == content2
