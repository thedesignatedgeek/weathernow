#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24
#  in conjunction with Tcl version 8.6
#    Jul 27, 2019 05:39:37 PM CDT  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import frmAlerts_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    frmAlerts_support.set_Tk_var()
    top = FormAlerts (root)
    frmAlerts_support.init(root, top)
    root.mainloop()

w = None
def create_FormAlerts(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    frmAlerts_support.set_Tk_var()
    top = FormAlerts (w)
    frmAlerts_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_FormAlerts():
    global w
    w.destroy()
    w = None

class FormAlerts:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font15 = "-family Ubuntu -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font16 = "-family Ubuntu -size 11 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font17 = "-family Ubuntu -size 10 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font18 = "-family Ubuntu -size 15 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("780x625+444+60")
        top.title("New Toplevel")
        top.configure(background="#595959")
        top.configure(highlightcolor="black")

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(x=20, y=215, height=347, width=740)
        self.Scrolledtext1.configure(background="#595959")
        self.Scrolledtext1.configure(font=font16)
        self.Scrolledtext1.configure(foreground="#ffffff")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(width=10)
        self.Scrolledtext1.configure(wrap="word")

        self.btnExit = tk.Button(top)
        self.btnExit.place(x=350, y=580,  height=31, width=80)
        self.btnExit.configure(activebackground="#f9f9f9")
        self.btnExit.configure(command=frmAlerts_support.on_btnExit)
        self.btnExit.configure(text='''Dismiss''')

        self.lblAlertCount = tk.Label(top)
        self.lblAlertCount.place(x=65, y=55,  height=31, width=309)
        self.lblAlertCount.configure(activebackground="#f9f9f9")
        self.lblAlertCount.configure(background="#595959")
        self.lblAlertCount.configure(font=font16)
        self.lblAlertCount.configure(foreground="#ffffff")
        self.lblAlertCount.configure(relief="sunken")
        self.lblAlertCount.configure(text='''There are X alerts for this area''')
        self.lblAlertCount.configure(textvariable=frmAlerts_support.AlertCount)

        self.frmTitleBar = tk.Frame(top)
        self.frmTitleBar.place(x=0, y=0, height=45, width=780)
        self.frmTitleBar.configure(relief='groove')
        self.frmTitleBar.configure(borderwidth="2")
        self.frmTitleBar.configure(relief="groove")
        self.frmTitleBar.configure(background="#595959")
        self.frmTitleBar.configure(width=775)

        self.lblTitle = tk.Label(self.frmTitleBar)
        self.lblTitle.place(x=120, y=5,  height=31, width=539)
        self.lblTitle.configure(activebackground="#f9f9f9")
        self.lblTitle.configure(background="#595959")
        self.lblTitle.configure(font=font15)
        self.lblTitle.configure(foreground="#ffffff")
        self.lblTitle.configure(text='''Label''')
        self.lblTitle.configure(textvariable=frmAlerts_support.Title)

        self.btnMinimize = tk.Button(self.frmTitleBar)
        self.btnMinimize.place(x=720, y=5,  height=31, width=41)
        self.btnMinimize.configure(activebackground="#f9f9f9")
        self.btnMinimize.configure(background="#595959")
        self.btnMinimize.configure(command=frmAlerts_support.on_btnMinimize)
        self.btnMinimize.configure(font=font18)
        self.btnMinimize.configure(foreground="#ff0000")
        self.btnMinimize.configure(text='''-''')

        self.btnPrevious = tk.Button(top)
        self.btnPrevious.place(x=10, y=55,  height=31, width=51)
        self.btnPrevious.configure(activebackground="#f9f9f9")
        self.btnPrevious.configure(command=frmAlerts_support.on_btnPrevious)
        self.btnPrevious.configure(text='''Prev''')

        self.btnNext = tk.Button(top)
        self.btnNext.place(x=380, y=55,  height=31, width=51)
        self.btnNext.configure(activebackground="#f9f9f9")
        self.btnNext.configure(command=frmAlerts_support.on_btnNext)
        self.btnNext.configure(text='''Next''')

        self.lblAlertSeverity = tk.Label(top)
        self.lblAlertSeverity.place(x=440, y=55,  height=31, width=319)
        self.lblAlertSeverity.configure(activebackground="#f9f9f9")
        self.lblAlertSeverity.configure(background="#595959")
        self.lblAlertSeverity.configure(font=font17)
        self.lblAlertSeverity.configure(foreground="#ffffff")
        self.lblAlertSeverity.configure(relief="groove")
        self.lblAlertSeverity.configure(text='''Advisory''')
        self.lblAlertSeverity.configure(textvariable=frmAlerts_support.Severity)

        self.msgRegions = tk.Message(top)
        self.msgRegions.place(x=20, y=125, height=52, width=740)
        self.msgRegions.configure(anchor='nw')
        self.msgRegions.configure(background="#595959")
        self.msgRegions.configure(font=font16)
        self.msgRegions.configure(foreground="#ffffff")
        self.msgRegions.configure(relief="groove")
        self.msgRegions.configure(text='''Bastrop, Caldwell, Hays, Travis, Williamson''')
        self.msgRegions.configure(textvariable=frmAlerts_support.Regions)
        self.msgRegions.configure(width=742)

        self.lblTimes = tk.Label(top)
        self.lblTimes.place(x=20, y=90,  height=31, width=740)
        self.lblTimes.configure(activebackground="#f9f9f9")
        self.lblTimes.configure(anchor='w')
        self.lblTimes.configure(background="#595959")
        self.lblTimes.configure(font=font16)
        self.lblTimes.configure(foreground="#ffffff")
        self.lblTimes.configure(relief="groove")
        self.lblTimes.configure(text='''Effective from Thu, 25 Jul 2019 19:10:00 GMT until Sun, 28 Jul 2019 00:00:00 GMT''')
        self.lblTimes.configure(textvariable=frmAlerts_support.Times)

        self.lblUrl = tk.Label(top)
        self.lblUrl.place(x=20, y=180,  height=31, width=740)
        self.lblUrl.configure(activebackground="#f9f9f9")
        self.lblUrl.configure(anchor='w')
        self.lblUrl.configure(background="#595959")
        self.lblUrl.configure(font=font17)
        self.lblUrl.configure(foreground="#ffffff")
        self.lblUrl.configure(relief="groove")
        self.lblUrl.configure(text='''Label''')
        self.lblUrl.configure(textvariable=frmAlerts_support.URL)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()




