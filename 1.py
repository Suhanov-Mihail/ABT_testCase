import os


def black_book(page: int) -> bool:
    status_code = os.system(f"./black-book -n {page}")
    return status_code == 0


def main():
    start = 1
    end = 10000000

    while start < end:
        middle = (start + end) // 2
        if black_book(middle):
            start = middle + 1
        else:
            end = middle

    last_page = start - 1
    print(f"Последняя страница книги - {last_page}")


if __name__ == '__main__':
    main()
