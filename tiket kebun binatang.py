#NAMA : AISHA MABELINA
#NIM : 065002400026

n = 0
money = 0
people = 0

print("===== SELAMAT DATANG DI KEBUN BINATANG TRISAKTI =====")
while (n != ''):
    n = str(input("Masukkan Umur: "))
    people += 1
    if (n == str('')):
        break;
    else:
        
        if (int(n) <= 2):
            print('Gratis')
            print("Running total = ", money)
            money += 0
            
        elif (3 <= int(n) <= 12):
            print("Harga $14.00")
            money += 14.00
            print("Running total = ", money)
        
        elif (150 >= int(n) >= 65):
            print('Harga $18.00')
            money += 18.00
            print("Running total = ", money)
            
        elif (13 <= int(n) <= 64):
            print('Harga $23.00')
            money += 23.00
            print("Runing total = ", money)
            
        else:
            people -= 1
            print('INVALID')
            
if(people == 1):
    print(" ")
else:
    pay = float(input("Masukkan Jumlah Uang = "))
    chance = pay - money
    print('Running kembalian = ', chance)