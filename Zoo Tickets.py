#Adult tickets = $10
#child tickets = $5
#family tickets = $26
#family tickets == 2 adult tickets + 2 child tickets

adults = int(input("Enter the no of adults : "))
children = int(input("Enter the no of children : "))

family = min((adults//2),(children//2))

adult_tickets = adults - (family*2)
child_tickets = children - (family*2)

print("Number of adult tickets : ", adult_tickets)
print("Number of child tickets : ", child_tickets)
print("Number of family ticket : ", family)

Total_Cost = (adult_tickets * 10) + (child_tickets * 5) + (family * 26)
print("Total Cost : $",Total_Cost)