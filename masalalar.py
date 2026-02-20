# # 1-masala
# class BankHisobi:
#     def __init__(self,egasi, boshlangich_balans=0):
#         self.__egasi = egasi
#         self.__balans = boshlangich_balans
#
#     def get_egasi(self):
#         return self.__egasi
#
#     def get_balans(self):
#         return self.__balans
#
#     def pul_qosh(self, miqdor):
#         if miqdor <= 0:
#             print("Noto'g'ri miqdor!")
#             return
#         self.__balans += miqdor
#
#     def pul_yech(self, miqdor):
#         if miqdor <= 0:
#             print("Noto'g'ri miqdor!")
#         elif miqdor > self.__balans:
#             print("Mablag' yetarli emas!")
#         else:
#             self.__balans -= miqdor
#
# hisob = BankHisobi("Ozodbek", 5_000_000)
# print(hisob.get_egasi())
# print(hisob.get_balans())
# hisob.pul_qosh(200_000)
# print(hisob.get_balans())
# hisob.pul_yech(1_100_000)
# print(hisob.get_balans())
# hisob.pul_yech(200_000)
# hisob.pul_qosh(-100_000)
