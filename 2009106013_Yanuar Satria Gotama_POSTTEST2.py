print(" ")
print("====================================")
print("Program menghitung Soal Khusus Balok")
print("====================================")
print(" ")

def Luas_Permukaan(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L

def Volume(p,l,t):
    V = p * l * t
    return V

def Keliling(p,l,t):
    K = 4 * (p + l + t)
    return K

import math
def Diagonal(p,l,t):
    D = math.sqrt(pow(p,2) + pow(l,2) + pow(t,2))
    return D

print("Rumus yang ingin Digunakan")
print("1. Luas Permukaan Balok [Kode: Luas]")
print("2. Volume Balok         [Kode: Vol]")
print("3. Keliling Balok       [Kode: Kel]")
print("4. Diagonal Ruang Balok [Kode: Diag]")

Rumus = input("Masukan pilihan: ")

if Rumus == "Luas":
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    Luas_Permukaan(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai Luas Permukaan:{}'.format(p,l,t, Luas_Permukaan(p,l,t)))

elif Rumus == "Vol":
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    Volume(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai Volume:{}'.format(p,l,t, Volume(p,l,t)))
 
elif Rumus =="Kel":
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    Keliling(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai Keliling:{}'.format(p,l,t, Keliling(p,l,t)))

elif Rumus =="Diag":
    p = int(input("Masukan panjang balok: "))
    l = int(input("Masukan lebar balok: "))
    t = int(input("Masukan tinggi balok: "))
    Diagonal(p,l,t)
    print('Jadi balok dengan ukuran\npanjang:{}\nlebar:{}\ntinggi:{}\nMempunyai Diagonal Ruang:{}'.format(p,l,t, Diagonal(p,l,t)))
 
else:
    print("Rumus tidak tersedia")