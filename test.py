import asyncio
from g4f.client import Client
from g4f.gui import run_gui


# run_gui()

# async def gpt_answer(question):
#     client = Client()
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": f"{question}"}],
#     )
#     print(response.choices[0].message.content)
#
# async def main():
#     question = input("Введите ваш запрос: ")
#     await gpt_answer(question)
#
# # Запускаем основную функцию
# asyncio.run(main())

str = "88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589"

print(len(str))
