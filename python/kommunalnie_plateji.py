# !!!!!!!!! - ВВЕДИ ТЕКУЩИЕ ПОКАЗАНИЯ - строки 12, 13, 14
# - расчет коммунальных платежей - тарифы с января 2026 - тут ммай 2026

mes = input('введи месяц словом на русском:   ')
god = input('введи год полностью - 4 цифры:   ')

tar_svet = 7.28
tar_gor = 317.71
tar_hol = 66.87
tar_vodootv = 52.48

svet = (13586 - 13464)   # новое - старое
gor = (382 - 379)      # новое - старое
hol = (17 - 11)      # новое - старое
vodootv = (gor + hol)

hol_vod = tar_hol * hol
gor_vod = tar_gor * gor
svet_1 = tar_svet * svet
vodootv_1 = vodootv * tar_vodootv

summ = hol_vod + gor_vod + svet_1 + vodootv_1

print()
print(f'Коммунальные платежи за {mes} {god}:')
print()
print(f'холодная вода - {hol} х {tar_hol} р. = {hol_vod:.2f} р.')
print(f'горячая вода - {gor} х {tar_gor} р. = {gor_vod:.2f} р.')
print(f'электроэнергия - {svet} х {tar_svet} р. = {svet_1:.2f} р.')
print(f'водоотведение - {vodootv} х {tar_vodootv} р. = {vodootv_1:.2f} р.')
print()
print(f'ИТОГО - {summ // 1:.0f} руб. {(summ % 1)//0.01:.0f} коп.')
