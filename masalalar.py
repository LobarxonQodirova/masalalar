# #  1-masala
#  class BankHisobi:
#      def __init__(self,egasi, boshlangich_balans=0):
#          self.__egasi = egasi
#          self.__balans = boshlangich_balans
#
#      def get_egasi(self):
#          return self.__egasi
#
#      def get_balans(self):
#          return self.__balans
#
#      def pul_qosh(self, miqdor):
#          if miqdor <= 0:
#              print("Noto'g'ri miqdor!")
#              return
#          self.__balans += miqdor
#
#      def pul_yech(self, miqdor):
#          if miqdor <= 0:
#              print("Noto'g'ri miqdor!")
#          elif miqdor > self.__balans:
#              print("Mablag' yetarli emas!")
#          else:
#              self.__balans -= miqdor
#
#  hisob = BankHisobi("Ozodbek", 5_000_000)
#  print(hisob.get_egasi())
#  print(hisob.get_balans())
#  hisob.pul_qosh(200_000)
#  print(hisob.get_balans())
#  hisob.pul_yech(1_100_000)
#  print(hisob.get_balans())
#  hisob.pul_yech(200_000)
#  hisob.pul_qosh(-100_000)
#
#
# # 3-masala
# class Talaba:
#     def __init__(self, ism, fan):
#         self.__ism = ism
#         self.__fan = fan
#         self.__baholar = []
#
#     def get_ism(self):
#         return self.__ism
#     def get_fan(self):
#         return self.__fan
#
#     def baho_qosh(self, baho):
#         if not (0 <= baho <= 100):
#             print("Baho 0 dan 100 gacha bo'lishi kerak!")
#             return
#         else:
#             self.__baholar.append(baho)
#
#     def get_baholar(self):
#         return self.__baholar.copy()
#
#     def ortacha_baho(self):
#         if not self.__baholar:
#             print("Hali baholar yo'q!")
#             return
#         else:
#             return round(sum(self.__baholar) / len(self.__baholar), 2)
#
#
# talaba = Talaba("Durbek", "Matematika")
# talaba.baho_qosh(100)
# talaba.baho_qosh(100)
# talaba.baho_qosh(70)
# print(f"Talaba baholari: {talaba.get_baholar()}")
# print(f"Talaba o'rtacha bahosi: {talaba.ortacha_baho()}")
#
# talaba.baho_qosh(1000)
# print(f"Talaba baholari: {talaba.get_baholar()}")


# 4-masala
