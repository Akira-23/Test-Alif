import pickle

listfile = "list_file.data"
mlist = ["Огурцы - 20", "Помидоры - 30", "Масло - 50"]

res = 1
while res > 0:
    print("1-Сохранить файл.\n2-Показать список."
        "\n3-Добавить в спикок."
        "\n4-Изменить запись в списке."
        "\n5-Удалить из списка."
        "\n6-Вычесть общую сумму."
        "\n7-Вызов сохраненного файла."
        "\nНажмите другию клавишу для выхода.")
    dop = input("Ввод: (1,2,3,4,5,6) ")

    if dop == "1":
        f = open(listfile, "wb")
        pickle.dump(mlist, f)
        f.close()
        del mlist
        print("Файл сохранен.")

    elif dop == "2":
        print(mlist)

    elif dop == "3":
        name = input("Введите название - (Пример: Огурец) ")
        prise = input("Введите цену: ")
        result = (f"{name} - {prise}")
        mlist.append(result)
        print(mlist)

    elif dop == "4":
        print("Введите индекс изменяемого объекта.")
        change = int(input("Ввод: "))
        name = input("Введите название - (Пример: Огурец) ")
        prise = input("Введите цену: ")
        add = (f"{name} - {prise}")
        mlist[change] = add
        print(mlist)
    
    elif dop == "5":
        print("Введите индекс удаляемого объекта.")
        delete = int(input("Ввод: "))
        del mlist[delete]
        print(mlist)

    elif dop == "6":
        print("Общая сумма =", len(mlist))

    elif dop == "7":
        name_file = input("Имя файла: (list_file.data) ")
        do_file = input("Действие: (rb) ")

        file = open(f"{name_file}", f"{do_file}")

        storedlist = pickle.load(file)
        print(storedlist)
        
    else:
        yep = input("Продолжить: (Да)(Нет) ")
        if yep == "Да" or yep == "да":
            res = 1
        if yep == "Нет" or yep == "нет":
            res = 0

