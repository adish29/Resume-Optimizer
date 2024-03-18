from dotenv import load_dotenv
import openai

class myOpenAI:
    chat_model = "gpt-4-turbo-preview"
    embeddings_model = "text-embedding-3-large"

    def __init__(self, api_key, chat_model = chat_model, embeddings_model = embeddings_model):
        """
        Wrapper for the OpenAI API
        :param api_key:
        :param chat_model:
        :param embeddings_model:
        """
        openai.api_key = api_key or load_dotenv("OPENAI_API_KEY")
        self.chat_model = chat_model
        self.embeddings_model = embeddings_model

    def ask_llm(self, prompt):
        """
        Uses the openai ChatCompletion API to generate a response
        :param prompt:
        :return:
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.chat_model,
                messages=prompt,
            )
        except openai.error.OpenAIError as e:
            print("Error: ", e)
            return

        return response.choices[0]["message"]["content"].strip()
    
    def create_embedding(self, text):
        """
        Uses the openai EmbeddingCreate API to generate an embedding
        :param text:
        :return:
        """
        return openai.Embedding.create(
            input=text,
            model=self.embeddings_model,
        )

    @staticmethod
    def create_prompt(system_prompt=None, user_prompt=None):
        """
        Generate a message for the LLM with given prompts
        for the chat completion API
        :param user_prompt: User prompt
        :param system_prompt: System prompt (Optional)
        :return:
        """
        system_message = {"role": "system", "content": system_prompt}
        user_message = {"role": "user", "content": user_prompt}
        if not user_prompt:
            raise ValueError("User prompt cannot be empty")
        return [system_message, user_message] if system_prompt else [user_message]