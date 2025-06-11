import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from call_function import available_functions, call_function
from prompts import system_prompt
from call_function import available_functions


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):

    for x in range(20):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )
        for candidate in response.candidates:
            messages.append(candidate.content)
        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        if not response.function_calls:
            print("Final response:")
            print(response.text)
            return

        for function_call_part in response.function_calls:
            call = call_function(function_call_part, verbose)
            response_part = call.parts[0]
            messages.append(call)
            if not hasattr(response_part, "function_response") or not hasattr(response_part.function_response, "response"):
                raise Exception("Function response missing from call_function result!")
            if verbose:
                print(f"-> {response_part.function_response.response}")
    print("Final response:")
    print(response.text)
    return
    

if __name__ == "__main__":
    main()