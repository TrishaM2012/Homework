class animal:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
dog_1 = animal('golden retriever', 'golden')
dog_2 = animal('husky', 'white')

print("The first dog is a", dog_1.breed, "and has a", dog_1.color,"color.")
print("The second dog is a", dog_2.breed, "and has a", dog_2.color,"color.")


    

