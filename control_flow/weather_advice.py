sitution = input("What's the weather like today? (sunny/rainy/cold): ")
if sitution.lower() == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif sitution.lower() == "rainy":
  print("Don't forget your umbrella and a raincoat.")
elif sitution.lower() == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("Sorry, I don't have recommendations for this weather.")