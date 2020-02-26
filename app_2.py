from flask import Flask, render_template, redirect, request
from todo import ToDoList

app = Flask(__name__)

todolist = ToDoList()

@app.route('/')
def show_todolist():
    return render_template('showtodo.html', todolist=todolist.get_all())

@app.route('/additem', methods=['POST'])
def add_todoitem():
    title = request.form['title']    
    if not title:
        return redirect('/')
    
    todolist.add(title)
    return redirect('/')

@app.route('/deleteitem/<int:item_id>')
def delete_todoitem(item_id):
    todolist.delete(item_id)
    return redirect('/')

@app.route('/updatedone/<int:item_id>')
def update_todoitem_done(item_id):
    todolist.update(item_id)
    return redirect('/')

@app.route('/deletealldoneitems')
def delete_alldone_todoitems():
    todolist.delete_doneitem()
    return redirect('/')