clima = int(input("Digite a temperatura atual(°C) :"))#recebimento de dados 
if clima <=25:
    print("frio")#Saidas  
if clima >25 and clima <30:
    print("Gostosin")#Saidas  
if clima >= 30:
    print("Calor pra cacete")#Saidas  

ventos = int(input("Digite a atual velocidade dos ventos(KM/h) : "))#recebimento de dados 
if ventos <89:
    print("Normal")#Saidas  
if ventos >89 and ventos<= 130:
    print("Tespestade corra")#Saidas      
if ventos >103 and ventos<= 118:
    print("Tepestade violenta reza e corre")#Saidas  
if ventos >= 118:
    print("Furacão sai daqui")#Saidas     