import torch
from transformers import pipeline, AutoTokenizer
import telepot
from telepot.loop import MessageLoop
import time

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
                torch_dtype=torch.float32, device_map="auto")  # Use float32 if bfloat16 isn't supported

print("Pipeline loaded successfully.")
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg['text'])
    messages = [
    {"role": "user", "content": msg['text']},]
    # Generate text from the pipeline
    outputs = pipe(messages, max_length=100, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    # Extract the assistant's response
    assistant_response = None
    if len(outputs) > 0:
        assistant_response = outputs[0]['generated_text'][1]["content"]
    else:
        assistant_response = "I'm sorry, I don't have a response"
    # Print the assistant's response
    print(assistant_response)
    bot.sendMessage(chat_id, assistant_response)
bot = telepot.Bot('Bot API')
MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)
