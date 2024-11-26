import my_function
import math
from PIL import  Image
from my_function import substrat

# sum = my_function.add(5,6)
# print(sum)
#
# minus = my_function.substrat(10,7)
# print(minus)
#
# into = my_function.multiply(5,6)
# print(into)
#
# divide = my_function.divide(4,2)
# print(divide)
#
# math = math.isqrt(9)
# print(math)

my_image = Image.open("tel pro.jpg")
roteated = my_image.rotate(60)
roteated.save('ppk.jpg')
roteated.show()