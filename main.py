# MODULES IMPORTS
from datetime import date
from tkinter import *
from tkinter import ttk
import sys
import oracledb as cx_oracle
from fpdf import FPDF
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk,Image
import functional_dependencies as f
import logging
# ROOT WINDOW INITIALIZATION AS Tk()
rootWin = Tk()
screen_width = rootWin.winfo_screenwidth()
screen_height = rootWin.winfo_screenheight()
# FD Initialization
fds=f.FDSet()
# GLOBAL VARIABLES

ADMIN_ID = StringVar()
PASSWORD = StringVar()
AD_ID=StringVar()
PD=StringVar()
RPD=StringVar()
ID= StringVar()
NAME=StringVar()
EMAIL=StringVar()
BRAND_ID=DoubleVar()
BRAND_NAME = StringVar()
BRAND_STATUS = StringVar()
BRAND_SORT=StringVar()
CATEGORY_ID=DoubleVar()
CATEGORY_NAME = StringVar()
CATEGORY_STATUS = StringVar()
CATEGORY_SORT=StringVar()
SEARCH = StringVar()
PRODUCT_ID =DoubleVar()
PRODUCT_NAME = StringVar()
QUANTITY = IntVar()
RATE = DoubleVar()
PRODUCT_BRAND = StringVar()
PRODUCT_CATEGORY = StringVar()
PRODUCT_STATUS = StringVar()
PRODUCT_SORT=StringVar()
ORDER_SORT=StringVar()
ORDER_DATE = StringVar()
ORDER_ID=DoubleVar()
CLIENT_NAME = StringVar()
CLIENT_N0 = StringVar()
TOTAL = DoubleVar()
SUB_AMOUNT = DoubleVar()
TOTAL_AMOUNT = DoubleVar()
PAID_AMOUNT = DoubleVar()
DUE_AMOUNT = DoubleVar()
PAYMENT_STATUS = StringVar()
GST = DoubleVar()
LFDINPUT=StringVar()
RFDINPUT=StringVar()
# VARIABLE INITIALIZATION
brand_sort=['BRAND_ID','BRAND_NAME','BRAND_STATUS']
category_sort=['CATEGORY_ID','CATEGORY_NAME','CATEGORY_STATUS']
product_sort=['PRODUCT_ID','PRODUCT_NAME','QUANTITY','RATE','PRODUCT_BRAND','PRODUCT_CATEGORY','STATUS']
order_sort=['ORDER_ID','ORDER_DATE','CLIENT_NAME','CLIENT_NO','PRODUCT','QUANTITY','TOTAL_AMOUNT','PAID_AMOUNT','DUE_AMOUNT','PAYMENT_STATUS']
status = ['AVAILABLE', 'NOT AVAILABLE']
brands = []
category = []
products = []
orders = []
orderCount = []
brandCount = []
productCount = []
paymentStatus = ['ADVANCE PAYMENT', 'FULL PAYMENT', 'NO PAYMENT']
BRAND_STATUS.set('SELECT')
CATEGORY_STATUS.set('SELECT')
PRODUCT_BRAND.set('SELECT')
PRODUCT_CATEGORY.set('SELECT')
PRODUCT_STATUS.set('SELECT')
PAYMENT_STATUS.set('SELECT')
ORDER_SORT.set('SELECT')
PRODUCT_SORT.set('SELECT')
CATEGORY_SORT.set('SELECT')
BRAND_SORT.set('SELECT')
# ROOT WINDOW FUNCTION

def InvSys():
    
    global lbl_rootErr
    rootWin.attributes('-fullscreen', True,)
    
    
    # ==============================================TITLE FRAME=================================================
    Label(rootWin, text="Inventory Management System", font=('Calibri', 32, 'bold'),
          fg="#2e5da3",).place(x=500,y=10)
    Label(rootWin, fg="#2e5da3",
          text="_________________________________________________________"
               "________________________________________________________").place(x=500,y=70)
    
    exit_img = PhotoImage(file='assets/icons/exit.png')
    Button(rootWin, image=exit_img, relief=FLAT, cursor="hand2", command=Exit).place(x=screen_width - 50, y=10)
    minimize_img = PhotoImage(file='assets/icons/minimize.png')
    Button(rootWin, image=minimize_img, relief=FLAT, cursor="hand2", command=Minimize).place(x=screen_width - 96, y=10)

    # ==============================================LOGIN FRAME=================================================
    profile=PhotoImage(file="profile.png")
    lbl_menu = Label(rootWin,i=profile,bg="#F4F2F2")
    lbl_username = Label(rootWin, text="Admin ID", font=('calibri', 14), fg="#2e5da3")
    lbl_password = Label(rootWin, text="Password", font=('calibri', 14), fg="#2e5da3")
    entry_username = Entry(rootWin, textvariable=ADMIN_ID, width=35, font=('calibri', 12, 'bold'), justify='center',
                           fg="#2e5da3", relief_=RIDGE, bd=2)
    entry_password = Entry(rootWin, textvariable=PASSWORD, width=35, font=('calibri', 12), show="*", justify='center',
                           fg="#2e5da3", relief_=RIDGE, bd=2)
    img_login = PhotoImage(file='login.png')
    btn_login = Button(rootWin, image=img_login, relief=FLAT, cursor="hand2", command=Login)
    img_Reg = PhotoImage(file='sign.png',width=130,height=50)
    btn_Reg = Button(rootWin, image=img_Reg, relief=FLAT, cursor="hand2", command=Register)
    lbl_menu.place(x=screen_width / 2 - 45, y=screen_height / 2 - 220)
    lbl_username.place(x=screen_width / 2 - 30, y=screen_height / 2 - 120)
    entry_username.place(x=screen_width / 2 - 132, y=screen_height / 2 - 90)
    lbl_password.place(x=screen_width / 2 - 30, y=screen_height / 2 - 40)
    entry_password.place(x=screen_width / 2 - 132, y=screen_height / 2 - 10)
    btn_login.place(x=screen_width / 2 - 95, y=screen_height / 2 + 50)
    btn_Reg.place(x=screen_width / 2 - 59,y=screen_height / 2 + 100)
    lbl_rootErr=Label(rootWin,text="",font=('calibri', 14),bg="#f2f2f2",fg="red")
    lbl_rootErr.place(x=screen_width/2-125,y=screen_height/2+200)
    rootWin.mainloop()


# HOME WINDOW
def Home(name):
    global homeWin, brand_count, product_count, order_count
    homeWin = Toplevel()
    homeWin.attributes('-fullscreen', True)
    
    # ==============================================TITLE FRAME=================================================
    Label(homeWin, text="Inventory Management System", font=('Calibri', 32, 'bold'),
          fg="#2e5da3").place(x=700, y=10)
    Label(homeWin, fg="#2e5da3",
          text="___________________________________________________________"
               "____________________________________________________________").place(x=700, y=60)
    exit_imgHome = PhotoImage(file='assets/icons/exit.png')
    exit_Button = Button(homeWin, image=exit_imgHome, relief=FLAT, cursor="hand2", command=ExitHome)
    exit_Button.image = exit_imgHome
    exit_Button.place(x=screen_width - 50, y=10)

    minimize_imgHome = PhotoImage(file='assets/icons/minimize.png')
    minimize_Button = Button(homeWin, image=minimize_imgHome, relief=FLAT, cursor="hand2", command=MinimizeHome)
    minimize_Button.image = minimize_imgHome
    minimize_Button.place(x=screen_width - 96, y=10)

    menuFrame = Frame(homeWin, bd=2, relief_=RIDGE)
    menuFrame.pack(side='left', fill=Y, ipadx=20)

    btnFrame = Frame(menuFrame)
    btnFrame.pack(pady=100)

    welcome_lbl = Label(btnFrame, fg='#2e5da3', font=('calibri', 20, 'bold'))
    welcome_lbl['text'] = "Welcome, " + name
    welcome_lbl.pack(padx=20, pady=5, ipadx=30)

    btn_orders = Button(btnFrame, text='Orders', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                        cursor="hand2", command=Orders)
    btn_orders.pack(padx=20, pady=15, ipadx=30)
    btn_brands = Button(btnFrame, text='Brands', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                        cursor="hand2", command=Brands)
    btn_brands.pack(padx=20, pady=15, ipadx=30)
    btn_products = Button(btnFrame, text='Products', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                          cursor="hand2", command=Products)
    btn_products.pack(padx=20, pady=15, ipadx=30)

    btn_category = Button(btnFrame, text='Category', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                          cursor="hand2", command=Category)
    btn_category.pack(padx=20, pady=15, ipadx=30)
    btn_report = Button(btnFrame, text='Report', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                        cursor="hand2", command=Report)
    btn_report.pack(padx=20, pady=15, ipadx=30)
    btn_ER = Button(btnFrame, text='ER daigram', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                        cursor="hand2", command=ERdaigram)
    btn_ER.pack(padx=20, pady=15, ipadx=30)
    btn_FD = Button(btnFrame, text='FD', bg="#f2f2f2", fg="#2e5da3", font=('calibri', 16, 'bold'), width=25,
                        cursor="hand2", command=FD)
    btn_FD.pack(padx=20, pady=15, ipadx=30)
    Label(homeWin, text="Dashboard", font=('calibri', 32, 'bold'), fg='#2e5da3').place(x=900, y=120)

    bimg = PhotoImage(file='assets/images/download.png')
    brandFrame = Frame(homeWin, bd=2, relief_=RIDGE,bg='magenta')
    brandFrame.place(x=600, y=230)

    
    Label(brandFrame, text="Total Brands", font=('calibri', 24, 'bold'), fg='magenta').pack(ipadx=100, ipady=50)
    brand_count = Label(brandFrame, text="0", font=('calibri', 32, 'bold'), fg='#fff',bg='magenta')
    brand_count.pack(ipadx=100, pady=20)

    productFrame = Frame(homeWin, bd=2, relief_=RIDGE, bg='#856ff8')
    productFrame.place(x=screen_width - 500, y=230)
    Label(productFrame, text="Total Products", font=('calibri', 24, 'bold'), fg='#856ff8').pack(ipadx=100, ipady=50)
    product_count = Label(productFrame, text="0", font=('calibri', 32, 'bold'), fg='#fff', bg='#856ff8')
    product_count.pack(ipadx=100, pady=20)

    orderFrame = Frame(homeWin, bd=2, relief_=RIDGE, bg='green')
    orderFrame.place(x=screen_width - 750, y=500)
    Label(orderFrame, text="Total Orders", font=('calibri', 24, 'bold'), fg='green').pack(ipadx=100, ipady=50)
    order_count = Label(orderFrame, text="0", font=('calibri', 32, 'bold'), fg='#fff', bg='green')
    order_count.pack(ipadx=100, pady=20)

    BrandCount()
    ProductCount()
    OrderCount()


# ==============================================BRANDS START HERE======================================================
def Brands():
    global brandTree, lbl_brandErr
    brandWin = Toplevel()
    brandWin.title("Inventory Management System")
    dwidth = 1080
    dheight = 800
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    brandWin.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    brandWin.resizable(0, 0)

    Label(brandWin, text="Brands", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    Label(brandWin, text="Sort By    : ", font=('calibri', 14)).place(x=100, y=80)
    optionMenu_bsort = ttk.Combobox(brandWin, textvariable=BRAND_SORT)
    optionMenu_bsort['values'] = brand_sort
    optionMenu_bsort.config(font=('calibri', 14), width=20)
    optionMenu_bsort.place(x=200, y=82)
    Button(brandWin, text="Sort", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=Sortbrand).place(x=420, y=78)
   
    Label(brandWin, text="Search    : ", font=('calibri', 14)).place(x=640, y=80)
    entry_search = Entry(brandWin, textvariable=SEARCH, font=('calibri', 14))
    entry_search.place(x=740, y=82)
    Button(brandWin, text="Search", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=SearchBrand).place(x=960, y=78)

    spaceView = Frame(brandWin)
    spaceView.pack(pady=20)

    btnView = Frame(brandWin)
    btnView.pack(pady=40)

    btn_add = Button(btnView, text="Add", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                     width=10, height=1, cursor="hand2", command=AddBrandForm)
    btn_add.grid(row=0, column=0, padx=30, pady=10)

    btn_edit = Button(btnView, text="Edit", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                      width=10, height=1, cursor="hand2", command=EditBrand)
    btn_edit.grid(row=0, column=1, padx=30, pady=10)

    btn_delete = Button(btnView, text="Delete", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                        width=10, height=1, cursor="hand2", command=DeleteBrand)
    btn_delete.grid(row=0, column=2, padx=30, pady=10)

    btn_reset = Button(btnView, text="Reset", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                       width=10, height=1, cursor="hand2", command=ResetBrandData)
    btn_reset.grid(row=0, column=3, padx=30, pady=10)

    scrollbary = Scrollbar(brandWin, orient=VERTICAL)

    style = ttk.Style(brandWin)
    style.theme_use("default")
    style.configure("Treeview")
    style.configure("Treeview", highlightthickness=0, bd=0, font=('calibri', 12))
    style.configure("Treeview.Heading", font=('calibri', 12, 'bold'), foreground="#fff", background="#2e5da3")

    brandTree = ttk.Treeview(brandWin, columns=("Brand ID", "Brand Name", "Status"), style="Treeview",
                             selectmode="extended", yscrollcommand=scrollbary.set)
    scrollbary.config(command=brandTree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    brandTree.heading('Brand ID', text="BRAND ID", anchor=CENTER)
    brandTree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    brandTree.heading('Brand Name', text="BRAND NAME", anchor=CENTER)
    brandTree.column('#1', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    brandTree.heading('Status', text="STATUS", anchor=CENTER)
    brandTree.column('#2', stretch=NO, minwidth=0, width=500, anchor=CENTER)

    brandTree.pack(fill="both", expand=True)
    lbl_brandErr = Label(brandWin, text="", font=('calibri', 14), bg="#f2f2f2", fg="red")
    lbl_brandErr.pack(fill=X, side=BOTTOM)
    ShowBrandData()


def AddBrandForm():
    BRAND_ID.set("")
    BRAND_NAME.set("")
    BRAND_STATUS.set("SELECT")
    global lbl_brandErrAdd
    addBrandWin = Toplevel()
    addBrandWin.title("Inventory Management System")
    width = 640
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addBrandWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addBrandWin.resizable(0, 0)

    Label(addBrandWin, text="+ Add Brand", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=20)
    lbl_brandID = Label(addBrandWin, text="Brand ID     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_brandID = Entry(addBrandWin, textvariable=BRAND_ID, width=30, font=('calibri', 14))
    lbl_brandName = Label(addBrandWin, text="Brand Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_brandName = Entry(addBrandWin, textvariable=BRAND_NAME, width=30, font=('calibri', 14))
    lbl_brandStatus = Label(addBrandWin, text="Status       :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_brandStatus = ttk.Combobox(addBrandWin, textvariable=BRAND_STATUS)
    optionMenu_brandStatus['values'] = status
    optionMenu_brandStatus.config(font=('calibri', 14), width=29)
    lbl_brandErrAdd = Label(addBrandWin, text="", font=('calibri', 14), fg="red")

    btn_saveBrand = Button(addBrandWin, text="Save", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=InsertBrand)
    lbl_brandID.place(x=100, y=100)
    entry_brandID.place(x=230, y=100)
    lbl_brandName.place(x=80, y=150)
    entry_brandName.place(x=230, y=150)
    lbl_brandStatus.place(x=120, y=200)
    optionMenu_brandStatus.place(x=230, y=200)
    btn_saveBrand.place(x=230, y=250)
    lbl_brandErrAdd.pack(fill=X, side=BOTTOM)
    optionMenu_brandStatus.current()


def EditBrandForm():
    global lbl_brandErrEdit
    editBrandWin = Toplevel()
    editBrandWin.title("Inventory Management System")
    width = 640
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    editBrandWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    editBrandWin.resizable(0, 0)

    Label(editBrandWin, text="+ Edit Brand", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=20)

    lbl_brandName = Label(editBrandWin, text="Brand Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_brandName = Entry(editBrandWin, textvariable=BRAND_NAME, width=30, font=('calibri', 14), fg="#000",
                            state=DISABLED)
    lbl_brandStatus = Label(editBrandWin, text="Status       :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_brandStatus = ttk.Combobox(editBrandWin, textvariable=BRAND_STATUS)
    optionMenu_brandStatus['values'] = status
    optionMenu_brandStatus.config(font=('calibri', 14), width=29)
    lbl_brandErrEdit = Label(editBrandWin, text="", font=('calibri', 14), fg="red")

    btn_updateBrand = Button(editBrandWin, text="Update", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                             font=('calibri', 12, 'bold'), width=20, height=1, cursor="hand2", command=UpdateBrand)

    lbl_brandName.place(x=80, y=100)
    entry_brandName.place(x=230, y=100)
    lbl_brandStatus.place(x=120, y=150)
    optionMenu_brandStatus.place(x=230, y=150)
    btn_updateBrand.place(x=230, y=220)
    lbl_brandErrEdit.pack(fill=X, side=BOTTOM)
    optionMenu_brandStatus.current()


# FUNCTIONS FOR BRAND----------
def ShowBrandData():
    Database()
    try:
        cursor.execute("SELECT * FROM brands ORDER BY brand_id")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        brandTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def InsertBrand():
    Database()
    brandid=(float(BRAND_ID.get()))
    brandName = (str(BRAND_NAME.get()))
    brandStatus = (str(BRAND_STATUS.get()))

    if BRAND_NAME.get() == "":
        lbl_brandErrAdd['text'] = "Brand name can't be empty!"
    elif BRAND_STATUS.get() == "SELECT":
        lbl_brandErrAdd['text'] = "Choose required field!"
    else:
        sql_insert_data = "INSERT INTO brands (brand_id,brand_name, status) VALUES (:bid,:bname, :bstatus)"
        try:
            cursor.execute(sql_insert_data, {'bid':brandid,'bname': brandName, 'bstatus': brandStatus})
            BRAND_ID.set("")
            BRAND_NAME.set("")
            BRAND_STATUS.set("SELECT")
            lbl_brandErrAdd.config(fg="#2e5da3")
            lbl_brandErrAdd['text'] = "Data Added Successfully"
            print("Data Added Successfully!")
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            lbl_brandErrAdd['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()
    ResetBrandData()
    brandCount.clear()
    BrandCount()


def SearchBrand():
    Database()
    lbl_brandErr.config(fg="#2e5da3")
    lbl_brandErr['text'] = "Searching..."
    print("Searching...")
    search = SEARCH.get()
    if  SEARCH.get()!="":
        brandTree.delete(*brandTree.get_children())
        sql_search_data = "SELECT * FROM brands WHERE UPPER(brand_name) LIKE  '%' || UPPER(:s) || '%'"
        try:
            cursor.execute(sql_search_data, {'s': search})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            print(msg)
    fetch = cursor.fetchall()
    for data in fetch:
        brandTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()
    lbl_brandErr['text'] = "Searching Finished"
    print("Searching Finished...")

def Sortbrand():
    Database()
    BS=BRAND_SORT.get()
    if  BS=="BRAND_ID":
        brandTree.delete(*brandTree.get_children())
        sql_sort_data = "SELECT * FROM brands ORDER BY BRAND_ID"
        cursor.execute(sql_sort_data)
    elif BRAND_SORT.get()=="BRAND_NAME":
        brandTree.delete(*brandTree.get_children())
        sql_sort_data = "SELECT * FROM brands ORDER BY BRAND_NAME"
        cursor.execute(sql_sort_data)
    elif BRAND_SORT.get()=="BRAND_STATUS":
        brandTree.delete(*brandTree.get_children())
        sql_sort_data = "SELECT * FROM brands ORDER BY BRAND_STATUS"
        cursor.execute(sql_sort_data)
    fetch = cursor.fetchall()
    for data in fetch:
        brandTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def DeleteBrand():
    if not brandTree.selection():
        print("ERROR")
        lbl_brandErr['text'] = "Item not selected"
    else:
        curItem = brandTree.focus()
        content = (brandTree.item(curItem))
        selectedItem = content['values']
        brandTree.delete(curItem)
        Database()
        sql_delete_data = "DELETE FROM brands WHERE brand_name = :d"
        try:
            cursor.execute(sql_delete_data, {'d': selectedItem[1]})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
        conn.commit()
        cursor.close()
        conn.close()
        brandCount.clear()
        BrandCount()


def EditBrand():
    if not brandTree.selection():
        print("ERROR: NOT SELECTED")
        lbl_brandErr['text'] = "Item not selected"
    else:
        curItem = brandTree.focus()
        content = (brandTree.item(curItem))
        selectedItem = content['values']
        BRAND_NAME.set(selectedItem[1])
        BRAND_STATUS.set(selectedItem[2])
        EditBrandForm()


def UpdateBrand():
    bnm = (str(BRAND_NAME.get()))
    bst = (str(BRAND_STATUS.get()))

    Database()
    sql_update_data = "UPDATE brands SET brand_name= :bn, status= :st WHERE brand_name= :bn"
    try:
        cursor.execute(sql_update_data, {'bn': bnm, 'st': bst})
        lbl_brandErrEdit.config(fg="#2e5da3")
        lbl_brandErrEdit['text'] = "Data Updated Successfully!"
        print("Data Updated Successfully!")
        ResetBrandData()
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
        msg = str(exception)
        lbl_brandErrEdit['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()


def ResetBrandData():
    SEARCH.set("")
    BRAND_NAME.set("")
    BRAND_STATUS.set("SELECT")
    BRAND_SORT.set("SELECT")
    lbl_brandErr['text'] = ""
    brandTree.delete(*brandTree.get_children())
    ShowBrandData()


# ===============================================BRAND END HERE========================================================

# =============================================CATEGORY START HERE=====================================================
def Category():
    global categoryTree, lbl_categoryErr
    categoryWin = Toplevel()
    categoryWin.title("Inventory Management System")
    dwidth = 1080
    dheight = 800
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    categoryWin.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    categoryWin.resizable(0, 0)

    Label(categoryWin, text="Category", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    Label(categoryWin, text="Sort By    : ", font=('calibri', 14)).place(x=100, y=80)
    optionMenu_csort = ttk.Combobox(categoryWin, textvariable=CATEGORY_SORT)
    optionMenu_csort['values'] = category_sort
    optionMenu_csort.config(font=('calibri', 14), width=20)
    optionMenu_csort.place(x=200, y=82)
    Button(categoryWin, text="Sort", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=Sortcategory).place(x=420, y=78)

    Label(categoryWin, text="Search    : ", font=('calibri', 14)).place(x=640, y=80)
    entry_search = Entry(categoryWin, textvariable=SEARCH, font=('calibri', 14))
    entry_search.place(x=740, y=82)
    Button(categoryWin, text="Search", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=SearchCategory).place(x=960, y=78)

    spaceView = Frame(categoryWin)
    spaceView.pack(pady=20)

    btnView = Frame(categoryWin)
    btnView.pack(pady=40)

    btn_add = Button(btnView, text="Add", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                     width=10, height=1, cursor="hand2", command=AddCategoryForm)
    btn_add.grid(row=0, column=0, padx=30, pady=10)

    btn_edit = Button(btnView, text="Edit", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                      width=10, height=1, cursor="hand2", command=EditCategory)
    btn_edit.grid(row=0, column=1, padx=30, pady=10)

    btn_delete = Button(btnView, text="Delete", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                        width=10, height=1, cursor="hand2", command=DeleteCategory)
    btn_delete.grid(row=0, column=2, padx=30, pady=10)

    btn_reset = Button(btnView, text="Reset", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                       width=10, height=1, cursor="hand2", command=ResetCategoryData)
    btn_reset.grid(row=0, column=3, padx=30, pady=10)

    scrollbary = Scrollbar(categoryWin, orient=VERTICAL)

    style = ttk.Style(categoryWin)
    style.theme_use("default")
    style.configure("Treeview")
    style.configure("Treeview", highlightthickness=0, bd=0, font=('calibri', 12))
    style.configure("Treeview.Heading", font=('calibri', 12, 'bold'), foreground="#fff", background="#2e5da3")

    categoryTree = ttk.Treeview(categoryWin, columns=("Category ID", "Category Name", "Status"), style="Treeview",
                                selectmode="extended", yscrollcommand=scrollbary.set)
    scrollbary.config(command=categoryTree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    categoryTree.heading('Category ID', text="CATEGORY ID", anchor=CENTER)
    categoryTree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    categoryTree.heading('Category Name', text="CATEGORY NAME", anchor=CENTER)
    categoryTree.column('#1', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    categoryTree.heading('Status', text="STATUS", anchor=CENTER)
    categoryTree.column('#2', stretch=NO, minwidth=0, width=500, anchor=CENTER)

    categoryTree.pack(fill="both", expand=True)
    lbl_categoryErr = Label(categoryWin, text="", font=('calibri', 14), bg="#f2f2f2", fg="red")
    lbl_categoryErr.pack(fill=X, side=BOTTOM)
    ShowCategoryData()


def AddCategoryForm():
    CATEGORY_ID.set("")
    CATEGORY_NAME.set("")
    CATEGORY_STATUS.set("SELECT")
    global lbl_categoryErrAdd
    addCategoryWin = Toplevel()
    addCategoryWin.title("Inventory Management System")
    width = 640
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addCategoryWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addCategoryWin.resizable(0, 0)

    Label(addCategoryWin, text="+ Add Category", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=20)
    lbl_categoryId = Label(addCategoryWin, text="Category ID     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_categoryId = Entry(addCategoryWin, textvariable=CATEGORY_ID, width=30, font=('calibri', 14))
    lbl_categoryName = Label(addCategoryWin, text="Category Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_categoryName = Entry(addCategoryWin, textvariable=CATEGORY_NAME, width=30, font=('calibri', 14))
    lbl_categoryStatus = Label(addCategoryWin, text="Status       :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_categoryStatus = ttk.Combobox(addCategoryWin, textvariable=CATEGORY_STATUS)
    optionMenu_categoryStatus['values'] = status
    optionMenu_categoryStatus.config(font=('calibri', 14), width=29)
    lbl_categoryErrAdd = Label(addCategoryWin, text="", font=('calibri', 14), fg="red")

    btn_saveBrand = Button(addCategoryWin, text="Save", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=InsertCategory)
    
    lbl_categoryId.place(x=100, y=100)
    entry_categoryId.place(x=230, y=100)
    lbl_categoryName.place(x=80, y=150)
    entry_categoryName.place(x=230, y=150)
    lbl_categoryStatus.place(x=120, y=200)
    optionMenu_categoryStatus.place(x=230, y=200)
    btn_saveBrand.place(x=230, y=270)
    lbl_categoryErrAdd.pack(fill=X, side=BOTTOM)
    optionMenu_categoryStatus.current()


def EditCategoryForm():
    global lbl_categoryErrEdit
    editCategoryWin = Toplevel()
    editCategoryWin.title("Inventory Management System")
    width = 640
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    editCategoryWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    editCategoryWin.resizable(0, 0)

    Label(editCategoryWin, text="+ Edit Category", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=20)

    lbl_brandName = Label(editCategoryWin, text="Brand Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_brandName = Entry(editCategoryWin, textvariable=CATEGORY_NAME, width=30, font=('calibri', 14), fg="#000",
                            state=DISABLED)
    lbl_brandStatus = Label(editCategoryWin, text="Status       :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_brandStatus = ttk.Combobox(editCategoryWin, textvariable=CATEGORY_STATUS)
    optionMenu_brandStatus['values'] = status
    optionMenu_brandStatus.config(font=('calibri', 14), width=29)
    lbl_categoryErrEdit = Label(editCategoryWin, text="", font=('calibri', 14), fg="red")

    btn_updateBrand = Button(editCategoryWin, text="Update", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                             font=('calibri', 12, 'bold'), width=20, height=1, cursor="hand2", command=UpdateCategory)

    lbl_brandName.place(x=80, y=100)
    entry_brandName.place(x=230, y=100)
    lbl_brandStatus.place(x=120, y=150)
    optionMenu_brandStatus.place(x=230, y=150)
    btn_updateBrand.place(x=230, y=220)
    lbl_categoryErrEdit.pack(fill=X, side=BOTTOM)
    optionMenu_brandStatus.current()


# FUNCTIONS FOR CATEGORY
def ShowCategoryData():
    Database()
    try:
        cursor.execute("SELECT * FROM category ORDER BY category_id")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        categoryTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def InsertCategory():
    Database()
    cid=(float(CATEGORY_ID.get()))
    cname = (str(CATEGORY_NAME.get()))
    cst = (str(CATEGORY_STATUS.get()))

    if CATEGORY_STATUS.get() == "SELECT":
        lbl_categoryErrAdd['text'] = "Choose required field!"
    elif CATEGORY_NAME.get() == "":
        lbl_categoryErrAdd['text'] = "Brand name can't be empty!"
    else:
        sql_insert_data = "INSERT INTO category (category_id,category_name, status) VALUES (:c_id,:bname, :bstatus)"
        try:
            cursor.execute(sql_insert_data, {'c_id':cid,'bname': cname, 'bstatus': cst})
            CATEGORY_ID.set("")
            CATEGORY_NAME.set("")
            CATEGORY_STATUS.set("SELECT")
            lbl_categoryErrAdd.config(fg="#2e5da3")
            lbl_categoryErrAdd['text'] = "Data Added Successfully"
            print("Data Added Successfully!")
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            lbl_categoryErrAdd['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()
    ResetCategoryData()


def SearchCategory():
    Database()
    lbl_categoryErr.config(fg="#2e5da3")
    lbl_categoryErr['text'] = "Searching..."
    print("Searching...")
    search = SEARCH.get()
    if SEARCH.get() != "":
        categoryTree.delete(*categoryTree.get_children())
        sql_search_data = "SELECT * FROM category WHERE UPPER(category_name) LIKE  '%' || UPPER(:s) || '%'"
        try:
            cursor.execute(sql_search_data, {'s': search})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            print(msg)
        fetch = cursor.fetchall()
        for data in fetch:
            categoryTree.insert('', 'end', values=data)
        cursor.close()
        conn.close()
        lbl_categoryErr['text'] = "Searching Finished"
        print("Searching Finished...")

def Sortcategory():
    Database()
    CS=CATEGORY_SORT.get()
    if  CS=="CATEGORY_ID":
        categoryTree.delete(*categoryTree.get_children())
        sql_sort_data = "SELECT * FROM category ORDER BY CATEGORY_ID"
        cursor.execute(sql_sort_data)
    elif CS=="CATEGORY_NAME":
        categoryTree.delete(*categoryTree.get_children())
        sql_sort_data = "SELECT * FROM category ORDER BY CATEGORY_NAME"
        cursor.execute(sql_sort_data)
    elif CS=="CATEGORY_STATUS":
        categoryTree.delete(*categoryTree.get_children())
        sql_sort_data = "SELECT * FROM category ORDER BY STATUS"
        cursor.execute(sql_sort_data)
    fetch = cursor.fetchall()
    for data in fetch:
        categoryTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()

def DeleteCategory():
    if not categoryTree.selection():
        print("ERROR")
        lbl_categoryErr['text'] = "Item not selected"
    else:
        curItem = categoryTree.focus()
        content = (categoryTree.item(curItem))
        selectedItem = content['values']
        categoryTree.delete(curItem)
        Database()
        sql_delete_data = "DELETE FROM category WHERE category_name = :d"
        try:
            cursor.execute(sql_delete_data, {'d': selectedItem[1]})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
        conn.commit()
        cursor.close()
        conn.close()


def EditCategory():
    if not categoryTree.selection():
        print("ERROR: NOT SELECTED")
        lbl_categoryErr['text'] = "Item not selected"
    else:
        curItem = categoryTree.focus()
        content = (categoryTree.item(curItem))
        selectedItem = content['values']
        CATEGORY_NAME.set(selectedItem[1])
        CATEGORY_STATUS.set(selectedItem[2])
        EditCategoryForm()


def UpdateCategory():
    bnm = (str(CATEGORY_NAME.get()))
    bst = (str(CATEGORY_STATUS.get()))

    Database()
    sql_update_data = "UPDATE category SET category_name= :bn, status= :st WHERE category_name= :bn"
    try:
        cursor.execute(sql_update_data, {'bn': bnm, 'st': bst})
        lbl_categoryErrEdit.config(fg="#2e5da3")
        lbl_categoryErrEdit['text'] = "Data Updated Successfully!"
        print("Data Updated Successfully!")
        ResetCategoryData()
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
        msg = str(exception)
        lbl_categoryErrEdit['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()


def ResetCategoryData():
    SEARCH.set("")
    CATEGORY_NAME.set("")
    CATEGORY_STATUS.set("SELECT")
    CATEGORY_SORT.set("SELECT")
    lbl_categoryErr['text'] = ""
    categoryTree.delete(*categoryTree.get_children())
    ShowCategoryData()


# =============================================CATEGORY END HERE=======================================================

# ===============================================PRODUCTS START HERE===================================================
def Products():
    global lbl_productErr, productTree
    productdWin = Toplevel()
    productdWin.title("Inventory Management System")
    dwidth = 1080
    dheight = 800
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    productdWin.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    productdWin.resizable(0, 0)

    Label(productdWin, text="Products", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    Label(productdWin, text="Sort By    : ", font=('calibri', 14)).place(x=100, y=80)
    optionMenu_psort = ttk.Combobox(productdWin, textvariable=PRODUCT_SORT)
    optionMenu_psort['values'] = product_sort
    optionMenu_psort.config(font=('calibri', 14), width=20)
    optionMenu_psort.place(x=200, y=82)
    Button(productdWin, text="Sort", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=Sortproduct).place(x=420, y=78)

    Label(productdWin, text="Search    : ", font=('calibri', 14)).place(x=640, y=80)
    entry_search = Entry(productdWin, textvariable=SEARCH, font=('calibri', 14))
    entry_search.place(x=740, y=82)
    Button(productdWin, text="Search", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=SearchProduct).place(x=960, y=78)

    spaceView = Frame(productdWin)
    spaceView.pack(pady=20)

    btnView = Frame(productdWin)
    btnView.pack(pady=40)

    btn_add = Button(btnView, text="Add", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                     width=10, height=1, cursor="hand2", command=AddProductForm)
    btn_add.grid(row=0, column=0, padx=30, pady=10)

    btn_edit = Button(btnView, text="Edit", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                      width=10, height=1, cursor="hand2", command=EditProduct)
    btn_edit.grid(row=0, column=1, padx=30, pady=10)

    btn_delete = Button(btnView, text="Delete", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                        width=10, height=1, cursor="hand2", command=DeleteProduct)
    btn_delete.grid(row=0, column=2, padx=30, pady=10)

    btn_reset = Button(btnView, text="Reset", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                       width=10, height=1, cursor="hand2", command=ResetProductData)
    btn_reset.grid(row=0, column=3, padx=30, pady=10)

    scrollbarx = Scrollbar(productdWin, orient=HORIZONTAL)
    scrollbary = Scrollbar(productdWin, orient=VERTICAL)

    style = ttk.Style(productdWin)
    style.theme_use("default")
    style.configure("Treeview")
    style.configure("Treeview", highlightthickness=0, bd=0, font=('calibri', 12))
    style.configure("Treeview.Heading", font=('calibri', 12, 'bold'), foreground="#fff", background="#2e5da3")

    productTree = ttk.Treeview(productdWin, columns=("Product ID", "Product Name", "Quantity",
                                                     "Rate", "Brand", "Category", "Status"), style="Treeview",
                               selectmode="extended", xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

    scrollbary.config(command=productTree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    productTree.heading('Product ID', text="PRODUCT ID", anchor=CENTER)
    productTree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    productTree.heading('Product Name', text="PRODUCT NAME", anchor=CENTER)
    productTree.column('#1', stretch=NO, minwidth=0, width=150, anchor=CENTER)
    productTree.heading('Quantity', text="QUANTITY", anchor=CENTER)
    productTree.column('#2', stretch=NO, minwidth=0, width=400, anchor=CENTER)
    productTree.heading('Rate', text="RATE", anchor=CENTER)
    productTree.column('#3', stretch=NO, minwidth=0, width=200, anchor=CENTER)
    productTree.heading('Brand', text="BRAND", anchor=CENTER)
    productTree.column('#4', stretch=NO, minwidth=0, width=250, anchor=CENTER)
    productTree.heading('Category', text="CATEGORY", anchor=CENTER)
    productTree.column('#5', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    productTree.heading('Status', text="STATUS", anchor=CENTER)
    productTree.column('#6', stretch=NO, minwidth=0, width=300, anchor=CENTER)

    productTree.pack(fill="both", expand=True)
    scrollbarx.config(command=productTree.xview)
    scrollbarx.pack(padx=10, fill=X)
    lbl_productErr = Label(productdWin, text="", font=('calibri', 14), bg="#f2f2f2", fg="red")
    lbl_productErr.pack(fill=X, side=BOTTOM)
    ShowProductData()


def AddProductForm():
    PRODUCT_ID.set("")
    PRODUCT_NAME.set("")
    QUANTITY.set("")
    RATE.set("")
    PRODUCT_BRAND.set("SELECT")
    PRODUCT_CATEGORY.set("SELECT")
    PRODUCT_STATUS.set("SELECT")
    global lbl_productErrAdd
    addCategoryWin = Toplevel()
    addCategoryWin.title("Inventory Management System")
    width = 640
    height = 500
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addCategoryWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addCategoryWin.resizable(0, 0)

    brands.clear()
    category.clear()
    FetchBrands()
    FetchCategory()

    Label(addCategoryWin, text="+ Add Product", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=0)
    lbl_productID = Label(addCategoryWin, text="Product ID     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productID = Entry(addCategoryWin, textvariable=PRODUCT_ID, width=30, font=('calibri', 14))
    lbl_productName = Label(addCategoryWin, text="Product Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productName = Entry(addCategoryWin, textvariable=PRODUCT_NAME, width=30, font=('calibri', 14))
    lbl_productQuantity = Label(addCategoryWin, text="Quantity     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productQuantity = Entry(addCategoryWin, textvariable=QUANTITY, width=30, font=('calibri', 14))
    lbl_productRate = Label(addCategoryWin, text="Rate     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productRate = Entry(addCategoryWin, textvariable=RATE, width=30, font=('calibri', 14))
    lbl_productBrand = Label(addCategoryWin, text="Brand Name        :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_productBrand = ttk.Combobox(addCategoryWin, textvariable=PRODUCT_BRAND)
    optionMenu_productBrand['values'] = brands
    optionMenu_productBrand.config(font=('calibri', 14), width=29)

    lbl_productCategory = Label(addCategoryWin, text="Category Name      :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_productCategory = ttk.Combobox(addCategoryWin, textvariable=PRODUCT_CATEGORY)
    optionMenu_productCategory['values'] = category
    optionMenu_productCategory.config(font=('calibri', 14), width=29)

    lbl_productStatus = Label(addCategoryWin, text="Status       :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_productStatus = ttk.Combobox(addCategoryWin, textvariable=PRODUCT_STATUS)
    optionMenu_productStatus['values'] = status
    optionMenu_productStatus.config(font=('calibri', 14), width=29)

    btn_saveBrand = Button(addCategoryWin, text="Save", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=InsertProduct)

    lbl_productErrAdd = Label(addCategoryWin, text="", font=('calibri', 14), fg="red")
    lbl_productID.place(x=80,y=50)
    entry_productID.place(x=230,y=50)
    lbl_productName.place(x=70, y=100)
    entry_productName.place(x=230, y=100)
    lbl_productQuantity.place(x=115, y=150)
    entry_productQuantity.place(x=230, y=150)
    lbl_productRate.place(x=145, y=200)
    entry_productRate.place(x=230, y=200)
    lbl_productBrand.place(x=70, y=250)
    optionMenu_productBrand.place(x=230, y=250)
    lbl_productCategory.place(x=55, y=300)
    optionMenu_productCategory.place(x=230, y=300)
    lbl_productStatus.place(x=120, y=350)
    optionMenu_productStatus.place(x=230, y=350)

    btn_saveBrand.place(x=230, y=400)
    lbl_productErrAdd.pack(fill=X, side=BOTTOM)
    optionMenu_productBrand.current()
    optionMenu_productCategory.current()
    optionMenu_productStatus.current()


def EditProductForm():
    global lbl_productErrEdit
    editCategoryWin = Toplevel()
    editCategoryWin.title("Inventory Management System")
    width = 640
    height = 500
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    editCategoryWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    editCategoryWin.resizable(0, 0)

    FetchBrands()
    FetchCategory()

    Label(editCategoryWin, text="+ Add Product", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=20)
    
    lbl_productName = Label(editCategoryWin, text="Product Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productName = Entry(editCategoryWin, textvariable=PRODUCT_NAME, width=30, font=('calibri', 14),
                              state=DISABLED)
    lbl_productQuantity = Label(editCategoryWin, text="Quantity     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productQuantity = Entry(editCategoryWin, textvariable=QUANTITY, width=30, font=('calibri', 14))
    lbl_productRate = Label(editCategoryWin, text="Rate     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_productRate = Entry(editCategoryWin, textvariable=RATE, width=30, font=('calibri', 14))

    lbl_productBrand = Label(editCategoryWin, text="Brand Name        :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_productBrand = ttk.Combobox(editCategoryWin, textvariable=PRODUCT_BRAND)
    optionMenu_productBrand['values'] = brands
    optionMenu_productBrand.config(font=('calibri', 14), width=29)

    lbl_productCategory = Label(editCategoryWin, text="Category Name      :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_productCategory = ttk.Combobox(editCategoryWin, textvariable=PRODUCT_CATEGORY)
    optionMenu_productCategory['values'] = category
    optionMenu_productCategory.config(font=('calibri', 14), width=29)

    lbl_productStatus = Label(editCategoryWin, text="Status       :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_productStatus = ttk.Combobox(editCategoryWin, textvariable=PRODUCT_STATUS)
    optionMenu_productStatus['values'] = status
    optionMenu_productStatus.config(font=('calibri', 14), width=29)

    btn_saveBrand = Button(editCategoryWin, text="Save", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=UpdateProduct)

    lbl_productErrEdit = Label(editCategoryWin, text="", font=('calibri', 14), fg="red")

    lbl_productName.place(x=70, y=100)
    entry_productName.place(x=230, y=100)
    lbl_productQuantity.place(x=115, y=150)
    entry_productQuantity.place(x=230, y=150)
    lbl_productRate.place(x=145, y=200)
    entry_productRate.place(x=230, y=200)
    lbl_productBrand.place(x=70, y=250)
    optionMenu_productBrand.place(x=230, y=250)
    lbl_productCategory.place(x=55, y=300)
    optionMenu_productCategory.place(x=230, y=300)
    lbl_productStatus.place(x=120, y=350)
    optionMenu_productStatus.place(x=230, y=350)

    btn_saveBrand.place(x=230, y=400)
    lbl_productErrEdit.pack(fill=X, side=BOTTOM)
    optionMenu_productBrand.current()
    optionMenu_productCategory.current()
    optionMenu_productStatus.current()


# FUNCTIONS FOR CATEGORY
def ShowProductData():
    Database()
    try:
        cursor.execute("SELECT * FROM products ORDER BY product_id")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        productTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def InsertProduct():
    Database()
    p_id=(float(PRODUCT_ID.get()))
    pname = (str(PRODUCT_NAME.get()))
    qty = (int(QUANTITY.get()))
    rate = (float(RATE.get()))
    bname = (str(PRODUCT_BRAND.get()))
    bcat = (str(PRODUCT_CATEGORY.get()))
    cst = (str(PRODUCT_STATUS.get()))

    if PRODUCT_NAME.get() == "":
        lbl_productErrAdd['text'] = "Product name can't be empty!"
    elif QUANTITY.get() == "":
        lbl_productErrAdd['text'] = "Quantity can't be empty!"
    elif RATE.get() == "":
        lbl_productErrAdd['text'] = "Rate can't be empty!"
    elif PRODUCT_BRAND.get() == "SELECT":
        lbl_productErrAdd['text'] = "Choose required field!"
    elif PRODUCT_CATEGORY.get() == "SELECT":
        lbl_productErrAdd['text'] = "Choose required field!"
    elif PRODUCT_STATUS.get() == "SELECT":
        lbl_productErrAdd['text'] = "Choose required field!"
    else:
        sql_insert_data = "INSERT INTO products (product_id,product_name, quantity, rate, product_brand, product_category, " \
                          "status) VALUES (:pid,:pname, :qty, :rate, :pbrand, :pcat, :bstatus) "
        try:
            cursor.execute(sql_insert_data, {'pid':p_id, 'pname': pname, 'qty': qty, 'rate': rate,
                                             'pbrand': bname, 'pcat': bcat, 'bstatus': cst})
            PRODUCT_ID.set("")
            PRODUCT_NAME.set("")
            QUANTITY.set("")
            RATE.set("")
            PRODUCT_BRAND.set("SELECT")
            PRODUCT_CATEGORY.set("SELECT")
            PRODUCT_STATUS.set("SELECT")
            lbl_productErrAdd.config(fg="#2e5da3")
            lbl_productErrAdd['text'] = "Data Added Successfully"
            print("Data Added Successfully!")
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            lbl_productErrAdd['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()
    ResetProductData()
    productCount.clear()
    ProductCount()


def SearchProduct():
    Database()
    lbl_productErr.config(fg="#2e5da3")
    lbl_productErr['text'] = "Searching..."
    print("Searching...")
    search = SEARCH.get()
    if SEARCH.get() != "":
        productTree.delete(*productTree.get_children())
        sql_search_data = "SELECT * FROM products WHERE UPPER(product_name) LIKE  '%' || UPPER(:s) || '%'"
        try:
            cursor.execute(sql_search_data, {'s': search})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            print(msg)
        fetch = cursor.fetchall()
        for data in fetch:
            productTree.insert('', 'end', values=data)
        cursor.close()
        conn.close()
        lbl_productErr['text'] = "Searching Finished"
        print("Searching Finished...")
def Sortproduct():
    Database()
    PS=PRODUCT_SORT.get()
    if  PS=="PRODUCT_ID":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY PRODUCT_ID"
        cursor.execute(sql_sort_data)
    elif PS=="PRODUCT_NAME":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY PRODUCT_NAME"
        cursor.execute(sql_sort_data)
    elif PS=="QUANTITY":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY QUANTITY"
        cursor.execute(sql_sort_data)
    elif PS=="RATE":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY RATE"
        cursor.execute(sql_sort_data)  
    elif PS=="PRODUCT_BRAND":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY PRODUCT_BRAND"
        cursor.execute(sql_sort_data)
    elif PS=="PRODUCT_CATEGORY":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY PRODUCT_CATEGORY"
        cursor.execute(sql_sort_data)
    elif PS=="STATUS":
        productTree.delete(*productTree.get_children())
        sql_sort_data = "SELECT * FROM products ORDER BY STATUS"
        cursor.execute(sql_sort_data) 
    fetch = cursor.fetchall()
    for data in fetch:
        productTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()

def DeleteProduct():
    if not productTree.selection():
        print("ERROR")
        lbl_productErr['text'] = "Item not selected"
    else:
        curItem = productTree.focus()
        content = (productTree.item(curItem))
        selectedItem = content['values']
        productTree.delete(curItem)
        Database()
        sql_delete_data = "DELETE FROM products WHERE product_name = :d"
        try:
            cursor.execute(sql_delete_data, {'d': selectedItem[1]})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
        conn.commit()
        cursor.close()
        conn.close()
        productCount.clear()
        ProductCount()


def EditProduct():
    if not productTree.selection():
        print("ERROR: NOT SELECTED")
        lbl_productErr['text'] = "Item not selected"
    else:
        curItem = productTree.focus()
        content = (productTree.item(curItem))
        selectedItem = content['values']
        PRODUCT_NAME.set(selectedItem[1])
        QUANTITY.set(selectedItem[2])
        RATE.set(selectedItem[3])
        PRODUCT_BRAND.set(selectedItem[4])
        PRODUCT_CATEGORY.set(selectedItem[5])
        PRODUCT_STATUS.set(selectedItem[6])
        EditProductForm()


def UpdateProduct():
    pname = (str(PRODUCT_NAME.get()))
    qty = (int(QUANTITY.get()))
    rate = (float(RATE.get()))
    bname = (str(PRODUCT_BRAND.get()))
    bcat = (str(PRODUCT_CATEGORY.get()))
    cst = (str(PRODUCT_STATUS.get()))

    Database()
    sql_update_data = "UPDATE products SET product_name = :bn, quantity = :qty, rate = :rate, product_brand = :brand," \
                      "product_category = :cat,  status = :st WHERE product_name = :bn"
    try:
        cursor.execute(sql_update_data, {'bn': pname, 'qty': qty, 'rate': rate, 'brand': bname, 'cat': bcat, 'st': cst})
        lbl_productErrEdit.config(fg="#2e5da3")
        lbl_productErrEdit['text'] = "Data Updated Successfully!"
        print("Data Updated Successfully!")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
        msg = str(exception)
        lbl_productErrEdit['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()
    ResetProductData()


def ResetProductData():
    SEARCH.set("")
    PRODUCT_NAME.set("")
    QUANTITY.set("")
    RATE.set("")
    PRODUCT_BRAND.set("SELECT")
    PRODUCT_CATEGORY.set("SELECT")
    PRODUCT_STATUS.set("SELECT")
    PRODUCT_SORT.set("SELECT")
    lbl_productErr['text'] = ""
    productTree.delete(*productTree.get_children())
    ShowProductData()


# ==============================================PRODUCT END HERE=======================================================


# ================================================ORDER START HERE=====================================================
def Orders():
    global orderTree, lbl_orderErr
    orderWin = Toplevel()
    orderWin.title("Inventory Management System")
    dwidth = 1080
    dheight = 800
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    orderWin.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    orderWin.resizable(0, 0)

    Label(orderWin, text="Orders", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)
    
    Label(orderWin, text="Sort By    : ", font=('calibri', 14)).place(x=100, y=80)
    optionMenu_osort = ttk.Combobox(orderWin, textvariable=ORDER_SORT)
    optionMenu_osort['values'] = order_sort
    optionMenu_osort.config(font=('calibri', 14), width=20)
    optionMenu_osort.place(x=200, y=82)
    Button(orderWin, text="Sort", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=Sortorder).place(x=420, y=78)
    
    Label(orderWin, text="Search    : ", font=('calibri', 14)).place(x=640, y=80)
    entry_search = Entry(orderWin, textvariable=SEARCH, font=('calibri', 14))
    entry_search.place(x=740, y=82)
    Button(orderWin, text="Search", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12),
           width=8, height=1, cursor="hand2", command=SearchOrder).place(x=960, y=78)

    spaceView = Frame(orderWin)
    spaceView.pack(pady=20)

    btnView = Frame(orderWin)
    btnView.pack(pady=40)

    btn_add = Button(btnView, text="Add", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                     width=10, height=1, cursor="hand2", command=AddOrderForm)
    btn_add.grid(row=0, column=0, padx=30, pady=10)

    btn_edit = Button(btnView, text="Edit", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                      width=10, height=1, cursor="hand2", command=EditOrder)
    btn_edit.grid(row=0, column=1, padx=30, pady=10)

    btn_delete = Button(btnView, text="Delete", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                        width=10, height=1, cursor="hand2", command=DeleteOrder)
    btn_delete.grid(row=0, column=2, padx=30, pady=10)

    btn_reset = Button(btnView, text="Reset", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                       width=10, height=1, cursor="hand2", command=ResetOrderData)
    btn_reset.grid(row=0, column=3, padx=30, pady=10)

    scrollbarx = Scrollbar(orderWin, orient=HORIZONTAL)
    scrollbary = Scrollbar(orderWin, orient=VERTICAL)

    style = ttk.Style(orderWin)
    style.theme_use("default")
    style.configure("Treeview")
    style.configure("Treeview", highlightthickness=0, bd=0, font=('calibri', 12))
    style.configure("Treeview.Heading", font=('calibri', 12, 'bold'), foreground="#fff", background="#2e5da3")

    orderTree = ttk.Treeview(orderWin, columns=("Order ID", "Date", "Client Name", "Contact No.", "Product", "Quantity",
                                                "Total Amount", "Paid Amount", "Due Amount", "Payment Status"),
                             style="Treeview", selectmode="extended",
                             xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

    scrollbary.config(command=orderTree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)

    orderTree.heading('Order ID', text="ORDER ID", anchor=CENTER)
    orderTree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    orderTree.heading('Date', text="DATE", anchor=CENTER)
    orderTree.column('#1', stretch=NO, minwidth=0, width=150, anchor=CENTER)
    orderTree.heading('Client Name', text="CLIENT NAME", anchor=CENTER)
    orderTree.column('#2', stretch=NO, minwidth=0, width=200, anchor=CENTER)
    orderTree.heading('Contact No.', text="CONTACT NO", anchor=CENTER)
    orderTree.column('#3', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    orderTree.heading('Product', text="PRODUCT", anchor=CENTER)
    orderTree.column('#4', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    orderTree.heading('Quantity', text="QUANTITY", anchor=CENTER)
    orderTree.column('#5', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    orderTree.heading('Total Amount', text="TOTAL AMOUNT", anchor=CENTER)
    orderTree.column('#6', stretch=NO, minwidth=0, width=200, anchor=CENTER)
    orderTree.heading('Paid Amount', text="PAID AMOUNT", anchor=CENTER)
    orderTree.column('#7', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    orderTree.heading('Due Amount', text="DUE AMOUNT", anchor=CENTER)
    orderTree.column('#8', stretch=NO, minwidth=0, width=300, anchor=CENTER)
    orderTree.heading('Payment Status', text="PAYMENT STATUS", anchor=CENTER)
    orderTree.column('#9', stretch=NO, minwidth=0, width=300, anchor=CENTER)

    orderTree.pack(fill="both", expand=True)
    scrollbarx.config(command=orderTree.xview)
    scrollbarx.pack(padx=10, fill=X)
    lbl_orderErr = Label(orderTree, text="", font=('calibri', 14), bg="#f2f2f2", fg="red")
    lbl_orderErr.pack(fill=X, side=BOTTOM)
    ShowOrderData()


def AddOrderForm():
    global lbl_orderErrAdd
    ORDER_ID.set("")
    CLIENT_NAME.set("")
    CLIENT_N0.set("")
    PRODUCT_NAME.set("SELECT")
    QUANTITY.set("0")
    RATE.set("0.0")
    TOTAL.set("0.0")
    SUB_AMOUNT.set("0.0")
    TOTAL_AMOUNT.set("0.0")
    PAID_AMOUNT.set("0.0")
    DUE_AMOUNT.set("0.0")
    GST.set("0.0")
    PAYMENT_STATUS.set("SELECT")

    addOrderWin = Toplevel()
    addOrderWin.title("Inventory Management System")
    width = 940
    height = 640
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addOrderWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addOrderWin.resizable(0, 0)

    brands.clear()
    category.clear()
    products.clear()
    FetchBrands()
    FetchCategory()
    FetchProducts()

    Label(addOrderWin, text="+ Add Order", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=0)
    lbl_orderID = Label(addOrderWin, text="Order ID     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_orderID = Entry(addOrderWin, textvariable=ORDER_ID, width=65, font=('calibri', 14))
    lbl_orderDate = Label(addOrderWin, text="Order Date  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_orderDate = DateEntry(addOrderWin, textvariable=ORDER_DATE, width=64, font=('calibri', 14), year=202)
    lbl_clientName = Label(addOrderWin, text="Client Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_clientName = Entry(addOrderWin, textvariable=CLIENT_NAME, width=65, font=('calibri', 14))
    lbl_clientNo = Label(addOrderWin, text="Contact No  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_clientNo = Entry(addOrderWin, textvariable=CLIENT_N0, width=65, font=('calibri', 14))
    lbl_product = Label(addOrderWin, text="Product  :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_product = ttk.Combobox(addOrderWin, textvariable=PRODUCT_NAME)
    optionMenu_product['values'] = products
    optionMenu_product.config(font=('calibri', 14), width=19)
    lbl_rate = Label(addOrderWin, text="Rate  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_rate = Entry(addOrderWin, textvariable=RATE, width=20, font=('calibri', 14), state=DISABLED)

    lbl_quantity = Label(addOrderWin, text="Quantity  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_quantity = Entry(addOrderWin, textvariable=QUANTITY, width=20, font=('calibri', 14))
    lbl_total = Label(addOrderWin, text="Total  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_total = Entry(addOrderWin, textvariable=TOTAL, width=20, font=('calibri', 14), state=DISABLED)

    lbl_subAmount = Label(addOrderWin, text="Sub Amount  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_subAmount = Entry(addOrderWin, textvariable=SUB_AMOUNT, width=20, font=('calibri', 14), state=DISABLED)
    lbl_paidAmount = Label(addOrderWin, text="Paid  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_paidAmount = Entry(addOrderWin, textvariable=PAID_AMOUNT, width=20, font=('calibri', 14))

    lbl_GST = Label(addOrderWin, text="GST 12%     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_GST = Entry(addOrderWin, textvariable=GST, width=20, font=('calibri', 14), state=DISABLED)
    lbl_dueAmount = Label(addOrderWin, text="Dues     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_dueAmount = Entry(addOrderWin, textvariable=DUE_AMOUNT, width=20, font=('calibri', 14), state=DISABLED)

    lbl_totalAmount = Label(addOrderWin, text="Total Amount  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_totalAmount = Entry(addOrderWin, textvariable=TOTAL_AMOUNT, width=20, font=('calibri', 14), state=DISABLED)
    lbl_paymentStatus = Label(addOrderWin, text="Payment Status  :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_paymentStatus = ttk.Combobox(addOrderWin, textvariable=PAYMENT_STATUS)
    optionMenu_paymentStatus['values'] = paymentStatus
    optionMenu_paymentStatus.config(font=('calibri', 14), width=19)

    btn_saveBrand = Button(addOrderWin, text="Save", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", width=20,
                           font=('calibri', 12, 'bold'), height=1, cursor="hand2", command=InsertOrder)

    btn_calculate = Button(addOrderWin, text="Calculate", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", width=20,
                           font=('calibri', 12, 'bold'), height=1, cursor="hand2", command=GetRate)
    lbl_orderErrAdd = Label(addOrderWin, text="", font=('calibri', 14), fg="red")

    lbl_orderID.place(x=50,y=50)
    entry_orderID.place(x=200,y=50)
    lbl_orderDate.place(x=50, y=100)
    entry_orderDate.place(x=200, y=100)
    lbl_clientName.place(x=50, y=150)
    entry_clientName.place(x=200, y=150)
    lbl_clientNo.place(x=50, y=200)
    entry_clientNo.place(x=200, y=200)

    lbl_product.place(x=50, y=250)
    optionMenu_product.place(x=200, y=250)
    lbl_rate.place(x=480, y=250)
    entry_rate.place(x=650, y=250)

    lbl_quantity.place(x=50, y=300)
    entry_quantity.place(x=200, y=300)
    lbl_total.place(x=480, y=300)
    entry_total.place(x=650, y=300)

    lbl_subAmount.place(x=50, y=350)
    entry_subAmount.place(x=200, y=350)
    lbl_paidAmount.place(x=480, y=350)
    entry_paidAmount.place(x=650, y=350)

    lbl_GST.place(x=50, y=400)
    entry_GST.place(x=200, y=400)
    lbl_dueAmount.place(x=480, y=400)
    entry_dueAmount.place(x=650, y=400)

    lbl_totalAmount.place(x=50, y=450)
    entry_totalAmount.place(x=200, y=450)
    lbl_paymentStatus.place(x=480, y=450)
    optionMenu_paymentStatus.place(x=650, y=450)
    optionMenu_paymentStatus.current()

    btn_saveBrand.place(x=300, y=550)
    btn_calculate.place(x=500, y=550)
    lbl_orderErrAdd.pack(fill=X, side=BOTTOM)
    optionMenu_product.current()


def EditOrderForm():
    global lbl_orderErrEdit

    editOrderWin = Toplevel()
    editOrderWin.title("Inventory Management System")
    width = 940
    height = 640
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    editOrderWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    editOrderWin.resizable(0, 0)

    brands.clear()
    category.clear()
    products.clear()
    FetchBrands()
    FetchCategory()
    FetchProducts()

    Label(editOrderWin, text="+ Edit Order", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=20)

    lbl_orderDate = Label(editOrderWin, text="Order Date  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_orderDate = DateEntry(editOrderWin, textvariable=ORDER_DATE, width=64, font=('calibri', 14),
                                year=2023, state=DISABLED)
    lbl_clientName = Label(editOrderWin, text="Client Name     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_clientName = Entry(editOrderWin, textvariable=CLIENT_NAME, width=65, font=('calibri', 14))
    lbl_clientNo = Label(editOrderWin, text="Contact No  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_clientNo = Entry(editOrderWin, textvariable=CLIENT_N0, width=65, font=('calibri', 14))

    lbl_product = Label(editOrderWin, text="Product  :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_product = ttk.Combobox(editOrderWin, textvariable=PRODUCT_NAME, state=DISABLED)
    optionMenu_product['values'] = products
    optionMenu_product.config(font=('calibri', 14), width=19)
    lbl_rate = Label(editOrderWin, text="Rate  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_rate = Entry(editOrderWin, textvariable=RATE, width=20, font=('calibri', 14), state=DISABLED)

    lbl_quantity = Label(editOrderWin, text="Quantity  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_quantity = Entry(editOrderWin, textvariable=QUANTITY, width=20, font=('calibri', 14), state='readonly')
    lbl_total = Label(editOrderWin, text="Total  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_total = Entry(editOrderWin, textvariable=TOTAL, width=20, font=('calibri', 14), state=DISABLED)

    lbl_subAmount = Label(editOrderWin, text="Sub Amount  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_subAmount = Entry(editOrderWin, textvariable=SUB_AMOUNT, width=20, font=('calibri', 14), state=DISABLED)
    lbl_paidAmount = Label(editOrderWin, text="Paid  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_paidAmount = Entry(editOrderWin, textvariable=PAID_AMOUNT, width=20, font=('calibri', 14))

    lbl_GST = Label(editOrderWin, text="GST 12%     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_GST = Entry(editOrderWin, textvariable=GST, width=20, font=('calibri', 14), state=DISABLED)
    lbl_dueAmount = Label(editOrderWin, text="Dues     :   ", font=('calibri', 14), fg="#2e5da3")
    entry_dueAmount = Entry(editOrderWin, textvariable=DUE_AMOUNT, width=20, font=('calibri', 14), state=DISABLED)

    lbl_totalAmount = Label(editOrderWin, text="Total Amount  :   ", font=('calibri', 14), fg="#2e5da3")
    entry_totalAmount = Entry(editOrderWin, textvariable=TOTAL_AMOUNT, width=20, font=('calibri', 14), state=DISABLED)
    lbl_paymentStatus = Label(editOrderWin, text="Payment Status  :   ", font=('calibri', 14), fg="#2e5da3")
    optionMenu_paymentStatus = ttk.Combobox(editOrderWin, textvariable=PAYMENT_STATUS)
    optionMenu_paymentStatus['values'] = paymentStatus
    optionMenu_paymentStatus.config(font=('calibri', 14), width=19)

    btn_saveBrand = Button(editOrderWin, text="Save", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", width=20,
                           font=('calibri', 12, 'bold'), height=1, cursor="hand2", command=UpdateOrder)

    btn_calculate = Button(editOrderWin, text="Calculate", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", width=20,
                           font=('calibri', 12, 'bold'), height=1, cursor="hand2", command=GetRate)

    btn_print = Button(editOrderWin, text="Print", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", width=20,
                       font=('calibri', 12, 'bold'), height=1, cursor="hand2", command=PrintInvoice)

    lbl_orderErrEdit = Label(editOrderWin, text="", font=('calibri', 14), fg="red")

    lbl_orderDate.place(x=50, y=100)
    entry_orderDate.place(x=200, y=100)
    lbl_clientName.place(x=50, y=150)
    entry_clientName.place(x=200, y=150)
    lbl_clientNo.place(x=50, y=200)
    entry_clientNo.place(x=200, y=200)

    lbl_product.place(x=50, y=250)
    optionMenu_product.place(x=200, y=250)
    lbl_rate.place(x=480, y=250)
    entry_rate.place(x=650, y=250)

    lbl_quantity.place(x=50, y=300)
    entry_quantity.place(x=200, y=300)
    lbl_total.place(x=480, y=300)
    entry_total.place(x=650, y=300)

    lbl_subAmount.place(x=50, y=350)
    entry_subAmount.place(x=200, y=350)
    lbl_paidAmount.place(x=480, y=350)
    entry_paidAmount.place(x=650, y=350)

    lbl_GST.place(x=50, y=400)
    entry_GST.place(x=200, y=400)
    lbl_dueAmount.place(x=480, y=400)
    entry_dueAmount.place(x=650, y=400)

    lbl_totalAmount.place(x=50, y=450)
    entry_totalAmount.place(x=200, y=450)
    lbl_paymentStatus.place(x=480, y=450)
    optionMenu_paymentStatus.place(x=650, y=450)
    optionMenu_paymentStatus.current()

    btn_calculate.place(x=200, y=550)
    btn_saveBrand.place(x=400, y=550)
    btn_print.place(x=600, y=550)
    lbl_orderErrEdit.pack(fill=X, side=BOTTOM)
    optionMenu_product.current()


# FUNCTIONS FOR CATEGORY
def ShowOrderData():
    Database()
    try:
        cursor.execute("SELECT order_id, TO_CHAR(order_date, 'mm/dd/yy'), client_name, client_no, product, quantity,"
                       "total_amount, paid_amount, due_amount, payment_status FROM orders ORDER BY order_date DESC")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        orderTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def InsertOrder():
    Database()
    o_id=(float(ORDER_ID.get()))
    odate = (str(ORDER_DATE.get()))
    cname = (str(CLIENT_NAME.get()))
    cno = (str(CLIENT_N0.get()))
    pname = (str(PRODUCT_NAME.get()))
    qty = (int(QUANTITY.get()))
    tamount = (float(TOTAL_AMOUNT.get()))
    pamount = (float(PAID_AMOUNT.get()))
    damount = (float(DUE_AMOUNT.get()))
    pst = (str(PAYMENT_STATUS.get()))

    if ORDER_ID.get()=="":
        lbl_orderErrAdd['text'] = "ID can't be empty!"
    elif ORDER_DATE.get() == "":
        lbl_orderErrAdd['text'] = "Date can't be empty!"
    elif CLIENT_NAME.get() == "":
        lbl_orderErrAdd['text'] = "Client Name can't be empty!"
    elif CLIENT_N0.get() == "":
        lbl_orderErrAdd['text'] = "Client No. can't be empty!"
    elif len(CLIENT_N0.get()) != 10:
        lbl_orderErrAdd['text'] = "Contact no. must be of 10 digits!"
    elif PRODUCT_NAME.get() == "SELECT":
        lbl_orderErrAdd['text'] = "Choose required field!"
    elif QUANTITY.get() == "0":
        lbl_orderErrAdd['text'] = "Quantity can't be empty!"
    elif PAYMENT_STATUS.get() == "SELECT":
        lbl_orderErrAdd['text'] = "Choose required field!"
    else:
        sql_insert_data = "INSERT INTO orders (order_id,order_date, client_name, client_no, product, quantity, " \
                          "total_amount, paid_amount, due_amount, payment_status) VALUES (:oid,TO_DATE(:dt, 'mm/dd/yy')," \
                          ":cn, :cno, :prd, :qty, :tam, :pam, :dam, :st)"

        sql_update_qty = "UPDATE products SET quantity = (quantity - :qty) WHERE product_name = :bn"
        try:
            cursor.execute(sql_insert_data, {'oid':o_id,'dt': odate, 'cn': cname, 'cno': cno, 'prd': pname,
                                             'qty': qty, 'tam': tamount, 'pam': pamount, 'dam': damount, 'st': pst})
            cursor.execute(sql_update_qty, {'qty': qty, 'bn': pname})
            ORDER_ID.set("")
            ORDER_DATE.set("")
            CLIENT_NAME.set("")
            CLIENT_N0.set("")
            QUANTITY.set("0")
            TOTAL.set("0.0")
            SUB_AMOUNT.set("0.0")
            TOTAL_AMOUNT.set("0.0")
            PAID_AMOUNT.set("0.0")
            DUE_AMOUNT.set("0.0")
            GST.set("0.0")
            PAYMENT_STATUS.set("SELECT")

            lbl_orderErrAdd.config(fg="#2e5da3")
            lbl_orderErrAdd['text'] = "Data Added Successfully"
            print("Data Added Successfully!")
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            lbl_orderErrAdd['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()
    ResetOrderData()
    orderCount.clear()
    OrderCount()


def SearchOrder():
    Database()
    print("Searching...")
    search = SEARCH.get()
    if SEARCH.get() != "":
        orderTree.delete(*orderTree.get_children())
        sql_search_data = "SELECT * FROM orders WHERE UPPER(client_name) LIKE  '%' || UPPER(:s) || '%'"
        try:
            cursor.execute(sql_search_data, {'s': search})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            print(msg)
        fetch = cursor.fetchall()
        for data in fetch:
            orderTree.insert('', 'end', values=data)
        cursor.close()
        conn.close()
        lbl_orderErr['text'] = "Searching Finished"
        print("Searching Finished...")

def Sortorder():
    Database()
    OS=ORDER_SORT.get()
    if  OS=="ORDER_DATE":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY ORDER_DATE"
        cursor.execute(sql_sort_data)
    elif OS=="ORDER_ID":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY ORDER_ID"
        cursor.execute(sql_sort_data)
    elif OS=="CLIENT_NAME":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY CLIENT_NAME"
        cursor.execute(sql_sort_data)
    elif OS=="CLIENT_NO":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY CLIENT_NO"
        cursor.execute(sql_sort_data)  
    elif OS=="PRODUCT":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY PRODUCT"
        cursor.execute(sql_sort_data)
    elif OS=="QUANTITY":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY QUANTITY"
        cursor.execute(sql_sort_data)
    elif OS=="TOTAL_AMOUNT":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY TOTAL_AMOUNT"
        cursor.execute(sql_sort_data) 
    elif OS=="PAID_AMOUNT":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY PAID_AMOUNT"
        cursor.execute(sql_sort_data) 
    elif OS=="DUE_AMOUNT":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY DUE_AMOUNT"
        cursor.execute(sql_sort_data)
    elif OS=="PAYMENT_STATUS":
        orderTree.delete(*orderTree.get_children())
        sql_sort_data = "SELECT * FROM orders ORDER BY PAYMENT_STATUS"
        cursor.execute(sql_sort_data) 
    fetch = cursor.fetchall()
    for data in fetch:
        orderTree.insert('', 'end', values=data)
    cursor.close()
    conn.close()

def DeleteOrder():
    if not orderTree.selection():
        print("ERROR")
        lbl_orderErr['text'] = "Item not selected"
    else:
        curItem = orderTree.focus()
        content = (orderTree.item(curItem))
        selectedItem = content['values']
        orderTree.delete(curItem)
        Database()
        sql_delete_data = "DELETE FROM orders WHERE order_id = :d"
        sql_update_qty = "UPDATE products SET quantity = (quantity + :qty) WHERE product_name = :bn"
        try:
            cursor.execute(sql_delete_data, {'d': selectedItem[0]})
            cursor.execute(sql_update_qty, {'qty': selectedItem[5], 'bn': selectedItem[4]})
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
        conn.commit()
        cursor.close()
        conn.close()
        orderCount.clear()
        OrderCount()


def EditOrder():
    global order_id
    if not orderTree.selection():
        print("ERROR: NOT SELECTED")
        lbl_orderErr['text'] = "Item not selected"
    else:
        curItem = orderTree.focus()
        content = (orderTree.item(curItem))
        selectedItem = content['values']
        order_id = selectedItem[0]
        ORDER_DATE.set(selectedItem[1])
        CLIENT_NAME.set(selectedItem[2])
        CLIENT_N0.set(selectedItem[3])
        PRODUCT_NAME.set(selectedItem[4])
        QUANTITY.set(selectedItem[5])
        TOTAL_AMOUNT.set(selectedItem[6])
        PAID_AMOUNT.set(selectedItem[7])
        DUE_AMOUNT.set(selectedItem[8])
        PAYMENT_STATUS.set(selectedItem[9])
        GetRate()
        EditOrderForm()


def UpdateOrder():
    cname = (str(CLIENT_NAME.get()))
    cno = (str(CLIENT_N0.get()))
    pamount = (float(PAID_AMOUNT.get()))
    damount = (float(DUE_AMOUNT.get()))
    pst = (str(PAYMENT_STATUS.get()))

    Database()
    sql_update_data = "UPDATE orders SET client_name = :cname, client_no = :cno, " \
                      "paid_amount = :paid, due_amount = :dues, payment_status = :pst WHERE order_id = :id"
    try:
        cursor.execute(sql_update_data, {'cname': cname, 'cno': cno, 'paid': pamount, 'dues': damount,
                                         'pst': pst, 'id': order_id})
        lbl_orderErrEdit.config(fg="#2e5da3")
        lbl_orderErrEdit['text'] = "Data Updated Successfully!"
        print("Data Updated Successfully!")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
        msg = str(exception)
        lbl_orderErrEdit['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()
    ResetOrderData()


def GetRate():
    prod = (str(PRODUCT_NAME.get()))

    if PRODUCT_NAME.get() == "SELECT":
        lbl_orderErrAdd['text'] = "Choose product first!"
    else:
        Database()
        sql_get_rate = "SELECT * FROM products WHERE product_name = :prd"
        cursor.execute(sql_get_rate, {':prd': prod})
        data = cursor.fetchone()
        RATE.set(data[3])
        rate = data[3]
        cursor.close()
        conn.close()
        CalculateAmount(rate)


def CalculateAmount(rate):
    qty = (int(QUANTITY.get()))
    paid = (float(PAID_AMOUNT.get()))

    total = (rate * qty)
    TOTAL.set(total)
    SUB_AMOUNT.set(total)

    subamount = (float(SUB_AMOUNT.get()))
    gst = (subamount * 12) / 100
    GST.set(gst)
    grand_total = (subamount + gst)
    TOTAL_AMOUNT.set(round(grand_total, 2))
    dues = (grand_total - paid)
    DUE_AMOUNT.set(round(dues, 2))


def ResetOrderData():
    SEARCH.set("")
    CLIENT_NAME.set("")
    CLIENT_N0.set("")
    QUANTITY.set("0")
    RATE.set("0.0")
    PRODUCT_NAME.set("")
    TOTAL.set("0.0")
    SUB_AMOUNT.set("0.0")
    TOTAL_AMOUNT.set("0.0")
    PAID_AMOUNT.set("0.0")
    DUE_AMOUNT.set("0.0")
    GST.set("0.0")
    PAYMENT_STATUS.set("SELECT")
    ORDER_SORT.set("SELECT")
    lbl_orderErr['text'] = ""
    orderTree.delete(*orderTree.get_children())
    ShowOrderData()


def PrintInvoice():
    cur_date = date.today()

    oId = order_id

    pdf = FPDF()
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('arial', 'B', 10, )
    pdf.cell(60)
    pdf.cell(60, 10, "Invoice", 0, 2, 'C')
    pdf.line(80, 18, 120, 18)
    pdf.cell(120, 10, "Date: " + (str(cur_date)), 0, 0)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    

    Database()
    sql_report = "SELECT order_id, TO_CHAR(order_date, 'mm/dd/yy'), client_name, client_no, product, quantity," \
                 "total_amount, paid_amount, due_amount, payment_status FROM orders WHERE order_id = :id"
    try:
        cursor.execute(sql_report, {'id': oId})
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    order = cursor.fetchone()

    prod = order[4]

    sql_get_rate = "SELECT * FROM products WHERE product_name = :prd"
    cursor.execute(sql_get_rate, {':prd': prod})
    data = cursor.fetchone()
    rate = data[3]
    brand = data[4]

    gst = (rate * 12) / 100

    pdf.cell(-120)
    pdf.set_font('arial', '', 8)
    pdf.cell(40, 5, 'Order Date     :   ' + (str(order[1])), 0, 2, '')
    pdf.cell(40, 5, 'Client Name   :   ' + (str(order[2])), 0, 2, '')
    pdf.cell(40, 5, 'Contact No     :   ' + (str(order[3])), 0, 2, '')
    pdf.cell(40, 5, 'Product          :   ' + (str(order[4])), 0, 2, '')
    pdf.cell(40, 5, 'Brand             :   ' + (str(brand)), 0, 2, '')
    pdf.cell(40, 5, 'Quantity         :   ' + (str(order[5])), 0, 2, '')

    pdf.cell(0.5)
    pdf.cell(40, 5, 'Rate              :   ' + (str(rate)), 0, 2, '')
    pdf.cell(40, 5, 'GST              :   ' + (str(round(gst, 2))), 0, 2, '')
    pdf.cell(40, 5, 'Total             :   ' + (str(order[6])), 0, 2, '')
    pdf.cell(40, 5, 'Paid              :   ' + (str(order[7])), 0, 2, '')
    pdf.cell(40, 5, 'Dues             :   ' + (str(order[8])), 0, 2, '')
    pdf.cell(40, 5, 'Status           :   ' + (str(order[9])), 0, 2, '')

    pdf.cell(30)
    pdf.cell(40, 30, " ", 0, 2)
    pdf.set_font('arial', 'B', 8)
    pdf.cell(40, 10, "Signature", 0, 2, 'R')
    pdf.output('docs/invoice.pdf', 'F')
    lbl_orderErrEdit['text'] = "Invoice Printed!"
    print("Invoice Printed!")
    cursor.close()
    conn.close()
# =================================================ORDER END HERE======================================================
# =================================================ER START HERE======================================================

def ERdaigram():
    ER=Toplevel(rootWin)
    ER.title("IMS ER")
    dwidth = 1200
    dheight = 800
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    ER.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    ER.resizable(0, 0)
    img=ImageTk.PhotoImage(file="ERdaigram.png")
    label=ttk.Label(ER,image=img)
    label.pack(fill="both",expand=True)
    ER.mainloop()
# =================================================ER END HERE======================================================

# =================================================FD START HERE======================================================

def FD():
    FDWin = Toplevel()
    FDWin.title("Inventory Management System")
    dwidth = 800
    dheight = 300
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    FDWin.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    FDWin.resizable(0, 0)

    Label(FDWin, text="Functionl Dependencies", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    btnView = Frame(FDWin)
    btnView.pack(pady=40)

    btn_add = Button(btnView, text="CANDIDATE KEY", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                     width=20, height=1, cursor="hand2", command=Candidate_key)
    btn_add.grid(row=0, column=0, padx=30, pady=30)

    btn_edit = Button(btnView, text="CLOSURE", relief=RAISED, bg="#2e5da3", fg="#f2f2f2", font=('calibri', 12),
                      width=20, height=1, cursor="hand2", command=Closure)
    btn_edit.grid(row=0, column=1, padx=30, pady=30)

# Candidate_Key Window

def Candidate_key():
    global result_cc
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
    CCWin = Toplevel()
    CCWin.title("Inventory Management System")
    width = 940
    height = 640
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    CCWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    CCWin.resizable(0, 0)
    
    Label(CCWin, text="CANDIDATE KEY", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    lbl_LFDINPUT= Label(CCWin, text="Left Side of FD :   ", font=('calibri', 14), fg="#2e5da3")
    entry_LFDINPUT=Entry(CCWin, textvariable=CLIENT_NAME, width=70, font=('calibri', 14))
    lbl_RFDINPUT= Label(CCWin, text="Right Side of FD :   ", font=('calibri', 14), fg="#2e5da3")
    entry_RFDINPUT= Entry(CCWin, textvariable=PRODUCT_NAME, width=70, font=('calibri', 14))
    lbl_LFDINPUT.place(x=40, y=150)
    entry_LFDINPUT.place(x=180, y=150)
    lbl_RFDINPUT.place(x=40, y=200)
    entry_RFDINPUT.place(x=180, y=200)

    btn_ADDFD = Button(CCWin, text="ADD TO FDSET", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=ADDFD)
    btn_ADDFD.place(x=420,y=250)
    btn_FCC = Button(CCWin, text="FIND CK", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=FCC)
    btn_FCC.place(x=240,y=300)
    btn_RST = Button(CCWin, text="RESET", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=RFD)
    btn_RST.place(x=600,y=300)
    lbl_cc= Label(CCWin, text="CANDIDATE KEY :  ", font=('calibri', 14), fg="#2e5da3")
    lbl_cc.place(x=50,y=350)
    result_cc= Label(CCWin, text="", font=('calibri', 14), fg="#2e5da3")
    result_cc.place(x=200,y=350)

def ADDFD():
    lstr=(str(CLIENT_NAME.get()))
    rstr=(str(PRODUCT_NAME.get()))
    LFD=set(lstr.split(','))
    RFD=set(rstr.split(','))
    fds.add(f.FD(LFD,RFD))
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
def FCC():
    fdsr = fds.key()
    result_cc['text']=fdsr
    result_cc.place(x=200,y=350)
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
def RFD():
    fds.clear()
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")

# CLOSURE Window

def Closure():
    
    global result_c
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
    BRAND_NAME.set("")
    CWin = Toplevel()
    CWin.title("Inventory Management System")
    width = 940
    height = 640
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    CWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    CWin.resizable(0, 0)
    
    Label(CWin, text="CLOSURE", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    lbl_LFDINPUT= Label(CWin, text="Left Side of FD :   ", font=('calibri', 14), fg="#2e5da3")
    entry_LFDINPUT=Entry(CWin, textvariable=CLIENT_NAME, width=70, font=('calibri', 14))
    lbl_RFDINPUT= Label(CWin, text="Right Side of FD :   ", font=('calibri', 14), fg="#2e5da3")
    entry_RFDINPUT= Entry(CWin, textvariable=PRODUCT_NAME, width=70, font=('calibri', 14))
    lbl_closure= Label(CWin, text="Closure of :   ", font=('calibri', 14), fg="#2e5da3")
    entry_closure= Entry(CWin, textvariable=BRAND_NAME, width=70, font=('calibri', 14))
    lbl_LFDINPUT.place(x=40, y=150)
    entry_LFDINPUT.place(x=180, y=150)
    lbl_RFDINPUT.place(x=40, y=200)
    entry_RFDINPUT.place(x=180, y=200)
    lbl_closure.place(x=40,y=250)
    entry_closure.place(x=180,y=250)

    btn_ADDFD = Button(CWin, text="ADD TO FDSET", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=ADDFD)
    btn_ADDFD.place(x=420,y=300)
    btn_FC = Button(CWin, text="FIND ClOSURE", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=FC)
    btn_FC.place(x=240,y=350)
    btn_RST = Button(CWin, text="RESET", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=RFD)
    btn_RST.place(x=600,y=350)
    lbl_c= Label(CWin, text="CLOSURE  :  ", font=('calibri', 14), fg="#2e5da3")
    lbl_c.place(x=50,y=420)
    result_c= Label(CWin, text="", font=('calibri', 14), fg="#2e5da3")
    result_c.place(x=200,y=420)

def ADDFD():
    lstr=(str(CLIENT_NAME.get()))
    rstr=(str(PRODUCT_NAME.get()))
    LFD=set(lstr.split(','))
    RFD=set(rstr.split(','))
    fds.add(f.FD(LFD,RFD))
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
def FC():
    cstr=(str(BRAND_NAME.get()))
    CL=set(cstr.split(','))
    fdsr = fds.closure(CL)
    result_c['text']=fdsr
    result_c.place(x=200,y=420)
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
    BRAND_NAME.set("")
def RFD():
    fds.clear()
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
    BRAND_NAME.set("")
# ================================================FD END HERE====================================================

# ================================================NF START HERE====================================================

def NORMAL_FORM():
    global result_nf
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
    NFWin = Toplevel()
    NFWin.title("Inventory Management System")
    width = 940
    height = 640
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    NFWin.geometry("%dx%d+%d+%d" % (width, height, x, y))
    NFWin.resizable(0, 0)
    
    Label(NFWin, text="NORMAL FORM", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=10)

    lbl_LFDINPUT= Label(NFWin, text="Left Side of FD :   ", font=('calibri', 14), fg="#2e5da3")
    entry_LFDINPUT=Entry(NFWin, textvariable=CLIENT_NAME, width=70, font=('calibri', 14))
    lbl_RFDINPUT= Label(NFWin, text="Right Side of FD :   ", font=('calibri', 14), fg="#2e5da3")
    entry_RFDINPUT= Entry(NFWin, textvariable=PRODUCT_NAME, width=70, font=('calibri', 14))
    lbl_LFDINPUT.place(x=40, y=150)
    entry_LFDINPUT.place(x=180, y=150)
    lbl_RFDINPUT.place(x=40, y=200)
    entry_RFDINPUT.place(x=180, y=200)

    btn_ADDFD = Button(NFWin, text="ADD TO FDSET", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=ADDFD)
    btn_ADDFD.place(x=420,y=250)
    btn_FCC = Button(NFWin, text="FIND NF", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=FNF)
    btn_FCC.place(x=240,y=300)
    btn_RST = Button(NFWin, text="RESET", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=RFD)
    btn_RST.place(x=600,y=300)
    lbl_cc= Label(NFWin, text="WHICH NORMAL FORM :  ", font=('calibri', 14), fg="#2e5da3")
    lbl_cc.place(x=50,y=350)
    result_cc= Label(NFWin, text="", font=('calibri', 14), fg="#2e5da3")
    result_cc.place(x=200,y=350)

def ADDFD():
    lstr=(str(CLIENT_NAME.get()))
    rstr=(str(PRODUCT_NAME.get()))
    LFD=set(lstr.split(','))
    RFD=set(rstr.split(','))
    fds.add(f.FD(LFD,RFD))
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
def FNF():
    # kunde=RelSchema(fds.attributes(), fds)
    # normalisiert =kunde.synthesize()
    # logging.debug(_rels2string(normalisiert))
    # result_cc['text']=len(normalisiert)
    result_cc.place(x=200,y=350)
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")
def RFD():
    fds.clear()
    CLIENT_NAME.set("")
    PRODUCT_NAME.set("")


# ================================================NF END HERE====================================================

# ================================================REPORT START HERE====================================================
def Report():
    global cal, lbl_report
    reportWin = Toplevel()
    reportWin.title("Inventory Management System")
    dwidth = 1080
    dheight = 800
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    reportWin.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    reportWin.resizable(0, 0)
    
    Label(reportWin, text="Report", font=('calibri', 32), fg='#2e5da3').pack(fill=X, pady=20)

    Label(reportWin, text="Choose Date", font=('calibri', 24), fg='#2e5da3').pack(fill=X, pady=10)
    cal = Calendar(reportWin, width=64,font=('calibri', 24), year=2023,textvariabl=ORDER_DATE )
    cal.pack(fill=BOTH, expand=True)

    btn_print = Button(reportWin, text="Print", relief=RAISED, bg="#f2f2f2", fg="#2e5da3", font=('calibri', 12, 'bold'),
                       width=20, height=1, cursor="hand2", command=PrintReport)

    btn_print.pack(pady=20)

    lbl_report = Label(reportWin, text="", font=('calibri', 14), fg="red")
    lbl_report.pack(fill=X, side=BOTTOM)


def PrintReport():
    cur_date = date.today()
    total = 0
    paid = 0
    dues = 0

    orders.clear()
    odate = cal.selection_get()

    pdf = FPDF()
    pdf.compress = False
    pdf.add_page()
    pdf.set_font('arial', 'B', 10, )
    pdf.cell(60)
    pdf.cell(60, 10, "Report", 0, 2, 'C')
    pdf.line(80, 18, 120, 18)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-50)
    pdf.set_font('arial', 'B', 8)
    pdf.cell(40, 10, 'Client Name', 1, 0, 'C')
    pdf.cell(40, 10, 'Product', 1, 0, 'C')
    pdf.cell(20, 10, 'Quantity', 1, 0, 'C')
    pdf.cell(20, 10, 'Total', 1, 0, 'C')
    pdf.cell(20, 10, 'Paid', 1, 0, 'C')
    pdf.cell(20, 10, 'Dues', 1, 2, 'C')
    pdf.cell(-140)
    pdf.set_font('arial', '', 8)
 
    Database()
    sql_report = "SELECT order_id, TO_CHAR(order_date, 'mm/dd/yy'), client_name, client_no, product, quantity, " \
                 "total_amount, paid_amount, due_amount, payment_status FROM orders WHERE order_date = :dt"
    try:
        cursor.execute(sql_report, {'dt': odate})
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for order in fetch:
        pdf.cell(40, 10, '%s' % (str(order[2])), 0, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(order[4])), 0, 0, 'C')
        pdf.cell(20, 10, '%s' % (str(order[5])), 0, 0, 'C')
        pdf.cell(20, 10, '%s' % (str(order[6])), 0, 0, 'C')
        pdf.cell(20, 10, '%s' % (str(order[7])), 0, 0, 'C')
        pdf.cell(20, 10, '%s' % (str(order[8])), 0, 2, 'C')
        pdf.cell(-140)
        total = total + order[6]
        paid = paid + order[7]
        dues = dues + order[8]

    cursor.close()
    conn.close()

    pdf.cell(80)
    pdf.cell(20, 5, ' ', 0, 2, 'C')
    pdf.cell(20, 5, 'Total', 1, 0, 'C')
    pdf.cell(20, 5, (str(round(total, 2))), 1, 0, 'C')
    pdf.cell(20, 5, (str(round(paid, 2))), 1, 0, 'C')
    pdf.cell(20, 5, (str(round(dues, 2))), 1, 2, 'C')
    pdf.cell(-140)
    pdf.cell(100, 20, " ", 0, 2)
    pdf.set_font('arial', 'B', 8)
    pdf.cell(100, 10, "Date: " + (str(cur_date)), 0, 0)
    pdf.cell(100, 10, "Signature", 0, 2, 'C')
    pdf.output('docs/report.pdf', 'F')
    lbl_report['text'] = "Report Printed!"
    print("Report Printed!")
# =================================================GLOBAL FUNCTIONS====================================================
def Database():
    global conn, cursor
    try:
        cx_oracle.init_oracle_client(lib_dir=r"C:\instantclient-basic-windows.x64-21.8.0.0.0dbru\instantclient_21_8")
        conn=cx_oracle.connect("system/Sm28@LAPTOP-RMR5K4N4:1522/xe")
        print("Connected to Oracle DB")
    except cx_oracle.DatabaseError as exception:
        msg = "Failed to connect to Oracle DB " + str(exception)
        print(msg)
    cursor = conn.cursor()


def Minimize():
    rootWin.iconify()
    
def MinimizeHome():
    homeWin.iconify()


def Exit():
    rootWin.destroy()
    sys.exit()


def ExitHome():
    homeWin.destroy()
    sys.exit()


def Login(event=None):
    global id
    admin_id = (str(ADMIN_ID.get()))
    password = (str(PASSWORD.get()))
    Database()
    if ADMIN_ID.get == "" or PASSWORD.get() == "":
        lbl_rootErr['text'] = "Please complete the required field!"
    else:
        sql_login_admin = "SELECT * FROM admin WHERE admin_id = :uname AND password = :upass"
        cursor.execute(sql_login_admin, {'uname': admin_id, 'upass': password})
        if cursor.fetchone() is not None:
            cursor.execute(sql_login_admin, {'uname': admin_id, 'upass': password})
            data = cursor.fetchone()
            id = data[0]
            name = data[1]
            ADMIN_ID.set("")
            PASSWORD.set("")
            print("Logged In Successfully!")
            rootWin.wm_withdraw()
            Home(name)
        else:
            lbl_rootErr['text'] = "Username or password is wrong!"


def Register():
    ID.set("")
    AD_ID.set("")
    PD.set("")
    RPD.set("")
    NAME.set("")
    EMAIL.set("")
    
    global lbl_signErrAdd
    Register = Toplevel()
    Register.title("Inventory management system")
    width = 640
    height = 600
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Register.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Register.resizable(0, 0)

    Label(Register, text="SIGN UP IN IMS", font=('calibri', 20, 'bold'), fg="#2e5da3").pack(fill=X, pady=0)
    lbl_ID = Label(Register, text="ID  :", font=('calibri', 14), fg="#2e5da3")
    entry_ID = Entry(Register, textvariable=ID, width=30, font=('calibri', 14))
    lbl_AD_ID = Label(Register, text="ADMIN_ID  :", font=('calibri', 14), fg="#2e5da3")
    entry_AD_ID = Entry(Register, textvariable=AD_ID, width=30, font=('calibri', 14))
    lbl_PD = Label(Register, text="PASSWORD  :", font=('calibri', 14), fg="#2e5da3")
    entry_PD = Entry(Register, textvariable=PD, width=30,show="*", font=('calibri', 14))
    lbl_RPD = Label(Register, text="RE-ENTER PASSWORD  :", font=('calibri', 14), fg="#2e5da3")
    entry_RPD = Entry(Register, textvariable=RPD, width=30,show="*", font=('calibri', 14))
    lbl_NAME = Label(Register, text="NAME  :", font=('calibri', 14), fg="#2e5da3")
    entry_NAME = Entry(Register, textvariable=NAME, width=30, font=('calibri', 14))
    lbl_EMAIL = Label(Register, text="EMAIL  :", font=('calibri', 14), fg="#2e5da3")
    entry_EMAIL = Entry(Register, textvariable=EMAIL, width=30, font=('calibri', 14))

    btn_saveBrand = Button(Register, text="SIGN UP", relief=RAISED, bg="#2e5da3", fg="#f2f2f2",
                           font=('calibri', 12, 'bold'),
                           width=20, height=1, cursor="hand2", command=Insertadmin)

    lbl_signErrAdd = Label(Register, text="", font=('calibri', 14), fg="red")
    lbl_ID.place(x=168,y=100)
    entry_ID.place(x=230,y=100)
    lbl_AD_ID.place(x=100, y=150)
    entry_AD_ID.place(x=230, y=150)
    lbl_PD.place(x=90, y=200)
    entry_PD.place(x=230, y=200)
    lbl_RPD.place(x=10, y=250)
    entry_RPD.place(x=230, y=250)
    lbl_NAME.place(x=133, y=300)
    entry_NAME.place(x=230, y=300)
    lbl_EMAIL.place(x=130, y=350)
    entry_EMAIL.place(x=230, y=350)
    btn_saveBrand.place(x=230, y=400)
    lbl_signErrAdd.pack(fill=X, side=BOTTOM)

def Insertadmin():
    Database()
    aid=(str(ID.get()))
    adid = (str(AD_ID.get()))
    pasw=(str(PD.get()))
    rpas=(str(RPD.get()))
    na= (str(NAME.get()))
    Ema= (str(EMAIL.get()))

    if  ID.get() == "":
        lbl_signErrAdd['text'] = "ID can't be empty!"
    elif AD_ID.get() == "":
        lbl_signErrAdd['text'] = "ADMIN ID can't be empty!"
    elif PD.get() == "":
        lbl_signErrAdd['text'] = "password can't be empty!"
    elif NAME.get() == "":
        lbl_signErrAdd['text'] = "Name required!"
    elif EMAIL.get() == "":
        lbl_signErrAdd['text'] = "Email can't be empty!"
    elif rpas!=pasw:
        lbl_signErrAdd['text'] = "Password not matched!"
    else:
        sql_insert_admin= "INSERT INTO admin (id,admin_id,password,name,email) VALUES (:aid,:ad_id,:pw,:nam,:em)"
        try:
            cursor.execute(sql_insert_admin,{'aid':aid,'ad_id':adid,'pw':pasw,'nam':na,'em':Ema} )
            ID.set("")
            AD_ID.set("")
            PD.set("")
            RPD.set("")
            NAME.set("")
            EMAIL.set("")
            lbl_signErrAdd.config(fg="#2e5da3")
            lbl_signErrAdd['text'] = "Data Added Successfully"
            print("Data Added Successfully!")
        except cx_oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            lbl_signErrAdd['text'] = msg
    conn.commit()
    cursor.close()
    conn.close()

def FetchBrands():
    Database()
    try:
        cursor.execute("SELECT brand_name FROM brands WHERE status='AVAILABLE' ORDER BY brand_name")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        brands.extend(data)
    cursor.close()
    conn.close()


def FetchCategory():
    Database()
    try:
        cursor.execute("SELECT category_name FROM category WHERE status ='AVAILABLE' ORDER BY category_name")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        category.extend(data)
    cursor.close()
    conn.close()


def FetchProducts():
    Database()
    try:
        cursor.execute("SELECT product_name FROM products WHERE status ='AVAILABLE' ORDER BY product_name")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        products.extend(data)
    cursor.close()
    conn.close()


def BrandCount():
    Database()
    try:
        cursor.execute("SELECT brand_name FROM brands")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        brandCount.extend(data)
        brand_count['text'] = len(brandCount)
    cursor.close()
    conn.close()


def ProductCount():
    Database()
    try:
        cursor.execute("SELECT product_name FROM products")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        productCount.extend(data)
        product_count['text'] = len(productCount)
    cursor.close()
    conn.close()


def OrderCount():
    Database()
    try:
        cursor.execute("SELECT order_id FROM orders")
    except cx_oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        orderCount.extend(data)
        order_count['text'] = len(orderCount)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    InvSys()
