money = int(input("Введите сумму вклада: "))
print(money)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
deposit_TKB = deposit.append(float(money / 100 * per_cent['ТКБ']))
deposit_SKB = deposit.append(float(money / 100 * per_cent['СКБ']))
deposit_VTB = deposit.append(float(money / 100 * per_cent['ВТБ']))
deposit_SBER = deposit.append(float(money / 100 * per_cent['СБЕР']))
print('Накопленные средства за год вклада в каждом из банков:', deposit)
print("Максимальная сумма, которую вы можете заработать — [%i]" % max(deposit))