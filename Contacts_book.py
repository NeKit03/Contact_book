contact=dict()
Menu=[1,2,3,4,5,0]
def Find_Name():
    print("ввдедите фио")
    name=input()
    if name in contact:
        print('телефон',contact[name][0],'комментарий',contact[name][1])
    else:
        print('Контакт отсутствует')
def Dell_Name():
    print("введите ФИО удаляемого контакта")
    del contact[input()]
def Change_Name():
    print("введите фио изменяемого контакта и новое имя через пробел")
    name1,name2=input().split()
    contact[name2] = contact.pop(name1)
    print('Новое имя контакта',name2,'телефон',contact[name2][0],'комментарий',contact[name2][1])
    
def Append_Name():
    print("введите фио")
    name=input()
    s=[]
    print("введите телефон")
    s.append(input())
    print("введите коментарий")
    s.append(input())
    contact[name]=s
    print('Новый контакт')
    print(name,'телефон',contact[name][0],'комментарий',contact[name][1])
    
def Print_Full_Name():
    for key,value in contact.items():
        print(key,'телефон',value[0], 'комментарий',value[1])
    
def Print_Menu():
    print("menu:")
    print("Нажмите 1 для получения контакта")
    print("Нажмите 2 для удаления контакта")
    print("Нажмите 3 для изменения контакта")
    print("Нажмите 4 для добавления контакта")
    print("Нажмите 5 для вывода всех контактов")
    print("Нажмите 0 для завершения программы")
def Menu_Contact_book(a):
    while a:
        if a==1:
           Find_Name() 
        elif a==2:
            Dell_Name()    
        elif a==3:
            Change_Name()
        elif a==4:
            Append_Name()
        elif a==5:
            Print_Full_Name()      
        
        Print_Menu()
        a=int(input())
        
def Correct_Namber_Menu(a):
    while not (a in Menu):
        print('Введите коректное число')
        Print_Menu()
        a=int(input())
    Menu_Contact_book(a)  
    

def Update_File_Contacts():
    for key,value in contact.items():
        print(key,value)
        contacts.write(str(key)+' ')
        contacts.write(str(value[0])+' ')
        contacts.write(str(value[1])+' ')
        contacts.write('\n')
def open_file():
    with open('input.txt', 'r+') as contacts:
        A=contacts.readline().split()
        while A:
            contact[A[0]]=A[1:]
            A=contacts.readline().split() 
           
open_file()            
Print_Menu()
a=int(input())
Correct_Namber_Menu(a)
contacts.close()
contacts=open('input.txt','w')
Update_File_Contacts()
    

    
        
        
        
        
        
        