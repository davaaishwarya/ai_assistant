
from django.shortcuts import render
from groq import Groq

client = Groq(
    api_key="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"
)

def home(request):
    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        if question:
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant. Answer any question clearly and accurately."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response.choices[0].message.content

    return render(request, "home.html", {"answer": answer})
