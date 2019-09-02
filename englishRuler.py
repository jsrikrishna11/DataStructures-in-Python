ticks = '-'
level = 0
def  draw_line(tick_length, label=''):
    print(ticks*tick_length + label)

def draw_centre(centre_length):
    if centre_length >0:
        draw_centre(centre_length - 1)
        draw_line(centre_length)
        draw_centre(centre_length - 1)

def draw_ruler(inches, tick_length):
    draw_line(tick_length,'0')
    for j in range(1, inches+1):
        draw_centre(tick_length - 1)
        draw_line(tick_length, str(j))

draw_ruler(2, 5)