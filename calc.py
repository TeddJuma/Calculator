import tkinter as tk

class MyGUI:
    def __init__(self):
        """
        The constructor for the MyGUI class.
        It sets up the main window and its properties.
        It then creates a label and a text box and assigns them to the window.
        It binds the key press event to the textbox and the arrow key press event to the root window.
        It then calls the keypad method to create the keypad buttons and finally starts the main event loop of the window.
        """
        self.root= tk.Tk()
        
        self.root.title("Calculator.py")
        self.root.geometry("500x600")
        
        self.label =tk.Label(self.root,text = "CALCULATOR", font =('Arial',18))
        self.label.pack(padx=10,pady=10)
        
        self.textbox = tk.Text(self.root, height=2,font=('Arial',16))
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(padx=10,pady=10)
        
        self.num = "" # Represents the number currently being entered.
        self.work_load = [] # This is where the arithmetic operations will be represented as a list, in preparation for being operated on.
        self.result_status = 0 # Value Used to check the history of operations. 0 = "No Previous History", 1 = "1 Previous History".
        
        self.root.bind_all('<Key>',self.keyPress)
        
        self.keypad()
        self.root.mainloop()
      
    def keypad(self):
        '''
        Creates the keypad for the calculator application.
        This method sets up a grid of buttons within a frame for the calculator.
        Each button is assigned a command that either inserts a number or operation
        into the calculator's textbox or performs a specific function such as delete
        or calculate the result. 
        The buttons are organized into a grid layout to
        mimic a traditional calculator keypad.
        '''
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.columnconfigure(1,weight=1)
        self.buttonFrame.columnconfigure(2,weight=1)
        self.buttonFrame.columnconfigure(3,weight=1)
        
        self.btn_del = tk.Button(self.buttonFrame,text="DEL",bg="grey", font=('Arial',18),command=self.delete)
        self.btn_del.grid(row=0,column=0, sticky=tk.W+tk.E)
        
        self.btn_root = tk.Button(self.buttonFrame,text="x^1/2",bg="grey", font=('Arial',18), command=lambda: self.insert_op("^1/2"))
        self.btn_root.grid(row=0,column=1, sticky=tk.W+tk.E)
        
        self.btn_square = tk.Button(self.buttonFrame,text="x^2",bg="grey", font=('Arial',18), command=lambda: self.insert_op("^2"))
        self.btn_square.grid(row=0,column=2, sticky=tk.W+tk.E)

        self.btn_plus = tk.Button(self.buttonFrame,text="+",bg="grey", font=('Arial',18), command=lambda: self.insert_op(" + "))
        self.btn_plus.grid(row=0,column=3, sticky=tk.W+tk.E)
        
        self.btn_1 = tk.Button(self.buttonFrame,text="1", font=('Arial',18), command=lambda: self.insert_text("1"))
        self.btn_1.grid(row=1,column=0, sticky=tk.W+tk.E)
        
        self.btn_2 = tk.Button(self.buttonFrame,text="2", font=('Arial',18), command=lambda: self.insert_text("2"))
        self.btn_2.grid(row=1,column=1, sticky=tk.W+tk.E)
        
        self.btn_3 = tk.Button(self.buttonFrame,text="3", font=('Arial',18), command=lambda: self.insert_text("3"))
        self.btn_3.grid(row=1,column=2, sticky=tk.W+tk.E)
        
        self.btn_minus = tk.Button(self.buttonFrame,text="-",bg="grey", font=('Arial',18), command=lambda: self.insert_op(" - "))
        self.btn_minus.grid(row=1,column=3, sticky=tk.W+tk.E)
        
        self.btn_4 = tk.Button(self.buttonFrame,text="4", font=('Arial',18), command=lambda: self.insert_text("4"))
        self.btn_4.grid(row=2,column=0, sticky=tk.W+tk.E)
        
        self.btn_5 = tk.Button(self.buttonFrame,text="5", font=('Arial',18), command=lambda: self.insert_text("5"))
        self.btn_5.grid(row=2,column=1, sticky=tk.W+tk.E)
        
        self.btn_6 = tk.Button(self.buttonFrame,text="6", font=('Arial',18), command=lambda: self.insert_text("6"))
        self.btn_6.grid(row=2,column=2, sticky=tk.W+tk.E)
        
        self.btn_mult = tk.Button(self.buttonFrame,text="x",bg="grey", font=('Arial',18), command=lambda: self.insert_op(" x "))
        self.btn_mult.grid(row=2,column=3, sticky=tk.W+tk.E)
        
        self.btn_7 = tk.Button(self.buttonFrame,text="7", font=('Arial',18), command=lambda: self.insert_text("7"))
        self.btn_7.grid(row=3,column=0, sticky=tk.W+tk.E)
        
        self.btn_8 = tk.Button(self.buttonFrame,text="8", font=('Arial',18), command=lambda: self.insert_text("8"))
        self.btn_8.grid(row=3,column=1, sticky=tk.W+tk.E)
        
        self.btn_9 = tk.Button(self.buttonFrame,text="9", font=('Arial',18), command=lambda: self.insert_text("9"))
        self.btn_9.grid(row=3,column=2, sticky=tk.W+tk.E)
        
        self.btn_div = tk.Button(self.buttonFrame,text="/",bg="grey", font=('Arial',18), command=lambda: self.insert_op(" / "))
        self.btn_div.grid(row=3,column=3, sticky=tk.W+tk.E)
        
        self.btn_point = tk.Button(self.buttonFrame,text=".", font=('Arial',18), command=lambda: self.insert_text("."))
        self.btn_point.grid(row=4,column=0, sticky=tk.W+tk.E)
        
        self.btn_0 = tk.Button(self.buttonFrame,text="0", font=('Arial',18), command=lambda: self.insert_text("0"))
        self.btn_0.grid(row=4,column=1, sticky=tk.W+tk.E)
        
        self.btn_equals = tk.Button(self.buttonFrame,text="=", font=('Arial',18), command= self.result)
        self.btn_equals.grid(row=4,column=2, sticky=tk.W+tk.E)
        
        self.buttonFrame.pack(fill="x",padx=50,pady=20)
  
    def delete(self):
        '''Deletes all the text in the text box, and resets the number to an empty string and work_load to an empty list.'''
        self.textbox.delete('1.0',tk.END)
        self.num = ""
        self.work_load = []
        
    def insert_text(self, key):
        """
        Inserts a number into the text box and updates the current number being entered.
        If the result status is 1, it clears the text box and resets the number to an empty string and work_load to an empty list.
        """
        if self.result_status == 1:
            self.textbox.delete('1.0',tk.END)
            self.textbox.insert(tk.END, key)
            self.num = self.num + key
            print(self.num)
            self.result_status = 0
            self.work_load = []
        else:
            self.textbox.insert(tk.END, key)
            self.num = self.num + key
            print(self.num)

    def back_space(self):
        """Deletes the last character from the text box."""
        self.textbox.delete('end-1c','end')
        
    def insert_op(self,key):
        """Inserts an operator into the text box and also updates it the work_load.
        Converts the current number to a float or int.
        Adds the converted number to the work_load
        Reset the current number to be entered to an empty string."""
        self.textbox.insert(tk.END, key)
        self.work_load.append(self.num_conv(self.num))
        self.work_load.append(key)
        self.num = ""
        print(self.work_load) 
        
    def num_conv(self,num):
        """
        Converts a number to a float or int based on if the number contains a decimal point.
        Args:
            num (str): The number to be converted.
        Returns:
            float or int: The converted number.
        """
        self.num =num
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        return num
            
    def result(self):
        # Inserting the latest digit into the work-load
        """
        Calculates the result of an arithmetic expression stored in the work_load list.
        
        This method processes arithmetic operations in the following order of precedence:
        division, multiplication, addition, and subtraction. 
        It iterates over the work_load list, performing the operations based on the operator found, and 
        updates the list until only the final result remains. 
        
        The method then updates the final_results attribute with the result and displays it in the textbox.

        The method also resets the current number being entered and sets the result status
        to indicate that a previous history of calculation exists.
        """
        self.work_load.append(self.num_conv(self.num))
        print("\n\nInitialization: ",self.work_load, '\n')
        self.num = ""
        
        '''DIVISION'''
        while ' / ' in self.work_load:
            print("Starting on Division...", f"\n{self.work_load}")
            # getting the position of the operand.
            self.sign_pos = self.work_load.index(' / ')
                
            self.res = self.work_load[self.sign_pos-1] / self.work_load[self.sign_pos+1]
            
            # Removing the used figures and operands from the work-load.
            self.sign_pos = self.sign_pos + 1
            
            for i in range(2):
                self.work_load.remove(self.work_load[self.sign_pos])
                self.sign_pos = self.sign_pos - 1
                
            self.work_load[self.sign_pos] = self.res 
            
            print(self.work_load,'\n')
            
        '''MULTIPLICATION'''
        while ' x ' in self.work_load:
            print("Starting on Multiplication...", f"\n{self.work_load}")
            # getting the position of the operand.
            self.sign_pos = self.work_load.index(' x ')
                
            self.res = self.work_load[self.sign_pos-1] * self.work_load[self.sign_pos+1]
            
            # Removing the used figures and operands from the work-load.
            self.sign_pos = self.sign_pos + 1
            
            for i in range(2):
                self.work_load.remove(self.work_load[self.sign_pos])
                self.sign_pos = self.sign_pos - 1
                
            self.work_load[self.sign_pos] = self.res 
            
            print(self.work_load, '\n')
            
        '''ADDITION'''
        while ' + ' in self.work_load:
            print("Starting on Addition...", f"\n{self.work_load}")
            # getting the position of the operand.
            self.sign_pos = self.work_load.index(' + ')
                
            self.res = self.work_load[self.sign_pos-1] + self.work_load[self.sign_pos+1]
            
            # Removing the used figures and operands from the work-load.
            self.sign_pos = self.sign_pos + 1
            
            for i in range(2):
                self.work_load.remove(self.work_load[self.sign_pos])
                self.sign_pos = self.sign_pos - 1
                
            self.work_load[self.sign_pos] = self.res 
            
            print(self.work_load, '\n')
            
        '''SUBTRACTION'''
        while ' - ' in self.work_load:
            print("Starting on Subtraction...", f"\n{self.work_load}")
            # getting the position of the operand.
            self.sign_pos = self.work_load.index(' - ')
                
            self.res = self.work_load[self.sign_pos-1] - self.work_load[self.sign_pos+1]
            
            # Removing the used figures and operands from the work-load.
            self.sign_pos = self.sign_pos + 1
            
            for i in range(2):
                self.work_load.remove(self.work_load[self.sign_pos])
                self.sign_pos = self.sign_pos - 1
                
            self.work_load[self.sign_pos] = self.res 
            
            print(self.work_load, '\n')
           
        self.final_results = self.work_load.copy()
        self.result_status = 1
        
        print(f"Final Result = {self.final_results[0]}")
        
        self.textbox.insert( tk.END, f"\n{self.final_results[0]}")    
                
                             
    def keyPress(self,event):
        """
        Handles key press events for the calculator. 
        Inserts numbers and operators into the text box based on the key pressed.
        
        If an operator is pressed, it appends the operator to the work_load list.
        If the enter key is pressed, it calls the result method to calculate the result of the arithmetic expression stored in the work_load list.
        If the delete key is pressed, it calls the delete method to clear the text box and the work_load list.
        """
        self.nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0','.'}
        self.syms = {'/', '*', '-', '+', '\r', '\x08'}
        
        if event.char in self.nums:
            self.insert_text(event.char)
        elif event.char in self.syms:
            if event.char == '*':
                self.insert_op(' x ')
            elif event.char == '\x08':
                self.back_space()
            elif event.char == '\r':
                self.result()
            else:
                self.insert_op(f" {event.char} ")
                
        if event.keysym == 'Delete':
            self.delete()
    
    def shortcut(self,event):
        """
        Handles shortcut events for the calculator. 
        Prints the event object for debugging purposes.
        """
        print(event)
    
MyGUI()