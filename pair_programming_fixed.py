def feet_and_inches_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    return meters

# Good function, could use more comments/documentation

# Test 1
def test_1():
    myheight = feet_and_inches_to_meters(5,10)
    print(myheight)
    return myheight

# Test 2
def test_2():
    zero = feet_and_inches_to_meters(0,0)
    print(zero)
    return zero