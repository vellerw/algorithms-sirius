# F. Прыжки по лестнице

# Алла хочет доказать, что она умеет прыгать вверх по лестнице быстрее всех. 
# На этот раз соревнования будут проходить на специальной прыгательной лестнице. 
# С каждой её ступеньки можно прыгнуть вверх на любое расстояние от 1 до k. Число k придумывает Алла.

# Гоша не хочет проиграть, поэтому просит вас посчитать количество способов 
# допрыгать от первой ступеньки до n-й. Изначально все стоят на первой ступеньке.

# Формат ввода
# В единственной строке даны два числа — n и k (1 ≤ n ≤ 1000, 1 ≤ k ≤ n).

# Формат вывода
# Выведите количество способов по модулю 10 в 9 + 7.

# Пример 1
# Ввод: 6 3
# Вывод: 13

# Пример 2
# Ввод: 7 7
# Вывод: 32

def alla(n, k=2):
    dp = [0] * (max(n, k)+1)
    dp[0] = 0
    for i in range(k):
        dp[i+1] = 2**i
    
    q = 10**9 +7
    print(f'q: {q}')
    if n <= k:
        return dp[n-1] % q
    for i in range(k+1, n):
        for j in range(1, k+1):
            print(f'j:{j}')
            dp[i] += dp[i - j]
        
    print(dp)
    return dp[n-1] % q
    
    
    
def test(result, expected):
    if result != expected:
        print(f'error: {result} != {expected}')
    else:
        print("OK!")
        
        
# test(alla(1), 1)
# test(alla(2), 2)
# test(alla(3), 3)
# test(alla(4), 5)
# test(alla(5), 8)

test(alla(6, 3), 13)
test(alla(7, 7), 32)
test(alla(2, 2), 1)
test(alla(79, 34), 470472762)

# Пример 3
# Ввод: 2 2
# Вывод: 1
