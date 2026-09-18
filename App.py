import tkinter as tk
from calculation import *
from tkinter import ttk

# from formula import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SUVAT v.1.0.0")
        self.geometry("400x300")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2
        self.geometry(f"+{x-100}+{y}")
        photo = tk.PhotoImage(file = 'SUVAT.png')
        self.iconphoto(False,photo, photo)
        
        # Container to hold all stacked frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Initialize both pages
        for PageClass in (HomePage, Move1,Move2,Move3,Move4,Move5):
            frame = PageClass(container, self)
            self.frames[PageClass] = frame
            # Put all frames in the same grid cell (stacking them)
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial page
        self.show_frame(HomePage)

    def show_frame(self, page_class):
        """Bring the specified frame to the top."""
        frame = self.frames[page_class]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.canvas = tk.Canvas(self,width=90,height=100)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0,0),window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )

        self.canvas.bind("<Configure>", lambda e:self.canvas.itemconfig(self.canvas_window, width = e.width))


        self.frame.bind("<Enter>", self._bind_mousewheel)
        self.frame.bind("<Leave>", self._unbind_mousewheel)
        
        label = tk.Label(self.frame, text="SUVAT", font=("Impact", 30))
        label.pack(pady=10)
        
        
        btn1 = tk.Button(
            self.frame, 
            text="v = u + a·t formula", 
            font = ("Arial", 20),
            bg= 'yellow',
            command=lambda: controller.show_frame(Move1)
        )
        btn1.pack()

        btn2 = tk.Button(
            self.frame, 
            text="s = ((u + v) / 2) · t formula", 
            font= ("Arial", 20),
            bg='red',
            command=lambda: controller.show_frame(Move2)
        )
        btn2.pack()
        
        btn3 = tk.Button(
            self.frame, 
            text="s = u·t + (1/2)·a·t²", 
            font= ("Arial", 20),
            bg = 'green',
            command=lambda: controller.show_frame(Move3)
        )
        btn3.pack()
        
        btn4 = tk.Button(
            self.frame, 
            text="s = v·t − ½·a·t²", 
            font= ("Arial", 20),
            bg='blue',
            command=lambda: controller.show_frame(Move4)
        )
        btn4.pack()
        
        btn5 = tk.Button(
            self.frame, 
            text="v² = u² + 2·a·s", 
            font= ("Arial", 20),
            bg='pink',
            command=lambda: controller.show_frame(Move5)
        )
        btn5.pack()
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        
class Move1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.canvas = tk.Canvas(self,width=90,height=100)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0,0),window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )


        self.canvas.bind("<Configure>", lambda e:self.canvas.itemconfig(self.canvas_window, width = e.width))


        self.frame.bind("<Enter>", self._bind_mousewheel)
        self.frame.bind("<Leave>", self._unbind_mousewheel)


        
        self.label = tk.Label(self.frame, text="v = u + a·t", font=("Impact", 20))
        self.label.pack(pady=20)
        
        self.find = ['Current Velocity(v)','Starting Velocity(u)','Acceleration(a)','Time(t)']
        self.choose = tk.StringVar()
        self.cb = ttk.Combobox(self.frame,values=self.find,textvariable=self.choose)
        # print(choose)
        self.cb.set('Value to find')
        self.cb.pack()
        self.lb = tk.Label(self.frame, text=f'Finding...')
        self.lb.pack()

        self.value = ''
        self.btn1 = tk.Button(self.frame,text='Apply change',command=self.read)
        self.btn1.pack()
        
        self.lb1 = tk.Label(self.frame, text="Current Velocity(v)(if not know don't enter):")
        self.lb1.pack()
        self.v1 = tk.DoubleVar()
        self.e1 = tk.Entry(self.frame, textvariable=self.v1)
        self.e1.pack()
       
        self.lb1 = tk.Label(self.frame, text="Starting Velocity(u)(if not know don't enter):")
        self.lb1.pack()
        self.u1 = tk.DoubleVar()
        self.e2 = tk.Entry(self.frame, textvariable=self.u1)
        self.e2.pack()
       
        
        self.lb1 = tk.Label(self.frame, text="Acceleration(a)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.a1 = tk.DoubleVar()
        self.e3 = tk.Entry(self.frame, textvariable=self.a1)
        self.e3.pack()
        
        
        self.lb1 = tk.Label(self.frame, text="Time(t)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.t1 = tk.DoubleVar()
        self.e4 = tk.Entry(self.frame, textvariable=self.t1)
        self.e4.pack()
        
        
        self.result_btn = tk.Button(self.frame,text = 'Calculate', command=self.calc)
        self.result_btn.pack()
        self.lb2 = tk.Label(self.frame,text='Calculation result:...')
        self.lb2.pack()

        self.btn = tk.Button(
            self.frame, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        self.btn.pack()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
    
    def read(self):
            value2 = self.choose.get()

            mapping = {
                self.find[0]: 'v',
                self.find[1]: 'u',
                self.find[2]: 'a',
                self.find[3]: 't',
            }
            
            self.value = mapping.get(value2, 'None')
            self.lb.config(text=f'Finding, {self.value}...')
    
    def calc(self):
        v = self.v1.get()
        u = self.u1.get()
        a = self.a1.get()
        t = self.t1.get()
        result = formula_1(self.value,u,v,a,t)
        self.lb2.config(text=f'{self.value} = {result}')
        
class Move2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.canvas = tk.Canvas(self,width=90,height=100)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0,0),window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )


        self.canvas.bind("<Configure>", lambda e:self.canvas.itemconfig(self.canvas_window, width = e.width))


        self.frame.bind("<Enter>", self._bind_mousewheel)
        self.frame.bind("<Leave>", self._unbind_mousewheel)
        
        
        label = tk.Label(self.frame, text="s = ((u + v) / 2) · t", font=("Impact", 20))
        label.pack(pady=20)
        
        self.find = ['Current Velocity(v)','Starting Velocity(u)','Displacement(s)','Time(t)']
        self.choose = tk.StringVar()
        self.cb = ttk.Combobox(self.frame,values=self.find,textvariable=self.choose)
        # print(choose)
        self.cb.set('Value to find')
        self.cb.pack()
        self.lb = tk.Label(self.frame, text=f'Finding...')
        self.lb.pack()

        self.value = ''
        self.btn1 = tk.Button(self.frame,text='Apply change',command=self.read)
        self.btn1.pack()
        
        self.lb1 = tk.Label(self.frame, text="Current Velocity(v)(if not know don't enter):")
        self.lb1.pack()
        self.v1 = tk.DoubleVar()
        self.e1 = tk.Entry(self.frame, textvariable=self.v1)
        self.e1.pack()
       
        self.lb1 = tk.Label(self.frame, text="Starting Velocity(u)(if not know don't enter):")
        self.lb1.pack()
        self.u1 = tk.DoubleVar()
        self.e2 = tk.Entry(self.frame, textvariable=self.u1)
        self.e2.pack()
       
        
        self.lb1 = tk.Label(self.frame, text="Displacement(s)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.s1 = tk.DoubleVar()
        self.e3 = tk.Entry(self.frame, textvariable=self.s1)
        self.e3.pack()
        
        
        self.lb1 = tk.Label(self.frame, text="Time(t)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.t1 = tk.DoubleVar()
        self.e4 = tk.Entry(self.frame, textvariable=self.t1)
        self.e4.pack()
        
        
        self.result_btn = tk.Button(self.frame,text = 'Calculate', command=self.calc)
        self.result_btn.pack()
        self.lb2 = tk.Label(self.frame,text='Calculation result:...')
        self.lb2.pack()

        self.btn = tk.Button(
            self.frame, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        self.btn.pack()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        
        
    def read(self):
            value2 = self.choose.get()

            mapping = {
                self.find[0]: 'v',
                self.find[1]: 'u',
                self.find[2]: 's',
                self.find[3]: 't',
            }
            
            self.value = mapping.get(value2, 'None')
            self.lb.config(text=f'Finding, {self.value}...')
    
    def calc(self):
        v = self.v1.get()
        u = self.u1.get()
        s = self.s1.get()
        t = self.t1.get()
        result = formula_2(self.value,u,v,s,t)
        self.lb2.config(text=f'{self.value} = {result}')

class Move3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.canvas = tk.Canvas(self,width=90,height=100)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0,0),window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )


        self.canvas.bind("<Configure>", lambda e:self.canvas.itemconfig(self.canvas_window, width = e.width))


        self.frame.bind("<Enter>", self._bind_mousewheel)
        self.frame.bind("<Leave>", self._unbind_mousewheel)
        
        
        label = tk.Label(self.frame, text="s = u·t + (1/2)·a·t²", font=("Impact", 20))
        label.pack(pady=20)
        
        self.find = ['Starting Velocity(u)','Acceleration(a)','Displacement(s)','Time(t)']
        self.choose = tk.StringVar()
        self.cb = ttk.Combobox(self.frame,values=self.find,textvariable=self.choose)
        # print(choose)
        self.cb.set('Value to find')
        self.cb.pack()
        self.lb = tk.Label(self.frame, text=f'Finding...')
        self.lb.pack()

        self.value = ''
        self.btn1 = tk.Button(self.frame,text='Apply change',command=self.read)
        self.btn1.pack()
       
        self.lb1 = tk.Label(self.frame, text="Starting Velocity(u)(if not know don't enter):")
        self.lb1.pack()
        self.u1 = tk.DoubleVar()
        self.e2 = tk.Entry(self.frame, textvariable=self.u1)
        self.e2.pack()
       
        
        self.lb1 = tk.Label(self.frame, text="Acceleration(a)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.a1 = tk.DoubleVar()
        self.e5 = tk.Entry(self.frame, textvariable=self.a1)
        self.e5.pack()
        
        self.lb1 = tk.Label(self.frame, text="Displacement(s)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.s1 = tk.DoubleVar()
        self.e3 = tk.Entry(self.frame, textvariable=self.s1)
        self.e3.pack()
        
        
        self.lb1 = tk.Label(self.frame, text="Time(t)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.t1 = tk.DoubleVar()
        self.e4 = tk.Entry(self.frame, textvariable=self.t1)
        self.e4.pack()
        
        
        self.result_btn = tk.Button(self.frame,text = 'Calculate', command=self.calc)
        self.result_btn.pack()
        self.lb2 = tk.Label(self.frame,text='Calculation result:...')
        self.lb2.pack()

        self.btn = tk.Button(
            self.frame, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        self.btn.pack()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        
        
    def read(self):
            value2 = self.choose.get()

            mapping = {
                self.find[0]: 'u',
                self.find[1]: 'a',
                self.find[2]: 's',
                self.find[3]: 't',
            }
            
            self.value = mapping.get(value2, 'None')
            self.lb.config(text=f'Finding, {self.value}...')
    
    def calc(self):
        u = self.u1.get()
        a = self.a1.get()
        s = self.s1.get()
        t = self.t1.get()
        result = formula_3(self.value,u,a,s,t)
        self.lb2.config(text=f'{self.value} = {result}')
                
class Move4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.canvas = tk.Canvas(self,width=90,height=100)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0,0),window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )


        self.canvas.bind("<Configure>", lambda e:self.canvas.itemconfig(self.canvas_window, width = e.width))


        self.frame.bind("<Enter>", self._bind_mousewheel)
        self.frame.bind("<Leave>", self._unbind_mousewheel)
        
        
        label = tk.Label(self.frame, text="s = v·t − ½·a·t²", font=("Impact", 20))
        label.pack(pady=20)
        
        self.find = ['Current Velocity(v)','Acceleration(a)','Displacement(s)','Time(t)']
        self.choose = tk.StringVar()
        self.cb = ttk.Combobox(self.frame,values=self.find,textvariable=self.choose)
        # print(choose)
        self.cb.set('Value to find')
        self.cb.pack()
        self.lb = tk.Label(self.frame, text=f'Finding...')
        self.lb.pack()

        self.value = ''
        self.btn1 = tk.Button(self.frame,text='Apply change',command=self.read)
        self.btn1.pack()
        
        self.lb1 = tk.Label(self.frame, text="Current Velocity(v)(if not know don't enter):")
        self.lb1.pack()
        self.v1 = tk.DoubleVar()
        self.e1 = tk.Entry(self.frame, textvariable=self.v1)
        self.e1.pack()
        
        self.lb1 = tk.Label(self.frame, text="Acceleration(a)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.a1 = tk.DoubleVar()
        self.e5 = tk.Entry(self.frame, textvariable=self.a1)
        self.e5.pack()
        
        self.lb1 = tk.Label(self.frame, text="Displacement(s)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.s1 = tk.DoubleVar()
        self.e3 = tk.Entry(self.frame, textvariable=self.s1)
        self.e3.pack()
        
        
        self.lb1 = tk.Label(self.frame, text="Time(t)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.t1 = tk.DoubleVar()
        self.e4 = tk.Entry(self.frame, textvariable=self.t1)
        self.e4.pack()
        
        
        self.result_btn = tk.Button(self.frame,text = 'Calculate', command=self.calc)
        self.result_btn.pack()
        self.lb2 = tk.Label(self.frame,text='Calculation result:...')
        self.lb2.pack()

        self.btn = tk.Button(
            self.frame, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        self.btn.pack()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        
        
    def read(self):
            value2 = self.choose.get()

            mapping = {
                self.find[0]: 'v',
                self.find[1]: 'a',
                self.find[2]: 's',
                self.find[3]: 't',
            }
            
            self.value = mapping.get(value2, 'None')
            self.lb.config(text=f'Finding, {self.value}...')
    
    def calc(self):
        v = self.v1.get()
        a = self.a1.get()
        s = self.s1.get()
        t = self.t1.get()
        result = formula_4(self.value,v,a,s,t)
        self.lb2.config(text=f'{self.value} = {result}')
     
class Move5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.canvas = tk.Canvas(self,width=90,height=100)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0,0),window=self.frame, anchor='nw')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )


        self.canvas.bind("<Configure>", lambda e:self.canvas.itemconfig(self.canvas_window, width = e.width))


        self.frame.bind("<Enter>", self._bind_mousewheel)
        self.frame.bind("<Leave>", self._unbind_mousewheel)
        
        
        label = tk.Label(self.frame, text="v² = u² + 2·a·s", font=("Impact", 20))
        label.pack(pady=20)
        
        self.find = ['Current Velocity(v)','Acceleration(a)','Displacement(s)','Time(t)']
        self.choose = tk.StringVar()
        self.cb = ttk.Combobox(self.frame,values=self.find,textvariable=self.choose)
        # print(choose)
        self.cb.set('Value to find')
        self.cb.pack()
        self.lb = tk.Label(self.frame, text=f'Finding...')
        self.lb.pack()

        self.value = ''
        self.btn1 = tk.Button(self.frame,text='Apply change',command=self.read)
        self.btn1.pack()
        
        self.lb1 = tk.Label(self.frame, text="Current Velocity(v)(if not know don't enter):")
        self.lb1.pack()
        self.v1 = tk.DoubleVar()
        self.e1 = tk.Entry(self.frame, textvariable=self.v1)
        self.e1.pack()
        
        self.lb1 = tk.Label(self.frame, text="Starting Veclocity(u)(if not know don't enter):")
        self.lb1.pack()
        self.u1 = tk.DoubleVar()
        self.e4 = tk.Entry(self.frame, textvariable=self.u1)
        self.e4.pack()
        
        self.lb1 = tk.Label(self.frame, text="Acceleration(a)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.a1 = tk.DoubleVar()
        self.e5 = tk.Entry(self.frame, textvariable=self.a1)
        self.e5.pack()
        
        self.lb1 = tk.Label(self.frame, text="Displacement(s)(if not know don't enter)(>0):")
        self.lb1.pack()
        self.s1 = tk.DoubleVar()
        self.e3 = tk.Entry(self.frame, textvariable=self.s1)
        self.e3.pack()
        
        self.result_btn = tk.Button(self.frame,text = 'Calculate', command=self.calc)
        self.result_btn.pack()
        self.lb2 = tk.Label(self.frame,text='Calculation result:...')
        self.lb2.pack()

        self.btn = tk.Button(
            self.frame, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        self.btn.pack()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        
        
    def read(self):
            value2 = self.choose.get()

            mapping = {
                self.find[0]: 'u',
                self.find[1]: 'a',
                self.find[2]: 's',
                self.find[3]: 't',
            }
            
            self.value = mapping.get(value2, 'None')
            self.lb.config(text=f'Finding, {self.value}...')
    
    def calc(self):
        v = self.v1.get()
        u = self.u1.get()
        a = self.a1.get()
        s = self.s1.get()
        result = formula_5(self.value,u,v,a,s)
        self.lb2.config(text=f'{self.value} = {result}')

if __name__ == "__main__":
    app = App()  
    app.mainloop()
