import threading
import time

def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        time.sleep(0.1)
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}\n')
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f'Работа потоков:{end_time - start_time} секунд')

threads = []

start_time = time.time()

threads.append(threading.Thread(target=write_words, args=(10,'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30,'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200,'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100,'example8.txt')))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f'Работа потоков:{end_time - start_time} секунд')