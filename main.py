import requests
import html

def get_trivia_question():
    url = "https://opentdb.com/api.php?amount=1"
    response = requests.get(url)
    data = response.json()
    question = html.unescape(data["results"][0]["question"])
    correct_answer = html.unescape(data["results"][0]["correct_answer"])
    return question, correct_answer

def trivia_quiz():
    question, correct_answer = get_trivia_question()
    print("Here's a trivia question for you:")
    print(question)
    user_answer = input("Type your answer here: ")
    if user_answer.lower() == correct_answer.lower():
        print("You got it right!")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

if __name__ == "__main__":
    trivia_quiz()