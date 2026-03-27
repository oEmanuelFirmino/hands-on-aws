import boto3
import json

from app.core.settings import settings
from app.resources.prompt import refinement_prompt


class BedrockClient:

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            aws_access_key_id=settings.aws_acces_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region,
        )

    def invoke(self, prompt: str) -> str:
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "temperature": 0.5,
            "messages": [{"role": "user", "content": prompt}],
        }

        response = self.client.invoke_model(
            modelId=settings.bedrock_model_id, body=json.dumps(body)
        )

        response_body = json.loads(response["body"].read())

        return response_body["content"][0]["text"]

    def refine_prompt(self, user_prompt: str) -> str:
        prompt = f"{refinement_prompt}\n{user_prompt}"
        return self.invoke(prompt)
