---
title: Settings Tesseract
sections:
  - PSM
  - OEM
---
### PSM
PSM is Page segmentation mode. That affects how Tesseract splits image in lines of text and words.

Page segmentation mode can be set:
```
PSM = Page Segmentation Mode
    - 0 = Orientation and script detection (OSD) only.
    - 1 = Automatic page segmentation with OSD.
    - 2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
    - 3 = Fully automatic page segmentation, but no OSD. (Default)
    - 4 = Assume a single column of text of variable sizes.
    - 5 = Assume a single uniform block of vertically aligned text.
    - 6 = Assume a single uniform block of text. (Default)
    - 7 = Treat the image as a single text line.
    - 8 = Treat the image as a single word.
    - 9 = Treat the image as a single word in a circle.
    - 10 = Treat the image as a single character.
    - 11 = Sparse text. Find as much text as possible in no particular order.
    - 12 = Sparse text with OSD.
    - 13 = Raw line. Treat the image as a single text line,
         bypassing hacks that are Tesseract-specific.
```

Automatic mode is much slower than more specific ones, and may affect performance. Sometimes, it’s feasible to implement a simple domain-specific field extraction pipeline and combine it with Single Line (7) or Single Word (8) page segmentation mode.

### OEM
OEM is Engine mode. Engine Mode controls the type of algorithm used by Tesseract.

```
OEM = Engine Mode
    - 0 = Original Tesseract only.
    - 1 = Neural nets LSTM only.
    - 2 = Tesseract + LSTM.
    - 3 = Default, based on what is available (Default)
```