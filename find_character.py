def char_find(list, character):
    newList = []
    for i in range(0,len(list)):
        if list[i].find(character)!=-1:
            newList.append(list[i])

    print newList
