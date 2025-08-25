from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from openai import OpenAI

st.title("このアプリは２種類の専門家に回答を求める事ができます。")
st.title("専門家A：料理に強い専門家、専門家B：医療に強い専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで回答を求めることができます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["専門家A", "専門家B"]
)

input_message = ""
if selected_item == "専門家A":
    input_message = st.text_input(label="料理に関する質問をしてください")
elif selected_item == "専門家B":
    input_message = st.text_input(label="医療に関する質問をしてください")

if st.button("実行"):
    if not input_message:
        st.error("質問内容を入力してください")
    else:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        if selected_item == "専門家A":
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたは料理研究家です。アドバイスを提供してください。"},
                    {"role": "user", "content": input_message}
                ],
                temperature=0.5
            )
            st.write(completion.choices[0].message.content)

        elif selected_item == "専門家B":
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"},
                    {"role": "user", "content": input_message}
                ],
                temperature=0.5
            )
            st.write(completion.choices[0].message.content)