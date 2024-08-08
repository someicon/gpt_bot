import asyncio
from g4f.client import Client
from g4f.gui import run_gui


# run_gui()

async def gpt_answer(question):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{question}"}],
    )
    print(response.choices[0].message.content)

async def main():
    question = input("Введите ваш запрос: ")
    await gpt_answer(question)

# Запускаем основную функцию
asyncio.run(main())
