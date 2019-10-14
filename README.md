# cgap_test
Interview challenge.

*To Run* (These instructions assume knowledge of Python and virtualenv)
1. Download cgap_test.zip to your computer, and extract to location of your choice.
2. Use virtualenv and requirements.txt to create the Python environment.  This project was built with Python 3.7.3 and tested on macOS Mojave (although OS shouldn't matter).
3. Run cgap_test with the command "python manage.py runserver"
4. Navigate your browser (Chrome preferred) to [ip]:[port]/participants/ to access the submission form, or [ip]:[port]/participants/list/ to see the list of logged participants.

*Implementation Notes*
- Mutations and Environmental Exposures are stored as JSON strings.
- It is recommended to run this application with DEBUG set to True in settings.py, as an alternative method for serving static files locally has not been implemented.
- No uniqueness restrictions have been added to the database.

*Musings on Improvements*
1. _What are some measures we could take to secure this application?_
A. The two big ones are implementing password-controlled user access (Django has some basic tools), adding https protocols, and putting some form of audit logging into effect.  For an extra layer of protection, certain database engines like MariaDB support encryption, but this can have a sizeable impact on performance.
2. _What are some ways in which this application could be made more dynamic, from a UI/UX perspective?_
Strictly speaking, it isn't necessary that this application be separated into two views.  For instance, a narrow side pane could display a list of existing study participants, with a button that brings up a modal with the submission form.  Selecting an existing Participant could display its details in a wider pane.  Many applications, including Atlassian's popular JIRA software, implement this approach.
