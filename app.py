import flask
from flask.templating import render_template
import stories
app = flask.Flask(__name__)
story = stories.Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def show_home_page():
    return render_template("form.html", words=story.prompts)

@app.route('/story')
def show_story_page():
    keys = dict()
    for prompts in story.prompts:
        keys[prompts] = flask.request.args[prompts]
    return render_template("story.html", story=story.generate(keys))