import tkinter
import tkinter.messagebox


class Order_Pizza:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("700x500")
        self.main_window.title("Pizza Order")
        self.main_window.configure(bg ="Blue")

        self.name_frame = tkinter.Frame(self.main_window,bg = "Blue")
        self.middle_frame = tkinter.Frame(self.main_window,bg = "Blue")
        self.bottom_frame = tkinter.Frame(self.main_window,bg = "Blue")


        self.prompt_label = tkinter.Label(self.name_frame, text = "Enter Customer Full Name: ",bg = "Red",fg = "White", font = ("Times New Roman",12))
        self.Toppings_Label = tkinter.Label(self.middle_frame,text = "Toppings: ",bg= "Red",fg = "White",font = ("Times New Roman",12))
        self.Crusts_Label = tkinter.Label(self.bottom_frame,text = "Type of Crust: ",bg= "Red",fg = "White",font = ("Times New Roman",12))
        self.Customer_Entry = tkinter.Entry(self.name_frame, width = 60)

        self.prompt_label.pack(side = "left")
        self.Customer_Entry.pack(side = "right")
        self.Toppings_Label.pack(side = "left")
        self.Crusts_Label.pack(side = "left")

#########################################################################################################################

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.toppings4_var = tkinter.IntVar()
        self.toppings5_var = tkinter.IntVar()
        self.toppings6_var = tkinter.IntVar()
        self.toppings7_var = tkinter.IntVar()
        self.toppings8_var = tkinter.IntVar()

        self.radio_var = tkinter.IntVar()


#########################################################################################################################

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.toppings4_var.set(0)
        self.toppings5_var.set(0)
        self.toppings6_var.set(0)
        self.toppings7_var.set(0)
        self.toppings8_var.set(0)

        self.cb1 = tkinter.Checkbutton(self.middle_frame, text = "Pepperoni", variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.middle_frame, text = "Ham", variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.middle_frame, text = "Pineapples", variable = self.cb_var3)
        self.toppings4 = tkinter.Checkbutton(self.middle_frame, text = "Tomatos", variable = self.toppings4_var)
        self.toppings5 = tkinter.Checkbutton(self.middle_frame, text = "Olives", variable = self.toppings5_var)
        self.toppings6 = tkinter.Checkbutton(self.middle_frame, text = "Green Peppers", variable=self.toppings6_var)
        self.toppings7 = tkinter.Checkbutton(self.middle_frame, text = "Spinach", variable = self.toppings7_var)
        self.toppings8 = tkinter.Checkbutton(self.middle_frame, text = "Onions", variable = self.toppings8_var)

        self.rb1 = tkinter.Radiobutton(self.bottom_frame, text = "Thick/Regular", variable = self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.bottom_frame, text = "Thin", variable = self.radio_var,value = 2)
        self.rb3 = tkinter.Radiobutton(self.bottom_frame, text = "Brooklyn Style", variable = self.radio_var,value = 3)
        self.rb4 = tkinter.Radiobutton(self.bottom_frame, text = "Pan Style", variable = self.radio_var,value = 4)
        self.rb5 = tkinter.Radiobutton(self.bottom_frame, text = "Gluten Free", variable = self.radio_var,value = 5)


#########################################################################################################################        
        
        self.cb1.pack(side = "left")
        self.cb2.pack(side = "left")
        self.cb3.pack(side = "left")
        self.toppings4.pack(side = "left")
        self.toppings5.pack(side = "left")
        self.toppings6.pack(side = "left")
        self.toppings7.pack(side = "left")
        self.toppings8.pack(side = "left")

        self.rb1.pack(side = "left")
        self.rb2.pack(side = "left")
        self.rb3.pack(side = "left")
        self.rb4.pack(side = "left")
        self.rb5.pack(side = "left")




        self.Calculation_Button = tkinter.Button(self.main_window, text = "Calculate", command = self.calc)

        self.Quit_Button = tkinter.Button(self.main_window, text = "Quit", command = self.main_window.destroy)

        self.name_frame.pack(side = "top")
        self.middle_frame.pack(side = "top")
        self.bottom_frame.pack(side = "top")

        
        self.Quit_Button.pack(side = "bottom")
        self.Calculation_Button.pack(side = "bottom")

        tkinter.mainloop()

#########################################################################################################################

    def calc(self):
        self.message = "Pizza Toppings & Crust selected:   \n"
        self.total = 0

        if self.cb_var1.get() == 1:
             self.message += 'Pepperoni \n'
             self.total += 8

        if self.cb_var2.get() == 1:
            self.message += 'Ham \n'
            self.total += 8

        if self.cb_var3.get() == 1:
            self.message += 'Pineapples \n'
            self.total += 5

        if self.toppings4_var.get() == 1:
            self.message += 'Tomatoes \n'
            self.total += 3

        if self.toppings5_var.get() == 1:
            self.message += 'Olives \n'
            self.total += 3

        if self.toppings6_var.get() == 1:
            self.message += 'Green Peppers \n'
            self.total += 3

        if self.toppings7_var.get() == 1:
           self.message += 'Spinach \n'
           self.total += 3

        if self.toppings8_var.get() == 1:
           self.message += 'Onions \n'
           self.total += 3

        if self.radio_var.get() == 1:
            self.message += 'Thick/Regular \n'
            self.total += 0

        if self.radio_var.get() == 2:
            self.message += 'Thin \n '
            self.total += 1

        if self.radio_var.get() == 3:
            self.message += 'Brooklyn Style \n '
            self.total += 2

        if self.radio_var.get() == 4:
            self.message += 'Pan Style \n '
            self.total += 3

        if self.radio_var.get() == 5:
            self.message += 'Gluten Free \n '
            self.total += 5

           
        tkinter.messagebox.showinfo("Order Receipt",self.message + "\n" + "Customer Name: " + self.Customer_Entry.get() + "\n"  + "Total Cost: $" + str(self.total))

customer_order = Order_Pizza()