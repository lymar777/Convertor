import datetime
import logging
import os
import re
from tkinter import *
import tkinter as tk




''
"Главная функция"
''
def main1():
   def multiply_values():
    try:
        num1 = float(percent_entry.get())/100
        num2 = float(money_entry.get())
        num3 = float(period_entry.get())
        result = (num1 * num2) * num3
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")
    except Exception as e:
        result_label.config(text=f"Ошибка: {e}")
   def validate_digit_input(new_value): 
        if new_value == "": 
            return True 
        elif new_value.isdigit(): 
            return True 
        else: 
            return False 
   def show_percent():

      s1x = percent_entry.get()
      print (s1x)
      return
   def show_money():

      s2x = money_entry.get()
      print (s2x)
      return 
   def show_period():

      s3x = period_entry.get()
      print (s3x)
      return
   
   window1 = Tk()
   validate_digit_command = window1.register(validate_digit_input)
   
   window1.title("Calculator")
   window1.geometry ('500x400')
   window1.resizable (False, False)

   result_label = tk.Label(window1, text="Результат: ")
   result_label.pack()

   percent_label = tk.Label(window1, text="Введите годовой %:")
   money_label = tk.Label(window1, text="Введите сумму займа:")
   period_label = tk.Label(window1, text="Введите период займа в годах:")
   group_lbl = percent_label, money_label, period_label
   print(group_lbl.__class__)
   for i in group_lbl:
      i.pack()
   
   percent_entry = tk.Entry(window1,validate="key", validatecommand=(validate_digit_command, '%P'))
   money_entry = tk.Entry(window1,validate="key", validatecommand=(validate_digit_command, '%P'))
   period_entry = tk.Entry(window1,validate="key", validatecommand=(validate_digit_command, '%P'))

   group_entry= percent_entry,money_entry,period_entry
   for i in group_entry:
      i.pack()
   
   btn1 = tk.Button(window1,text="Вывести", bg='light green', command=show_percent)
   btn2 = tk.Button(window1,text="Вывести", bg='light green', command=show_money)
   btn3 = tk.Button(window1,text="Вывести", bg='light green', command=show_period)
   btn4 = tk.Button(window1, text= "OK", bg='light blue',command=multiply_values)
   group_btn = btn1, btn2, btn3, btn4

   print(group_btn.__class__)
   for i in group_btn:
      i.pack(expand=1)

   
   


   return window1.mainloop ()
   
''
"Д"
''
def main():
      def finish():
         window.destroy()
   
      # Root -> window
      window = Tk()
      window.title ("Главное окно")
      window.geometry ('540x600')
      window.resizable (False, False)
      lbl = Label(window, text="Bombino!", font=("Arial Bold", 50))
      lbl.pack()

      btn1 = Button(width= 50, height= 3, bg='yellow', text='Калькулятор переплат', command=main1)
      btn2 = Button(width= 50, height= 3, bg='light green', text='Конвертор в рубли', command=finish)
      btn3 = Button(width= 50, height= 3, bg='light blue', text='Записная книжка', command=finish)
      btn4 = Button(width= 50, height= 3, bg='orange', text='Админка', command=finish)
      btn5 = Button(window, text="Выход", command=finish)

    # https://www.alphavantage.co/documentation/

      group_btn = btn1, btn2, btn3, btn4, btn5
      print(group_btn.__class__)
      for i in group_btn:
         i.pack(expand=1)

      return window.mainloop ()

if __name__ == '__main__':
   main()


