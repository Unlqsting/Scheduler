# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition

# import weatherapi

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/Calendar/')  # connects /stub/ URL to stub() function
def Calendar():
    return render_template("Calendar.html")

@app.route('/api/weather/')  # connects /stub/ URL to stub() function
def Wapi():
    return render_template("wapi.html")

# @app.route('/weatherapi/')  # connects /stub/ URL to stub() function
# def weather():
#     return weatherapi()
   
    # apidata = 'apidata.json'
    # with open(apidata, 'w') as wd:
    #     wd.writelines(response.json())

    # this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
