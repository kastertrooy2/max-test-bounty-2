def calculate_reward(amount):
    bonus = 10
    total = amount + bonus
    return total

print("Система расчета вознаграждения запущена...")
result = calculate_reward(50)
print(f"Итоговая сумма: {result}")
