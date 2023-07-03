from langchain import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains.conversation.memory import ConversationBufferMemory

import streamlit as st # for the easy showcase of the frontend

# we create various functions that will allow the users to ask certain questions
# for encryption and decryption of a word
def ceaser_cypher(word):
    word_input = ''
    for letter in word:
        word_input += chr(ord(letter)+3)
    return word_input

def decrypt(word):
    decrypt_word = ''
    for letter in word:
        decrypt_word += chr(ord(letter)-3)
    return decrypt_word
# to find factorial of a number
def fact(n):
    if n ==1:
        return 1
    else:
        return(n*fact(n-1))
# to sort the string given by user 
def sorting(string):
    return ''.join(sorted(string))

tools = [
    Tool(
        name = "Ceaser Cypher",
        func = lambda string: ceaser_cypher(string),
        description= "use when user wants to find the ceaser cypher of a word", 
    ),
    Tool(
        name = "Decryption",
        func = lambda string: decrypt(string),
        description= "use when user wants to get the original word back", 
    ),
    Tool(
        name = "Factorial",
        func = lambda n: str(fact(int(n))),
        description= "use when user wants to find the factorial of a number", 
    )
]

memory = ConversationBufferMemory(memory_key = "chat_history")
llm = OpenAI(temperature = 0, verbrose = True)
agent_chain = initialize_agent(tools, llm, agent = "conversational-react-description", memory = memory, verbrose = True)

st.header(":purple[Ask me and I'll respond :)]")
user_input = st.text_input("You: ")
#initialize the memory buffer
if 'memory' not in st.session_state:
    st.session_state['memory'] = ''
# streamlit button
if st.button('Sumbit'):
    st.markdown(agent_chain.run(input = user_input))
    #prints the memory buffer
    # adds conversation history to the memory buffer
    st.session_state['memory'] += memory.buffer
    print(st.session_state['memory'])
    

