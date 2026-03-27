import os

import boto3
import json

from app.core.settings import settings
from app.resources.prompt.refinement_prompt import build_refinement_prompt
from dotenv import load_dotenv

load_dotenv()


class BedrockClient:

    def __init__(self):
        self.client = boto3.client(
            "bedrock-runtime",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region,
        )

    def invoke(self, prompt: str) -> str:
        response = self.client.invoke_model(
            modelId=os.getenv(
                "BEDROCK_MODEL_ID", "global.anthropic.claude-haiku-4-5-20251001-v1:0"
            ),
            body=json.dumps(
                {
                    "anthropic_version": "bedrock-2023-05-31",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                }
            ),
        )

        response_body = json.loads(response["body"].read())

        return response_body["content"][0]["text"]

    def refine_prompt(self, user_prompt: str) -> str:
        prompt = build_refinement_prompt(user_prompt)
        return self.invoke(prompt)
