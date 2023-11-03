from flask import Flask, request, render_template,jsonify

from src.pipeline.predict_pipeline import  CustomData, PredictPipeline
from flask_cors import CORS, cross_origin

from sklearn.preprocessing import StandardScaler


application= Flask(__name__)
app= application

### Route for a home page

# @app.route('/')
# def index():
#      return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data= CustomData(
            gender=request.form.get('gender'), 
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get('lunch'), 
            test_preparation_course=request.form.get('test_preparation_course'), 
            reading_score= float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score")), 

        )
        pred_df= data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=round(results[0],2))

@app.route('/predictAPI', methods=['POST'])
@cross_origin()
def predict_api():
    if request.method=='POST':
        data = CustomData( 
            gender=request.json['gender'], 
            race_ethnicity=request.json['ethnicity'],
            parental_level_of_education=request.json["parental_level_of_education"],
            lunch=request.json['lunch'], 
            test_preparation_course=request.json['test_preparation_course'], 
            reading_score= float(request.json["reading_score"]),
            writing_score=float(request.json["writing_score"]), 
        )
            
        pred_df= data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
            
        dct = {'maths_score': round(results[0],2)}
        return jsonify(dct)

        

    
if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0")