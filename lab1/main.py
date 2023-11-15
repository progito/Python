def main():
    name= input("введи имя")
    folowers= int(input("введи к-во подписчиков"))
    link= input("оставь ссылку")
    print("Привет", name )
    if 100000 <= folowers < 1000000:
        print("У вас уже есть серебрянная кнопка")
    elif 1000000 <= folowers:
        print("У вас уже есть серебрянная и золотая кнопки")
    elif folowers < 100000:
        print("У вас пока недостаточно подписчиков для кнопки Ютуба")
    else: 
        print("дурачек")
    print("Подписаться на канал", name, "вот ссылка", link )
