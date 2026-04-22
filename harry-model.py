from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="harry-model")
respuesta = llm.invoke("Hola, ¿cómo estás?")
respuesta = llm.invoke("Quien descubrio america ?")
print(respuesta)
