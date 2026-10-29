import sys
import os
import json


def get_inventory() -> dict:
    with open(os.path.join(sys.path[0], "inventory.json")) as json_file:
        return json.load(json_file)


def add_product(
        inventory: dict, product_id: str, name: str, category: str, price: float, stock: int, variants: dict) -> bool:
    """
    Adds a product to the given inventory.
    Ensures the product ID is unique.
    Returns `True` if the product was successfully added, `False` otherwise.
    """
    if product_id in inventory:
        return False

    inventory[product_id] = {
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
        "variants": variants.copy(),
    }
    return True


def update_product(inventory: dict, product_id: str, price: float = None, variants: dict = None) -> bool:
    """
    Updates an existing product's price and/or variant stock and total stock.
    Ensures the product exists.
    Ensures the variants exist.
    Ensures the total stock matches the sum of the variants stock.
    Returns `True` if the product was successfully updated, `False` otherwise.
    """
    if product_id not in inventory:
        return False

    product = inventory[product_id]
    current_variants = product["variants"]

    if variants is not None and not set(variants).issubset(current_variants):
        return False

    if price is not None:
        product["price"] = price

    if variants is not None:
        current_variants.update(variants)
        product["stock"] = sum(current_variants.values())

    return True


def delete_product(inventory: dict, product_id: str) -> bool:
    """
    Removes a product from the inventory.
    Ensures the product exists.
    Returns `True` if the product was successfully deleted from the inventory, `False` otherwise.
    """
    if product_id not in inventory:
        return False

    del inventory[product_id]
    return True


def _read_variants() -> dict:
    variants = {}
    while input("Do you want to enter a variant (yes/no)? ").strip().lower() == "yes":
        name = input("Enter variant name: ").strip()
        stock = int(input("Enter variant stock level: "))
        variants[name] = stock
    return variants


def main() -> None:
    inventory = get_inventory()

    while True:
        print("\n[A] Add a new product")
        print("[U] Update an existing product")
        print("[D] Delete an existing product")
        print("[Q] Quit the program")
        choice = input("Choose an option: ").strip().upper()

        if choice == "A":
            product_id = input("Input product ID: ").strip()
            name = input("Input product name: ").strip()
            category = input("Input product category: ").strip()
            price = float(input("Input product price: "))
            variants = _read_variants()
            stock = sum(variants.values())

            if add_product(inventory, product_id, name, category, price, stock, variants):
                print("Product added!")
            else:
                print("Product ID already exists")

        elif choice == "U":
            product_id = input("Input product ID: ").strip()

            if product_id not in inventory:
                print("ID doesn't exist")
            else:
                price = float(input("Input product price: "))
                variants = _read_variants()

                if update_product(inventory, product_id, price, variants):
                    print("Product updated!")
                else:
                    print("Variant doesn't exist")

        elif choice == "D":
            product_id = input("Input product ID: ").strip()
            if delete_product(inventory, product_id):
                print("Product deleted!")
            else:
                print("ID doesn't exist")

        elif choice == "Q":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()