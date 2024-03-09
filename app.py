from flask import Flask, render_template, redirect, session, flash
from models import db, connect_db, User, Feedback
from forms import RegistrationForm, LoginForm, CreateFeedbackForm, EditFeedbackForm



DATABASE_URL = 'postgresql:///users_db_exercise'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'some-secret-key'

connect_db(app)

"""Routes"""

@app.route('/')
def redirect_to_register():
    try:
        if session['use_id']:
            return render_template('home.html')
    except KeyError:
        return redirect('/register');

@app.route('/register', methods=['GET', 'POST'])
def display_registration_form():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        new_user = User.register(username, password, email, first_name, last_name)

        db.session.add(new_user)
        try:
            db.session.commit()
        except:
            form.username.errors.append('Username take. Please pick another')
            return render_template('register.html', form=form)
        session['user_id'] = new_user.id
        print('-'*50)
        print('USER REGISTERED')
        print('-'*50)
        flash(f'Welcome {username}! Account Created Successfully.', "success")
        
        return redirect('/login')

    return render_template('register.html', form=form)

# @app.route('/register', methods=['POST'])
# def process_registration_form():
#     pass

@app.route('/login', methods=['GET', 'POST'])
def display_login_form():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        u = User.authenticate(username, password)

        if u:
            flash(f"Welcome back, {u.username}!", 'primary')
            session['user_id'] = u.id
            return redirect(f'/users/{u.username}')
    
    return render_template('login.html', form=form)

@app.route('/users/<uname>')
def display_secret_form(uname):
    try:
        if session['user_id']:
            user = User.query.filter_by(username=uname).first()
            feedback = Feedback.query.filter_by(username=uname).all()
            return render_template('user_show_info.html', user=user, feedback=feedback)
    except KeyError:
        flash("You don't have permissions to view this webpage")
        return redirect('/login')

@app.route('/users/<uname>/delete', methods=['POST'])
def delete_user(uname):
    if check_authority():
        # delete all user posts, then the user itself
        feed_back_to_delete = Feedback.query.filter_by(username=uname).all()
        for i in feed_back_to_delete:
            db.session.delete(i)
        User.query.filter_by(username=uname).delete()
        db.session.commit()
        session.clear()
        return redirect('/')
    return redirect('/')

@app.route('/users/<uname>/feedback/add', methods=['GET', 'POST'])
def display_process_create_feedback_form(uname):
    if check_authority():
        form = CreateFeedbackForm()
        if form.validate_on_submit(): # if form is completed and user is authorized then create new feedback and add it to db
            user = User.query.filter_by(username=uname).first()
            title = form.title.data
            content = form.content.data

            new_feedback = Feedback(title=title, content=content, username=user.username)
            db.session.add(new_feedback)
            db.session.commit()
            return redirect(f'/users/{uname}')
        else:
            return render_template('feedback_create_form.html', form=form)
    else:
        flash("You don't have permissions to view this webpage")
        return redirect('/login')

@app.route('/feedback/<int:feedback_id>/update', methods=['GET', 'POST'])
def display_process_edit_feedback_form(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    form = EditFeedbackForm(obj=feedback)
    if check_authority():
        if form.validate_on_submit():
            user = User.query.filter_by(id=session['user_id']).first() # check to see if user and feedback are the same
            # feedback = Feedback.query.filter_by(id=feedback_id).first()

            if user.username == feedback.username:
                feedback.title = form.title.data
                feedback.content = form.content.data

                db.session.add(feedback)
                db.session.commit()
                return redirect(f'/users/{user.username}')
            else:
                flash("You aren't allowed to do that, redirected to homepage")
                return redirect('/')
        else:
            return render_template('feedback_edit_form.html', form=form)
    else:
        return redirect('/')

@app.route('/feedback/<int:feedback_id>/delete', methods=['POST'])
def delete_feedback(feedback_id):
    if check_authority():
        # delete feedback then commit and redirect to user info page
        Feedback.query.filter_by(id=feedback_id).delete()
        db.session.commit()
        user = User.query.filter_by(id=session['user_id']).first()
        return redirect(f'/users/{user.username}')


@app.route('/logout')
def logout():
    """clears sessionStorage and redirects user to login page"""
    session.clear()
    return redirect('/')

"""helpful functions"""
def check_authority():
    """Quick check to see if user is validated, use this bit of code a lot so decided to just put it all in a function"""
    return session['user_id']