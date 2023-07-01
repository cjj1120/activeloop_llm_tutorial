## Input Limitation 
Each LLM has maximum token limitation, but u can split the document into chunk and let the LLM consume. Although, splitting into multiple chunks can hurt the coherence of the text. 

GPT-family models use Causal Language modeling, which enable them to generate contextually relevant text. 


## callback for visibility 
```
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

llm = OpenAI(model_name="text-davinci-003", n=2, best_of=2)

with get_openai_callback() as cb:
    result = llm("Tell me a joke")
    print(cb)
```

Output:
```
Tokens Used: 46
	Prompt Tokens: 4
	Completion Tokens: 42
Successful Requests: 1
Total Cost (USD): $0.0009199999999999999
```



