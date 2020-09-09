import tkinter as tk 
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os 

main_application = tk.Tk()
main_application.geometry('1200x1000')
main_application.title('Vpad text editor')

main_menu=tk.Menu()

#file icons
new_icon=tk.PhotoImage(file='new.png')
open_icon=tk.PhotoImage(file="open.png")
save_icon=tk.PhotoImage(file="save.png")

file=tk.Menu(main_menu,tearoff=False)

#edit icons
copy_icon=tk.PhotoImage(file='copy.png')
paste_icon=tk.PhotoImage(file="paste.png")
cut_icon=tk.PhotoImage(file="cut.png")
find_icon=tk.PhotoImage(file="find.png")

edit=tk.Menu(main_menu,tearoff=False)



#view icons
status_bar_icon=tk.PhotoImage(file='status_bar.png')
view=tk.Menu(main_menu,tearoff=False)

#theme
light_default_icon=tk.PhotoImage(file='light_default.png')
light_plus_icon=tk.PhotoImage(file='light_plus.png')
dark_icon=tk.PhotoImage(file='dark.png')

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon)
theme=tk.Menu(main_menu,tearoff=False)
color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d')
}

#casade
main_menu.add_cascade(label='file',menu=file)
main_menu.add_cascade(label='edit',menu=edit)
main_menu.add_cascade(label='view',menu=view)
main_menu.add_cascade(label='theme',menu=theme)

##########toolbar#######



#font box
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Comic Sans MS'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(2)
font_size.grid(row=0,column=1)

#bold button
bold_icon=tk.PhotoImage(file='bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=2)
#italic button
italic_icon=tk.PhotoImage(file='italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=2)
#underlinr button
underline_icon=tk.PhotoImage(file='underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=2)

#align left
align_left_icon=tk.PhotoImage(file='align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=5,padx=2)

#align left
align_right_icon=tk.PhotoImage(file='align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=6,padx=2)

#align left
align_center_icon=tk.PhotoImage(file='align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=2)
##########################

##########text editor#######
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and size
current_font_family='Comic Sans MS'
current_font_size=12
def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)

#buttons functionality
#bold
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

#italic
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

#underline
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

#align
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
align_left_btn.configure(command=align_left)
 

def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
align_center_btn.configure(command=align_center)


def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
align_right_btn.configure(command=align_right)

###########################


#######main status bar######
status_bar=ttk.Label(main_application,text='Status bar')
status_bar.pack(side=tk.BOTTOM)
############################

###########main menu functionality#####
#file commands
file.add_command(label='new',image=new_icon,compound=tk.LEFT ,accelerator='Ctrl+N')
file.add_command(label='open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
#edit commands
edit.add_command(label='copy',image=copy_icon,compound=tk.LEFT ,accelerator='Ctrl+C')
edit.add_command(label='paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')

view.add_checkbutton(label='status bar',image=status_bar_icon,compound=tk.LEFT)

#theme commands
count=0 
for i in color_dict:
    theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT)
    count=count+1
##############################

main_application.config(menu=main_menu)
main_application.mainloop()
