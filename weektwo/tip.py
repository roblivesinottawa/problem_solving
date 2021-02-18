def calculate_tip(bill, tip):
    return (bill + tip ) / 2


bill = 47.28
tip = bill * 0.15

share = calculate_tip(bill, tip)
print(f"each person needs to pay {str(share)}")