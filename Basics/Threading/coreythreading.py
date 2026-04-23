import time

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second....")
    time.sleep(4)
    print("do something")

do_something()

finish = time.perf_counter()

result = f"{round(finish-start,2)} second"

print(result)


result1 = time.time()
print(result1)

#started with corey threading