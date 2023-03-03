from flask import *
from flask_mail import Mail, Message
import os
import pandas as pd 
import datetime

# def read_excel():
#     FL_Graph=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="FL_Graph")
#     TL_Graph=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="TL_Graph")
#     DR_Graph=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="DR_Graph")
#     FL_VI=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="FL_VI")
#     TL_VI=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="TL_VI")
#     DR_VI=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="DR_VI")
#     return FL_Graph, TL_Graph, DR_Graph, FL_VI, TL_VI, DR_VI

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='lgekrhqmh01.lge.com',
    MAIL_PORT=25,
    MAIL_DEFAULT_SENDER=('CostReview', 'eunbi1.yoon@lge.com'),
)

mail = Mail(app)


# @app.route("/tables")
# def show_tables():
#     data = pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="FL_Graph")
#     return render_template('index.html',tables=data.to_html())

@app.route("/")
def index():
    subject = 'Bulk email'
    receiver=['eunbi1.yoon@lge.com']
    #data
    FL_Graph=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="FL_Graph").to_html()
    TL_Graph=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="TL_Graph").to_html()
    DR_Graph=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="DR_Graph").to_html()
    FL_VI=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="FL_VI").to_html()
    TL_VI=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="TL_VI").to_html()
    DR_VI=pd.read_excel('C:/Users/RnD Workstation/Documents/CostReview/0221/report.xlsx',sheet_name="DR_VI").to_html()
    year, week_num, day_of_week = datetime.date.today().isocalendar()


    msg = Message(
        subject=subject,
        recipients=receiver,
        html=render_template('index.html',FL_Graph=FL_Graph, TL_Graph=TL_Graph, DR_Graph=DR_Graph, FL_VI=FL_VI, TL_VI=TL_VI, DR_VI=DR_VI,week_num=week_num)
    )
    #send mail
    # mail.send(msg)

    # return 
    return render_template('index.html',FL_Graph=FL_Graph, TL_Graph=TL_Graph, DR_Graph=DR_Graph, FL_VI=FL_VI, TL_VI=TL_VI, DR_VI=DR_VI,week_num=week_num)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
