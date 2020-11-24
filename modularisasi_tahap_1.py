"""
program menghitung luas segitiga
luas _segitiga = alas * tinggi/2
"""
print('menghitung luas segitiga')
alas= 10
tinggi =6
luas_segitiga =alas * tinggi /2
print(f'segitiga dengan alas={alas}dan tinggi={tinggi}memiliki luas{luas_segitiga}')

print('menghitung luas dengan fungsi')
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi/2
    return luas_segitiga
print(hitung_luas_segitiga(10,12))
print(hitung_luas_segitiga(8,12))
print(f'Menghitung segitiga dengan fungsi,haasilnya={hitung_luas_segitiga(12,10)}')
print(f'Menghitung segitiga dengan fungsi,haasilnya={hitung_luas_segitiga(11,10)}')
