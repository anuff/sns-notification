from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Initialize SNS client
topic_arn = "YOUR_SNS_TOPIC_ARN"  # Replace with your SNS topic ARN
sns_client = boto3.client("sns")

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']  # Get the message from the form
    subject = "User Input Notification"  # Subject for the notification
    
    # Publish message to SNS topic
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return "Notification sent successfully!"
        else:
            return "Failed to send notification."
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
