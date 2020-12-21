# pylint: disable = too-few-public-methods
"""Browser automation libraries' classes.
"""

from typing import Callable, Iterable


class BrowserOperator:
    """Provides access to running instance of RobotFramework's
    used browser automation library. This library is specified via `type_` keyword.

    Currently supported `type_` values:
        - selenium
        - playwright

    Args:
        rf_built_in (Callable): RobotFramework's `BuiltIn()` method
        type_ (str): used browser automation library
    """

    def __init__(self, rf_built_in: Callable, type_: str) -> None:
        if type_ == "selenium":
            self.instance = SeleniumBrowser(rf_built_in)

        elif type_ == "playwright":
            self.instance = PlaywrightBrowser(rf_built_in)

        else:
            rf_built_in().fatal_error(
                "Browser automation library of '{type_}' is not supported.\
                \nChoose either 'selenium' or 'playwright'.".format(
                    type_=type_
                )
            )


class SeleniumBrowser:
    """Initializes object that represents `robotframework-seleniumLibrary`
    running instance.

    Args:
        rf_built_in (Callable): RobotFramework's `BuiltIn()` method
    """

    def __init__(self, rf_built_in: Callable) -> None:
        self.browser = rf_built_in().get_library_instance("SeleniumLibrary")

    def capture_page_screenshot(self, filepath: str) -> None:
        """Captures and saves screenhot of the viewport of the browser.

        Args:
            filepath (str): filepath to save the screenshot to.
        """
        self.browser.capture_page_screenshot(filepath)

    def set_window_size(self, width: int, height: int) -> None:
        """Sets the size of the browser window.

        Args:
            width (int): width in pixels
            height (int): height in pixels
        """
        self.browser.set_window_size(width, height)

    def execute_script(self, x_coord: int, y_coord: int) -> Iterable:
        """Executes hardcoded javascript piece of code.

        Args:
            x_coord (int): x coords in the browser window.
            y_coord (int): y coords in the browser window.

        Returns:
            Iterable: list of element objects found on given coordinates.
        """
        return self.browser.driver.execute_script(
            f"return document.elementsFromPoint({x_coord}, {y_coord});"
        )


class PlaywrightBrowser:
    """Initializes object that represents `robotframework-browser`
    aka `playwright` running instance.

    Args:
        rf_built_in (Callable): RobotFramework's `BuiltIn()` method
    """

    def __init__(self, rf_built_in: Callable) -> None:
        self.browser = rf_built_in().get_library_instance("Browser")

    def capture_page_screenshot(self, filepath: str) -> None:
        """Captures and saves screenhot of the viewport of the browser.

        Args:
            filepath (str): filepath to save the screenshot to.
        """
        # since robotframework-browser keyword automatically adds .png
        # we have to cut it
        self.browser.take_screenshot(filename=filepath, fullPage=False)

    def set_window_size(self, width: int, height: int) -> None:
        """Sets the size of the browser window.

        Args:
            width (int): width in pixels
            height (int): height in pixels
        """
        self.browser.set_viewport_size(width, height)

    def execute_cript(self, x_coord: int, y_coord: int) -> Iterable:
        """Executes hardcoded javascript piece of code.

        Args:
            x_coord (int): x coords in the browser window.
            y_coord (int): y coords in the browser window.

        Returns:
            Iterable: list of element objects found on given coordinates.
        """
        return self.browser.execute_javascript(
            f"return document.elementsFromPoint({x_coord}, {y_coord});"
        )
