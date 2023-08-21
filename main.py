#!/usr/bin/env python3
from itertools import product, permutations


def apply_operations(nums, ops):
  # Apply mathematical operations to list of numbers
  result = nums[0]
  j = 0
  for i in range(len(ops)):
    if j > i:
      return result
    j += 1
    if ops[i] == '+':
      result += nums[i + 1]
    elif ops[i] == '-':
      result -= nums[i + 1]
    elif ops[i] == '*':
      result *= nums[i + 1]
    elif ops[i] == '/':
      if nums[i + 1] != 0:
        result /= nums[i + 1]
      else:
        return None
    elif ops[i] == '^':
      if result == 0 and nums[i + 1] < 0:
        break
      result **= nums[i + 1]
    elif ops[i] == '&':
      if i + 2 < len(nums):
        """
                in comes result and i
                it then takes nums[i] and does an operation using the next number
                This new total exponent is then applied to the result
                """
        exponent = nums[i + 1]
        if ops[i + 1] == '+':
          exponent += nums[i + 2]
          j += 1
          result **= exponent
        elif ops[i + 1] == '-':
          exponent -= nums[i + 2]
          j += 1
          result **= exponent
        elif ops[i + 1] == '*':
          exponent *= nums[i + 2]
          j += 1
          result **= exponent
        elif ops[i + 1] == '/':
          exponent /= nums[i + 2]
          j += 1
          if result == 0 and exponent < 0:
            break
          result **= exponent
  return result


def find_operations(nums, goal):
  # Find mathematical operations that yield the goal output number
  for i in range(1, len(nums) + 1):
    # brute force solution through every permutation and order of numbers
    for perm in permutations(nums, i):
      # brute force solution through every permutation and order of operations, with repetition allowed
      for ops in product('+-*/^&', repeat=i - 1):
        result = apply_operations([*perm], ops)
        if result is not None and result == goal:
          return ops, perm

  # if nothing found return None
  return None


# getting numbers for the game
nums_list = input("Enter numbers: ")
input_nums = nums_list.split(" ")
nums = []
for i in input_nums:
  nums.append(int(i))

# looping and outputting numbers as far as specified
loops = int(input("Furthest iteration: "))
iteration = 1

if loops == 0:
  loops = 999999999

while iteration <= loops:
  # set goal number to current iteration and get permutation of numbers and operations needed for the goal
  goal = iteration
  result = find_operations(nums, goal)

  # continue with the process if there is a solution, else just print an empty goal
  if result is not None:
    #split result into its operations and permutations
    ops, perm = result
    #if there is only one number needed, skip all the other code
    if len(perm) == 1:
      print(f"{goal:>3}: {perm[0]}")

    else:
      # initailize the output as empty before adding permutation and operations and add an empty operation so the solution looks right
      outpt = ''
      print_ops = ops + (" ", )
      num_of_exclaimations = 0
      for i in range(len(perm)):
        # if this is the first number, dont put a parenthesis between the number and operator, otherwise add the parenthesis for reading clarity
        if i == 0:
          outpt += f"{str(perm[i])}{str(print_ops[i])}"

        else:
          if print_ops[i - 1] != '&':
            reg_parenthesis = ')'
            exclaim_parenthesis = None
          else:
            reg_parenthesis = None
            exclaim_parenthesis = '('
          outpt += f"{exclaim_parenthesis or ''}{str(perm[i])}{reg_parenthesis or ''}{print_ops[i]}"
        # print the output and the goal number it satisfies
      for i in ops:
        if i == '&':
          num_of_exclaimations += 2

      print(
        f"{goal:>3}: {'(' * (len(ops)-num_of_exclaimations)}{outpt.replace('&', '^').replace('+-', '-').replace('-+', '-')}"
      )

  else:
    print(f"{goal:>3}: ")
    if loops == 999999999:
      break

  iteration += 1
