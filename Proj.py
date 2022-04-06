import sys
import urllib.request
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pandas as pd
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import openpyxl
import matplotlib.pyplot as plt  # 시각화
from matplotlib import font_manager, rc



font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)  # 한글화

Test2 = pd.read_excel('C:/imis_Final/data/imisData2017.xlsx')
Test3 = pd.read_excel('C:/imis_Final/data/imisData2018.xlsx')
Test4 = pd.read_excel('C:/imis_Final/data/imisData2019.xlsx')
Test5 = pd.read_excel('C:/imis_Final/data/imisData2020.xlsx')
Imis = pd.read_excel('C:/imis_Final/data/imisData.xlsx')
Seoul = pd.read_excel('C:/imis_Final/data/서울.xlsx')
Busan = pd.read_excel('C:/imis_Final/data/부산.xlsx')
Incheon = pd.read_excel('C:/imis_Final/data/인천.xlsx')
Gyeonggi = pd.read_excel('C:/imis_Final/data/경기.xlsx')
Sum =  pd.read_excel('C:/imis_Final/data/SumData.xlsx')

Detail = pd.read_excel('C:/imis_Final/data/Test.xlsx')
Detail2 = pd.read_excel('C:/imis_Final/data/Test2.xlsx')
Detail3 = pd.read_excel('C:/imis_Final/data/Test3.xlsx')
Detail4 = pd.read_excel('C:/imis_Final/data/Test4.xlsx')
Detail5 = pd.read_excel('C:/imis_Final/data/Test5.xlsx')
Detail6 = pd.read_excel('C:/imis_Final/data/Test6.xlsx')

Run = pd.read_excel('C:/imis_Final/data/RunningTest.xls')

a = Run.loc[23]
df = pd.DataFrame(a)
df.to_excel('C:/imis_Final/data/runTest.xlsx', index = False)

    # #클라우드 데이터 추출
    # a = Test2.loc[0]
    # b = Test3.loc[0]
    # c = Test4.loc[0]
    # d = Test5.loc[0]
    # df = pd.DataFrame({'year' : ['2017', '2018', '2019', '2020'],
    #                    'data' : [a.data, b.data, c.data, d.data],
    #                    'val' : [a.val, b.val, c.val, d.val]})
    # df.to_excel('D:/imis/data/Test.xlsx', index = False)


    # #빅데이터 데이터 추출
    # a2 = Test2.loc[1]
    # b2 = Test3.loc[1]
    # c2 = Test4.loc[1]
    # d2 = Test5.loc[1]
    # df = pd.DataFrame({'year' : ['2017', '2018', '2019', '2020'],
    #                    'data' : [a2.data, b2.data, c2.data, d2.data],
    #                    'val' : [a2.val, b2.val, c2.val, d2.val]})
    # df.to_excel('D:/imis/data/Test2.xlsx', index = False)

    # # IOT 데이터 추출
    # a3 = Test2.loc[2]
    # b3 = Test3.loc[2]
    # c3 = Test4.loc[2]
    # d3 = Test5.loc[2]
    # df = pd.DataFrame({'year' : ['2017', '2018', '2019', '2020'],
    #                    'data' : [a3.data, b3.data, c3.data, d3.data],
    #                    'val' : [a3.val, b3.val, c3.val, d3.val]})
    # df.to_excel('D:/imis/data/Test3.xlsx', index = False)


    # #AI데이터 추출
    # a4 = Test2.loc[3]
    # b4 = Test3.loc[3]
    # c4 = Test4.loc[3]
    # d4 = Test5.loc[3]

    # df = pd.DataFrame({'year' : ['2017', '2018', '2019', '2020'],
    #                    'data' : [a4.data, b4.data, c4.data, d4.data],
    #                    'val' : [a4.val, b4.val, c4.val, d4.val]})
    # df.to_excel('D:/imis/data/Test4.xlsx', index = False)

    # # VR/AR/MR 데이터 추출
    # a5 = Test2.loc[4]
    # b5 = Test3.loc[4]
    # c5 = Test4.loc[4]
    # d5 = Test5.loc[4]
    # df = pd.DataFrame({'year' : ['2017', '2018', '2019', '2020'],
    #                    'data' : [a5.data, b5.data, c5.data, d5.data],
    #                    'val' : [a5.val, b5.val, c5.val, d5.val]})
    # df.to_excel('D:/imis/data/Test5.xlsx', index = False)


    # #블록체인 데이터 추출
    # a6 = Test2.loc[5]
    # b6 = Test3.loc[5]
    # c6 = Test4.loc[5]
    # d6 = Test5.loc[5]
    # df = pd.DataFrame({'year' : ['2017', '2018', '2019', '2020'],
    #                    'data' : [a6.data, b6.data, c6.data, d6.data],
    #                    'val' : [a6.val, b6.val, c6.val, d6.val]})
    # df.to_excel('D:/imis/data/Test6.xlsx', index = False)


# 정보통신 시각화
plt.figure(0)
x = Imis.loc[:, '연도']
w = 0.15

y = Imis.loc[:, '수요인원']
y1 = Imis.loc[:, '공급인원']

plt.bar(x, y, width=0.2, label="수요인원")
x = x + w
plt.bar(x, y1, width=0.2, label="공급인원")

plt.legend(loc=5)
plt.legend(loc='upper center')

plt.xlabel("(연도)")
plt.ylabel("(만명)", rotation=0, loc='bottom', labelpad=10)

plt.xticks(x - 0.15)
plt.title('연도 별 IT계열 수요 인원')

x = Imis.loc[:, '연도']
w = 0.15
y1 = Imis.loc[:, '공급인원']
y = Imis.loc[:, '수요인원']
plt.ylim(0, 80000)

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],  # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize=9,
             color='black',
             horizontalalignment='center',  # horizontal alignment (left, center, right)
             verticalalignment='bottom')

x += w
for i, v in enumerate(x):
    plt.text(v, y1[i], y1[i],  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize=9,
             color='black',
             horizontalalignment='center',  # horizontal alignment (left, center, right)
             verticalalignment='bottom')

plt.savefig("C:/imis_Final/data/pic/IT계열수요인원.png")
#plt.show()

# # 2017 데이터
# plt.figure()
# x = Test2.loc[:, 'data']
# y = Test2.loc[:, 'val']
#
# plt.bar(x, y, width = 0.3)
#
# plt.xlabel("(분야별)")
# plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
# plt.ylim(0, 1.2)
# plt.title('2017년')
#
# for i, v in enumerate(x):
#     plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
#              fontsize = 9,
#              color = 'black',
#              horizontalalignment = 'center',  # (left, center, right)
#              verticalalignment = 'bottom')
# plt.savefig("2017.png")
#
#
# # 2018 데이터
# plt.figure()
# x = Test3.loc[:, 'data']
# y = Test3.loc[:, 'val']
#
# plt.bar(x, y, width = 0.3)
#
# plt.xlabel("(분야별)")
# plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
# plt.ylim(0, 1.2)
# plt.title('2018년')
#
# for i, v in enumerate(x):
#     plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
#              fontsize = 9,
#              color = 'black',
#              horizontalalignment = 'center',  # (left, center, right)
#              verticalalignment = 'bottom')
#
# plt.savefig("2018.png")
#
#
# # 2019 데이터
# plt.figure()
# x = Test4.loc[:, 'data']
# y = Test4.loc[:, 'val']
#
# plt.bar(x, y, width = 0.3)
#
# plt.xlabel("(분야별)")
# plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
# plt.ylim(0, 1.2)
# plt.title('2019년')
#
# for i, v in enumerate(x):
#     plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
#              fontsize = 9,
#              color = 'black',
#              horizontalalignment = 'center',  # (left, center, right)
#              verticalalignment = 'bottom')
#
# plt.savefig("2019.png")
#
#
# # 2020 데이터
# plt.figure()
# x = Test5.loc[:, 'data']
# y = Test5.loc[:, 'val']
#
# plt.bar(x, y, width = 0.3)
#
# plt.xlabel("(분야별)")
# plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
# plt.ylim(0, 1.2)
# plt.title('2020년')
#
# for i, v in enumerate(x):
#     plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
#              fontsize = 9,
#              color = 'black',
#              horizontalalignment = 'center',  # (left, center, right)
#              verticalalignment = 'bottom')
# plt.savefig("2020.png")
#
#
# # 클라우드 데이터
plt.figure(1)
x = Detail.loc[:, 'year']
y = Detail.loc[:, 'val']

plt.bar(x, y, width = 0.3)

plt.xlabel("연도")
plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
plt.xticks([2017, 2018, 2019, 2020])
plt.ylim(0, 1.2)
plt.title('클라우드')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')

plt.savefig("C:/imis_Final/data/pic연도별클라우드.png")
plt.show



# # 빅데이터 데이터
plt.figure(2)
x = Detail2.loc[:, 'year']
y = Detail2.loc[:, 'val']

plt.bar(x, y, width = 0.3)

plt.xlabel("연도")
plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
plt.xticks([2017, 2018, 2019, 2020])
plt.ylim(0, 1.2)
plt.title('빅데이터')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/연도별빅데이터.png")
#

# # IOT 데이터
plt.figure(3)
x = Detail3.loc[:, 'year']
y = Detail3.loc[:, 'val']

plt.bar(x, y, width = 0.3)

plt.xlabel("연도")
plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
plt.xticks([2017, 2018, 2019, 2020])
plt.ylim(0, 1.2)
plt.title('IoT')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/연도별IoT.png")
#
# # AI 데이터
plt.figure(4)
x = Detail4.loc[:, 'year']
y = Detail4.loc[:, 'val']

plt.bar(x, y, width = 0.3)

plt.xlabel("연도")
plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
plt.xticks([2017, 2018, 2019, 2020])
plt.ylim(0, 1.2)
plt.title('인공지능')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/연도별AI.png")



# # VR/AR/MR 데이터
plt.figure(5)
x = Detail5.loc[:, 'year']
y = Detail5.loc[:, 'val']

plt.bar(x, y, width = 0.3)

plt.xlabel("연도")

plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
plt.xticks([2017, 2018, 2019, 2020])
plt.ylim(0, 1.2)
plt.title('VR/AR/MR')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/연도별VR-AR-MR.png")


# # 블록체인 데이터
plt.figure(6)
x = Detail6.loc[:, 'year']
y = Detail6.loc[:, 'val']

plt.bar(x, y, width = 0.3)

plt.xlabel("연도")
plt.ylabel("(천명)", rotation = 0, loc = 'center', labelpad = 15)
plt.xticks([2017, 2018, 2019, 2020])
plt.ylim(0, 1.2)
plt.title('블록체인')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/연도별블록체인.png")

plt.figure(7)
x = Sum.loc[:, 'year']
y = Sum.loc[:, '클라우드']
y2 = Sum.loc[:, '빅데이터']
y3 = Sum.loc[:, 'IoT']
y4 = Sum.loc[:, 'AI']
y5 = Sum.loc[:, 'VR/AR/MR']
y6 = Sum.loc[:, '블록체인']

plt.plot(x, y, '-o', c = 'red', label = '클라우드')
plt.plot(x, y2, '-o', c = 'black', label = '빅데이터')
plt.plot(x, y3, '-o', c = 'green', label = 'IoT')
plt.plot(x, y4, '-o', c = 'blue', label = 'AI')
plt.plot(x, y5, '-o', c = 'gray', label = 'VR/AR/MR')
plt.plot(x, y6, '-o', c = 'purple', label = '블록체인')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')

for i, v in enumerate(x):
    plt.text(v, y2[i], y2[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')

for i, v in enumerate(x):
    plt.text(v, y3[i], y3[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'top')

for i, v in enumerate(x):
    plt.text(v, y4[i], y4[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')

for i, v in enumerate(x):
    plt.text(v, y5[i], y5[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'top')

for i, v in enumerate(x):
    plt.text(v, y6[i], y6[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')

plt.xlabel('연도')
plt.ylabel('(천명)')
plt.ylim(0, 1.2)
plt.xticks([2017, 2018, 2019, 2020])
plt.title('종합 데이터')

plt.legend(loc = 5)
plt.legend(loc = 'upper center')
plt.savefig("C:/imis_Final/data/pic/연도별세부직종.png")
#plt.show()


## 서울 데이터
plt.figure(8)
x = Seoul.loc[:, 'data']
y = Seoul.loc[:, 'val']

plt.bar(x, y, width = 0.3)
plt.xlabel("연도")
plt.ylim(0, 700)
plt.title('서울')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("D:/imis_Final/data/pic/서울.png")


plt.figure(9)
x = Busan.loc[:, 'data']
y = Busan.loc[:, 'val']

plt.bar(x, y, width = 0.3)
plt.xlabel("연도")
plt.ylim(0, 60)
plt.title('부산')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/부산.png")

plt.figure(10)
x = Gyeonggi.loc[:, 'data']
y = Gyeonggi.loc[:, 'val']
plt.bar(x, y, width = 0.3)
plt.xlabel("연도")
plt.ylim(0, 310)

plt.title('경기')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/경기.png")


plt.figure(11)
x = Incheon.loc[:, 'data']
y = Incheon.loc[:, 'val']

plt.bar(x, y, width = 0.3)
plt.xlabel("연도")
plt.ylim(0, 60)
plt.title('인천')

for i, v in enumerate(x):
    plt.text(v, y[i], y[i],                 # 좌표 (x축 = v, y축 = y[0]..y[0], 표시 = y[0]..y[0])
             fontsize = 9,
             color = 'black',
             horizontalalignment = 'center',  # (left, center, right)
             verticalalignment = 'bottom')
plt.savefig("C:/imis_Final/data/pic/인천.png")

text = ""
pic2addr=""
form_class = uic.loadUiType("C:/imis_Final/Proj.ui")[0]
class WindowClass(QMainWindow, form_class) :
    resized = QtCore.pyqtSignal()
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.cb1.activated.connect(self.cb1Event)
        self.cb2.activated.connect(self.cb2Event)
        self.tabWidget.currentChanged.connect(self.tabChange)

    def tabChange(self):
        index = self.tabWidget.currentIndex()
        tabName = (self.tabWidget.tabText(index))

        if tabName == "연도별 IT계열 세부직종 구인현황":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별세부직종.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
        elif tabName == "11월 지역별 구인현황":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\서울.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic3.setPixmap(self.qPixmapFileVar)            
        print(tabName)

    def cb1Event(self):
        text = (self.cb1.currentText())
        if text=="클라우드":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별클라우드.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
            print(text)

        elif text == "블록체인":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별블록체인.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
            print(text)

        elif text == "빅데이터":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별빅데이터.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
            print(text)  

        elif text == "IoT":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별IoT.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
            print(text) 

        elif text == "인공지능":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별AI.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
            print(text) 

        elif text == "VR/AR/MR":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별VR-AR-MR.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)
            print(text) 
        elif text == "전체":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\연도별세부직종.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic2.setPixmap(self.qPixmapFileVar)

    def cb2Event(self):
        text = (self.cb2.currentText())
        if text == "서울":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\서울.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic3.setPixmap(self.qPixmapFileVar)     
        elif text == "경기":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\경기.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic3.setPixmap(self.qPixmapFileVar)            
        elif text == "부산":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\부산.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic3.setPixmap(self.qPixmapFileVar)              
        elif text == "인천":
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("C:\\imis_Final\\data\\pic\\인천.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(630)
            self.pic3.setPixmap(self.qPixmapFileVar)        

    # def pic2ImgLoad(self) :
    #     #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
    #     self.qPixmapFileVar = QPixmap()
    #     self.qPixmapFileVar.load("C:\\Users\\don99\\Desktop\\PythonWorkSpace\\세부직종전체.png")
    #     self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
    #     self.pic1.setPixmap(self.qPixmapFileVar)
    
     
#여기


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 