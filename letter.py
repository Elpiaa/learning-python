def huruf_b(kata) :
    jum_b = 0
    for i in range(0,len(kata)) :
        if 'A' < kata[i] < 'Z' :
            jum_b+=1
    return jum_b
def huruf_k(kata) :
    jum_k = 0
    for i in range(0,len(kata)) :
        if 'a' < kata[i] < 'z' :
            jum_k+=1
    return jum_k
    
kata = 'The quick Brow Fox'
print('Output Huruf Besar : ',huruf_b(kata))
print('Output Huruf Kecil  : ',huruf_k(kata))