
from ollama import chat

questions = [
    "What is 2 + 2? Answer with only the number.",
    "What is the capital of France?",
    "Write only the word ORANGE."
]

for question in questions:

    print("\nQUESTION:", question)

    response = chat(
        model="gemma3:1b",
        messages=[
            {"role": "user", "content": question}
        ],
        options={"temperature": 0}
    )

    print("ANSWER:", response.message.content)
