"""
The Desired Capabilities implementation.
"""


class DesiredCapabilities:
    """
        Set of default supported desired capabilities.

        Use this as a starting point for creating a desired capabilities object for
        requesting remote webdrivers for connecting to selenium server or selenium grid.

        Usage Example::

            # Create a desired capabilities object as a starting point.
            capabilities = DesiredCapabilities.FIREFOX.copy()
            capabilities['platform'] = "WINDOWS"
            capabilities['version'] = "10"

            # Instantiate an instance of Remote WebDriver with the desired capabilities.
            driver = webdriver.Remote(desired_capabilities=capabilities,
                                      command_executor=selenium_grid_url)

        Note: Always use '.copy()' on the DesiredCapabilities object to avoid the side
        effects of altering the Global class instance.

        """

    FIREFOX = {
        "browserName": "firefox",
        "acceptInsecureCerts": True,
    }

    CHROME = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
    }
