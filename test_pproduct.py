from product import product_details

def test_product_details():
    result = product_details(101, "Laptop", 5, 45000)

    expected_output = (
        "Product ID: 101\n"
        "Product Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 45000"
    )

    assert result == expected_output 