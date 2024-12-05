# streaming 처리

import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# 처음 호출 할 떄 모델을 생성한 뒤 cache(저장소)에 저장하며, 
# 그리고 다음 요청시 새로 생성하지 않고 cache 에 저장한 모델을 반환한다.

@st.cache_resource # cache 에 model을 저장하고 계속 사용함.. 매번 model을 생성하지 않아도 됨.
def get_model():
    model = ChatOpenAI(model="gpt-4o-mini", streaming=True)
    return model

model = get_model()

st.title("ChatBot 위젯 튜토리얼")

## session_state 생성(dictionary 형식) ->  시작부터 종료까지 사용자별로 유지되는 값.
#### "message_list":[{"role":"user", "message":"1.질문"}, {"role":"ai", "message":"1답변"}, {}, {}, ...]

# session_state 에 message_list를 추가
if "message_list" not in st.session_state:
    st.session_state["message_list"] = []  # 비어있는 리스트로 저장.


###########################################
# 기존 대화내용을 출력
###########################################
for message in st.session_state['message_list']:
    with st.chat_message(message['role']):
        st.write(message['message'])


## 사용자 질문(prompt)를 입력받기 - chat_input()
prompt = st.chat_input("User:")
if prompt:

    # session_state의 message_list에 {"role":"user", "message":prompt} 추가
    st.session_state["message_list"].append({"role":"user", "message":prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("ai"):
        full_message = ""
        message_placeholder = st.empty()    # update 가능한 container
        for chunk in model.stream(prompt):  # 토큰이 생성되는대로 전달됨.
            full_message += chunk.content
            message_placeholder.write(full_message)
        # 응답이 완ㅇ료
        st.sesstion_state['message_list'].append({"ai":full_message})
