def fibonacci_succession(succession_length):
  fibonacci = [0, 1]
  for i in fibonacci:
    print(','.join(str(x) for x in fibonacci))
    fibonacci_length = len(fibonacci)
    if fibonacci_length <= succession_length:
      last = fibonacci[-1]
      penultimate = fibonacci[-2]
      succession = last + penultimate
      fibonacci.append(succession)
    else:
      break
    
fibonacci_succession(20)