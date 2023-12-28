from tkinter import *
import random

root=Tk()
root.title("Picnic bag list")
root.geometry("600x600")

l_list = Label(root)
l_item = Label(root)

l_item = ["Water Bottle", "Tiffin Box", "Id Card", "Chocolates", "Chips", "Wonderla Tickets", "Picnic mat"]
l_list["text"] = "Listed Items : " + str(l_item)

def bag_items():
    random_item = random.sample(range(1, 7), 1)
    l_item["text"]= "Put Item no. " + str(random_item) + "In Bag"
    
l_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)    

btn = Button(root, text=" Which Item To Pur in The bag?", command = bag_items, bg = "orange", fg="white")
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

l_item.pack(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()

    


