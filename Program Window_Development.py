import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


import tkinter as tk
from tkinter import ttk

import urllib
from urllib.request import urlopen
import json
import pandas as pd
import numpy as np



LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

style.use('ggplot')

f = Figure()
a = f.add_subplot(111)

exchange = "coingecko"
DatCounter = 9000
programName = "btce"
resampleSize = '15Min'
dataPace = 'tick'
candleWidth = 0.008
paneCount = 1

topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"

chartLoad = True

EMAs = []
SMAs = []






def changeExchange(toWhat, pn):
    global exchange
    global DatCounter
    global programName

    exchange = toWhat
    programName = pn
    DatCounter = 9000


def popupmsg(msg):
    popup = tk.Tk()

    def leavemini():
        popup.destroy()

    popup.wm_title('!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10 )
    B1 = ttk.Button(popup, text='Okay', command = leavemini)
    B1.pack()
    popup.mainloop()


def animate(i):
    global refreshRate
    global DatCounter

    if chartLoad:
        if dataPace =='tick':
            try:
                a = plt.subplot2grid((6,4),(0,0), rowspan=5, colspan=4)
                a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex = a)

                # dataLink = cg.get_price(ids='ethereum', vs_currencies='gbp', last_updated=True )

                dataLink = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=gbp&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=true"
                data = urllib.request.urlopen(dataLink)
                data = data.read().decode('utf-8')
                data = json.loads(data)
                data = data["ethereum"]
                gpb = data['gbp']
                # lastupdate = np.array(data['last_updated_at']).astype('datatime64(s)')

                import datetime

                timestamp = data['last_updated_at']
                lastupdate = datetime.datetime.fromtimestamp(timestamp)
                time = lastupdate.strftime('%H:%M:%S')

                # a.clear()

                a.plot_date(time, gpb)
                # a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                #     ncol=2, borderaxespad=0)
                title = "ETHGBP Prices\nLast Price: " + str(gpb)
                a.set_title(title)

            except Exception as e:
                print('Failed because of:', e)













class Etsy(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        tk.Tk.wm_title(self, 'Sea of BTC client')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand='True')

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff=0)

        filemenu.add_command(label='Save settings', command=lambda: popupmsg('Not support just yet!'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='File', menu=filemenu)

        etsyChoice = tk.Menu(menubar, tearoff=1)

        etsyChoice.add_command(label="Edit Tags",
                                   command=lambda: edit_tags())
        etsyChoice.add_command(label='Delete Images',
                                   command=lambda: delete_images())
        etsyChoice.add_command(label="New Listing",
                                   command=lambda: new_listing())


        menubar.add_cascade(label="Etsy", menu=etsyChoice)



        tradeButton = tk.Menu(menubar, tearoff=1)
        tradeButton.add_command(label="Manual Trading",
                                command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label="Automated Trading",
                                command=lambda: popupmsg("This is not live yet"))

        tradeButton.add_separator()
        tradeButton.add_command(label="Quick Buy",
                                command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label="Quick Sell",
                                command=lambda: popupmsg("This is not live yet"))

        tradeButton.add_separator()
        tradeButton.add_command(label="Set-up Quick Buy/Sell",
                                command=lambda: popupmsg("This is not live yet"))

        menubar.add_cascade(label="Trading", menu=tradeButton)


        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for F in (StartPage, BTCe_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""Alpha Bitcoin Trading Application'
                                        There is no warranty and users are useing this at their 
                                        own risk. There will be no comeback"""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Agree', command=lambda: controller.show_frame(BTCe_page))
        button1.pack()

        button2 = ttk.Button(self, text='Disagree', command=quit)
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, contoller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One !!!!!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to home', command=lambda: contoller.show_frame(StartPage))
        button1.pack()


class BTCe_page(tk.Frame):
    def __init__(self, parent, contoller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph Page!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to home', command=lambda: contoller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)





app = Etsy()
ani = animation.FuncAnimation(f, animate, interval=30000)
app.geometry('1280x720')
app.mainloop()
