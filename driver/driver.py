from selenium import webdriver

class Selenium:

    def __init__(self) -> None:
        self.driver = None
        self.options = None

    def initial_browser(self, browserName, programPath):
        temp = str(browserName).lower().strip()

        if not temp:
            raise ValueError("Error with input browser name")
        
        temp = str(programPath).lower().strip()

        if not temp:
            raise ValueError("No definition of local executable program path")
        
        match temp:
            case "firefox":
                self.driver = webdriver.Firefox(executable_path=programPath)
                self.options = webdriver.FirefoxOptions()
                return "firefox"
            case "edge":
                self.driver = webdriver.Edge(executable_path=programPath)
                self.options = webdriver.EdgeOptions()
                return "edge"
            case "chrome":
                self.driver = webdriver.Chrome(executable_path=programPath)
                self.options = webdriver.ChromeOptions()
                return "chrome"