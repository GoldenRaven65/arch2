def europay(amount):
    for banknote in (5, 10, 20, 50, 100, 200, 500):
        if banknote >= amount:
            return banknote


print(europay(19))
#werkend
assert europay(50) == 50
assert europay(51) == 100
assert europay(49) == 50
assert europay(48) == 50
assert europay(47) == 50
assert europay(5) == 5
assert europay(4) == 5
assert europay(1) == 5
assert europay(2) == 5
assert europay(3) == 5
assert europay(6) == 10
assert europay(7) == 10
assert europay(8) == 10
assert europay(9) == 10
assert europay(10) == 10
assert europay(11) == 20
assert europay(12) == 20
assert europay(13) == 20
assert europay(14) == 20
assert europay(15) == 20
assert europay(16) == 20
assert europay(17) == 20
assert europay(20) == 20
assert europay(18) == 20
assert europay(21) == 50
assert europay(19) == 20
assert europay(22) == 50
assert europay(100) == 100
assert europay(101) == 200
assert europay(199) == 200
assert europay(200) == 200
assert europay(201) == 500
assert europay(499) == 500
assert europay(500) == 500
assert europay(501) == None
assert europay(1000) == None