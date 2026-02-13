# Test Cases - E-Commerce Cart

| TC ID | Scenario | Input | Expected Output |
|-------|----------|--------|----------------|
| TC01 | Add valid item | 500 | Item added |
| TC02 | Add invalid item | -100 | Invalid price |
| TC03 | Remove existing item | 500 | Item removed |
| TC04 | Calculate total | 500 + 300 | 800 |
| TC05 | Apply valid discount | 10% | Reduced total |
| TC06 | Apply invalid discount | 150% | Invalid discount |
