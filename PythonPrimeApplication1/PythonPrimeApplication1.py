import tkinter as tk
import tkinter.font as tkFont
import numpy


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Sets the window size
        parent.title("Prime")
        parent.geometry("600x650")
        parent.resizable(width=True, height=False)

        # Making a font for all text
        self.font1 = tkFont.Font(family="Aerial", size="15")
        self.font2 = tkFont.Font(family="Aerial", size="17")

        # A label for just text
        self.label = tk.Label(self, text="Enter a number", font=self.font2)
        self.label.pack(expand = True)

        # Entry to put a number
        self.number = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.number, width=23, font=self.font2)
        self.entry.pack(expand = True)
       
        # Button then pressed checks the number
        self.button = tk.Button(self, text="Check", command=self.prime, width=15, font=self.font2)
        self.button.pack(side="top", expand = True)

        # Check button which toggles factorization on and off (Default off)
        self.factorize = tk.IntVar()
        self.check = tk.Checkbutton(self, text="Factorization", variable=self.factorize, font=self.font2)
        self.check.pack(side="top")

        # Label which displays the answer of the number
        self.answer = tk.Label(self, font=self.font1)
        self.answer.pack(expand=True)

        # Label that says the version of a program
        self.version = tk.Label(self, text="V1.6")
        self.version.pack(side="bottom")

        # Making a list of prime numbers
        self.primes = numpy.ones(10**7, dtype=numpy.bool)
        self.primes[:2] = False
        self.primes[4::2] = False
        for p in range(3, int((10**7)**.5)+1, 2):
            if self.primes[p]:
                self.primes[p*p::p*2] = False
        self.primes = self.primes.nonzero()[0]

    def prime(self):
        try:  # Checks if the input is integer only
            number = int(self.number.get())
            self.button["bg"] = "SystemButtonFace"
            self.answer["bg"] = "SystemButtonFace"
            if number < 2:
                self.answer["text"] = "0; 1 and negative numbers aren't prime"
                okey = False
            else:
                self.answer["text"] = "Calculating..."
                self.parent.update_idletasks()
                okey = True
        except ValueError:  # If the input on the entry is not an integer
            self.answer["text"] = "Put a number here only"
            self.button["bg"] = "red"
            self.answer["bg"] = "red"
            okey = False

        if okey:  # Makes sure that the input is an integer

            if self.factorize.get() == 0:  # If the user doesn't want to factorize the number

                if number in self.primes:
                    self.answer["text"] = "It's a prime"
                else:
                    for x in range(2, int(number**(1/2))+1):
                        if number % x == 0:
                            self.answer["text"] = "It's not a prime"
                            break
                    else:
                        self.answer["text"] = "It's a prime"
            else:  # Factorizing
                numbers = []
                cofactors = {}            
                if_prime = True
                if number in self.primes:  # Checks if the number is in the list of prime numbers
                    cofactors[number] = 1
                    if_prime = True
                else:
                    for n in self.primes:  # If the number is divisible from 2 to 999983
                        if number % n == 0:
                            a = 0
                            if_prime = False
                            while number % n == 0:  # If the number is divisible by the same number more than once
                                a += 1
                                number = number // int(n)
                            cofactors[n] = a
                    if number >= 99999820000081:  # If the number is still bigger than 9999991**2
                        for n in range(9999992, int(number**.5)+1):  # Divides given number from 9999992 to numbers square root
                            if number % n == 0:
                                a = 0
                                if_prime = False
                                while number % n == 0:
                                    a += 1
                                    number = number // int(n)
                                cofactors[n] = a
                    if if_prime:
                        cofactors[number] = 1
                    else:
                        if number != 1:
                            cofactors[number] = 1
                text = "Prime = {}".format(if_prime)
                SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
                for z in cofactors.keys():
                    numbers.append(str(z)+str(cofactors[z]).translate(SUP))
                self.answer["text"] = "{0}\n{1} = {2}".format(str(text), " * ".join(numbers), self.number.get())


if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
