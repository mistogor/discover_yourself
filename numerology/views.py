from django.shortcuts import render
from numerology.forms import *
from django.contrib.auth.decorators import login_required 
from numerology.models import *
import datetime
from collections import Counter

def destiny_number(request):
    date_of_birth = str(request.user.date_of_birth)
    destiny_number = 0
    temp = 0
    for char in date_of_birth: 
        if char.isdigit():
            temp += int(char)
        else:
            continue
    
    destiny_number = int(str(temp)[0]) + int(str(temp)[-1])
    destiny_result = DestinyNumber.objects.get(condition = destiny_number)

    return render(request, 'numerology/destiny_number.html', {
        'destiny_number': destiny_number,
        'destiny_result': destiny_result,
    })


def soul_number(request):
    date_of_birth = str(request.user.date_of_birth)
    soul_number = int(date_of_birth[-1]) + int(date_of_birth[-2])
    
    soul_result = SoulNumber.objects.get(condition=soul_number)
    
    return render(request, 'numerology/soul_number.html', {
        'date_of_birth': date_of_birth,
        'soul_number': soul_number,
        'soul_result': soul_result,
    })
    
def pithagor_matrix(request):
    input_birthday = str(request.user.date_of_birth)
    date_of_birth = datetime.datetime.strptime(input_birthday, '%Y-%m-%d').strftime('%d.%m.%Y')
    digits = [int(item) for item in date_of_birth if item.isdigit()]
    digits_str = [str(item) for item in digits]

    first_number = sum(digits)
    second_number = sum(map(int,str(first_number)))
    third_number = first_number - digits[0]*2
    forth_number = sum(map(int,str(third_number)))

    final_list = digits_str + list(''.join(str(first_number)) + ''.join(str(second_number))+ ''.join(str(third_number)) + ''.join(str(forth_number)))

    ones = final_list.count('1')

    if ones >= 6:
        ones_result = PithagorOnes.objects.get(condition=6)
    else:
        ones_result = PithagorOnes.objects.get(condition=ones)
    
    twos = final_list.count('2')
    if twos >= 4:
        twos_result = PithagorTwos.objects.get(condition=4)
    else:
        twos_result = PithagorTwos.objects.get(condition=twos)
    
    threes = final_list.count('3')
    if threes >= 4:
        threes_result = PithagorThrees.objects.get(condition=4)
    else:
        threes_result = PithagorThrees.objects.get(condition=threes)

    fours = final_list.count('4')
    if fours >= 2:
        fours_result = PithagorFours.objects.get(condition=2)
    else:
        fours_result = PithagorFours.objects.get(condition=fours)
    

    fives = final_list.count('5')
    if fives >= 3:
        fives_result = PithagorFives.objects.get(condition=3)
    else:
        fives_result = PithagorFives.objects.get(condition=fives)
    sixes = final_list.count('6')
    if sixes >= 3:
        sixes_result = PithagorSixes.objects.get(condition=3)
    else:
        sixes_result = PithagorSixes.objects.get(condition=sixes)
    sevens = final_list.count('7')
    if sevens >= 3:
        sevens_result = PithagorSevens.objects.get(condition=3)
    else:
        sevens_result = PithagorSevens.objects.get(condition=sevens)
    eights = final_list.count('8')
    if eights >= 2:
        eights_result = PithagorEights.objects.get(condition=2)
    else:
        eights_result = PithagorEights.objects.get(condition=eights)
    nines = final_list.count('9')
    if nines == 0:
        nines_result = PithagorNines.objects.get(condition=1)
    elif nines >= 3:
        nines_result = PithagorNines.objects.get(condition=3)
    else:
        nines_result = PithagorNines.objects.get(condition=nines)
# Lines results...
    first_line = ones + fours + sevens
    second_line = twos + fives + eights
    third_line = threes + sixes + nines
    
    if first_line <6:
        first_line_result = PithagorFirstLine.objects.get(condition = first_line)
    else:
        first_line_result = PithagorFirstLine.objects.get(condition = 6)
    
    if second_line <6:
        second_line_result = PithagorSecondLine.objects.get(condition = second_line)
    else:
        second_line_result = PithagorSecondLine.objects.get(condition = 6)

    if third_line <6:
        third_line_result = PithagorThirdLine.objects.get(condition = third_line)
    else:
        third_line_result = PithagorThirdLine.objects.get(condition = 6)


# Columns results...

    first_column = ones + twos + threes
    second_column = fours + fives + sixes
    third_column = sevens + eights + nines

    if first_column <=3:
        first_column_result = PithagorFirstColumn.objects.get(condition = 0)
    elif first_column >= 6:
        first_column_result = PithagorFirstColumn.objects.get(condition = 6)
    else:
        first_column_result = PithagorFirstColumn.objects.get(condition = first_column)


    if second_column <6:
        second_column_result = PithagorSecondColumn.objects.get(condition = second_column)
    else:
        second_column_result = PithagorSecondColumn.objects.get(condition = 6)

    third_column_result = PithagorThirdColumn.objects.get(condition = 0)


    # Ascending diagonal ...

    ascending_diagonal = threes + fives + sevens

    if ascending_diagonal <6:
        ascending_diagonal_result = PithagorAscendingDiagonal.objects.get(condition = second_column)
    else:
        ascending_diagonal_result = PithagorAscendingDiagonal.objects.get(condition = 6)

    # Descending diagonal...
    descending_diagonal = ones + fives + nines
    descending_diagonal_result = PithagorDescendingDiagonal.objects.get(condition = 0)

    return render(request, 'numerology/pithagor_matrix.html', {
        'ones_result': ones_result,
        'twos_result': twos_result,
        'threes_result': threes_result,
        'fours_result': fours_result,
        'fives': fives,
        'fives_result': fives_result,
        'sixes_result': sixes_result,
        'sixes': sixes,
        'sevens_result': sevens_result,
        'sevens': sevens,
        'eights_result': eights_result,
        'eights': eights,
        'nines_result': nines_result,
        'nines': nines,
        'first_line_result': first_line_result,
        'second_line_result': second_line_result,
        'third_line_result': third_line_result,
        'first_column_result': first_column_result,
        'second_column_result': second_column_result,
        'third_column': third_column,
        'third_column_result': third_column_result,
        'ascending_diagonal_result': ascending_diagonal_result,
        'descending_diagonal': descending_diagonal,
        'descending_diagonal_result': descending_diagonal_result,
    })





