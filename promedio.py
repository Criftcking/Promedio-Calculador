from symtable import SymbolTableFactory
import colorama
from colorama import Style
from colorama import Fore
import time
import os


colorama.init()
#programa para calcular 3 notas
#ESPANIOL

print(Fore.BLUE + Style.BRIGHT + "/By Criftcking-@GhostHat/" + Style.RESET_ALL)
print(Fore.RED + "*********************************" + Style.RESET_ALL)
print(Fore.RED + "****NOTA PROMEDIO DE ESPANIOL****" + Style.RESET_ALL)
print(Fore.RED + "*********************************" + Style.RESET_ALL)
print(Fore.GREEN + "")
nt = int(input("nota 1 :"))
nv = int(input("nota 2 :"))
ng = int(input("nota 3 :"))
nf = int(input("Nota 4 :"))
print("" + Style.RESET_ALL)
media = (nt + nv + ng + nf) / 4

text = ("Tu Promedio de espaniol es :" , str(media))

print (text)


print()
print()

#Matematica

De = (input("Deseas ver tu promedio de Matematica? (SI-NO) :"))
##########
am = "si"
ap = "SI"
al = "Si"
##########

nl = "no"
nh = "NO"
np = "No"
en = ""


J = (Fore.YELLOW + "*********************************" + Style.RESET_ALL)
H = (Fore.YELLOW + "****NOTA PROMEDIO DE MATEMATICA**" + Style.RESET_ALL)
K = (Fore.YELLOW + "*********************************" + Style.RESET_ALL)

#Funciones De (SI)
if De == am:
    print(J)
    print(H)
    print(K)

    
if De == ap:
    print(J)
    print(H)
    print(K)

        
if De == al:
    print(J)
    print(H)
    print(K)

#Funciones De (NO)

if De == nl:
    os.system("cls")
    os.system("clear")
    exit()
     
 
         
if De == nh:
    os.system("cls")
    os.system("clear")
    exit()
    
if De == np:
    os.system("cls")
    os.system("clear")
    exit()

if De == en:
    os.system("cls")
    os.system("clear")
    exit()


#preceso matematica
print(Fore.GREEN + "")
nt = (int)(input("nota 1 :"))
nv = (int)(input("nota 2 :"))
ng = (int)(input("nota 3 :"))
nf = (int)(input("Nota 4 :"))
print("" + Style.RESET_ALL)
media = (nt + nv + ng + nf) / 4

text = ("Tu Promedio de Matematica es :" , str(media))

print (text)


print()
print()

#SOCIALES


soc = (input("Deseas ver tu promedio de Sociales? (SI-NO) :"))


##########
kl = "si"
km = "SI"
kj = "Si"
##########
cd = "no"
cg = "NO"
cy = "No"

M = (Fore.LIGHTCYAN_EX + "*********************************" + Style.RESET_ALL)
E = (Fore.LIGHTCYAN_EX + "****NOTA PROMEDIO DE SOCIALES****" + Style.RESET_ALL)
A = (Fore.LIGHTCYAN_EX + "*********************************" + Style.RESET_ALL)


#Funciones De Sociales (SI)
if soc == kl:
    print(M)
    print(E)
    print(A)
    
if soc == km:
    print(M)
    print(E)
    print(A)
    
if soc == kj:
    print(M)
    print(E)
    print(A)
    
# Funciones De Sociales (NO)

if soc == cd:
    os.system("cls")
    os.system("clear")
    exit()
    
if soc == cg:
    os.system("cls")
    os.system("clear")
    exit()
    
if soc == cy:
    os.system("cls")
    os.system("clear")
    exit()
    
if De == en:
    os.system("cls")
    os.system("clear")
    exit()

#Proceso sociales 

print(Fore.GREEN + "")
yo = (int)(input("nota 1 :"))
ye = (int)(input("nota 2 :"))
yh = (int)(input("nota 3 :"))
yl = (int)(input("Nota 4 :"))
print("" + Style.RESET_ALL)
media = (yo + ye + yh + yl) / 4

text = ("Tu Promedio de Sociales es :" , str(media))

print (text)

print()
print()

#NATURALES
nat = (input("Deseas ver tu promedio de Naturales? (SI-NO) :"))


##########
nx = "si"
ns = "SI"
ny = "Si"
en = ""
##########
de = "no"
ws = "NO"
wu = "No"

lo = (Fore.LIGHTCYAN_EX + "*********************************" + Style.RESET_ALL)
la = (Fore.LIGHTCYAN_EX + "****NOTA PROMEDIO DE NATURALES***" + Style.RESET_ALL)
le = (Fore.LIGHTCYAN_EX + "*********************************" + Style.RESET_ALL)



#funciones Naturales (SI)

if nat == nx:
    print(lo)
    print(la)
    print(le)

if nat == ns:
    print(lo)
    print(la)
    print(le)
    
if nat == ny:
    print(lo)
    print(la)
    print(le)
    
#funciones Naturales (NO)

if nat == de:
    os.system("cls")
    os.system("clear")
    exit()
    
if nat == ws:
    os.system("cls")
    os.system("clear")
    exit()
    
if nat == wu:
    os.system("cls")
    os.system("clear")
    exit()

if nat == en:
    os.system("cls")
    os.system("clear")
    exit()

#proceso Naturales
print(Fore.GREEN + "")
yo = (int)(input("nota 1 :"))
ye = (int)(input("nota 2 :"))
yh = (int)(input("nota 3 :"))
yl = (int)(input("Nota 4 :"))
print("" + Style.RESET_ALL)
media = (yo + ye + yh + yl) / 4

text = ("Tu Promedio de Naturales es :" , str(media))

print (text)



print()
print(Fore.BLUE + "*************************************")
l = input("PRESIONA CUALQUIER TECLA PARA CERRAR")
print(Fore.BLUE + "*************************************")
time.sleep(0.5)
os.system("cls")
os.system("clear")
print("GRACIAS POR USAR MI PROGRAMA")










