AI Writer project summary

Main Features:
Dynamic Story Framework
Begin with the bones of your tale. Create storylines with multiple acts, chapters, and scenes. Utilize storyline templates to swiftly build compelling narratives. Introduce characters, locations, and even weave in historical events. As your tale unfolds, nest your story components with ease.

Intuitive AI Assistance
The AI is your co-author, mentor, and critic. Seek its help to:

Generate content when inspiration runs dry.
Proofread and polish your work.
Explore potential plot twists or delve deeper into character psyches.
Extract and summarize pivotal story moments.
Gain feedback and engage in constructive discussions about your narrative.
Customizable Elements
Define the heartbeat of your tale with themes, moods, and tones. While the AI can suggest, remember, every element is yours to imagine and tailor.

Your Story, Your Rules
While the writing assistant has an understanding of the entire context of your story, you're always in control. Interact with the AI to shape your story as it evolves and the plot progresses.

Share Your Work
Seamlessly export to formats like EPUB, PDF, and DOC, paving the way for distribution, collaboration, and sharing your tales with the world.

The Road Ahead:
This is just the beginning! As you weave your stories, the AI learns, adapts, and grows, offering richer feedback and insights. Envision a future where you can collaborate with fellow writers, share your narratives, and explore diverse writing domains.

Start your new writing project today, and let every word tell a tale!
This is the folder structure of the project:

Application framework:

the application framework being used is Flask:

Flask is a popular Python web framework that often structures its projects with app, routes, models, and templates directories.
Flask often integrates with SQLAlchemy as its ORM (Object Relational Mapper), which in turn uses Alembic for migration management.
Flask uses WTForms for form handling, which fits with the presence of forms and form-related files.
Flask uses Jinja2 as its templating engine, which would use the .html files in the templates directory.

Directory structure:

In directory: .
.gitignore
directory_structure.py
directory_structure.txt
project_templates.json
randkey.py
README.md
requirements.txt

In directory: .\app
chat_gpt.py
exceptions.py
__init__.py

In directory: .\app\db
conversations.py
projects.py
__init__.py

In directory: .\app\forms
login_form.py
registration_form.py
__init__.py

In directory: .\app\models
activity.py
chat_history.py
chat_message.py
collection.py
notification.py
relationships.py
story_part.py
user.py
writing_project.py
__init__.py

In directory: .\app\routes
__init__.py

In directory: .\app\routes\api\v1
chat.py
project.py
user.py

In directory: .\app\routes\www
chat.py
project.py
story.py
user.py

In directory: .\app\services
activity_manager.py
chat_history_manager.py
chat_message_manager.py
notification_manager.py
project_manager.py
story_manager.py
token_manager.py
user_manager.py
__init__.py

In directory: .\app\static\css
aiw.css

In directory: .\app\templates
base.html
create_project.html
dashboard.html
delete_project.html
landing_page.html
login.html
profile.html
project_detail.html
register.html
update_project.html
_index_project_widget.html

In directory: .\app\testing
test_token_manager.py
__init__.py

In directory: .\migrations
alembic.ini
env.py
README
script.py.mako

In directory: .\migrations\versions
659ad5610d40_initial_migration.py
aaf23a3614b7_implemented_core_models.py
d3bd5e51645c_updated_user_model.py

