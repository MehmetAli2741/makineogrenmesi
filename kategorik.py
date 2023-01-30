
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


ülke = veriler.iloc[:,0:1].values

print(ülke)

# Kategorik  Verileri dönüştürmek için
from sklearn import preprocessing

le = preprocessing.LabelEncoder() # labelencoder metodunu dönüştürmrk için kullanıyoruz
ülke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ülke)

#metinsel verileri sayısal verilere dönüştürmek
ohe = preprocessing.OneHotEncoder()
ülke =ohe.fit_transform(ülke).toarray()
print(ülke)
print("*******************************************************************")

# Verilerimizi diziden dataframe dönüştürmek
#ülke verilerini dataframe cevirmek için
sonuc = pd.DataFrame(data = ülke,index=range(22),columns=["fr","tr","us"])
print(sonuc)
print("*******************************************************************")
sonuc2 = pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])
print(sonuc2)
print("*******************************************************************")
cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)
print("*******************************************************************")
sonuc3 = pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])
print(sonuc3)
print("*******************************************************************")
#verileri birleştirmek için
data = pd.concat([sonuc,sonuc2],axis=1)#axis=1 yapılmassa indexlerde nan degerler olusacaktır
print(data)
print("*******************************************************************")


data1 = pd.concat([data,sonuc3],axis=1)
print(data1)
#(sonuc olarak elimizdeki veri setini işleme hazır hale getirmiş bulunmaktayız)
print("*******************************************************************")


#Verileri Train ve Test olarak ayıracagız
from sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test = train_test_split(data,sonuc3,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

#öznitelik ölçekleme

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)



















