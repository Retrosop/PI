from abc import ABC, abstractmethod
#Определение интерфейса IMessage
class IMessage(ABC):
    @abstractmethod
    def send(self):
        pass
#Реализация конкретных классов сообщений
class TextMessage(IMessage):
    def __init__(self, content):
        self.content = content

    def send(self):
        return f"Отправлено текстовое сообщение: {self.content}"

class ImageMessage(IMessage):
    def __init__(self, image_path):
        self.image_path = image_path

    def send(self):
        return f"Отправлено изображение: {self.image_path}"

class VideoMessage(IMessage):
    def __init__(self, video_path):
        self.video_path = video_path

    def send(self):
        return f"Отправлено видео: {self.video_path}"
#Создание фабрики сообщений
class MessageFactory:
    @staticmethod
    def create_message(message_type, content):
        if message_type == "text":
            return TextMessage(content)
        elif message_type == "image":
            return ImageMessage(content)
        elif message_type == "video":
            return VideoMessage(content)
        else:
            raise ValueError("Неизвестный тип сообщения")

if __name__ == "__main__":
    text_message = MessageFactory.create_message("text", "Привет, как дела?")
    print(text_message.send())

    image_message = MessageFactory.create_message("image", "/path/to/image.jpg")
    print(image_message.send())

    video_message = MessageFactory.create_message("video", "/path/to/video.mp4")
    print(video_message.send())
