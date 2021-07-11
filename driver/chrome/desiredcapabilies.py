class Capabilities:

    def __init__(self):
        self.capability = {}

    def add_capability(self, attribute, value):
        self.capability[attribute] = value

    def add_desired_capability(self, attribute, value):
        if self.capability.get('desiredCapabilities') is None:
            self.capability['desiredCapabilities'] = {}
        self.capability['desiredCapabilities'][attribute] = value

    def add_chrome_option(self, attribute, value):
        if self.capability['desiredCapabilities'].get("chromeoptions") is None:
            self.capability['desiredCapabilities']['chromeoptions'] = {}
        self.capability['desiredCapabilities']['chromeoptions'][attribute] = value
