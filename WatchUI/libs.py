"""Browser automation libraries' classes.
"""

from typing import Callable, Iterable


class BrowserOperator:
    def __init__(self, type_: str, rf_built_in: Callable) -> None:
        if type_ == "selenium":
            self.instance = SeleniumBrowser(rf_built_in)

        if type_ == "playwright":
            self.instance = PlaywrightBrowser(rf_built_in)


class SeleniumBrowser:
    def __init__(self, rf_built_in: Callable) -> None:
        self.browser = rf_built_in().get_library_instance("SeleniumLibrary")

    def capture_page_screenshot(self, filepath: str) -> None:
        self.browser.capture_page_screenshot(filepath)

    def set_window_size(self, width: int, height: int) -> None:
        self.browser.set_window_size(width, height)

    def execute_script(self, x_coord: int, y_coord: int) -> Iterable:
        return self.browser.driver.execute_script(
            f"return document.elementsFromPoint({x_coord}, {y_coord});"
        )


class PlaywrightBrowser:
    def __init__(self, rf_built_in: Callable) -> None:
        self.browser = rf_built_in().get_library_instance("Browser")

    def capture_page_screenshot(self, filepath: str) -> None:
        self.browser.take_screenshot(filename=filepath, fullpage=False)

    def set_window_size(self, width: int, height: int) -> None:
        self.browser.set_viewport_size(width, height)

    def execute_cript(self, x_coord: int, y_coord: int) -> Iterable:
        return self.browser.execute_javascript(
            f"return document.elementsFromPoint({x_coord}, {y_coord});"
        )
