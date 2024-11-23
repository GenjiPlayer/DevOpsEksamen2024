import base64
import boto3
import json
import random
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bucket = os.environ['BUCKET']
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")  
s3_client = boto3.client("s3")

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))
    
    model_id = "amazon.titan-image-generator-v1"
    
    try:
        body = json.loads(event["body"])
        prompt = body.get("prompt")
        if not prompt:
            raise ValueError("Missing 'prompt' in request body")
        
        seed = random.randint(0, 2147483647)
        s3_image_path = f"58/titan{seed}.png"

        native_request = {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": prompt},
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "quality": "standard",
                "cfgScale": 8.0,
                "height": 1024,
                "width": 1024,
                "seed": seed,
            }
        }

        logger.info("Invoking Bedrock model with request: %s", json.dumps(native_request))
        response = bedrock_client.invoke_model(  
            modelId=model_id,
            body=json.dumps(native_request)
        )

        logger.info("Bedrock response: %s", response)
        model_response = json.loads(response["body"].read())

        base64_image_data = model_response["images"][0]
        image_data = base64.b64decode(base64_image_data)

        logger.info("Uploading image to S3 at %s", s3_image_path)
        s3_client.put_object(Bucket=bucket, Key=s3_image_path, Body=image_data)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Det funker?",
                "s3_image_path": f"s3://{bucket}/{s3_image_path}",
                "prompt": prompt
            })
        }

    except Exception as e:
        logger.error("Error occurred: %s", str(e), exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "raaaah >:(",
                "error": str(e)
            })
        }
