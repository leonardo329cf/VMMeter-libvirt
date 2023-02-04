# Monitoramento de VMs com Python e libvirt
Este código permite monitorar as estatísticas de CPU e memória de máquinas virtuais (VMs) usando a biblioteca libvirt e Python.

Requisitos
Python 3.x
libvirt
Instalação
Para instalar o libvirt em um sistema operacional Linux, basta executar o seguinte comando:

python
Copy code
sudo apt-get install libvirt-dev libvirt-bin
Para instalar o Python 3 e as dependências, você pode usar o gerenciador de pacotes pip:

Copy code
pip install -r requirements.txt
Uso
Antes de usar o código, é necessário especificar os nomes das VMs que deseja monitorar na lista vm_names. O tempo de medição (em segundos) e o intervalo de medição (em segundos) também podem ser configurados nas variáveis measurement_time e measurement_interval, respectivamente.

Execute o código com o seguinte comando:

Copy code
python monitor_vms.py
Após a execução, será gerado um arquivo CSV benchmark.csv com as estatísticas coletadas. As informações incluídas são:

Nome da VM
Horário de medição
Tempo de CPU (ns)
Tempo de sistema (ns)
Tempo de usuário (ns)
Memória alocada (B)
Memória não utilizada (B)
Memória disponível (B)
Memória usável (B)
Caches de disco (B)

Observações
Este código foi testado com sucesso em um sistema operacional Ubuntu 20.04. É importante verificar se o libvirt está configurado corretamente em seu sistema e se você tem privilégios adequados para acessar as informações das VMs.
