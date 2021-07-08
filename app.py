from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

STORIES = {"silly" : silly_story, "excited" : excited_story}

@app.route('/')
def homepage():
    """Shows homepage where you can choose which story"""
    return render_template("choose.html", stories = ["silly", "excited"])


@app.route('/madlibs')
def madlibs():
    """Shows the Madlib prompt form"""

    selected_story = request.args["story"]
    prompt_list = STORIES[selected_story].prompts

    return render_template("questions.html", prompts = prompt_list, selected_story = selected_story)

@app.route('/results/<selected_story>')
def result_story(selected_story):
    """Creates a dictionary of prompt and user's answers
        Generates a story. 
    """

    ans = request.args

    result_story = STORIES[selected_story].generate(ans)

    return render_template("story.html", story=result_story)

    # request.args is dictionary-like