import threading
from datetime import datetime

class MyThread1(threading.Thread):
    def __init__(self, thread_id, file_name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.file_name = file_name
        
    def run(self):
        for i in range(num_executions):
            with open(self.file_name, "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y")
                dt_string2 = now.strftime("%H:%M:%S")
                f.write(f"{i+1} Programa1 - Thread{self.thread_id} - Data: {dt_string} - Hora: {dt_string2} \n")

num_executions = int(input("Digite a quantidade de execuções: "))
threads = []

for i in range(3):
    t = MyThread1(i+1, "registro1.txt")
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()