import multiprocessing
import time

def read_info(name):
    all_data = []
    file = open(name,'r')
    line = file.readline()
    while line:
        all_data.append(line)
        line = file.readline()
    file.close()
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]


if __name__ == '__main__':
    start_time_linear = time.time()
    all_data_linear = []
    for filename in filenames:
        all_data_linear.extend(read_info(filename))
    end_time_linear = time.time()
    print(f'Время выполнения линейного вызова: {end_time_linear - start_time_linear}')


    start_time_multiprocessing = time.time()
    with multiprocessing.Pool(4) as pool:
        data = pool.map(read_info, filenames)
    end_time_multiprocessing = time.time()
    print(f'Время выполнения многопроцессного вызова: {end_time_multiprocessing - start_time_multiprocessing}')
