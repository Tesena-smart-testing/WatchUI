# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=redefined-outer-name
import pytest
from hamcrest import assert_that, is_

from WatchUI.IBasics.Basics import Basics


@pytest.fixture(params=["png", "jpg"])
def image_format(request):
    return request.param


class TestBasics:
    def test_check_image_format(self, image_format):
        file_extension = Basics.check_image_format(Basics, image_format)

        if image_format == "png":
            assert_that(file_extension, is_(".png"))
        if image_format == ".jpg":
            assert_that(file_extension, is_(".jpg"))
