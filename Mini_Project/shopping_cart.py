cart=[]
while True:
    item=input("Enter an item(or type 'done' to finish): ")
    if item.lower()=="done":
        break
    cart.append(item)
print(f"\nTotal number of items in cart: {len(cart)}")
print("Items in cart:",sorted(cart))
remove_choice=input("Do you want to remove any item?(yes/No):")
if remove_choice=="yes":
    to_remove=input("Enter item to remove: ")
    if to_remove in cart:
        cart.remove(to_remove)
        print(f"{to_remove} removed from cart.")
    else:
        print(f"{to_remove} not found in cart.")
print("Final cart:", cart)