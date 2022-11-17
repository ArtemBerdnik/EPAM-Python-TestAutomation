from robot.libraries.BuiltIn import BuiltIn


class ScreenshotMakerListener:

    ROBOT_LISTENER_API_VERSION = 2

    @staticmethod
    def end_keyword(name, attrib):
        if "custom_screenshot" in attrib['tags']:
            print(f"\nmaking a screenshot of '{name}' keyword\n")
            seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
            seleniumlib.capture_page_screenshot()