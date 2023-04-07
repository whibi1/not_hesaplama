
def not_hesapla(satir):
    satir=satir[:-1]
    liste =satir.split(",")
    isim_soyisim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    ortalama=((not1*(3/10)))+(not2*(3/10))+(not3*(4/10))
    harf="AA"
    durum="geçti"
    
    if (ortalama>=90):
        harf="AA"
        durum="geçti"
    elif (ortalama>=85):
        harf="BA"
        durum="geçti"
    elif (ortalama>=80):
        harf="BB"
        durum="geçti"
    elif (ortalama>=75):
        harf="CB"
        durum="geçti"
    elif (ortalama>=70):
        harf="CC"
        durum="geçti"
    elif (ortalama>=65):
        harf="DC"
        durum="koşullu geçti"
    elif (ortalama>=60):
        harf="DD"
        durum="koşullu geçti"
    elif (ortalama>=55):
        harf="FD"
        durum="kaldı"
    elif (ortalama>=50):
        harf="FF"
        durum="kaldı"

    return isim_soyisim + "---------->" + harf+ "---------->" + durum +"\n"

with open ("dosya.txt","r",encoding="utf-8") as file:
    eklenecekler=[]
    for satir in file:
        eklenecekler.append( not_hesapla(satir))
    print(eklenecekler)
with open ("notlar.txt", "w",encoding="utf-8") as file2:
        for i in eklenecekler:
            file2.write(i)
