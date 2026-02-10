import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture
def config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


@pytest.fixture
def browser(config):
    browser_name = config.get("browser", "chrome").lower()
    
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        # Set window size to show only registration form
        options.add_argument("--window-size=500,800")
        options.add_argument("--window-position=800,100")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    
    elif browser_name == 'edge':
        options = webdriver.EdgeOptions()
        # Set window size to show only registration form
        options.add_argument("--window-size=500,800")
        options.add_argument("--window-position=800,100")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    yield driver
    driver.quit()        