
#ders-6:Kütüphanelerin yüklenmesi
#Kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Kodlar
#veri yükleme

veriler=pd.read_csv("eksikveriler.csv")  #pd.read_excel("Kitap1.xlsx")
print(veriler)


#veri on işleme
boy = veriler[["boy"]]
print(boy)

yascinsiyet = veriler[["yas","cinsiyet"]]
print(yascinsiyet)

#class tanımlamak
class insan:
    boy=170
    def kosmak (self,b):
        return b + 10
    
mehmet =insan()
print(mehmet.boy)
print(mehmet.kosmak(10))

# eksik verileri tamamlamak

from sklearn.impute import SimpleImputer

Imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
yas = veriler.iloc[:,1:4].values
print(yas)

Imputer = Imputer.fit(yas[:,1:4])

yas[:,1:4] = Imputer.transform(yas[:,1:4])
print(yas)    

