def car_listing(car_prices):
    result = ""
    for x in car_prices.keys():
        result += "{} costs {} dollars".format(x, car_prices[x]) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
                   "Ford Fiesta": 13000, "Toyota Prius": 24000}))
