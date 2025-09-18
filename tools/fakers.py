from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.middle_name()

    def integer(self, start: int, end: int) -> int:
        return self.faker.random_int(min=start, max=end)

    def estimated_time(self) -> str:
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        return self.integer(50, 100)

    def min_score(self) -> int:
        return self.integer(1, 49)


fake = Fake(Faker("ru_RU"))
