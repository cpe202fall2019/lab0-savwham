def weight_on_planets():
   earth = int(input("What do you weigh on earth? ")) #ask input, cast input as int
   mars = 0.38 * earth
   jupiter = 2.34 * earth
   print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars, jupiter))

if __name__ == '__main__':
   weight_on_planets()
