import hashlib
import random


class MarsURLEncoder:

    def __init__(self):
        self.url_storage = {}

    def encode(self, long_url):
        """ Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol. """

        def short_url_generator(choice):
            encode = (
                hashlib.sha256(
                    (choice + str(random.randrange(1, 1000))
                ).encode('utf-8')).hexdigest()
            )
            return f'https://ma.rs/{encode}'

        short_url = short_url_generator(long_url)
        if short_url not in self.url_storage:
            self.url_storage[short_url] = long_url
            return short_url
        else:
            short_url = short_url_generator(long_url[::7])
            self.url_storage[short_url] = long_url
            return short_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.url_storage[short_url]


def main():
    urls = (
        'https://www.programmersought.com/article/49359205008/',
        'https://github.com/PetrovKRS/backend_test_homework',
        'https://www.pythonanywhere.com/user/PetrovKRS/consoles/',
        'https://petrovkrs.pythonanywhere.com/auth/login/',
        'https://auto.ru/?from=tableau_yabro',
    )
    url_encoder = MarsURLEncoder()
    i = 0
    while i < len(urls):
        short_url = url_encoder.encode(urls[i])
        print(short_url)
        long_url_from_dict = url_encoder.decode(short_url)
        print(long_url_from_dict)
        i += 1


if __name__ == '__main__':
    main()
