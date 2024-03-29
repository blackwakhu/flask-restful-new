from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)
