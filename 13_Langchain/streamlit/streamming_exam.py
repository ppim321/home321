from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.callbacks import StreamingStdOutCallbackHandler
# LLM 의 응답을 chunk 단위(쪼개서 받는 것)로 받아서 출력하는 callback.
# callback -> LLM 과 연동할때 특정 Event(특정 상황)마다 호출되는 method를 제공하는 class들을 의미함.    
# 
load_dotenv()

prompt_template = ChatPromptTemplate(
    [
        ("system", "당신은 AI Assistant입니다. 질문에 정확한 답변을 해주세요. 모르면 모른다고 하세요"),
        ("user", "{query}")
    ]
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True,  # chunk 단위로 나눠서 제공해 달라. 생성되는 대로 제공.
    callbacks=[StreamingStdOutCallbackHandler()]

)


query = input("질의할 내용:")
prompt = prompt_template.invoke({"query":query})
# result = model.invoke(prompt).content
# print(result)
# # streaming=True:  model.stream(prompt):generator
for chunk in model.stream(prompt):
    print(chunk.content, end="")