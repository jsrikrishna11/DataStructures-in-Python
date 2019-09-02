ticks = '-'

def draw_line(count, number=''):
    print(ticks*count + number)
    return

def drawing(count):
    if count == 1:
        draw_line(1)
        return
    drawing(count -1)
    draw_line(count)
    drawing(count-1)

def scale(count, inches):
    draw_line(count,'0')
    j=1
    while j<= inches:
        drawing(count)
        draw_line(count,str(j))
        j+=1

scale(4,5)