def fibonacci_succession_v1(succession_length):
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
#fibonacci_succession_v1(20)

def fibonacci_sequence_v2(sequence_length):
  fibonacci_sequence_list = [0, 1]
  
  for i in fibonacci_sequence_list:
    #print(fibonacci_sequence_list)
    
    if len(fibonacci_sequence_list) <= sequence_length:
      fs_last_number = fibonacci_sequence_list[-1]
      fs_penultimate_number = fibonacci_sequence_list[-2]
      new_value = fs_last_number + fs_penultimate_number
      fibonacci_sequence_list.append(new_value)
    else:
      break
  return fibonacci_sequence_list
#fb = fibonacci_sequence(10)
#print(fb)
 
def fibonacci_sequence_v3(sequence_length: int) -> list[int]:
  if sequence_length == 0: return []
  if sequence_length == 1: return [0]
  
  fibonacci_sequence_list = [0, 1]
  if sequence_length == 2: return fibonacci_sequence
  
  for i in range(2, sequence_length):
    new_value = fibonacci_sequence_list[-1] + fibonacci_sequence_list[-2]
    fibonacci_sequence_list.append(new_value)
      
  return fibonacci_sequence_list

fb3 = fibonacci_sequence_v3(20)
print(fb3)   