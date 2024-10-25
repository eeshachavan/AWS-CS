import json
import boto3

def lambda_handler(event, context):
    # Log the event in CloudWatch
    print("Event: ", json.dumps(event))
    
    # Extract S3 bucket and object details
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Process the image (log details in this case)
    response = s3.get_object(Bucket=bucket, Key=key)
    print(f"Processing file {key} from bucket {bucket}")

    # Send a notification through SNS
    sns_client = boto3.client('sns')
    sns_topic_arn = "arn:aws:sns:eu-north-1:010928190992:MyTopic"  # Replace with your SNS Topic ARN
    
    message = f"File {key} from bucket {bucket} has been processed successfully."
    
    # Publish message to SNS
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject="S3 Image Processing Notification"
    )
    
    print(f"Notification sent to SNS topic: {sns_topic_arn}")
    
    # Additional logs for verification
    print(f"Lambda function updated! Now processing {key} from {bucket}.")
    print("again updated")

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed and notification sent successfully!')
    }
