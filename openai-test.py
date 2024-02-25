from dotenv import load_dotenv
import extractPdfText

load_dotenv()  # Load environment variables from .env file


from openai import OpenAI
client = OpenAI()

# def generate_keywords(prompt):
#     response = client.chat.completions.create(
#         model="gpt-4-turbo-preview", 
#         messages=[
#           {"role": "system", "content": "You are vell versed and skilled in analysing technical documents and understand the field of software engineering"},
#           {"role": "user", "content": prompt}
#         ],
#     )
#     generated_keywords = response.choices[0].message.content
#     return generated_keywords

# print(extractPdfText.jd_text)
# print("-----------------------------")

# prompt = "Generate keywords relevant to the techical stack and skills required for the given job description."\
#    " Include any programming language, technology name, etc mentioned in the description as keywords too"\
#    " Also include technical qualifications required in keywords like framework names, etc eg. React, tensorflow, etc "\
#    " Only include keywords mentioned in the following job description. What I have mentioned are examples"\
  #  " Make sure the output result is comma separated. eg. keyword1, keyword2, keyword3. Job Description follows:  \n\n" + extractPdfText.jd_text

# print(prompt)
# generated_keywords = generate_keywords(prompt)
# keywords = generated_keywords.split(', ')

# Print or use the generated keywords
# print(generated_keywords)

def compareJDResume(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview", 
        messages=[
          {"role": "system", "content": "You are vell versed and skilled in analysing technical documents and understand the field of software engineering"},
          {"role": "user", "content": prompt}
        ],
        seed=1
    )
    result = response.choices[0].message.content
    return result

prompt = "Here is a given job description: \n\n" + extractPdfText.jd_text + "\n\n"\
        "Understand the above job description, skills required, qualifications, technical stack required."\
        "Now consider the following text from my resume: \n\n" + extractPdfText.resume_text + "\n\n"\
        "Align my resume to the given job description and score based on 100. Output format: Resume Score = [value]."\
        "Dont include anything else in output, no reason, no justification"

print(compareJDResume(prompt))