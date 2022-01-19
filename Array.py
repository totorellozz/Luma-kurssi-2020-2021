taulukko = ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai']

paiva = int(input("Mikä päivä tänään on numeroina: "))

match paiva:
    case 1:
        print('Tänään on Maanantai')
    case 2:
        print('Tänään on Tiistai.')
    case 3:
        print('Tänään on Keskiviikko.')
    case 4:
        print('Tänään on Torstai.')
    case 5:
        print('Tänään on Perjantai.')
    case 6:
        print('Tänään on Lauantai.')
    case 7:
        print('Tänään on Sunnuntai.')

# if paiva == 1:
#     print('Tänään on Maanantai')
# if paiva == 2:
#     print('Tänään on Tiistai.')
# if paiva == 3:
#     print('Tänään on Keskiviikko.')
# if paiva == 4:
#     print('Tänään on Torstai.')
# if paiva == 5:
#     print('Tänään on Perjantai.')
# if paiva == 6:
#     print('Tänään on Lauantai.')
# if paiva == 7:
#     print('Tänään on Sunnuntai.')
