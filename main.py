from itertools import product, permutations

def apply_operations(nums, ops):
    # Apply mathematical operations to list of numbers
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i+1]
        elif ops[i] == '-':
            result -= nums[i+1]
        elif ops[i] == '*':
            result *= nums[i+1]
        elif ops[i] == '/':
            if nums[i+1] != 0:
                result /= nums[i+1]
            else:
                return None
        elif ops[i] == '^':
            result **= nums[i+1]
    return result

def find_operations(nums, goal):
    # Find mathematical operations that yield the goal output number
    for i in range(1, len(nums)+1):
        for comb in permutations(nums, i):
            for ops in product('+-*/^', repeat=i-1):
                result = apply_operations([*comb], ops)
                if result is not None and result == goal:
                    return ops, comb
    return None

# Example usage

# getting numbers for the game
input = input("Enter numbers: ")
input_nums = input.split(" ")
nums = []
for i in input_nums:
    nums.append(int(i)) 
  
loops = 1
while loops < 101:
  goal = loops
  result = find_operations(nums, goal)
  if result is not None:
    ops, comb = result
    if len(comb) == 1:
        print(f"{goal:>3}: {comb[0]}")
    else:
        outpt = ''
        print_ops = ops + (" ",)
        for i in range(len(comb)):
          if i == 0:
            outpt += f"{str(comb[i])}{str(print_ops[i])}"
          else:
            outpt += f"{str(comb[i])}){str(print_ops[i])}" 
        print(f"{goal:>3}: {('(' * len(ops))}{outpt}")
  else:
    print(f"{goal:>3}: ")
  loops += 1
