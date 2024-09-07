import logging
import openai
from openai import OpenAI



"""

TRYING EACH KEY TO CHECK IF IT'S VALID

"""

def check_key(key):

    try:

        client = OpenAI(api_key = str(key).strip())

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say 'Hi'"}])

        response = completion.choices[0].message.content

        logging.info(f"\n\n------\n{response}\n------\n\n")

        return True

    except Exception as e:

        logging.info(f"{str(e).split()[2]} - Key is invalid: {key}")

        return False
