from google import genai
from config import GEMINI_API_KEY
import time

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_answer(prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"Attempt {attempt+1} failed...")

            if attempt == 2:
                raise e

            time.sleep(5)