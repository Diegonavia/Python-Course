print("How many kilometers did you cycle today?")
kms = float(input())
miles = float(kms)/1.60934
miles = round(miles,2)
print(f"your {kms}km ride is equal  to {miles} miles ")
#round()