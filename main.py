def tot(pr, u):
    return pr * u

def mfunc():
    price=200
    units=5
    tot = tot(price, units)
    print("The total price is ", tot, " bucks")

if __name__ == "__main__":
    mfunc()
