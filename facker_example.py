from faker import Faker

fake = Faker("ru_RU")
print()
print(fake.name())
print(fake.address())
print(fake.email(domain="yandex.ru"))
