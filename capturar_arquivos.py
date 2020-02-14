import shutil
import os
import os.path
import time

Caminho = 'C:/Users/wvj/Desktop/Script_Python/Arquivos_Capturados/'

while 1 == 1:
    
    print("---------------------------------------------------")
    print("Iniciando capitura de arquivos do SIACP...")
    
    newAdress = Caminho + 'ROBO_SIACP/'
    oldAdress = 'S:/Area_Transferencia_Comum/SIACP/PRODUÇÃO/' #ORIGEM
    x = 0

    if len(os.listdir(oldAdress)) > 0:

        print("Iniciando rotina para copiar arquivos do robô do SIACP")
        
        lista = os.listdir(oldAdress) #lista separando apenas os arquivos do caminho.
        tamanho = len(os.listdir(oldAdress))
        
        while x < ( tamanho ):
            caminhoCompleto_old = oldAdress + lista[x]
            caminhoCompleto_new = newAdress + lista[x]

            if not os.path.isfile(caminhoCompleto_new):
                if not os.path.isfile(caminhoCompleto_new):
                    print(caminhoCompleto_old)
                    shutil.copy(caminhoCompleto_old, caminhoCompleto_new) 
                    print(x, '-', lista[x]) #apenas para ver como está sendo feito
                
            x += 1
    print("---------------------------------------------------")
    print("Iniciando capitura de arquivos do SECPGRET...")
    
    newAdress = Caminho + 'SECPGRET/COB_RETORNO/'
    oldAdress = '//MGINFRAEDIP2.scl.corp/COB_RETORNO/' #ORIGEM
    x = 0

    if len(os.listdir(oldAdress)) > 0:

        print("Iniciando rotina para copiar arquivos COB_RETORNO")

        lista = os.listdir(oldAdress) #lista separando apenas os arquivos do caminho.
        tamanho = len(os.listdir(oldAdress))
        
        while x < ( tamanho ):

            if '.' in lista[x][-4::]:
                
                caminhoCompleto_old = oldAdress + lista[x]
                caminhoCompleto_new = newAdress + lista[x]
            
                if not os.path.isfile(caminhoCompleto_new):
                    shutil.copy(caminhoCompleto_old, caminhoCompleto_new) 
                    print(x, '-', lista[x]) #apenas para ver como está sendo feito
                
            x += 1


    print("---------------------------------------------------")
    
    newAdress = Caminho + 'SECPGRET/COB_REMESSA/'
    oldAdress = '//MGINFRAEDIP2.scl.corp/COB_REMESSA/' #ORIGEM
    x = 0

    if len(os.listdir(oldAdress)) > 0:

        print("Iniciando rotina para copiar arquivos COB_REMESSA")

        lista = os.listdir(oldAdress) #lista separando apenas os arquivos do caminho.
        tamanho = len(os.listdir(oldAdress))
        
        while x < ( tamanho ):

            if '.' in lista[x][-4::]:
                
                caminhoCompleto_old = oldAdress + lista[x]
                caminhoCompleto_new = newAdress + lista[x]
            
                if not os.path.isfile(caminhoCompleto_new):
                    shutil.copy(caminhoCompleto_old, caminhoCompleto_new) 
                    print(x, '-', lista[x]) #apenas para ver como está sendo feito
                
            x += 1


        
