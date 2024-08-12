# qua llm

A Q&A chatbot built around Meta's latest open source large language model (Llama-3.1-70b).

### Mode of deployment
The chatbot is deployed via a RESTful API. 


### Installation

* Get a copy of the source code of this project into your local repository.

```
git clone https://github.com/KelvinJC/qua-llm.git
```

* The code will be packaged in a directory named qua-llm so change into that directory

```
cd qua-llm
```

* To begin using the application, initialise the server by running the following command

```
python main.py 
```

### Usage
By default, the api server listens to requeststhrough on port 8888 so once the server is running, 
copy and paste ```http://127.0.0.1:8888/chat``` into your Postman or any API client of your choice.<br>

To prevent clashes on port 8888, make sure no other app is running locally on that port.
