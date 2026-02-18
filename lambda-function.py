import json
import boto3
import time

polly = boto3.client("polly")
s3 = boto3.client("s3")

BUCKET_NAME = "polly-text-narrator-bucket"

def lambda_handler(event, context):
    try:
        if "body" in event and event["body"]:
            body = json.loads(event["body"])
        else:
            body = event

        text = body.get("text")

        if not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing text parameter"})
            }


        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna",  
            Engine="neural"
        )

        audio_stream = response["AudioStream"].read()

        file_name = f"speech-{int(time.time())}.mp3"

      
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=audio_stream,
            ContentType="audio/mpeg"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Audio generated successfully",
                "file": file_name
            })
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
