from selenium.webdriver.common.by import By



class HomePage:
    '''
    管理登录页面所有页面元素，格式为：定位方式，元素路径，元素描述信息
    '''
    search_input = (By.XPATH, '//*[@id="kw"]','百度搜索框')
    search_button =(By.XPATH,'//*[@id="su"]','百度一下搜索按钮')


