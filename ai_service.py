import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))   

def create_simple_task(task):
    if not client.api_key:
        raise ValueError("OpenAI API key is not set. Please set it in the .env file.")  
    try:
        prompt = f"""Desglosa la siguiente tarea complja en una lista de 3 a 5 subtareas simples y accionables
        Tarea: {task}
        Formato de respuesta:
        - Subtarea 1
        - Subtarea 2
        - Subtarea 3
        - Etc...
        Responde solo con la lista de subtareas, empezando cada línea con un -.
        """
        params = {
            "model": "gpt-3.5-turbo",   
            "messages": [
                {"role": "system", "content": "Eres un asistente que ayuda a desglosar tareas complejas en subtareas simples y accionables."},
                {"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 150,
        }
        response = client.chat.completions.create(**params)
    except Exception as e:
        print(f"Error creating task: {e}")