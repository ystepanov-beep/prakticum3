gradus = int(input("Введите количество градусов (от 0 до 360) на сколько изменилась часовая стрелка с начала суток"))
if 0<=gradus<=360:
    hour = gradus // 30
    minut = (gradus * 2) % 60
    print(f"({hour} ч. {minut} мин.)")