def kelvinToFahrenheit(Temp):
    assert (Temp>=0),"colder than absolute zero!"
    res=((Temp-273)*1.8)+32
    return res
try:
    print(kelvinToFahrenheit(273))
    print(kelvinToFahrenheit(505.78))
    print(kelvinToFahrenheit(-5))
except AssertionError as ob:
    print(ob)
print("Thank you")
