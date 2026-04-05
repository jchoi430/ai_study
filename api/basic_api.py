import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


def main():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-flash')
    return model.generate_content("Write a short poem about Python programming.")


if __name__ == "__main__":
    res = main()
    print("### Response ###")
    print(res.text)

