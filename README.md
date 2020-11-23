# WatchUI

## [Documentation](https://tesena-smart-testing.github.io/WatchUI/) | [Tesena](https://www.tesena.com/) | [Pypi](https://pypi.org/project/WatchUI/)


### Basic Info


Custom library for comparing images with use in Robot Framework.


### Folder structure

```
Testing-api
└── .github/workflows           # Folder with CI for github actions
└── Img                         # Folder with test data
└── test                        # Folder with example how to write rf test.
│    └── keywords               # Keywords and variables
│    └── unit_test.robot        # File with TC
└── WatchUI                     # Folder with WatchUI library
│    └── WatchUI.py             # File with custom library
└── README.MD                   # Here you are :-)
└── setup.py                    # File for easy setup use with pip install .
```

### Install
You can find detail in [Documentation](https://procesor2017.github.io/WatchUI/) but basically use pip:
```
pip install WatchUI
```


### Sample results

_Image where the differences are stored + You can see two black box in left corner. These black box are ignored during comparison._

<img src="/Img/logscreen.png" width="850" height="300">

_The red rectangles outlining missing elements on compared screens_

<img src="/Img/img_inlog.png" width="850" height="300">
