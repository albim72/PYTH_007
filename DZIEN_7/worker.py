import threading

def worker(num,shared_variable):
    shared_variable.append(num)
    print(f"Wątek {threading.current_thread().name} dodał {num} do zmiennej współdzielonej!")

shared_variable = []
threads = []

for i in range(10):
    t = threading.Thread(target=worker, args=(i,shared_variable))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'zmienna wpółdzielona: {shared_variable}')
