import shutil
import os
import os.path
import time

# Caminho onde será salvo os arquivos
Caminho = 'C:/Users/wvj/Desktop/Script_Python/Arquivos_Capturados/'   # Raiz do caminho onde será copiado os arquivos

# Pasta específica para guardar os arquivos
newAdress = Caminho + 'ROBO_SIACP/'
    
while 1 == 1:
    
    print("---------------------------------------------------")
    print("Iniciando capitura de arquivos...")
    
    # Local onde o script vai "observar" e copiar os arquivos
    oldAdress = 'S:/Area_Transferencia_Comum/SIACP/PRODUÇÃO/' #ORIGEM
    x = 0

    if len(os.listdir(oldAdress)) > 0:

        print("Iniciando rotina para copiar arquivos...")
        
        lista = os.listdir(oldAdress) # Lista separando apenas os arquivos do caminho.
        tamanho = len(os.listdir(oldAdress))
        
        while x < ( tamanho ):
            caminhoCompleto_old = oldAdress + lista[x]
            caminhoCompleto_new = newAdress + lista[x]

            if not os.path.isfile(caminhoCompleto_new):
                if not os.path.isfile(caminhoCompleto_new):
                    print(caminhoCompleto_old)
                    shutil.copy(caminhoCompleto_old, caminhoCompleto_new) 
                    print(x, '-', lista[x]) # Apenas para ver como está sendo feito
                
            x += 1
    print("Finalizando copia de arquivos.")
    print("---------------------------------------------------")

        
