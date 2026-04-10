from flask import Flask, render_template, jsonify, request
import os
import json
import creature
if os.path.exists("tama.json"):
    creature.creature = creature.load()
app = Flask(__name__)
creature.decay()
creature.save()

@app.route("/")
def home():
    return render_template("index.html", creature=creature.creature)

@app.route("/action/<action_name>")
def action(action_name):
    if action_name == "feed":
        creature.feed()
    elif action_name == "play":
        creature.play()
    elif action_name == "sleep":
        creature.sleep()
    creature.save()
    return jsonify(creature.creature)

if __name__ == "__main__":
    creature.decay()
    app.run(host="0.0.0.0", port=5000, debug=True)
