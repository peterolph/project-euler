
import itertools

vals = (0,1,2,3,4,5,6,7,8,9)

total = 0
for a in itertools.combinations(vals,6):
  for b in itertools.combinations(vals,6):
    if ((( 0 in a            and            1 in b ) or (           1 in a  and            0 in b )) and
        (( 0 in a            and            4 in b ) or (           4 in a  and            0 in b )) and
        (( 0 in a            and (9 in b or 6 in b)) or ((9 in a or 6 in a) and            0 in b )) and
        (( 1 in a            and (9 in b or 6 in b)) or ((9 in a or 6 in a) and            1 in b )) and
        (( 2 in a            and            5 in b ) or (           5 in a  and            2 in b )) and
        (( 3 in a            and (9 in b or 6 in b)) or ((9 in a or 6 in a) and            3 in b )) and
        (( 4 in a            and (9 in b or 6 in b)) or ((9 in a or 6 in a) and            4 in b )) and
        (((9 in a or 6 in a) and            4 in b ) or (           4 in a  and (9 in b or 6 in b))) and
        (( 8 in a            and            1 in b ) or (           1 in a  and            8 in b ))):
      total += 1

print total/2
