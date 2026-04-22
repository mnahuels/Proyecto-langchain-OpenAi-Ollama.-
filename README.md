
# LangChain Agent: OpenAI + Ollama con Herramientas de Búsqueda 🤖🔍

Este proyecto es una prueba sobre la implementación de agentes inteligentes utilizando **LangChain**. El objetivo principal fue comparar el rendimiento de modelos comerciales (**OpenAI**) frente a modelos locales (**Ollama**) y luego evaluarlos mediante el uso de herramientas de búsqueda externa.

## 🌟 Características

- **LLMs**: Se uso `gpt-3.5-turbo` (OpenAI) y un modelo local como `llama3`.
- **Agente**: Implementación de un agente que razona y actúa para resolver consultas .
- **Herramientas Integradas**:
  - **Wikipedia**: Para obtener resúmenes históricos y enciclopédicos.
  - **DuckDuckGo**: Para realizar búsquedas web de actualidad y noticias recientes.

---
## 🛠️ Requisitos 

1. **Python**
2. **Ollama** (si deseas ejecutar modelos locales): [Descargar aquí](https://ollama.com/)
3. **API Key de OpenAI** (opcional solo para las pruebas, ya que el agente esta realizado con Ollama).
4. **Instalacion de las dependencias** (pip install langchain langchain-openai langchain-community wikipedia duckduckgo-search)

---
