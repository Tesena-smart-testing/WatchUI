from WatchUI.IBasics.Basics import Basics
import fitz
import imutils

class Pdf(Basics):
    def pdf_to_image(self, path, save_folder, name, number_page):
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
        else:
            page = doc.loadPage(int(number_page))  # number of page
            pix = page.getPixmap()
            output = save_folder + "/" + name + ".png"
            pix.writePNG(output)

    def return_text_from_area(self, path, page_number: int, x1, y1, x2, y2):
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

    def should_exist_this_text(self, path, page_number: int, text):
        self.check_image_exists(path)
        doc = fitz.open(path)
        page = doc[page_number]
        text_instances = page.searchFor(text)
        if len(text_instances) > 0:
            return True
        else:
            return False

