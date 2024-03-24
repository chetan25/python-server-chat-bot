
from langchain.prompts import HumanMessagePromptTemplate, MessagesPlaceholder, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory
from dotenv import load_dotenv

load_dotenv()

class ChatBotSingleTon:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
        print('Creating the object')
        # chat = ChatOpenAI(verbose=True)

        # memory = ConversationSummaryMemory(
        #     memory_key="messages",
        #     return_messages=True,
        #     llm=chat
        # )

        # prompt = ChatPromptTemplate(
        #     input_variables=["content", "messages"],
        #     messages=[
        #         MessagesPlaceholder(variable_name="messages"),
        #         HumanMessagePromptTemplate.from_template("{content}")
        #     ]
        # )

        # cls.chain = LLMChain(
            # llm=chat,
            # prompt=prompt,
            # memory=memory,
            # verbose=True
        # )

        # cls.name = Shark()


        cls._instance = super(ChatBot, cls).__new__(cls)
    return cls._instance
  
class ChatBot:
   def __init__(self):
        print("Initializing chat bot")
        chat = ChatOpenAI(verbose=True)

        memory = ConversationSummaryMemory(
            memory_key="messages",
            return_messages=True,
            llm=chat
        )

        prompt = ChatPromptTemplate(
            input_variables=["content", "messages"],
            messages=[
                MessagesPlaceholder(variable_name="messages"),
                HumanMessagePromptTemplate.from_template("{content}")
            ]
        )

        self.chain = LLMChain(
            llm=chat,
            prompt=prompt,
            memory=memory,
            # verbose=True
        )

   def invoke(self, message):
      print(message)
      result = self.chain.invoke({
        "content": message
      })

      return result
          
