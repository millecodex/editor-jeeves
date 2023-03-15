# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
#help(openai)
#Set your OpenAI API key
openai.api_key = "xxx"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful editor that maintains latex formatting."},
        {"role": "user", "content": "Can you edit this paragraph of text?"},
        {"role": "user", "content": "The absence of sustainable development will lead to software stagnation although it can be difficult to determine if a project has died~\cite{Chengalur2010}. The concept of forking \begin{xx} [Definition? fit?]\end{xx} within the open source movement can preserve a project's genetic lineage by reviving abandoned repositories that have been  considered dead. New participants can easily fork code and evolve it into something new without the friction of attempting modifications on the original code base. It has been shown that forking benefits sustainability"}
    ],
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.7,
)

# # Create a new ChatCompletion request
# response = openai.Completion.create(
#     engine="davinci",
#     prompt="You are a helpful assistant.\n\nUser: Who won the world series in 2020?\nAssistant: The Los Angeles Dodgers won the World Series in 2020.\n\nUser: Where was it played?",
#     max_tokens=50,
#     n=1,
#     stop=None,
#     temperature=0.7,
# )

# Print the response
#print(response['choices'][0]['message']['content'])
print(response)