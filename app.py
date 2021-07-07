from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    """Shows the homepage with the Madlib prompt form"""

    prompt_list = silly_story.prompts

    return render_template("questions.html", prompts=prompt_list)

@app.route('/results')
def result_story():
    """Creates a dictionary of prompt and user's answers
        Generates a story. 
    """

    ans = request.args

    result_story = silly_story.generate(ans)

    return render_template("story.html", story=result_story)

    # request.args is dictionary-like