import warnings

warnings.filterwarnings("ignore")

import os

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file


def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local("./vectorstore/faiss_index", embeddings)

    return vectordb


def prompt_template():
    prompt_template = """Use the following pieces of context to answer the questions on SQL Injection Tools and Payloads at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    While answering use the format asked by the user. If required provide the necessary urls. For references, it is mandatory to provide the urls from the context.
    {context}

    Question: {question}
    Helpful Answer: """

    PROMPT_TEMPLATE = PromptTemplate(
        template=prompt_template, 
        input_variables=["context", "question"]
    )

    return PROMPT_TEMPLATE


def get_answer(user_prompt):
    vectordb = load_vectorstore()
    PROMPT_TEMPLATE = prompt_template()

    llm_chain = load_qa_chain(
        llm=OpenAI(model_name="gpt-3.5-turbo-0613"), 
        prompt=PROMPT_TEMPLATE
    )
    docs = vectordb.similarity_search(user_prompt)
    response = llm_chain(
        {"input_documents": docs, "question": user_prompt},
        return_only_outputs=True
    )

    return response["output_text"]
