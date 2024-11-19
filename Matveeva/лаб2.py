from abc import ABC, abstractmethod
import unittest

# Абстрактные классы для продуктов
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Конкретные продукты
class WindowsButton(Button):
    def render(self):
        return "Windows Button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows Checkbox"

class MacOSButton(Button):
    def render(self):
        return "MacOS Button"

class MacOSCheckbox(Checkbox):
    def render(self):
        return "MacOS Checkbox"

# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Юнит-тесты
class TestAbstractFactory(unittest.TestCase):
    def test_windows_factory(self):
        factory = WindowsFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        
        self.assertIsInstance(button, WindowsButton)
        self.assertIsInstance(checkbox, WindowsCheckbox)
        self.assertEqual(button.render(), "Windows Button")
        self.assertEqual(checkbox.render(), "Windows Checkbox")

    def test_macos_factory(self):
        factory = MacOSFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        
        self.assertIsInstance(button, MacOSButton)
        self.assertIsInstance(checkbox, MacOSCheckbox)
        self.assertEqual(button.render(), "MacOS Button")
        self.assertEqual(checkbox.render(), "MacOS Checkbox")

if __name__ == '__main__':
    unittest.main()