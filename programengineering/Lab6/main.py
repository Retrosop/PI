from PIL import Image, ImageFilter, ImageEnhance
class FilterStrategy:
    def apply(self, image):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")


class BlurFilter(FilterStrategy):
    def apply(self, image):
        return image.filter(ImageFilter.BLUR)


class ContrastFilter(FilterStrategy):
    def apply(self, image):
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(2)


class BlackAndWhiteFilter(FilterStrategy):
    def apply(self, image):
        return image.convert("L")


class ImageProcessor:
    def __init__(self):
        self.filter_strategy = None

    def set_filter_strategy(self, filter_strategy: FilterStrategy):
        self.filter_strategy = filter_strategy

    def process_image(self, image):
        if not self.filter_strategy:
            raise ValueError("Фильтр не установлен!")
        return self.filter_strategy.apply(image)


if __name__ == "__main__":
    input_image_path = "example.jpg"
    output_image_path = "output.jpg"

    try:
        image = Image.open(input_image_path)
    except FileNotFoundError:
        print(f"Файл {input_image_path} не найден. Проверьте путь к файлу.")
        exit()

    processor = ImageProcessor()

    print("Выберите фильтр для применения:")
    print("1. Размытие")
    print("2. Увеличение контраста")
    print("3. Черно-белый фильтр")

    choice = input("Введите номер фильтра: ")

    if choice == "1":
        processor.set_filter_strategy(BlurFilter())
    elif choice == "2":
        processor.set_filter_strategy(ContrastFilter())
    elif choice == "3":
        processor.set_filter_strategy(BlackAndWhiteFilter())
    else:
        print("Некорректный выбор!")
        exit()

    result_image = processor.process_image(image)

    result_image.show()
    result_image.save("filtered_" + output_image_path)
    print("Фильтр успешно применён и изображение сохранено!")
