from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

llm = OllamaLLM(model="llama3")

'template = PromptTemplate.from_template("Cuéntame un chiste en español que tenga sentido sobre {tema}")'
'chain = template | llm'
'print(chain.invoke({"tema": "El videjuego GTA5"}))'

template = ChatPromptTemplate.from_messages([("user", "Cuéntame un chiste en español que tenga sentido sobre {tema}")])
chain = template | llm
print(chain.invoke({"tema": "El videjuego Silent hill 2 remake"}))

'template = PromptTemplate.from_template("Dime una historia de {tema} que incluya al personaje {nombre} en español")'
'chain = template | llm'
'print(chain.invoke({"tema": "Terror", "nombre": "Harry Potter y freddy mercury"}))'

'respuesta = llm.invoke("El rainbow six siege es un juego competitivo ?")'
'print(respuesta)'

""" from langchain_core.prompts import PromptTemplate """
from langchain_core.prompts import ChatPromptTemplate
""" prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente de IA, Que esta basado en la edad media, que habla espanol y que es muy divertido"),
    ("user", "{consulta}"),
])
chain = prompt | llm
respuesta = chain.invoke({"consulta": "Como puedo cultivar trigo"})
print(respuesta)
 """
