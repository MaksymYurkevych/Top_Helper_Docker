from collections import UserDict
from datetime import datetime
from pretty_tables import ABview
from abstract_class import ShowRecords
import pickle
import re


class Field:
    """Parent class for all fields"""

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value

    def __repr__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    """Required field with username"""
    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)

    @Field.value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    """Optional field with phone numbers"""

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @Field.value.setter
    def value(self, value):
        if len(value) != 12:
            raise ValueError("Phone must contains 12 symbols.")
        if not value.startswith('380'):
            raise ValueError("Phone must starts from '380'.")
        if not value.isnumeric():
            raise ValueError("Phone number must include digits only.")
        self._value = value


class Birthday(Field):
    """Creating 'birthday' fields"""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        today = datetime.now().date()
        try:
            value = datetime.strptime(value, "%d-%m-%Y").date()
        except:
            raise ValueError("Birthday must be in a format 'DD-MM-YYYY'")
        if value > today:
            raise ValueError("Birthday can't be bigger than current date.")
        self._value = value


class Email(Field):
    """Creating 'email fields'"""

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not re.findall(r"\b[A-Za-z][\w+.]+@\w+[.][a-z]{2,3}", value):
            raise ValueError('Wrong format. Example: "mymail@gmail.com"')
        self._value = value


class Record:
    """Class for add, remove, change fields"""

    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None, email: Email = None):

        self.birthday = birthday
        self.email = email
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)
        return f"Phone {phone} was added successfully"

    def change(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                return f"Phone {old_phone} was successfully changed to {new_phone}"
            return f"Phone number '{old_phone}' was not found in the record"

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def add_email(self, email: Email):
        self.email = email

    def days_to_birthday(self):

        cur_date = datetime.now().date()
        cur_year = cur_date.year

        if self.birthday:
            bd = self.birthday.value
            this_year_bd = bd.replace(year=cur_year)
            delta = (this_year_bd - cur_date).days
            if delta > 0:
                return f"{self.name}'s birthday will be in {delta} days"
            else:
                next_year_bd = this_year_bd.replace(year=cur_year + 1)
                delta = (next_year_bd - cur_date).days
                return f"{self.name}'s birthday will be in {delta} days"
        else:
            return f"{self.name}'s birthday is unknown"

    def remove_phone(self, phone):
        phone = Phone(phone)
        for ph in self.phones:
            if ph.value == phone.value:
                self.phones.remove(ph)
                return f"Phone {ph} was successfully removed from {self.name}"
        return f"Number {phone} not found"


class AddressBook(UserDict, ShowRecords):
    """Class for creating address book"""

    def __init__(self):
        super().__init__()
        self.pt = ABview()

    def open_file(self):
        with open('AddressBook.txt', 'rb') as open_file:
            self.data = pickle.load(open_file)
        return self.data

    def write_file(self):
        with open('AddressBook.txt', 'wb') as write_file:
            pickle.dump(self.data, write_file)

    def search_in_file(self, data):
        result = []
        for record in self.data.values():
            if record in self.data.values():
                if str(data).lower() in str(record.name).lower():
                    result.append([record.name, record.birthday, record.email, ", ".join(ph.value for ph in record.phones)])
                else:
                    for phone in record.phones:
                        if str(data).lower() in str(phone):
                            result.append([record.name, record.birthday, record.email, ", ".join(ph.value for ph in record.phones)])
            else:
                continue
        return self.pt.create_table(result)

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def show_one_record(self, name):
        result = [name, self.data[name].birthday, self.data[name].email, ", ".join(str(ph.value) for ph in self.data[name].phones)]
        return self.pt.create_row(result)

    def show_all_records(self):
        result = []
        for rec in self.data.values():
            result.append([rec.name, rec.birthday, rec.email, ", ".join([ph.value for ph in rec.phones])])
        return self.pt.create_table(result)

    def change_record(self, username, old_n, new_n):
        record = self.data.get(username)
        if record:
            record.change(old_n, new_n)

    def iterator(self, n):
        records = list(self.data.keys())
        records_num = len(records)
        count = 0
        result = []
        if n > records_num:
            n = records_num
        for rec in self.data.values():
            if count < n:
                result.append([rec.name, rec.birthday, rec.email, ", ".join([ph.value for ph in rec.phones])])
                count += 1
        yield self.pt.create_table(result)


ADDRESSBOOK = AddressBook()
