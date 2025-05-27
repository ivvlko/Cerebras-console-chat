1. How to run locally:
- create virtualenv
- install huggingface_hub library (the only one needed) with **pip install huggingface_hub**
- replace my placeholder for API_KEY with actual key that I will send separately
- run **python llm_client.py** and the chat should pop up

2. What is this actually and why its done like this:
- HuggingFace is a nice completely free library for ML enthusiasts. Setting this took me 2 minutes and the model acts really well and I got free tokens and limited requests without sending any bank credentials (required for example with OpenAI). This is python client - [Click](https://github.com/huggingface/huggingface_hub)
- Generated API Key from the UI and gave permissions. You can see all the models here https://huggingface.co/models I chose Cerebras randomly https://huggingface.co/docs/inference-providers/en/providers/cerebras
- Fun fact - the model returns the thought process behind its final answer. Probably there is an argument that disables this but I didn't want to spend too much time looking at Cerebras API  so I wrap a quick cleaning process in *clean_thought_process_from_response* function. You will be asked at the beggining of the chat whether you want it enabled or disabled.
- Error handling is a bit dull at the moment. The server gives me a string as response even when unauthorized for example. So I can't check "response.status" or something like this quickly. We can go explore Cerebras api but as quick solution here I just check whether "Error: 401" is in response. This is bad and needs rework but its quick working solution.   
