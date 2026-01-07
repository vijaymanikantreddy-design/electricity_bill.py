def calculate_bill(units: int) -> float:
    """
    Calculate electricity bill based on tiered pricing.
    Includes a fixed charge of $50.
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    bill = 50  # fixed charge

    if units <= 100:
        bill += units * 1.50
    elif units <= 200:
        bill += (100 * 1.50) + (units - 100) * 2.50
    elif units <= 300:
        bill += (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        bill += (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00

    return bill


if __name__ == "__main__":
    try:
        units = int(input("Enter total units consumed: "))
        total_bill = calculate_bill(units)
        print(f"Total Units: {units}")
        print(f"Total Bill: ${total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")