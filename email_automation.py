

import pandas as pd
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

df = pd.read_csv("contacts.csv")
emails = []

for index, row in df.iterrows():
    name = row["name"]
    business = row["business"]
    need = row["need"]

    message = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens= 500,
        messages =[
            {"role": "user","content": f"Write a short professional email to {name} who owns{business}. They need help with {need}. keep it under 100 words. Friendly but professional tone."}
        ]
    )

    email_text = message.content[0].text
    emails.append({
        "name": name,
        "email": row["email"],
        "generated_email" : email_text

    })

    print(f"Generated email for {name})")
result_df = pd.DataFrame(emails)
result_df.to_csv("generated_emails.csv!")
print("All emails saved to generated_emails.csv!")


        
        
        









