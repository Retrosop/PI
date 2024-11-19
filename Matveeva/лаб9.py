from abc import ABC, abstractmethod

# Базовый класс для создания контента
class ContentCreationTemplate(ABC):
    def create_content(self):
        self.research_topic()
        self.write_content()
        self.publish_content()

    @abstractmethod
    def research_topic(self):
        pass

    @abstractmethod
    def write_content(self):
        pass

    @abstractmethod
    def publish_content(self):
        pass

# Подкласс для создания статей
class ArticleCreation(ContentCreationTemplate):
    def research_topic(self):
        print("Исследование темы для статьи...")

    def write_content(self):
        print("Написание текста статьи...")

    def publish_content(self):
        print("Публикация статьи на блоге...")

# Подкласс для создания видео
class VideoCreation(ContentCreationTemplate):
    def research_topic(self):
        print("Исследование темы для видео...")

    def write_content(self):
        print("Сценарий для видео готовится...")

    def publish_content(self):
        print("Публикация видео на YouTube...")

# Пример использования
if __name__ == "__main__":
    print("Создание статьи:")
    article_creator = ArticleCreation()
    article_creator.create_content()

    print("\nСоздание видео:")
    video_creator = VideoCreation()
    video_creator.create_content()