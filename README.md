# VMMeter-libvirt

# Leitura do Código Python para Monitoramento de Máquinas Virtuais

Este código tem como objetivo monitorar as máquinas virtuais (VMs) especificadas e armazenar as informações de desempenho em um arquivo CSV.

Bibliotecas Utilizadas

libvirt: Biblioteca de gerenciamento de hypervisors, como o QEMU, KVM e outros.
csv: Biblioteca para escrita e leitura de arquivos CSV.
datetime: Biblioteca para trabalhar com data e hora.
time: Biblioteca para trabalhar com tempo.

Variáveis

vm_names: Lista com os nomes das VMs a serem monitoradas.
measurement_time: Tempo de medição em segundos.
measurement_interval: Intervalo de medição em segundos.

Funções
write_csv: Função que escreve o conteúdo em um arquivo CSV. Recebe o nome do arquivo, as colunas (headers) e as linhas como parâmetros.
gather_vm_stats: Função que coleta informações sobre a VM, como tempo de CPU, memória utilizada, entre outras. Recebe a conexão com o hypervisor e a VM como parâmetros.

Fluxo de Execução
A biblioteca libvirt é usada para abrir uma conexão com o hypervisor QEMU.
As VMs especificadas são armazenadas em uma lista (vms).
As informações a serem coletadas sobre cada VM são definidas como colunas (headers).
O loop principal é iniciado e, a cada intervalo de tempo (measurement_interval), as informações sobre as VMs são coletadas pela função gather_vm_stats e armazenadas em uma lista de linhas (rows).
Quando o tempo de medição (measurement_time) é atingido, o conteúdo da lista de linhas é escrito em um arquivo CSV.
Por fim, a conexão com o hypervisor é fechada.

Este código pode ser adaptado para monitorar outros tipos de recursos além das VMs, basta modificar a função gather_vm_stats. Além disso, é possível alterar as colunas a serem coletadas e armazenadas, bem como o formato de saída (CSV, JSON, entre outros).



