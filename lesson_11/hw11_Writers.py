import threading
import random

# Реализовать решение следующей задачи:
# «Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) пишут в одну книгу.
# Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся,
# чтобы прочитать новые записи из неё. Каждый читатель и писатель – отдельный поток.
# Одновременно книгу может читать несколько читателей, но писать единовременно может только один писатель.»



Book = ""

writers_streams = 2  # количество потоков-писателей
readers_streams = 5  # количество потоков-читателей

readers_count = 0

taking_book = threading.Lock()  # взять одну книгу может и писатель, и читатель
working_with_book = threading.Lock()  # блокировка для собственной книги(на запись, на чтение)
readers_counter = threading.Lock()  # блокировка книги первым читателем, разблокировка последним


def writer():
    global Book

    while True:
        with taking_book:
            working_with_book.acquire()

        print(f'Сейчас пишет: {threading.current_thread().name}.')
        if len(Book) < 100:
            Book += "".join(map(chr, [random.randint(99, 200) for _ in range(20)]))  # Цифровая литература
        else:
            Book = "".join(map(chr, [random.randint(99, 200) for _ in range(20)]))
        print(f'Текст книги: {Book}')

        working_with_book.release()


def reader():
    global readers_count

    while True:
        with taking_book:
            readers_counter.acquire()
            readers_count += 1
            if readers_count == 1:
                working_with_book.acquire()
        readers_counter.release()

        print(f'Сейчас читает {threading.current_thread().name}:')

        with readers_counter:
            readers_count -= 1
            if readers_count == 0:
                working_with_book.release()


threads = [threading.Thread(target=reader) for _ in range(readers_streams)] + \
          [threading.Thread(target=writer) for _ in range(writers_streams)]

for thread in threads:
    thread.start()