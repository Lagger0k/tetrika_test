import requests
from bs4 import BeautifulSoup


def main(url: str, animals_dict: dict) -> None:
    """Рекурсивно считает кол-во животных на каждую букву, складывая результат в словарь"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_link = _search_next_page_link(soup)
    result = _search_animals(soup, animals_dict)
    if next_link and result:
        print('.', end='')
        return main(next_link, animals_dict)
    print('End of list')


def create_result_dict() -> dict:
    """Создает словарь, ключами которого, будут заглавные буквы кириллицы,
     в котором будут храниться результаты подсчета"""
    first_letter = ord('а')
    letters = [chr(i) for i in range(first_letter, first_letter + 6)] + [chr(first_letter + 33)] +\
              [chr(i) for i in range(first_letter + 6, first_letter + 32)]
    result_dict = dict.fromkeys(''.join(letters).upper(), 0)
    return result_dict


def _search_next_page_link(data: BeautifulSoup) -> str | None:
    """Ищет ссылку на следующую страницу пагинации"""
    base_url = 'https://ru.wikipedia.org/'
    link = data.find_all('a', text='Следующая страница')
    if len(link) > 0:
        return base_url + link[0].get('href')
    else:
        return None


def _search_animals(data: BeautifulSoup, animals_dict: dict) -> bool:
    """Ищет животных на странице и инкриминирует словарь с результирующим набором данных"""
    res = data.find_all('div', id='mw-pages')
    animals = res[0].find_all('li')
    count = 0
    for link in animals:
        try:
            animals_dict[link.text[0]] += 1
            count += 1
        except KeyError:
            continue
    return True if count > 0 else False


if __name__ == '__main__':
    start_link = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    result_dict = create_result_dict()

    main(start_link, result_dict)

    total_sum = 0
    for k, v in result_dict.items():
        print(f'{k}: {v}')
        total_sum += v
    print(f'Total sum: {total_sum}')
