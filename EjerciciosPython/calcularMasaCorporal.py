
def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(89.5, 1.65))

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(3, 4, 5))