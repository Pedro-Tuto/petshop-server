from typing import List, Optional
from petshop.pets.models import Pet

class PetCRUD:
    def __init__(self):
        self.pets = []
        self.counter = 1

    def create_pet(self, pet: Pet) -> Pet:
        pet.id = self.counter
        self.counter += 1
        self.pets.append(pet)
        return pet


    def read_pet(self, pet_id: int) -> Optional[Pet]:
        for pet in self.pets:
            if pet.id == pet_id:
                return pet
        return None


    def delete_pet(self, pet_id: int) -> bool:
        for i, pet in enumerate(self.pets):
            if pet.id == pet_id:
                del self.pets[i]
                return True
        return False
