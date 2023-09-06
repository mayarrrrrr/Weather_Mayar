from flask import *
from weather import main as get_weather

app=Flask(__name__)


@app.route('/weather',methods=['GET','POST'])
def index():
    
    if request.method== 'POST':
        city=request.form['cityname']
        country=request.form['countryname']
        data=get_weather(city,country)
        return render_template('index.html',data=data)
   
    else:
        data=None
        return render_template('index.html',data=data)
      

    




if __name__ == "__main__":
    app.run(debug=True,port=5000)