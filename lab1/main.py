
def main():
    name = input("введи имя")
    followers = int(input("введи к-во подписчиков"))
    link = input("оставь ссылку")
    print("Привет", name)
    if 100000 <= followers < 1000000:
        print("У вас уже есть серебрянная кнопка")
    elif 1000000 <= followers:
        print("У вас уже есть серебрянная и золотая кнопки")
    elif followers < 100000:
        print("У вас пока недостаточно подписчиков для кнопки Ютуба")
    else:
        print("дурачек")
    print("Подписаться на канал", name, "вот ссылка", link)
    
    
    
    
    
    