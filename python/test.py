# import numpy as np
# from ImageToComplexArray import ComplexImageConverter as CIC
# import matplotlib.pyplot as plt


# array = CIC(r'Images\Circle.png')
# x = np.linspace(-140.75,140.25,array.size)
# y1 = array.real
# y2 = array.imag
# y3 = np.fft.fft(array).real
# y4 = np.fft.fft(array).imag
# # y = np.sin(x)

# # plt.plot(x,y2,'g-')
# # plt.plot(x,y1,'r-')
# plt.plot(x,y3,'b-')
# plt.plot(x,y3,'r-')
# plt.show()




# test = 'Hello I am beatiful'
# while test.endswith('/') == False:
#     test = test[:-1]
#     print(test)

# seet = set()
# for A in range(1,7):
#     for B in range(1,7):
#         for D in range(1,7):
#             if D != A and D != B:
#                 for E in range(1,7):
#                     if E != B:
#                         for C in range(1,7):
#                             if C != A and C != E:
#                                 seet.add((A,B,C,D,E))
# print(len(seet))