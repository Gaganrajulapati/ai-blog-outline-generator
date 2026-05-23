import json
import os

from groq import Groq
from dotenv import load_dotenv

from parser import BlogOutput


# LOAD ENV VARIABLES
load_dotenv()


# CREATE GROQ CLIENT
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_blog(prompt):

    try:

        # GENERATE RESPONSE
        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "system",
                    "content": """
                    You are an expert AI blog strategist.

                    Return ONLY valid JSON.

                    Generate:
                    - SEO optimized blog title
                    - Blog introduction
                    - Blog outline
                    - Writing goal
                    - SEO keywords
                    """
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.7,
            max_tokens=1000

        )

        # GET RESPONSE
        result = response.choices[0].message.content


        # CLEAN JSON
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()


        # CONVERT TO JSON
        result = json.loads(result)


        # VALIDATE OUTPUT
        validated_output = BlogOutput(**result)


        return validated_output.dict()


    except Exception as e:

        return {
            "error": str(e)
        }