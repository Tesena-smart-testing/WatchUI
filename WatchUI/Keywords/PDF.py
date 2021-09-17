from WatchUI.IBasics.Basics import Basics
import fitz


class Pdf(Basics):
    def create_pdf_to_image(self, path: str, save_folder: str, name: str, number_page: str):
        save_folder = self.check_dir(save_folder)
        self.check_image_exists(path)

        doc = fitz.open(path)
        if number_page == "-1":
            page_count = doc.pageCount
            for x in range(0, page_count):
                page = doc.loadPage(x)  # load all pages one by one
                pix = page.getPixmap()
                output = save_folder + "/" + name + "_" + str(x) + ".png"
                pix.writePNG(output)
                self.set_log_message(work_object="Image", path_to_image=output)
        else:
            page = doc.loadPage(int(number_page))  # number of page
            pix = page.getPixmap()
            output = save_folder + "/" + name + ".png"
            pix.writePNG(output)
            self.set_log_message(work_object="Image", path_to_image=output)

    def create_return_text_from_area(self, path, page_number: int, x1: int, y1: int, x2: int, y2: int):
        self.check_image_exists(path)
        doc = fitz.open(path)
        page = doc[page_number]
        words_list = page.getTextWords()
        text = ""
        xy_numbers = 1

        for xy in words_list:
            if float(xy[0]) > float(x1) and float(xy[1]) > float(y1) and float(xy[2]) < float(x2) and \
                    float(xy[3]) < float(y2):
                if xy_numbers == len(words_list):
                    text += xy[4]
                else:
                    text += xy[4] + " "
            xy_numbers += 1
        return text

    def create_should_exist_this_text(self, path, page_number: int, text):
        self.check_image_exists(path)
        doc = fitz.open(path)
        page = doc[page_number]
        text_instances = page.searchFor(text)
        if len(text_instances) > 0:
            return True
        else:
            return False

