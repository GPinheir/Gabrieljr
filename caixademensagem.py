from tkinter import *
from tkinter import messagebox

tasks_lists = []
counter =  1

def imputError():
    if enterTaskField.get() == "" :
        messagebox.showerror("Erro", "Insira uma Tarefa")
        return 0
    return 1 

def clear_taskNumberField() :
    taskNumberField.delete(1.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    value = imputError()
    if value == 0 :
        return
    content = enterTaskField.get() + "\n"
    tasks_lists.append(content)
    TextArea.insert('end -1 chars', "["+str(counter)+"]" + content)
    counter += 1
    clear_taskField()

def delete() :
    global counter
    if len (tasks_lists) == 0 :
        messagebox.showerror("Nenhuma Tarefa", "Sem Tarefas para Excluir")
        return
    try: 
        task_no = int(taskNumberField.get(1.0, END))
    except ValueError:
        messagebox.showerror('Erro', 'Insira o número de tarefa válida')
        return
    clear_taskNumberField()
    if 1 <= task_no <= len(tasks_lists):
        tasks_lists.pop(task_no - 1)
        counter -= 1
        TextArea.delete(1.0, END)
        for i in range(len(tasks_lists)):
            TextArea.insert('end -1 chars', "[" + str(i + 1) + "]" + tasks_lists[i])
    else:
        messagebox.showerror('Erro', 'Insira o número de tarefa válida')
    
# Driver code
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title('ToDo App')
    gui.geometry("250x300")

    enterTask = Label(gui, text="Insira a tarefa", bg="light blue")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text="Enviar", fg="Black", bg="green", command= insertTask)
    TextArea = Text(gui, height=5, width=25, font="Arial 12")
    taskNumber = Label(gui, text="Excluir a tarefa", bg="blue")
    taskNumberField = Text(gui, height=1, width=2, font="Arial 12")
    delete = Button(gui, text='Apagar', fg="Black", bg="purple", command= delete)
    Exit = Button(gui, text="Sair", fg="Black", bg="Red", command= gui.destroy)

    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=50)
    Submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete.grid(row=6, column=2, pady=5)
    Exit.grid(row=7, column=2)

    gui.mainloop()