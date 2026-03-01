from groq import generate_response

def get_essay_details():
    print("\n=== AI Writing Essay Assistant ===\n")
    topic = input("What is the topic of your essay? ").strip()
    essay_type = input("What type of essay are you writing?").strip()
    lengths = ["300 words","900 words","1200 words","2000 words"]
    print("Select essay word count:")
    for i, l in enumerate(lengths, 1):
        print(f"{i}. {l}")
    try:
        idx = int(input("> ").strip()) 
        length = lengths[idx-1] if 1 <= len(lengths) else "300 words"
    except ValueError:
        length = "300 words"
    target_audience = input("Target audience (e.g. high school students): ").strip()
    return {"topic": topic, "essay_type": essay_type, "length": length, "target_audience": target_audience}

def generate_essay_content(details):
    