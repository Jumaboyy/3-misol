
"""1-masala
Triangle nomli class yozing. Class uchburchak tomonlarini qabul qilsin.
 Classni ichida object haqida ma'lumot qaytaruvchi, uchburchak perimeterni,
 uchburchak yuzasini hispbloychi funksiya yozing."""

# import  math
# class Triangle:
#     def __init__(self , atomon,btomon,ctomon):
#         self.atomon=atomon
#         self.btomon=btomon
#         self.ctomon=ctomon
#
#     def perimetr(self):
#         return self.atomon+self.btomon+self.ctomon
#
#     def yuza(self):
#         s=self.perimetr()/2
#         yuza=math.sqrt(s*(s-self.atomon)*(s-self.btomon)*(s-self.ctomon))
#         return yuza

# atomon=int(input('A tomon uzunligini kiriting: '))
# btomon=int(input('B tomon uzunligini kiriting: '))
# ctomon=int(input('C tomon uzunligini kiriting: '))
#
# uchburchak=Triangle(atomon,btomon,ctomon)
# print("Perimetr:", uchburchak.perimetr())
# print("Yuzasi:", uchburchak.yuza())

"""2-masala
Computer nomli class yozing. Class kompyuterning parameterlanni qabul qilsin. 
Va bu qabul qilingan parameterlardan bir nechtasini inkapsulyatsiya qiling. 
Bu classga kamida 10 ta method yozing."""
# class Kompyuter:
#     def __init__(self, model, brend, processor, ram, video_card):
#         self._model = model
#         self._brend = brend
#         self._processor = processor
#         self._ram = ram
#         self._video_card = video_card
#
#     def modelni_(self):
#         return f'Model: {self._model}'
#
#     def brendni_(self):
#         return f'Brend: {self._brend}'
#
#     def processorni_(self):
#         return f'Processor: {self._processor}'
#
#     def ramni_(self):
#         return f'RAM: {self._ram}'
#
#     def video_cardni_(self):
#         return f'Video_card: {self._video_card}'
#
# model = str(input('Modelni kiritng: '))
# brend = str(input('Brendni kiriting: '))
# processor = str(input('Processor ni kiriting: '))
# ram = int(input('RAM ni kiriting: '))
# video_card = str(input('Video_card ni kiriting: '))
#
# kompyuter = Kompyuter(model, brend, processor, ram, video_card)
#
# print('Model:', kompyuter.modelni_())
# print('Brend:', kompyuter.brendni_())
# print('Processor:', kompyuter.processorni_())
# print('RAM:', kompyuter.ramni_())
# print('Video_card:', kompyuter.video_cardni_())



