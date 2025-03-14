from google.protobuf.json_format import MessageToDict

import addressbook_pb2
import sys

# def PromptForAddress(person):
#     person.id= int(input("Enter person Id number:"))
#     person.name=input("Enter person's name:")
#     email=input("Enter person's email address(blank for none):")
#     if email !="":
#         person.email=email
#     while True:
#         number=input("Enter a phone number")
#         if number=="":
#             break
#
#         phone_number= person.phones.add()
#         phone_number.number= number
#         phone_type=input("Is this a mobile,home or work phone?")
#         if phone_type=="home":
#             phone_number.type= addressbook_pb2.Person.PhoneType.PHONE_TYPE_HOME
#         elif phone_type=="work":
#             phone_number.type= addressbook_pb2.Person.PhoneType.PHONE_TYPE_WORK
#         elif phone_type=="mobile":
#             phone_number.type= addressbook_pb2.Person.PhoneType.PHONE_TYPE_MOBILE
#         else:
#             print("Unknown phone type")
# if len(sys.argv) !=2:
#     print("Usage:",sys.argv[0],"ADDRESS_BOOK_FILE")
#     sys.exit(-1)
#
# address_book = addressbook_pb2.AddressBook()
#
# try:
#     with open(sys.argv[1],"rb") as f :
#         address_book.ParseFromString(f.read())
# except IOError:
#     print(sys.argv[1]+": Could not open file. Creating  a new one.")
#
# PromptForAddress(address_book.person.add())
# with open(sys.argv[1],"wb") as f :
#     f.write(address_book.SerializeToString())
person=addressbook_pb2.Person()
person.id=1234
person.name="GiSon Win"
person.email="gisonwin@qq.com"

phone_list = person.phones
print(type(phone_list))
phone_number=person.phones.add()
phone_number.number="555-5555-5"
phone_number.type=addressbook_pb2.Person.PHONE_TYPE_HOME

phone_number1=person.phones.add()
phone_number1.number="755-5666-5"
phone_number1.type=addressbook_pb2.Person.PHONE_TYPE_WORK

d=MessageToDict(person)
print(d)
serialized_person = person.SerializeToString()
print(serialized_person)

new_person = addressbook_pb2.Person()
new_person.ParseFromString(serialized_person)
print(new_person)