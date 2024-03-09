## Authentication/Authorization

#### Part 0: Setting Up your environment
- [x] You know the drill. Make a venv, pip install your dependecies, push your code to GitHub, etc.

#### Part 1: Create User Model
- [x] First, create a ***User*** model for SQLAlchemy. PUt this in a ***models.py*** file.
    - [x] ***username*** - a unique primary key that is no longer than 20 characters.
    - [x] ***password*** - a not-nullable column that is text.
    - [x] ***email*** - a not-nullable column that is unique and no longer than 50 characters.
    - [x] ***first_name*** - a not-nullable column that is no longer than 30 characters.
    - [x] ***last_name*** - a not-nullable column that is no longer than 30 characters.

#### Part 2: Make a base template
- [x] Add a base template with slots for the page title and content. Your other templates should use this.

#### Part 3: Make routes for users
- [x] Make routes for the following:
    - [x] ***GET  /***: Redirect to /register
    - [x] ***GET  /register***:  Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name. Make sure you are using WTForms and that your password input hides the characters that the user is typing!
    - [x] ***POST /register***: Process the registration form by adding a new user. Then redirect to /secret.
    - [x] ***GET  /login***: Show a form that when submitted will login a user. This form should accept a username and a password. Make sure you are using WTForms and that your password input hides the chatacters that the user is typing!
    - [x] ***POST /login***: Process the login form, ensuring the user is authenticated and going to /secret if so.
    - [x] ***GET  /secret***: Return the text "You made it!" (dont worry, we'll get rid of this soon).

#### Part 4: Don't let everyone go to /secret
- [x] Let's protect this route and make sure that only users who have logged in can access this route!

#### Part 5: Log out users
- [x] Make routes for the following:
    - [x] ***GET /logout***: Clear any information from the session and redirect to /

#### Part 6: Let's change /secret to /users/<username>
- [x] Now that we have some logging in and logging out working. Let's add some authorization! When a user logs in, take them to the following route:
    - [x] ***GET /users/<username>/***: Display a template that shows informatino about that user (everything except for their password). You should ensure that only logged in users can access this page.

#### Part 7: give us some more feedback!
It's time to add another model.
- [x] Create a ***Feedback*** model for SQLAlchemy. Put this in a ***models.py*** file.
- [x] It should have the following columns:
    - [x] ***id*** - a unique primary key that is an auto incrementing integer
    - [x] ***title*** - a not-nullable column that is at most 100 characters
    - [x] ***content*** - a not-nullable column that is text
    - [x] ***username*** - a foreign key that references the username column in the users table

#### Part 8: Make/Modify Routes For Users and Feedback
- [X] ***GET /users/<username>***: Show information about the given user. Show all of the feedback that the user has given. For each piece of feedback, display with a link to a form to edit the feedback and a button to delete the feedback. Have a link that sends you to a form to add more feedback and a button to delete the feedback. Have a link that sends you to a form to add more feedback and a button to delete the user **Make sure that only the user who is logged in can successfully view this page.**
- [X] ***POST /users/<username>/delete***: Remove the user from the database and make sure to also delete all of their feedback. Clear any user information in the session and redirect to /. **Make sure that only the user who is logged in can successfully delete their account.**
- [X] ***GET /users/<username>/feedback/add***: Display a form to add feedback **Make sure that only the user who is logged in can see this form.**
- [X] ***POST /users/<username>/feedback/add***: Add a new piece of feedback and redirect to /users/<username> -- **Make sure that only the user who is logged in can successfully add feedback.
- [X] ***GET /feedback/<feedback-id>/update***: Display a form to edit feedback -- **Make sure that only the user who has written that feedback can update it.**
- [X] ***POST /feedback/<feedback-id>/update***: Update a specific piece of feedback and redirect to /users/<username> -- **Make sure that only the user who has written that feedback can update it.**
- [X] ***POST /feedback/<feedback-id>/delete***: Delete a specific piece of feedback and redirect to /users/<username> -- **Make sure that only the user who has written that feedback can update it.**