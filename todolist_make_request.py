import time
import requests

###############
### все задачи
def showTodolist():
    url_todolist = f"http://localhost:8080/todolist"
    r = requests.get(url=url_todolist)

    todolist = r.json()

    for task in todolist:
        print(f"id:{task['id']} / Description task: {task['description']} / Status: {task['status']}")

    print()

#################
### задача по id
def showTask():
    id = int(input("Enter id task\n "))
    URL = f"http://localhost:8080/todolist/{id}"

    r = requests.get(url=URL)

    ###_обработаем под ошибку
    if r.status_code == 404:
        print(f"Error from the server: {r.json()['message']}, "
              f"{time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime(int(r.json()['timestamp']/1000)))}")
    else:
        task = r.json()
        print(f"Description task: {task['description']}")


####################
### добавляем запись
def createTask():
    description = input("Enter description:\n")
    status = input("Enter status:\n")
    deadline = int(input("Enter deadline:\n"))
    URL = f"http://localhost:8080/todolist"

    data = {
        "description": description,
        "status": status if status else "EMPTY",
        "deadline": deadline}

    r = requests.post(url=URL, json=data)
    if r.status_code == 200:
        print("Задача успешно создана")
    else:
        print("Ошибка, задача не создана")

### удаляем запись
def deleteTask():
    id = int(input("Enter id task\n "))
    URL = f"http://localhost:8080/todolist/del{id}"
    r = requests.post(url=URL)
    if r.status_code == 404:
        print(f"Ошибка {r.status_code}\n")
    else:
        print("Задача успешно удалена\n")


if __name__ == "__main__":
    # showTodolist()
    # showTask()
    # createTask()
    showTodolist()
    # deleteTask()