from flask import Flask, request, render_template
import database 
import sys
import imp



application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def input_html_function():
    return render_template('index.html')

@application.route('/input_data', methods=['GET', 'POST'])
def input_data_function():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        destination = request.form['destination']
        input_event = request.form['input_event']
        year = request.form['year']
        month = request.form['month']
        start_day = request.form['start_day']
        end_day = request.form['end_day']
        
        #database.save(uid, pwd, destination, input_event, year, month, start_day, end_day)
        
        return render_template('outer.html', uid=uid, pwd=pwd, destination=destination, input_event=input_event, year=year, month=month, start_day=start_day, end_day=end_day)
    
    return render_template('index.html')
      
if __name__ == '__main__':
    application.run(host='0.0.0.0')


