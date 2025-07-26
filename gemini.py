import google.generativeai as genai


def setup(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-1.5-flash")

def question_generator(model, content):
    prompt = (
        "Act like a knowledgeable teacher. Based on the following content, generate 10 multiple choice questions. "
        "Each question should have 4 options (a-d), and mark the correct answer.\n\n"
        f"Content:\n{content}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()
