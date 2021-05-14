"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra tilpumu un virsmas laukumu.

Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass.

Piezīme:
Ievaddati: Pamata rādiuss un cilindra augstums
Izvaddati: Cilindra virsmas laukums un tilpums 
"""
R1=float(input("Pamata rādiuss "))
R2=3*(R1*R1) 
CM=float(input("cilindra augstums "))


Ct=R2*CM

print(Ct,"cilindra tilpums")

San=2*3*R1*CM

Sp=2*R2+San

print(Sp,"cilindra virsmas laukums")



