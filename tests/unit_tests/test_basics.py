# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=redefined-outer-name
import os
import shutil

import pytest
from hamcrest import assert_that, instance_of, is_
from WatchUI.IBasics.Basics import Basics


@pytest.fixture(params=["png", "jpg"])
def image_format(request):
    return request.param


@pytest.fixture(params=["../Outputs", "Not-Default-Outputs"])
def output_path(request):
    yield request.param
    shutil.rmtree(request.param)


@pytest.fixture(params=[1.0, 0.0, 0.5])
def ssim(request):
    return request.param


@pytest.fixture(params=[4, 3, 5])
def no_of_args(request):
    return request.param


class TestBasics:
    def test_check_dir(self, output_path):
        dir_status = os.path.isdir(
            os.path.abspath(Basics.check_dir(Basics, output_path))
        )
        assert_that(dir_status, is_(True))
        assert_that(Basics.save_folder_path == output_path)

    def test_check_ssim(self, ssim):
        ssim_check = Basics.check_ssim(Basics, ssim)
        assert_that(ssim_check, instance_of(float))
        assert_that(ssim_check, is_(float(ssim)))

    def test_check_image_format(self, image_format):
        file_extension = Basics.check_image_format(Basics, image_format)

        if image_format == "png":
            assert_that(file_extension, is_(".png"))
        elif image_format == "jpg":
            assert_that(file_extension, is_(".jpg"))

    def test_no_of_args_check(self, no_of_args):
        if no_of_args == 4:
            assert_that(
                Basics.check_if_args_has_ok_numbers(0, 1, 2, 3),
                is_(True),
            )

        elif no_of_args == 3:
            with pytest.raises(ValueError):
                Basics.check_if_args_has_ok_numbers(0, 1, 2)

        elif no_of_args == 5:
            with pytest.raises(ValueError):
                Basics.check_if_args_has_ok_numbers(0, 1, 2, 3, 4)
