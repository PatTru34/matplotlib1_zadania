import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd
# Zad 1
# x = np.arange(1.0,21.0,1.0)
# y = 1.0/x
# plt.plot(x,y,'-',label='f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(title='Legenda')
# plt.show()

# Zad 2
# x = np.arange(1.0,21.0,1.0)
# y = 1.0/x
# plt.plot(x,y,'g>:',label='f(x)=1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(title='Legenda')
# plt.title('Wykres funkcji f(x) dla x[1,20]')
# plt.show()

# Zad 3

# x1 = np.arange(0.0,30.0,0.1)
# x2 = np.arange(0.0,30.0,0.1)
# y1 = np.sin(x1)
# y2 = np.cos(x2)
#
#
# plt.plot(x1,y1,'-',label='sin(x)')
# plt.title('Wartości sinusa i cosinusa')
# plt.ylabel('wartości sin(x) i cos(x)')
# plt.xlabel('x')
# plt.plot(x2,y2,'r-',label='cos(x)')
#
# plt.legend()
# plt.show()


# Zad 4

# x1 = np.arange(0.0,30.0,0.1)
# x2 = np.arange(0.0,30.0,0.1)
# y1 = np.sin(x1)+2
# y2 = np.sin(x2)
#
#
# plt.plot(x1,y1,'b-',label='sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.plot(x2,-y2,'-',color='orange',label='sin(x)')
#
# plt.legend(loc='center left')
# plt.show()

# Zad 6
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx,header=0)
# print(df)
# plt.subplot(3,2,1)
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar(fontsize=20,legend=(0,0))
#
# plt.subplot(3,2,4)
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar(fontsize=20,legend=(0,0))
# plt.show()

# Zad 7

df = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
print(df)
grupa= df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})


wykres = grupa.plot.pie(subplots=True,legend=False,explode=(0,0,0,0,0,0,0,0.1,0),shadow=True,
                        autopct=lambda pct:
                        '{:.1f}%'.format(pct),textprops=dict(color='black',fontsize=10)
                        )
plt.ylabel('')
plt.xticks(rotation=0)
plt.title('Ilość zamówień poszczególnych sprzedawców')
plt.show()