class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.next = None
        self.prev = None

class PersonQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, name, height, weight):
        new_person = Person(name, height, weight)
        if self.head is None:
            self.head = new_person
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_person
            new_person.prev = current

    def calculate_bmi_category(self, height, weight):
        bmi = weight / ((height / 100) ** 2)
        if bmi < 18.5:
            return "худой"
        elif bmi >= 18.5 and bmi < 25:
            return "нормальный"
        else:
            return "пухлый"

    def display_bmi_category(self):
        current = self.head
        while current:
            bmi_category = self.calculate_bmi_category(current.height, current.weight)
            print(f"{current.name}, ИМТ({bmi_category})")
            current = current.next



person_queue = PersonQueue()
person_queue.enqueue("Алексей", 175, 70)
person_queue.enqueue("Елена", 160, 55)
person_queue.enqueue("Иван", 180, 90)
person_queue.display_bmi_category()