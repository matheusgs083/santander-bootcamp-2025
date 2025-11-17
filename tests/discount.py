def calculate_final_value(weight, price, client_type):
    if client_type in client_types:
        discount = client_types[client_type]
    else:
        raise ValueError(f"Invalid client type: '{client_type}'")    

    value_with_discount = price * (1 - discount)

    final_value = value_with_discount * weight

    return final_value

client_types = {"cliente novo": 0, "cliente premium": 0.10, "cliente fidelizado": 0.05}

cargo_weight = float(input())
cargo_price = float(input())
client_type = input().lower()

amount_to_pay = calculate_final_value(cargo_weight, cargo_price, client_type)

print(f"{amount_to_pay:.2f}")
