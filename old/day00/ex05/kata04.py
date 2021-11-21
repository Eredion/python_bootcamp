#! /usr/bin/python3

t = (0, 4, 132.42222, 10000, 12345.67)

print("day_0", t[0], ", ex_0", t[1], " : ", '{0:.5g}'.format(t[2]), ", ",\
      "{:.2e}".format(t[3]), ", ", "{:.2e}".format(t[4]), sep = "")
