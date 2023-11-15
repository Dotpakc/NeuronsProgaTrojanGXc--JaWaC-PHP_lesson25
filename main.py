from faker import Faker
from hm16 import average_grades

faker = Faker()

grades = {faker.name(): [faker.random_int(min=0, max=100) for _ in range(3)] for _ in range(10)}

print(grades)
print(average_grades(grades))
