from langchain import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains.conversation.memory import ConversationBufferMemory

import streamlit as st # for the easy showcase of the frontend

# we create various functions that will allow the users to ask certain questions
# for encryption and decryption of a word
def ceaser_cypher(word):
    word_input = ""
    for letter in word:
        word_input += chr(ord(letter)+3)
    return word_input

def decrypt(word):
    decrypt_word = ""
    for letter in word:
        decrypt_word += chr(ord(letter)-3)
    return decrypt_word
# to find factorial of a number
def fact(n):
    if n ==1:
        return 1
    else:
        return(n*fact(n-1))
    
def sorting(string):
    return ''.join(sorted(string))

