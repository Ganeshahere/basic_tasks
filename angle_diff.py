import prompt
def diff(ang1, ang2):
    answer = min(
            (ang1 - ang2) % 360,
            (ang2 - ang1) % 360,
            )
    print('angle difference is:',answer)
    return answer
ang1 = prompt.integer('Type in first angle: ')
ang2 = prompt.integer('Type in second angle: ')
diff(ang1, ang2)
