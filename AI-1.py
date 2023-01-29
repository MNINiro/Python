import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="how to receive more traffic to my website www.mniniro.com?\n\n1. Create quality content that is relevant to your audience.\n2. Optimize your website for search engines by using targeted keywords.\n3. Use social media to promote your website and content.\n4. Perform link building to gain backlinks from other websites.\n5. Run targeted online advertising campaigns.\n6. Create a blog and post regular content.\n7. Submit your website to online directories.\n8. Reach out to influencers in your niche.\n9. Engage with your audience on forums and discussion boards.\n10. Leverage email marketing to reach out to potential customers.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)