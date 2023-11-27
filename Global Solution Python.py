#Baixando bibliotecas de Python. Para baixar a biblioteca, basta digitar o comando abaixo:
#pip install winotify 
#pip install datetime 
#pip install sympy

import time
import sympy
from winotify import Notification, audio

#Criando uma estrutura de dados do paciente
nome = str(input("Digite o seu nome: "))
idade =  int(input("Digite sua idade: "))
cpf = str(input("Digite o seu cpf sem pontos e traço: "))

#Criando uma lista pré definida caso o remédio já possua uma alta demanda de compras
medicamentos_prontos = ["dipirona", "tylenol", "doralgina", "neosaldina"]
#Definindo opção de medicamentos que estejam ou não na lista.
remedio = str(input("Qual o medicamente proposto pelo médico? "))

#Criação do código de aviso, para concientizar o paciente, de tomar seu remédio
notificacao = Notification(
            app_id="Alerming Notificação", title="Não esqueça de tomar seu remédio",
            msg= f"Olá {nome}, está na hora de você tomar o seu medicamento: {remedio}",
            duration="short")

notificacao2 = Notification(
    app_id= "Alerming Notificação", title= "Não esqueça de tomar seu remédio",
    msg= f"Olá {nome}, está na hora de tomar o seu medicamento: {remedio}",
    duration="short")

#Válidando informações do paciente com if, elif e else
if len(cpf) == 11:
    if idade >= 18:

        #Criando definições caso o medicamento escolhido não esteja na lista.
        if remedio not in medicamentos_prontos:
            #Adicionando informações de intervalo de tempo entre os avisos, e a quantidade de avisos
            #Exemplo, se definimos 20 segundos para 2 avisos, então teremos 1 aviso a cada 20 segundos, até completar a quantidade indicada
            intervalo = int(input("Defina o tempo em segundos: "))
            quantidade = int(input("Defina a quantidade de aviso de acordo com o médico: "))

            #Mostrando notificação na tela do paciente, caso as informações estejam certas
            for i in range(quantidade):
                #Adicionando áudio no código, com .set_audio()
                notificacao.set_audio(audio.LoopingAlarm, loop=False)
                notificacao.show()
                time.sleep(intervalo)

        else:
                #Definindo um pré-set pronto para medicamento com horários fixos
                quantidade_2 = 2
                intervalo_2 = 10
                for i in range(quantidade_2):
                #Adicionando áudio no código, com .set_audio()
                    notificacao2.set_audio(audio.LoopingAlarm, loop=False)
                    notificacao2.show()
                    time.sleep(intervalo_2)        

    #Negango informações caso seja menor de idade
    else:
        print ("Você ainda é menor de idade, seu login não pode ser efetuado")

#Negando acesso caso, CPF ou Idade sejam inválidas
elif idade <= 18 and len(cpf) != 11:
    print ("CPF e idade são invalidas, digite uma ideda e um CPF válidos")
else:
    print ("CPF inválido, por favor digite novamente")

        