import libvirt
import csv
import datetime as dt
import time

# Nomes das VMs
vm_names = ["java11", "java8"]  

# Tempo de medição em segundos
measurement_time = 5   

# Intervalo de medição em segundos
measurement_interval = 2  

# Número de medições calculado com base no intervalo de medição
number_measurements = int(measurement_time / measurement_interval)

def write_csv(filename, headers, rows):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)
    except Exception as e:
        print(f'Erro ao escrever arquivo {filename}: {e}')
        exit(1)

def gather_vm_stats(conn, vm):
    stats_cpu = vm.getCPUStats(True)
    stats_mem = vm.memoryStats()
    row = [vm.name, dt.datetime.now().strftime("%H:%M:%S")]
    row.extend([stats_cpu[0]['cpu_time'], stats_cpu[0]['system_time'], stats_cpu[0]['user_time']])
    for key in stats_mem:
        if key in ["actual", "unused", "available", "usable", "disk_caches"]:
            row.append(stats_mem[key])
    return row

# Abre conexão com qemu:///system
conn = libvirt.open('qemu:///system')
if not conn:
    raise Exception('Falha ao abrir conexão com qemu:///system')

# Armazena as VMs
vms = []
for name in vm_names:
    vm = conn.lookupByName(name)
    if not vm:
        raise Exception(f'Falha ao encontrar a VM {name}')
    vms.append(vm)

headers = ["VM", "Horário de Medição", "Tempo de CPU (ns)", "Tempo de Sistema (ns)", "Tempo de Usuário (ns)", "Memória Alocada (B)", "Memória Não Utilizada (B)", "Memória Disponível (B)", "Memória Usável (B)", "Caches de Disco (B)"]
rows = []

# Medindo as estatísticas das VMs a cada intervalo de tempo
for i in range(number_measurements):
    for vm in vms:
        rows.append(gather_vm_stats(conn, vm))
    time.sleep(measurement_interval)

write_csv("benchmark.csv", headers, rows)
conn.close()
exit(0)
