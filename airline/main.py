#!/usr/bin/env python3

import sys
from math import *

def distance(point1, point2):
    R = 6370
    lat1 = radians(point1[0])  #insert value
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2- lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

while True:
    N = sys.stdin.readline()

    if not N:
        break

    N = int(N)

    ports = []

    for i in range(N):
        lat, lon = map(float, input().split())
        # print(f'lat: {lat}, lon: {lon}')
        ports.append((lat, lon))

    m = (ports[0], sys.float_info.max)
    for i in range(N):
        s = [] 

        for j in range(N):
            dist = distance(ports[i], ports[j])
            # print(f'dist: {dist}')
            s.append(dist)

        s = max(s)

        if s <= m[1]:
            m = (ports[i], s)

    print(f'{m[0][0]:.2f} {m[0][1]:.2f}')
