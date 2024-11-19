class Document:
    def __init__(self):
        self.title = ""
        self.body = ""
        self.footer = ""

    def __str__(self):
        return f"Document:\nTitle: {self.title}\nBody: {self.body}\nFooter: {self.footer}"


class DocumentBuilder:
    def __init__(self):
        self.document = Document()

    def set_title(self, title):
        self.document.title = title
        return self

    def set_body(self, body):
        self.document.body = body
        return self

    def set_footer(self, footer):
        self.document.footer = footer
        return self

    def build(self):
        return self.document


# Пример использования
if __name__ == "__main__":
    builder = DocumentBuilder()

    # Получение пользовательского ввода
    title = input("Введите заголовок документа: ")
    body = input("Введите тело документа: ")
    footer = input("Введите подвал документа: ")

    document = (builder
                .set_title(title)
                .set_body(body)
                .set_footer(footer)
                .build())

    print(document)
