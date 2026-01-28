# To find given numbers is positive, negative, Zero
## if,elif,else are programming tools used for DECISION-MAKING.
# It executes the statements until the condition is TRUE.
# When there is more than one codition,elif is used.
#elif is used to * CHECK alternative conditons *
n = int(input("Enter a numbers: "))

if n > 0:
  print("Positive")
elif n < 0:           #elif can be multiple.
  print("Negative")
else:                # default or "catch all", runs when if and all elif are wrong.
  print("Zero")
