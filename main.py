from collections import UserDict

class PhoneValueError(Exception):
    ...


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self): 
        return str(self.value)

class Name(Field):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

class Phone(Field):
    def __init__ (self, phone: str) -> str:
        if not all([len(phone) == 10 and phone.isdigit()]):
            raise ValueError ("Please enter phone number in 10 digit format")
        self.value = phone

    def __repr__ (self) -> str:
        return self.value

    def __str__ (self) -> str:
        return f"{self.value}"



class Record:
    def __init__(self, name: str, phone=None) -> list:
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    def add_phone(self, phone: str) -> list:
        new_phone = Phone(phone)
        # print(new_phone)
        # print(self.phones)
        if not self.phones:
            self.phones.append(new_phone)
        else:
            for ph in self.phones:
                if new_phone.value == ph.value:
                    raise ValueError("This phone number in list")
                else:
                    return self.phones.append(new_phone)
         
    def edit_phone(self, phone: str, new_phone: str) -> str:
        if phone != None:
            old_phone = Phone(phone)
            new_phone = Phone(new_phone)
            print(self.phones)
            for ph in self.phones:
                print(self.phones.index(ph))
                if old_phone.value == ph.value:
                    self.phones[self.phones.index(ph)] = new_phone
                    return f"Phone {old_phone} changed to {new_phone}"
                    break
        raise ValueError("This phone number is not in list")
        
    def remove_phone(self, phone: str) -> str:
        rem_phone = Phone(phone)
        # if phone in self.phones:
        #     self.phones.remove(phone)
        #     return f"Phone number {phone} removed"
        # else:
        #     raise PhoneValueError("Phone number not in list")
        for ph in self.phones:
            if rem_phone.value == ph.value:
                self.phones.remove(ph)
                return f"Phone {rem_phone} has been removed"
                break
        raise PhoneValueError("This phone number is not in list")

    def find_phone(self, phone: str):
        phone_to_find = Phone(phone)
        if phone:
            for ph in self.phones:
                if phone_to_find.value == ph.value:
                    return Phone(phone)
        else:
            raise ValueError("No phone to find")

    def __str__(self):
        return f"Contact name: {self.name.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}        

    def add_record(self, record: Record):
        self.data[record.name.name] = record
        print("Record added")
        return

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print("Record not found")

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            print("Record not found")        

if __name__ == "__main__":
    # UserIvan = Record("Ivan")
    # UserIvan.add_phone("7777777777")
    # print(UserIvan)
    # UserIvan.add_phone("2222222222")
    # print(UserIvan)
    # UserIvan.edit_phone("2222222222", "1111111111")
    # print(UserIvan)
    # # UserIvan.remove_phone("1111111111")
    # # print(UserIvan)

    # book = AddressBook()
    # book.add_record(UserIvan)
    # print(str(book))

    # UserAndrey = Record("Andrey")
    # UserAndrey.add_phone("1212121212")
    # book.add_record(UserAndrey)
    # print(book)

    # for name, record in book.data.items():
    #     print(record)

    # john = book.find("Andrey")
    # print(john)

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")