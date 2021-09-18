# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=redefined-outer-name
import shutil
import os
import pytest
from hamcrest import assert_that, is_

from WatchUI.IBasics.Basics import Basics


@pytest.fixture(params=["png", "jpg"])
def image_format(request):
    return request.param


@pytest.fixture(params=["../Outputs", "Not-Default-Outputs"])
def output_path(request):
    yield request.param
    shutil.rmtree(request.param)


class TestBasics:
    def test_check_dir(self, output_path):
        dir_status = os.path.isdir(
            os.path.abspath(Basics.check_dir(Basics, output_path))
        )
        assert_that(dir_status, is_(True))
        assert_that(Basics.save_folder_path == output_path)

    def test_check_image_format(self, image_format):
        file_extension = Basics.check_image_format(Basics, image_format)

        if image_format == "png":
            assert_that(file_extension, is_(".png"))
        if image_format == ".jpg":
            assert_that(file_extension, is_(".jpg"))
