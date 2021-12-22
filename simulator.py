#!/usr/bin/python3

import random
from time import time, sleep
from jumpers import jumpers_list

#jumpers = {
#    'Kamil Stoch': [5, 5, 4],
#    'Dawid Kubacki': [4, 4, 4],
#    'Piotr Żyła': [4, 4, 4],
#    'Maciej Kot': [4, 4, 4],
#}

jumpers = jumpers_list
standings = {}

skijumps = {90: 100, 120: 134, 200: 240}
skijump = random.choice(list(skijumps.items()))

def shuffle_skijump():
    kpoint = float(skijump[0])
    hspoint = float(skijump[1])
    if kpoint < 100:
        factor = 2.0
        bonus = 60.0
    elif kpoint >=100 and kpoint < 170:
        factor = 1.8
        bonus = 60.0
    else:
        factor = 1.2
        bonus = 120.0
    return factor, bonus, kpoint, hspoint

def jump():
    factor,bonus,kpoint,hspoint = shuffle_skijump()
    distance = random.uniform(60,hspoint)
    distance = round(distance*2)/2
    return factor, bonus, kpoint, hspoint, distance

def judges_calculation():
    factor,bonus,kpoint,hspoint,distance = jump()
    judges = []
    for i in range(5):
        x = random.uniform(15, 20)
        x = round(x*2)/2
        judges.append(x)
    sort_judges = judges
    sort_judges.sort()
    judges_points = sort_judges[1:-1]
    judges_points = sum(judges_points)
    judges = ', '.join([str(elem) for elem in judges])
    return factor, bonus, kpoint, hspoint, distance, judges, judges_points

def meter_points_calculation():
    factor,bonus,kpoint,hspoint,distance,judges,judges_points = judges_calculation()
    if distance >= kpoint:
        difference = distance - kpoint
        meter_points = bonus + (difference * factor)
        meter_points = round(meter_points, 1)
    else:
        difference = kpoint - distance
        meter_points = bonus - (difference * factor)
        meter_points = round(meter_points, 1)
    return factor, bonus, kpoint, hspoint, distance, judges, judges_points, meter_points

def all_points_calculation():
    factor,bonus,kpoint,hspoint,distance,judges,judges_points,meter_points = meter_points_calculation()
    print("Skocznia K-" + str(int(kpoint)))
    print("Odległość: ", str(distance))
    print("Noty za styl: ", judges)
    print("Suma not za styl: ", str(judges_points))
    print("Punkty za odległość: ", str(meter_points))
    total_points = meter_points + judges_points
    total_points = round(total_points, 1)
    if total_points < 0:
        total_points = 0
    print("Nota za skok: ", str(total_points))
    return distance, total_points

if __name__ == '__main__':
    try:
        input("Aby rozpocząć kwalifikacje, naciśnij klawisz ENTER.")

        ### Kwalifikacje ###
        for current_jumper in jumpers.keys():
            print("\nNa belce siada teraz", current_jumper)
            all_points_calculation()
            distance_out,total_points_out = all_points_calculation()
            mts_pts_list = []
            mts_pts_list.append(distance_out)
            mts_pts_list.append(total_points_out)
            standings[current_jumper] = mts_pts_list
            sleep(0.1)

        qual_standings = {}
        print("\nWyniki kwalifikacji:")
        print("ZAWODNIK - ODLEGŁOŚĆ (M) - NOTA ŁĄCZNA (PKT)")

        # Sortowanie wyników
        for key, value in sorted(standings.items(), key=lambda t: t[1][1], reverse=True):
            qual_standings[key] = value

        # Wyświetlenie wyników
        for i, (k, v) in enumerate(qual_standings.items(), 1):
            v = ' '.join(str(e) for e in v)
            print(i, '. ', k, ' ', v, sep='')

        # Pozostawienie najlepszej 50-tki
        qual_standings = dict(list(qual_standings.items())[:50])

        input("Aby rozpocząć pierwszą serię, naciśnij klawisz ENTER.")

        ### 1. seria ###
        standings.clear()

        for current_jumper in qual_standings.keys():
            print("\nNa belce siada teraz", current_jumper)
            all_points_calculation()
            distance_out,total_points_out = all_points_calculation()
            mts_pts_list = []
            mts_pts_list.append(distance_out)
            mts_pts_list.append(total_points_out)
            standings[current_jumper] = mts_pts_list
            sleep(0.1)

        first_round_standings = {}
        print("\nWyniki I serii:")
        print("ZAWODNIK - ODLEGŁOŚĆ (M) - NOTA ŁĄCZNA (PKT)")

        # Sortowanie wyników
        for key, value in sorted(standings.items(), key=lambda t: t[1][1], reverse=True):
            first_round_standings[key] = value

        # Wyświetlenie wyników
        for i, (k, v) in enumerate(first_round_standings.items(), 1):
            v = ' '.join(str(e) for e in v)
            print(i, '. ', k, ' ', v, sep='')

        # Pozostawienie najlepszej 30-tki
        first_round_standings = dict(list(first_round_standings.items())[:30])

        #input("Aby rozpocząć drugą serię, naciśnij klawisz ENTER.")

        ### 2. seria ###
        second_round_order = {}
        for key, value in sorted(first_round_standings.items(), key=lambda t: t[1][1]):
            second_round_order[key] = value

        input("Aby rozpocząć drugą serię, naciśnij klawisz ENTER.")

        second_round_standings = {}

        for current_jumper in second_round_order.keys():
            points = second_round_order.get(current_jumper)
            points = points[1]
            first_jump = second_round_order.get(current_jumper)
            first_jump = first_jump[0]
            print("\nNa belce siada teraz", current_jumper, "Zawodnik ten w I serii otrzymał notę", points)
            all_points_calculation()
            distance_out,total_points_out = all_points_calculation()
            total_points = total_points_out + points
            total_points = round(total_points, 1)
            mts_pts_list = []
            mts_pts_list.append(first_jump)
            mts_pts_list.append(distance_out)
            mts_pts_list.append(total_points)
            second_round_standings[current_jumper] = mts_pts_list
            sleep(0.1)


        final_standings = {}
        print("\nWyniki zawodów:")
        print("ZAWODNIK - I SERIA (M) - II SERIA (M) - NOTA ŁĄCZNA (PKT)")

        for key, value in sorted(second_round_standings.items(), key=lambda t: t[1][2], reverse=True):
            final_standings[key] = value

        for i, (k, v) in enumerate(final_standings.items(), 1):
            v = ' '.join(str(e) for e in v)
            print(i, '. ', k, ' ', v, sep='')
    except KeyboardInterrupt:
        print("\nProgram został zatrzymany przez użytkownika!")