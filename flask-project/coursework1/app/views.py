from sqlalchemy import asc
from app import app, db, models
from flask import redirect, render_template, request
from datetime import datetime

@app.route('/')
def home():
    tasks = models.Property.query.all()
    return render_template('All_Assessment.html', tasks=tasks, name='Order By')

@app.route('/uncomplete_deadline')
def filter_by_deadline():
    tasks = models.Property.query.order_by(models.Property.completed, asc(models.Property.deadline)).all()
    return render_template('All_Assessment.html', tasks=tasks, name='Uncomplete Deadline')

@app.route('/uncomplete_filter')
def uncomplete_filter():
    tasks = models.Property.query.order_by(models.Property.completed).all()
    return render_template('All_Assessment.html', tasks=tasks, name='Uncomplete Assessments')

@app.route('/filter_by_deadline')
def uncomplete_deadline():
    tasks = models.Property.query.order_by(asc(models.Property.deadline)).all()
    return render_template('All_Assessment.html', tasks=tasks, name='Upcoming Deadline')

@app.route('/search', methods=['GET', 'POST'])
def search_box():
    if request.method == 'GET':
        search_text = request.args['search']
        if search_text:
            tasks = models.Property.query.filter(models.Property.title.contains(search_text)).all()
        else:
            tasks = models.Property.query.all()

        return render_template('All_Assessment.html', tasks=tasks, name='Search By Title') 
    else:
        return redirect('/')

@app.route('/Create_Assessment', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        titleform = request.form['Title']
        moduleform = request.form['Module']
        deadlineform = datetime.strptime(request.form['Deadline'],'%Y-%m-%d')
        descripteform = request.form['Description']

        new_task = models.Property(title=titleform, module=moduleform, deadline=deadlineform, description=descripteform)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error occurs'
    else:
        
        return render_template('Create_Assessment.html')

@app.route('/Completed_Assessment')
def complete():
    tasks = models.Property.query.filter_by(completed = True).all()
    return render_template('Completed_Assessment.html', tasks = tasks)

@app.route('/Uncomplete_Assessment')
def uncomplete_html():
    tasks = models.Property.query.filter_by(completed = False).all()
    return render_template('Uncomplete_Assessment.html', tasks = tasks)

@app.route('/Uncomplete_Assessment/<int:id>', methods=['GET', 'POST'])
def uncomplete(id):
    task = models.Property.query.get_or_404(id)
    if request.method == 'POST':
        task.completed = True
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error occurs'
    else:
        tasks = models.Property.query.all()
        return render_template('Uncomplete_Assessment.html', tasks = tasks)

@app.route('/Delete_Assessment')
def delete():
    tasks = models.Property.query.all()
    return render_template('Delete_Assessment.html', tasks = tasks)

@app.route('/Delete_Assessment/<int:id>', methods=['GET', 'POST'])
def delete_html(id):
        task = models.Property.query.get_or_404(id)
        if request.method == 'POST':
            try:
                db.session.delete(task)
                db.session.commit()
                return redirect('/Delete_Assessment')
            except:
                return 'Error occurs'
        else:
            tasks = models.Property.query.all()
            return render_template('Delete_Assessment.html', tasks = tasks)

