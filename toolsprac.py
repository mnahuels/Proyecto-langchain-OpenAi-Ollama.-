from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250) 
""" Que me devuelva el mejor resultado, con un maximo de 250 caracteres """
tool = WikipediaQueryRun(api_wrapper=api_wrapper)

""" print(tool.name)
print(tool.description)
print(tool.args) """

print (tool.run("Peñarol"))

