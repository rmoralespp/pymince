import os
import shutil
import tempfile
import zipfile

import pymince.file
import tests.test_file


def test_match_on_zip():
    with tempfile.TemporaryDirectory() as tmpdir:
        basename1 = "file1.log"
        basename2 = "file2.log"
        basename3 = "unexpected.log"
        tests.test_file.make_file(os.path.join(tmpdir, basename1))
        tests.test_file.make_file(os.path.join(tmpdir, basename2))
        tests.test_file.make_file(os.path.join(tmpdir, basename3))

        zip_path = shutil.make_archive(tmpdir, "zip", root_dir=tmpdir)
        with zipfile.ZipFile(zip_path) as zp:
            result = pymince.file.match_on_zip(zp, "^file")
            assert tuple(result) == (basename1, basename2)
