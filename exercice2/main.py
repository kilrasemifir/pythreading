from threading import Thread

final = []


def divisors(n):
    div_list = []
    for i in range(1, n//2+1):
        if n % i == 0:
            div_list.append(i)
    return div_list


def batch_divisors(start, end):
    for i in range(start, end):
        div = divisors(i)
        final.append((i, len(div), div))


threads = []
nb_threads = 100
max_index = 10000
for i in range(1, max_index, max_index//nb_threads):
    th = Thread(target=batch_divisors, args=(i, i+(max_index//nb_threads)))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

max_value = 0
max_value_number = 0
max_value_divisors = []
for i in final:
    if i[1] > max_value:
        max_value = i[1]
        max_value_number = i[0]
        max_value_divisors = i[2]

print(max_value_number, max_value, max_value_divisors)


