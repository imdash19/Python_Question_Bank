# There are four different points on a plane, P (xp, yp), Q (xq, yq), R (xr, yr) and S (xs, ys). Write a Python program to determine whether AB and CD are orthogonal.
# Input: xp, yp, xq, yq, xr, yr, xs and ys are -100 to 100 respectively and each value can be up to 5 digits after the decimal point It is given as a real number including the number of. Output:
# Output AB and CD are not orthogonal! or AB and CD are orthogonal!

xp, yp, xq, yq, xr, yr, xs, ys = map(float, input().split())

abx = xq - xp
aby = yq - yp
cdx = xs - xr
cdy = ys - yr

dot = abx * cdx + aby * cdy

if dot == 0:
    print("AB and CD are orthogonal!")
else:
    print("AB and CD are not orthogonal!")