# Function
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated cost for " + name + " is " + str(estimated_cost) + " dollars")
  return(estimated_cost)

# Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

# My insurance cost
joan_insurance_cost = calculate_insurance_cost("Joan", 18, 1, 24.9, 0, 0)
