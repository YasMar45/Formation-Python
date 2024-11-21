pen_price = 0.30
discount = float

pen_quantity = input("Entrez la quantité de crayon que vous voulez acheter: " )
pen_quantity = int(pen_quantity)

if pen_quantity <= 0:
    print("Veuillez rentrer un nombre valide !")

elif 0 < pen_quantity <= 10:
    discount = 0.0

elif 10 <= pen_quantity >= 25:
    discount = 0.05

elif 25 <= pen_quantity >= 50:
    discount = 0.10

elif 50 <= pen_quantity >= 100:
    discount = 0.15

elif pen_quantity > 100:
    discount = 0.20

print(f"{(pen_price*(1-discount))* pen_quantity}")