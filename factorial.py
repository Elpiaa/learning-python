def faktor(x) :
    if x == 0 :
        return 0
    elif x == 1 :
        return 1
    return faktor(x-1)*x
x = int(input('masukkan angka yang mau di factorial :  '))
print(f'faktorial dari {x} : ',faktor(x))