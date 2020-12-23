from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

from WatchUI import WatchUI
from WatchUI.libs import BrowserOperator


class WatchUISelenium(WatchUI):
    def __init__(
        self,
        _type: str = "selenium",
        _outputs_folder="../Outputs",
        _format_image="png",
        **kwargs,
    ) -> None:
        super().__init__(
            type_=_type,
            outputs_folder=_outputs_folder,
            format_image=_format_image,
            **kwargs,
        )

        try:
            self.browser = BrowserOperator(BuiltIn, self.type_)
        except RobotNotRunningError as e:
            print(
                f"If you are trying to build documentation, than this exception is just nuisance, skipping...\n{str(e)}"
            )
            pass
