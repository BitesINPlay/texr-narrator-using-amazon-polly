# Amazon Polly Lambda Narrator

## How It Works
1. Lambda function accepts JSON input with property "text"

2. Calls Amazon Polly (Neural TTS engine)

3. Generates MP3 audio file

4. Uploads file to S3 bucket

## Technologies Used
- Python 3.10+

- AWS Lambda

- Amazon Polly (Neural TTS)

- Amazon S3

- IAM Roles (за сигурен достъп)

- boto3 (AWS SDK for Python)


## Example Event

```json
{
  "text": "Some text"
}
