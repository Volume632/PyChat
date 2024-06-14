import subprocess

def run_multiple_clients(client_count):
    processes = []
    for i in range(client_count):
        process = subprocess.Popen(["python", "client.py", str(i)])
        processes.append(process)

    for process in processes:
        process.wait()

if __name__ == "__main__":
    run_multiple_clients(10)  # Запуск 10 клиентов