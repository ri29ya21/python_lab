
# Program 10: In-Memory Inventory Tracker with Dictionary Merging

def display_inventory(inventory, store_name):
    print(f"\n{store_name} Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")


def main():
    # Input inventory for Store 1
    store1 = {}
    n1 = int(input("Enter number of items in Store 1: "))

    for i in range(n1):
        item = input(f"Enter item {i + 1} name: ").strip()
        quantity = int(input(f"Enter quantity of {item}: "))
        store1[item] = store1.get(item, 0) + quantity

    # Input inventory for Store 2
    store2 = {}
    n2 = int(input("\nEnter number of items in Store 2: "))

    for i in range(n2):
        item = input(f"Enter item {i + 1} name: ").strip()
        quantity = int(input(f"Enter quantity of {item}: "))
        store2[item] = store2.get(item, 0) + quantity

    # Display individual inventories
    display_inventory(store1, "Store 1")
    display_inventory(store2, "Store 2")

    # Merge both inventories by adding quantities
    merged_inventory = store1.copy()

    for item, quantity in store2.items():
        merged_inventory[item] = (
            merged_inventory.get(item, 0) + quantity
        )

    display_inventory(merged_inventory, "Merged")

    # Search for an item
    search_item = input("\nEnter item name to search: ").strip()

    if search_item in merged_inventory:
        print(
            f"Total stock of {search_item}: "
            f"{merged_inventory[search_item]}"
        )
    else:
        print(f"{search_item} is not available in inventory.")

    # Update stock
    update_item = input("\nEnter item name to update: ").strip()
    new_quantity = int(input("Enter quantity to add: "))

    merged_inventory[update_item] = (
        merged_inventory.get(update_item, 0) + new_quantity
    )

    print("\nInventory after updating stock:")
    display_inventory(merged_inventory, "Updated")


if __name__ == "__main__":
    main()