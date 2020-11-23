---
title: License
date: 2020-11-20
sections:
  - Basic
  - License for openCV keywords
  - License for PyMuPDF keywords
  - License for tesseract keywords
---
### Basic
Basically, the WatchUI library is open source as stated in the MIT License. You can use for free projects without any limitations.

Because I use the openCV tool to check for errors in the image, PyMuPDF and tesseract, it is necessary to realize that they also have licenses that also allow free distribution of the software, but with some modifications.

The keyword distribution can be found [here](/WatchUI/keywords.html#keyword-breakdown)

### License for openCV keywords
OpenCV is library for recognize image. The library is cross-platform and free for use under the open-source [Apache 2 License](https://www.apache.org/licenses/LICENSE-2.0).

[Link on OpenCV license](https://github.com/opencv/opencv/blob/master/LICENSE)


### License for PyMuPDF keywords
PyMuPDF is library is a Python binding for MuPDF - “a lightweight PDF and XPS viewer”.
I use for work with PDF without tesseract. (Py)MuPDF use this license:
```
GNU Affero General Public License v3 or later (AGPLv3+), GNU General Public License v3 or later (GPLv3+)
```

[Read more about license for PyMuPDF](https://www.gnu.org/licenses/agpl-3.0.en.html)

### License for tesseract keywords
This package contains an OCR engine - libtesseract and a command line program - tesseract. Tesseract 4 adds a new neural net (LSTM) based OCR engine which is focused on line recognition, but also still supports the legacy Tesseract OCR engine of Tesseract 3 which works by recognizing character patterns. Compatibility with Tesseract 3 is enabled by using the Legacy OCR Engine mode (--oem 0). It also needs traineddata files which support the legacy engine, for example those from the tessdata repository.

Tesseract use Apache License 2.0. More you can find [here](https://github.com/tesseract-ocr/tesseract/blob/master/LICENSE)