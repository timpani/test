import mpmath as mp

# Set high precision (in decimal digits)
mp.mp.dps = 100  # 100 decimal places

value = mp.tan(mp.mpf('1e100'))
print(value)
