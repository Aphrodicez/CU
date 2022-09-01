def peaks(x):
  return [int(i) for i in range(1, len(x) - 1) if x[i] > max(x[i - 1], x[i + 1])]
  
exec(input())