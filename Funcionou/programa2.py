import threading
from datetime import datetime

# Define a classe MyThread2 que herda da classe Thread
class MyThread2(threading.Thread):
    def __init__(self, thread_id, file_name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.file_name = file_name
        
    def run(self):
        # Loop para executar a thread a quantidade de vezes especificada pelo usuário
        for i in range(num_executions):
            # Abre o arquivo correspondente a esta thread e escreve uma linha com as informações
            with open(self.file_name, "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y")
                dt_string2 = now.strftime("%H:%M:%S")
                f.write(f"{i+1} Programa2 - Thread{self.thread_id} - Data: {dt_string} - Hora: {dt_string2} \n")

# Pergunta ao usuário a quantidade de execuções
num_executions = int(input("Digite a quantidade de execuções: "))
threads = []

# Cria três threads e adiciona à lista threads
for i in range(3):
    t = MyThread2(i+1, "registro2.txt")
    threads.append(t)

# Inicia todas as threads na lista
for thread in threads:
    thread.start()

# Espera todas as threads na lista terminarem
for thread in threads:
    thread.join()
