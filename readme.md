Step 1- Create .env file and paste the below Api Keys and Configurations.

    OPEN_AI_API_KEY= YOUR API KEY
    LANGSMITH_API_KEY= YOUR API KEY
    TAVILY_API_KEY= YOUR API KEY
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_PROJECT=Reflexion Agent

Step 2- Install the dependencies using
    pip install -r requirements.txt

Step 3- Open the main.py file, update the user_query with your custom query.

Step 4- Run the file. It will take roughly 2 minutes to complete.
    Meanwhile, go to langsmith and start reading your traces.
    Boom, you have reflexion agent working with two chains.

    ![Image](https://github.com/user-attachments/assets/c2bba1f0-4a1f-4b06-bf97-44e9410744cc)
