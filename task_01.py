def search_zero_index(arr: str) -> int:
    """Находит индекс первого вхождения нуля в строку"""
    count = 0
    for char in arr:
        if char != '0':
            count += 1
        else:
            return count


def rectangles(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> int | bool:
    """Вычисляет, пересекаются ли прямоугольники, заданные входными точками.
    Если прямоугольники пересекаются, тогда возвращает площадь пересечения, если нет, возвращает False"""
    first_rect_x_list = [x for x in range(x1, x2 + 1)]
    first_rect_y_list = [y for y in range(y1, y2 + 1)]
    rectangle_one_points = {(x, y) for y in first_rect_y_list for x in first_rect_x_list}

    second_rect_x_list = [x for x in range(x3, x4 + 1)]
    second_rect_y_list = [y for y in range(y3, y4 + 1)]
    rectangle_two_points = {(x, y) for y in second_rect_y_list for x in second_rect_x_list}

    intersection = rectangle_one_points.intersection(rectangle_two_points)
    if not intersection:
        return False
    list_x = sorted([x[0] for x in intersection])
    list_y = sorted([y[1] for y in intersection])
    s = (list_x[-1] - list_x[0]) * (list_y[-1] - list_y[0])
    return s if s > 0 else False


if __name__ == '__main__':
    print(search_zero_index("111111111110000000000000000"))
    print(rectangles(1, 1, 2, 2, 3, 3, 4, 4))
