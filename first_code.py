# تعریف دیکشنری با یک مقدار مشخص برای ذخیره اطلاعات مخاطب‌ها
phone_book = {
  "sara": ["09011111111"]
}

# منوی اصلی برنامه
menu_text = """
---booklet---
1- Add contact
2- Add number to contact
3- Search for a phone number by name
4- Delete contact
5- Number of contacts
6- Exit
"""

# حلقه بی‌نهایت برای اجرای برنامه
while True:
  # دریافت ورودی از کاربر
  user_choice = input(menu_text)

  # بررسی دستور خروج از برنامه
  if user_choice == "6" or user_choice == "":
    print("Goodbye")
    break

  # ایجاد متغیر برای مدیریت پیام نتیجه
  result_message = ""

  # پیاده‌ سازی گزینه افزودن مخاطب
  if user_choice == "1":
    name = input("Enter the contact's name: ")
    if name in phone_book:
      result_message = "A contact with this name already exists"
    else:
      number = input("Enter the phone number: ")
      phone_book[name] = [number]
      result_message = "Contact successfully added."
 
 # پیاده سازی گزینه افزودن شماره به مخاطب 
  elif user_choice == "2":
    name = input("Enter the contact's name: ")
    if name not in phone_book:
      result_message = "No contact found with this name"
    else:
      number = input("Enter the new number: ")
      phone_book[name].append(number)
      result_message = "A new number has been added."

  # پیاده سازی گزینه جستجوی شماره تلفن با اسم
  elif user_choice == "3":
    name = input("Enter the contact's name: ")
    if name in phone_book:
      result_message = str(phone_book[name])
    else:
      result_message = "No contact found with this name"

  # پیاده سازی گزینه حذف مخاطب
  elif user_choice == "4":
    name = input("Enter the contact's name: ")
    if name in phone_book:
      del phone_book[name]
      result_message = "The contact has been deleted"
    else:
      result_message = "No contact found with this name"

  # پیاده سازی گزینه نمایش تعداد مخاطب‌ها
  elif user_choice == "5":
     result_message =  "Number of contacts:" + str(len(phone_book)) + " "

  # مدیریت کردن ورودی نامعتبر
  else:
    result_message = "The input must be a value between 1 and 6."

  # اضافه کردن پرسش به رشته نتیجه و جداسازی دو پیام با علامت خط تیره
  result_message = result_message + " " + "Do you want to continue?(Yes/No) - "
  
  # نمایش نتیجه و پرسش برای تمایل به ادامه دادن
  cont = input(result_message)
  if cont == "No" or cont == "":
    print("Goodbye")
    break  