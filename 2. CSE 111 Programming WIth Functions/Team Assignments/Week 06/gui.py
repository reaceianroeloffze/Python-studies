import tkinter as tk
import number_entry as nent

def main():
    
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Weight")
    frm_main.pack(padx=30, pady=15, fill=tk.BOTH, expand=1)
    
    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    fill_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()
    
def fill_window(frm_main):
    
    # Create a label that displays Mass.
    lbl_mass = tk.Label(frm_main, text="Enter Your Mass:")
    
    # Create an Integer entry box where the user will enter their mass.
    ent_mass = nent.FloatEntry(frm_main, 20, 120, width=5)
    
    # Create a label that displays the user's Weight.
    lbl_weight = tk.Label(frm_main, text="Your Weight in Newtons:")
    
    # Create a label that will display the user's weight.
    lbl_w = tk.Label(frm_main, width=4)
    
    # Create a label to display the SI unit for weight.
    lbl_Newton = tk.Label(frm_main, width=1, text="N")
    
    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")
    
    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_mass.grid(  row=0, column=0, padx=3, pady=3)
    ent_mass.grid(  row=0, column=1, padx=3, pady=3)
    lbl_weight.grid( row=1, column=0, padx=3, pady=3)
    lbl_w.grid( row=1, column=1, padx=3, pady=3)
    lbl_Newton.grid( row=1, column=2, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=5, sticky="w")
    
    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")
    
    def calculate_weight(weight):
        """
        Compute and display a user's weight.
        """
        
        try:
            # Get the mass of the user.
            m = ent_mass.get()
            
            # compute the weight of the user.
            w = m * 9.8

            # Display the user's weight.
            lbl_w.config(text=f"{w:.2f}")
            
        except ValueError:
            # When the user deletes all the digits in the mass
            # entry box, clear the displayed weight.
            lbl_w.config(text="")
    
    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_mass.delete(0, tk.END)
        lbl_w.config(text="")
        ent_mass.focus()


    # Bind the calculate function to the age entry box
    # so that the calculate function will be called when
    # the user changes the text in the entry box.
    ent_mass.bind("<KeyRelease>", calculate_weight)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_mass.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()