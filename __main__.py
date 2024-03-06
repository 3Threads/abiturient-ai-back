from infra.openAI.checker_ai import CheckerAI

if __name__ == "__main__":
    ai = CheckerAI()
    while True:
        prompt = input("Enter your prompt: ")
        print(ai.get_response_by_prompt(prompt))
