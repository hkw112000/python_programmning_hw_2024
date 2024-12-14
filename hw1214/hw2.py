#!/usr/bin/env python3

# Heron's formula
def areaT(s1, s2, s3):
    s = (s1 + s2 + s3)/2
    area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
    return area


print(areaT(3, 4, 5))
