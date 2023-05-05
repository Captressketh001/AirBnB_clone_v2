#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def all_states(state_id=None):

    states = storage.all('State')
    if state_id:
        i = "{}.{}".format('State', state_id)
        if i in states:
            states = states[i]
        else:
            states = None
    else:
        states = storage.all('States').values()
    """Return list of states"""
    return render_template('10-hbnb_filters.html', filter_states=states, id=state_id)



# def filter_states(id):
#     states = storage.all('State').values()
#     state = states.query.get_or_404(id)
#     return render_template('10-hbnb_filters.html', filter_states=state)

@app.teardown_appcontext
def teardown(self):
    """Remove alchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
