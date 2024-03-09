from flask import Flask, request, jsonify
import boto3
import pickle

app = Flask(__name__)

@app.route("/")
def get_recommendations():
    return "hi"

if __name__ == "__main__":
    # Replace 'your_access_key' and 'your_secret_key' with your AWS access key and secret key
    """
    s3 = boto3.client('s3', aws_access_key_id='AKIA5FTY6Z3OPDXFBDM7', aws_secret_access_key='XdYO6VJDXqjSAAKlYcpCm6NAnuHfSRhg1Sw4fTeg')

    bucket_name = 'animerecommenderdata'
    remote_file_key = 'recommender.pkl'

    # Load the machine learning model
    try:
        response = s3.get_object(Bucket=bucket_name, Key=remote_file_key)
        pickle_data = response['Body'].read()
        model = pickle.loads(pickle_data)
        prediction = model.predict(10, "Gintama: The Final")
        print(prediction.est)

    except Exception as e:
        print(f"Error loading the model: {str(e)}")
        model = None

    print("done")
    """
    app.run(debug=True)