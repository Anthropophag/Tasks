fruit_basket_1 = ['яблоко', 'груша', 'маракуя', "банан"]
fruit_basket_2 = ['личи', 'арбуз', "банан", 'маракуя']
fruit_basket_general = []

for fruit in fruit_basket_1:
    if fruit in fruit_basket_2:
        fruit_basket_general.append(fruit)
print(fruit_basket_general)









