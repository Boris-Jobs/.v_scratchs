from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

model_name = "Qwen/Qwen-1_8B-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cuda",
    trust_remote_code=True
).eval()
response, history = model.chat(tokenizer, "你听说过哪些大模型安全对齐的经典方法？", history=None)
print(response)