import tkinter as tk
from tkinter import ttk

class CableSizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cable Size Calc")

        # Variables for user inputs
        self.voltage_levels = ["230", "400"]
        self.voltage_level = tk.StringVar(value=self.voltage_levels[0])
        self.load_current = tk.DoubleVar()
        self.cable_length = tk.DoubleVar()
        self.ambient_temperature_options = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
        self.ambient_temperature = tk.StringVar(value=self.ambient_temperature_options[0])
        self.insulation_options = ["PVC", "XLPE"]
        self.cable_insulation = tk.StringVar(value=self.insulation_options[0])
        self.laying_method_options = [ "Direct Buried", "Tray", "In Air" ,"Overhead","Conduit"]
        self.cable_laying_method = tk.StringVar(value=self.laying_method_options[0])
        self.num_conductors_options = [1, 2, 3, 4, 5,6, 7, 8, 9, 12, 16, 20]
        self.num_conductors = tk.StringVar(value=self.num_conductors_options[0])
        self.voltage_drop = tk.DoubleVar()

        # Create and place widgets
        self.create_widgets()

    def calculate_cable_size(self):
        # Implement cable sizing calculations based on user inputs
        # For simplicity, let's just print the user inputs for now
        voltage = int(self.voltage_level.get())
        IB= self.load_current.get()
        L =  self.cable_length.get()
        temp= int(self.ambient_temperature.get())
        ins= self.cable_insulation.get()
        laying_meth = self.cable_laying_method.get()
        num_cond =  int(self.num_conductors.get())
        vd =  self.voltage_drop.get()
        vd = (vd*int(voltage))/100
        
        if laying_meth=="Conduit" and num_cond>1:
            K1 = 0.90
        else:
            K1 = 1
            
        temps = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55 ,60]   
        PVC = [1.22, 1.17, 1.12, 1.07, 1.02, 0.93, 0.87, 0.79, 0.71, 0.61, 0.6]
        XLPE = [1.15, 1.12, 1.08, 1.04, 1, 0.96, 0.91, 0.87, 0.82, 0.76, 0.71]
        conductor = [1, 2, 3, 4, 5,6, 7, 8, 9, 12, 16, 20]
        index1 = temps.index(temp)
        index2 = conductor.index(num_cond)
        
        
        if ins == 'PVC':
            K2 = PVC[index1]
        else:
            K2 = XLPE[index1]

        if laying_meth == "In Air" or laying_meth == "Overhead":
            val = [1, 0.8, 0.7, 0.65, 0.6, 0.57, 0.54, 0.52, 0.5, 0.45, 0.41, 0.38]
            K3 = val[index2]
        elif laying_meth == "Tray" or laying_meth == "Conduit":
            val = [1, 0.85, 0.79, 0.75, 0.73, 0.72, 0.72, 0.71, 0.7, 0.7, 0.65, 0.59]
            K3 = val[index2]
        else:
            K3 = 1

        IN = IB * 1.21
        IZ = IN/(K1*K2*K3)
        A = ["In Air","Overhead"]
        B = ["Conduit"]
        C = ["Tray"]
        E = ["Direct Buried"]
        sizes = [1.5, 2.5, 4 ,6, 10, 16, 25, 35]
        min1 = 0
        min2 = 0
        min3 = 0
        size = 1.5
        if laying_meth in A:
            if ins == "PVC":
                current1 = [13, 17.5, 23, 29, 39, 52, 68, 70]
                current2 = [13.5, 18, 24, 31, 42, 56, 73, 80]
                current3 = [14.5, 19.5, 26, 34, 46, 61, 80, 85]
                for i in range(len(sizes)):
                    if IZ > current1[i] :
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i
                    if IZ > current3[i]:  
                        min3 = current3[i] 
                        m = i

                if min1 > min2 and min1>min3:
                    size = sizes[j+1]
                if min2>min1 and min2>min3:
                    size = sizes[k+1]
                if min3>min1 and min3>min2:
                    size = sizes[m+1]

                            
            if ins =="XLPE":
                current1 = [15.5, 21, 28, 36, 50, 68, 89, 95]
                current2 = [17, 23, 31, 40, 54, 73, 95, 101]
                current3 = [18.5, 25, 34, 43, 60, 80, 101, 106]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i
                    if IZ > current3[i]:  
                        min3 = current3[i] 
                        m = i

                if min1 > min2 and min1>min3:
                    size = sizes[j+1]
                if min2>min1 and min2>min3:
                    size = sizes[k+1]
                if min3>min1 and min3>min2:
                    size = sizes[m+1]
        if laying_meth in B:
            if ins == "PVC":
                current1 = [14.5, 19.5, 26, 34, 46, 61, 80, 89]
                current2 = [15.5, 21, 28, 36, 50, 68, 89, 95]
                current3 = [17, 23, 31, 40, 54, 73, 95, 101]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i
                    if IZ > current3[i]:
                        min3 = current3[i]
                        m = i

                if min1 > min2 and min1 > min3:
                    size = sizes[j + 1]
                if min2 > min1 and min2 > min3:
                    size = sizes[k + 1]
                if min3 > min1 and min3 > min2:
                    size = sizes[m + 1]

            if ins == "XLPE":
                current1 = [18.5, 25, 34, 43, 60, 80, 101, 110]
                current2 = [19.5, 27, 36, 46, 63, 85, 110, 119]
                current3 = [22, 30, 40, 51, 70, 94, 119, 125]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i
                    if IZ > current3[i]:
                        min3 = current3[i]
                        m = i

                if min1 > min2 and min1 > min3:
                    size = sizes[j + 1]
                if min2 > min1 and min2 > min3:
                    size = sizes[k + 1]
                if min3 > min1 and min3 > min2:
                    size = sizes[m + 1]

        if laying_meth in C:
            if ins == "PVC":
                current1 = [17, 23, 31, 40, 54, 73, 95, 110]
                current2 = [19.5, 27, 36, 46, 63, 85, 110, 115]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i

                if min1 > min2:
                    size = sizes[j+1]
                if min2>min1 :
                    size = sizes[k+1]



                
            if ins =="XLPE":
                current1 = [22, 30, 40, 51, 70, 94, 119, 125]
                current2 = [24, 33, 45, 58, 80, 107, 135, 145]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i

                if min1 > min2:
                    size = sizes[j+1]
                if min2>min1 :
                    size = sizes[k+1]

        if laying_meth in E:
            if ins == "PVC":        
                current1 = [18.5, 25, 34, 43, 60, 80, 101, 110]
                current2 = [22, 30, 40, 51, 70, 94, 119, 125]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i

                if min1 > min2:
                    size = sizes[j+1]
                if min2>min1 :
                    size = sizes[k+1]

              
            if ins == "XLPE":
                current1 = [23, 31, 42, 54, 75, 100, 127, 135]
                current2 = [26, 36, 49, 63, 86, 115, 149, 160]
                for i in range(len(sizes)):
                    if IZ > current1[i]:
                        min1 = current1[i]
                        j = i
                    if IZ > current2[i]:
                        min2 = current2[i]
                        k = i

                if min1 > min2:
                    size = sizes[j+1]
                if min2>min1 :
                    size = sizes[k+1]
        R = (1.6*10**(-5)*L)/size
        V_cal = R*IB
        if V_cal <= vd:
            ttk.Label(self.root, text="Good Solution", background="#264653", foreground="white").grid(row=12, column=0, columnspan=2)
    
            
        ttk.Label(self.root, text="IN = " + str(IN), background="#264653", foreground="white").grid(row=9, column=0, columnspan=2)
        ttk.Label(self.root, text="IZ = " + str(IZ), background="#264653", foreground="white").grid(row=10, column=0, columnspan=2)
        ttk.Label(self.root, text="cable size = " + str(size), background="#264653", foreground="white").grid(row=11, column=0, columnspan=2)
        
    def create_widgets(self):

        self.root.geometry("400x400")
        self.root.title("Cable Size Calc")
        self.root.option_add('*TButton*Font', ('Monaco', 12))
        self.root.option_add('*TLabel*Font', ('Monaco', 12))

        self.root.configure(bg="#264653")

        self.style = ttk.Style()
        self.style.configure('TButton', background='Green', foreground='black')

        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self.root.winfo_width() / 2))
        y_cordinate = int((screen_height / 2) - (self.root.winfo_height() / 2))
        self.root.geometry(
            "{}x{}+{}+{}".format(self.root.winfo_width(), self.root.winfo_height(), x_cordinate, y_cordinate))

        ttk.Label(self.root, text="Voltage (V):", background="#264653", foreground="white").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        voltage_level_menu = ttk.Combobox(self.root, textvariable=self.voltage_level, values=self.voltage_levels, state="readonly")
        voltage_level_menu.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Current (A):", background="#264653", foreground="white").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(self.root, textvariable=self.load_current).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Cable Length (m):", background="#264653", foreground="white").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(self.root, textvariable=self.cable_length).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Temperature (°C):", background="#264653", foreground="white").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        ambient_temperature_menu = ttk.Combobox(self.root, textvariable=self.ambient_temperature, values=self.ambient_temperature_options, state="readonly")
        ambient_temperature_menu.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Insulation:", background="#264653", foreground="white").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        insulation_menu = ttk.Combobox(self.root, textvariable=self.cable_insulation, values=self.insulation_options, state="readonly")
        insulation_menu.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Cable Laying Method:", background="#264653", foreground="white").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        laying_method_menu = ttk.Combobox(self.root, textvariable=self.cable_laying_method, values=self.laying_method_options, state="readonly")
        laying_method_menu.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Number of Conductors:", background="#264653", foreground="white").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        num_conductors_menu = ttk.Combobox(self.root, textvariable=self.num_conductors, values=self.num_conductors_options, state="readonly")
        num_conductors_menu.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Voltage Drop:", background="#264653", foreground="white").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(self.root, textvariable=self.voltage_drop).grid(row=7, column=1, padx=10, pady=5)

        ttk.Button(self.root, text="Calculate", command=self.calculate_cable_size).grid(row=8, column=0, columnspan=2,
                                                                                        pady=10)
        
       

if __name__ == "__main__":
    root = tk.Tk()
    app = CableSizerApp(root)
    root.mainloop()
