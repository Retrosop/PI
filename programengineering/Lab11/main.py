from abc import ABC, abstractmethod
class DownloadState(ABC):
    @abstractmethod
    def start_download(self, downloader):
        pass

    @abstractmethod
    def cancel_download(self, downloader):
        pass

    @abstractmethod
    def complete_download(self, downloader):
        pass


class NotStartedState(DownloadState):
    def start_download(self, downloader):
        print("Начало загрузки файла...")
        downloader.set_state(DownloadingState())

    def cancel_download(self, downloader):
        print("Загрузка ещё не началась. Отмена невозможна.")

    def complete_download(self, downloader):
        print("Загрузка ещё не началась. Завершение невозможно.")


class DownloadingState(DownloadState):
    def start_download(self, downloader):
        print("Загрузка уже идёт.")

    def cancel_download(self, downloader):
        print("Загрузка отменена.")
        downloader.set_state(NotStartedState())

    def complete_download(self, downloader):
        print("Загрузка завершена.")
        downloader.set_state(CompletedState())


class CompletedState(DownloadState):
    def start_download(self, downloader):
        print("Файл уже загружен. Повторная загрузка невозможна.")

    def cancel_download(self, downloader):
        print("Загрузка уже завершена. Отмена невозможна.")

    def complete_download(self, downloader):
        print("Файл уже загружен.")


class FileDownloader:
    def __init__(self):
        self.state = NotStartedState()  

    def set_state(self, state: DownloadState):
        self.state = state

    def start_download(self):
        self.state.start_download(self)

    def cancel_download(self):
        self.state.cancel_download(self)

    def complete_download(self):
        self.state.complete_download(self)


if __name__ == "__main__":
    downloader = FileDownloader()

    print("\n--- Попытка завершить загрузку без начала ---")
    downloader.complete_download()

    print("\n--- Начало загрузки ---")
    downloader.start_download()

    print("\n--- Попытка начать загрузку снова ---")
    downloader.start_download()

    print("\n--- Завершение загрузки ---")
    downloader.complete_download()

    print("\n--- Попытка отменить завершённую загрузку ---")
    downloader.cancel_download()
