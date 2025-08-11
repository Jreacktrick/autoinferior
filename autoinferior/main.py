


def main():

    import os
    import sys
    from dotenv import load_dotenv
    from google import genai
    from google.genai import types

    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    
    try:
        
        user_prompt = sys.argv[1]
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages
        )
        if len(sys.argv) < 3:
            print(response.text)
        elif sys.argv[2] == '--verbose':
            print(f'User prompt: {user_prompt}')
            print(f'{response.text}')
            print('Prompt tokens:',response.usage_metadata.prompt_token_count)
            print('Response tokens:',response.usage_metadata.candidates_token_count)
        
    except:
        print("You need to provide a question!")
        sys.exit(1)


#    print(f"User prompt:{user_prompt}\n{response.text}")
#    print('Prompt tokens:',response.usage_metadata.prompt_token_count)
#    print('Response tokens:',response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
