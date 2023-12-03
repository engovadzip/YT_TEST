from selenium.common.exceptions import (ElementNotVisibleException, NoSuchElementException,
                                        TimeoutException, WebDriverException)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Actions:
# Ожидание появления элемента страницы
    def wait(self, browser, time, how, what):
        try:
            WebDriverWait(browser, time).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        except ElementNotVisibleException:
            return False
        except NoSuchElementException:
            return False
        return True

# Ожидание "кликабельности" элемента страницы
    def clickable(self, browser, time, how, what):
        try:
            WebDriverWait(browser, time).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        except WebDriverException:
            return False
        except NoSuchElementException:
            return False
        except ElementNotVisibleException:
            return False
        return True

# Клик по объекту, с которым не срабатывает click()
    def click(self, browser, obj):
        ActionChains(browser).click(obj).perform()

# Клик правой кнопкой мыши
    def right_click(self, browser, obj):
        ActionChains(browser).context_click(obj).perform()

# Проверка появления элемента на странице
    def assert_wait(self, browser, time, how, what, message):
        self.wait(browser, time, how, what)
        assert self.wait(browser, time, how, what), message

# Проверка наличия и "кликабельности" элемента
    def assert_clickable(self, browser, time, how, what, message):
        self.clickable(browser, time, how, what)
        assert self.clickable(browser, time, how, what), message

# Прокручивание мышью до области видимости элемента
    def scroll_to_element(self, browser, element):
        browser.execute_script("arguments[0].scrollIntoView();", element)

# Перемещение мыши к элементу
    def move_to_element(self, browser, element):
        ActionChains(browser).move_to_element(element).perform()

# Перемещение одного элемента к другому
    def drag_and_drop(self, browser, el1, el2):
        ActionChains(browser).drag_and_drop(el1, el2).perform()