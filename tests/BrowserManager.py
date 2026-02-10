from selenium import webdriver

def get_brower(browser_name):
    if browser_name.lower() == 'chrome':
       options = webdriver.ChromeOptions()
       options.add_argument("--start-maximized")
       return webdriver.Chrome(options=options)
    elif browser_name.lower() == 'edge':
          options = webdriver.EdgeOptions()
          options.add_argument("--start-maximized")
          return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")