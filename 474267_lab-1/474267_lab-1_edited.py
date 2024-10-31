# лабораторная работа №1 Гончаров Александр Сергеевич 474267

# 7 вариант


# Задание №1


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(color):
    line = '  '
    print(f"{SET_COLOR}{color}m{line}{END}",end = '')


def draw_flag_of_Japan():
    width = 50
    height = 25
    radius = 9
    color = [1,255]


    for y in range(height):
        for x in range(width):
            if ((x - width // 2) ** 2 + (y - height // 2) ** 2) -9 <= radius ** 2:
                draw_line(color[0])
            else:
                draw_line(color[1])
        print()

if __name__ == "__main__":
    print('Задание №1. Флаг Японии')
    draw_flag_of_Japan()
    print()


# Задание №2


color = [232,255]

def draw_element(color,k):
    line = ' ' * k
    print(f"{SET_COLOR}{color}m{line}{END}",end = '')


def draw_pattern():

    def first_line(n = 4):
        for i in range(n):
            draw_element(color[1],12)
            draw_element(color[0],3)
            draw_element(color[1],9)
        print('',end = '')

    def second_line(n = 4):
        for i in range(n):
            draw_element(color[1],9)
            draw_element(color[0],3)
            draw_element(color[1],3)
            draw_element(color[0],3)
            draw_element(color[1],6)
        print('',end = '')

    def third_line(n = 4):
        for i in range(n):
            draw_element(color[1],6)
            draw_element(color[0],3)
            draw_element(color[1],9)
            draw_element(color[0],3)
            draw_element(color[1],3)
        print('',end = '')

    def fourth_line(n = 4):
        for i in range(n):
            draw_element(color[1],3)
            draw_element(color[0],3)
            draw_element(color[1],15)
            draw_element(color[0],3)
            draw_element(color[1],0)
        print('',end = '')
        
    def fifth_line(n = 4):
        for i in range(n):
            draw_element(color[0],3)
            draw_element(color[1],21) 
            draw_element(color[0],0)
        print('',end = '')

    for i in range(4):
        first_line() 
        draw_element(color[1],3)
        print()

        second_line()
        draw_element(color[1],3)
        print()

        third_line() 
        draw_element(color[1],3)
        print()

        fourth_line() 
        draw_element(color[1],3)
        print()

        fifth_line() 
        draw_element(color[0],3)
        print()

        fourth_line()
        draw_element(color[1],3)
        print()

        third_line() 
        draw_element(color[1],3)
        print()

        second_line()
        draw_element(color[1],3)
        print()

    first_line() 
    draw_element(color[1],3)
    print()


if __name__ == "__main__":
    print('Задание №2. Узор')
    draw_pattern()
    print()
    

#задание 3



def draw_function():
    color = [232,255]
    for y in range(20,0,-1):
        print(y,'',end = '')
        for x in range(10):

            if y == x * 3:
                print(f"{SET_COLOR}{color[1]}m{' '}{END}", end = '')
            else:
                print(f"{'  '}{END}", end = '')
        print()
    print('0   1 2 3 4 5 6 7 8 9')


if __name__ == "__main__":
    print('Задание №3. График функции y = 3x')
    draw_function()
    print()


#задание 4


def draw_diagram(filename, color1 = 1, color2 = 20):


    file = open('sequence.txt', 'r')
    list = []
    for number in file:
        if float(number) <= 0:
            list.append(float(number))
    file.close()


    more_then_minus_5 = [(list[i]) for i in range(len(list)) if float(list[i]) > -5]
    less_then_minus_5 = [(list[i]) for i in range(len(list)) if float(list[i]) < -5]


    count = len(more_then_minus_5) + len(less_then_minus_5)
    percent_more = (len(more_then_minus_5) / count) * 100
    percent_less = (len(less_then_minus_5) / count) * 100


    line_more_then_minus_5 = round(percent_more) * ' '
    line_less_then_minus_5 = round(percent_less) * ' '


    print(f"Неположительные числа больше -5: {percent_more} %  {SET_COLOR}{color1}m{line_more_then_minus_5}{END}")
    print(f"Неположительные числа меньше -5: {percent_less} %  {SET_COLOR}{color2}m{line_less_then_minus_5}{END}")


    


if __name__ == "__main__":
    print('Задание №4. Диаграммa процентного соотношения')
    draw_diagram('sequence.txt')
    print()


