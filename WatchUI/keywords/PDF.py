# pylint: disable=no-member, invalid-name, too-many-arguments
"""
PDF class module
"""
from typing import Any
import fitz
from robot.api.deco import keyword
from ..Ibasic.IBasic import IBasic


class Pdf(IBasic):
    """Class representing PDF and its methods.
    Class is not being instantiated itself, but inherited by main WatchUI.py module.
    Args:
        Basics (object): interface class
    """

    save_folder = ""

    @keyword
    def pdf_to_image(
        self,
        path: str,
        name: str = "img",
        page_number: int = -1,
        zoom: int = 3,
        save_folder=save_folder,
    ) -> None:
        """Converts pdf to image - .png format.
        Args:
            path (str): path to the .pdf file
            save_folder (str): path to the save folder
            name (str): name of the file of the image to be saved
            number_page (str): page from the pdf document to be saved as image.
            if value is `-1`, then saves all pages as separated .png files.
        """
        checked_save_folder: str = self.check_dir(save_folder)
        self.check_image_exists(path)

        doc: Any = fitz.open(path)
        page: Any
        pix: Any
        mat = fitz.Matrix(zoom, zoom)
        if page_number == "-1":
            page_count: int = doc.pageCount
            for x in range(0, page_count):
                page = doc.load_page(x)  # load all pages one by one
                pix = page.get_pixmap(matrix=mat)
                output: str = f"{checked_save_folder}/{name}_{str(x)}.png"
                pix.save(output)
                self.set_log_message(work_object="Image", path_to_image=output)
        else:
            page = doc.load_page(int(page_number))  # number of page
            pix = page.get_pixmap(matrix=mat)
            output = f"{checked_save_folder}/{name}.png"
            pix.save(output)
            self.set_log_message(work_object="Image", path_to_image=output)

    @keyword
    def return_text_from_area(
        self, path: str, page_number: int, x1: int, y1: int, x2: int, y2: int
    ) -> str:
        """Opens provided PDF file and returns text from the given area.
        Args:
            path (str): path to the pdf file
            page_number (int): page number in the pdf file
            x1 (int):
            y1 (int):
            x2 (int):
            y2 (int):
        Returns:
            str: selected text from the area
        """
        self.check_image_exists(path)
        doc: Any = fitz.open(path)
        page: Any = doc[page_number]
        words_list: list[Any] = page.get_text_words()
        text: str = ""
        xy_numbers: int = 1

        for xy in words_list:
            if (
                float(xy[0]) > float(x1)
                and float(xy[1]) > float(y1)
                and float(xy[2]) < float(x2)
                and float(xy[3]) < float(y2)
            ):
                if xy_numbers == len(words_list):
                    text += xy[4]
                else:
                    text += xy[4] + " "
            xy_numbers += 1
        return text

    @keyword
    def should_exist_this_text(self, path: str, page_number: int, text: str) -> bool:
        """Verifies, whether given text is present in the document and given page.
        Args:
            path (str): path to pdf document
            page_number (int): page number
            text (str): text to check for presence
        Returns:
            bool: `True` if present, else `False`
        """
        self.check_image_exists(path)
        doc: Any = fitz.open(path)
        page: Any = doc[page_number]
        text_instances: list[Any] = page.search_for(text)
        if len(text_instances) > 0:
            return True

        return False
