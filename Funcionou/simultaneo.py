import threading
from datetime import datetime

# Define a classe MyThread1, que herda de threading.Thread
class MyThread1(threading.Thread):
    # Define o método construtor da classe
    def __init__(self, thread_id):
        # Chama o construtor da classe mãe
        threading.Thread.__init__(self)
        # Define o ID da thread
        self.thread_id = thread_id
        # Define o nome do arquivo de registro
        self.file_name = "registro.txt"
        
     # Define o método run(), que será executado quando a thread for iniciada
    def run(self):
        # Itera a quantidade de execuções definida pelo usuário
        for i in range(num_executions):
            # Abre o arquivo de registro em modo de adição de conteúdo ("a")
            with open(self.file_name, "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y")
                dt_string2 = now.strftime("%H:%M:%S")
                 # Escreve no arquivo a linha com as informações de registro
                f.write(f"{i+1} Programa1 - Thread{self.thread_id} - Data: {dt_string} - Hora: {dt_string2} \n")

class MyThread2(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.file_name = "registro.txt"
        
    def run(self):
        for i in range(num_executions):
            with open(self.file_name, "a") as f:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y")
                dt_string2 = now.strftime("%H:%M:%S")
                f.write(f"{i+1} Programa2 - Thread{self.thread_id} - Data: {dt_string} - Hora: {dt_string2} \n")

# Solicita ao usuário a quantidade de execuções que cada thread deve realizar
num_executions = int(input("Digite a quantidade de execuções: "))

# Cria uma lista vazia para armazenar as threads
threads = []

# Itera três vezes (uma para cada thread)
for i in range(3):
    # Cria uma instância da classe MyThread1, passando o ID da thread
    t1 = MyThread1(i+1)
    # Cria uma instância da classe MyThread2, passando o ID da thread
    t2 = MyThread2(i+1)
    # Adiciona as duas threads à lista de threads
    threads.append(t1)
    threads.append(t2)

# Inicia todas as threads
for thread in threads:
    thread.start()

# Aguarda todas as threads finalizarem
for thread in threads:
    thread.join()
