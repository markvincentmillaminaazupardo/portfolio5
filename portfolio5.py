# Portfolio 5: My Canteen Order Checker

# **Description:**
# A simple program I made using string methods to clean up and check my lunch order.

# A messy string of what I usually order for lunch
my_lunch_order = "   Spicy Bicol Express with Extra Rice   "

# 1. Use strip() to clean the extra spaces at the beginning and end
clean_order = my_lunch_order.strip()

# 2. Use upper() to capitalize everything so it looks like a printed canteen receipt
receipt_text = clean_order.upper()

# Display the cleaned up string
print("Processing Order:", receipt_text)

# 3. Use the 'in' operator to check if my order contains a specific word
if 'SPICY' in receipt_text:
    print("Warning: This meal is going to be hot. Buy extra water!")
    
    # 4. Use replace() to swap out a word if I decide I want a milder lunch today
    new_order = receipt_text.replace('SPICY', 'MILD')
    print("Changed my mind. Updated Order:", new_order)
else:
    print("Order looks good and safe to eat. Enjoy!")
