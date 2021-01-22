# text-similarity-scorer
This repo contains files to code that deploys an API endpoint for a user to detect text similarity between 2 texts without the use of any libraries.


## Directory Structure
The directory structure is provided below.

```console
.
├── Dockerfile
├── DocumentSimilarity.py
├── LICENSE
├── README.md
├── constants.py
├── requirements.txt
├── server.py
├── similarity_scorer.py
├── templates
    ├── base.html
    ├── index.html
    └── output.html

 ```

##  Build steps:
Listed below are different ways to build and run the system. There are a total of 3 ways to build and run the system. They are:
1. Build from the git repo.
2. Build using docker image. 
    
---
   

## 1.  Build from the git repo.
*   Clone the project Git repo.
    ```console
    foo@bar:~$ git clone https://github.com/likith11/text-similarity-scorer.git
    ```
*   Move into the project directory.
    ```console
    foo@bar:~$ cd text-similarity-scorer
    ```
*   Create a virtual environment and activate it.
    ```console
    foo@bar:~$ python3 -m venv venv 
    foo@bar:~$ source venv/bin/activate
    ```

*   Install requirements from requirements.txt
    ```console
    (venv) foo@bar:~$ pip install -r requirements.txt
    ```
    &nbsp;



___

### ``` (1.1) - To RUN the command line text similarity scorer. Run the following command: ```
```console
(venv) foo@bar:~$ python similarity_scorer.py "Text 1 goes here" "Text 2 goes here"
```
> NOTE: Here "Text 1 goes here" and "Text 2 goes here" are 2 strings that are passed as the arguments. Replace text within double quotes to pass custom input. For more help pass -h after the executable file. A similarity score is displayed as output.
&nbsp;
### ``` (1.2) - To RUN the web server: ```
```console
(venv) foo@bar:~$ python server.py
```
> GUI Steps: 
> * Navigate to [http://0.0.0.0:5000/](http://0.0.0.0:5000/) or [http://localhost:5000/](http://localhost:5000/) (Replace port number if its a different port on your machine. The default port above is 5000).
> * Two text areas with label _Text Area 1_ and _Text Area 2_ along with a blue _Process_ button is displayed.
> * Input text to be compared to the text boxes.
> *  Click on _Process__
> * A new screen with Translucent alert box is shown with the corresponding Similarity Score calculated
> * Click on _Retry?_ button to go back to the main screen and repeat the process.

> API Call: 
> * API end point is deployed at [http://0.0.0.0:5000/api/similarity](http://0.0.0.0:5000/api/similarity) where POST request is accepted.
> * The API accepts text inputs in the JSON format of 
> ```json
>   {
>        "text_one" : "Text 1 goes here",
>        "text_two" : "Text 2 goes here"
>
>    }
>```
> * An example _curl_ command is 
> ```console 
> curl -d '{"text_one" : "Text 1 goes here", "text_two" : "Text 2 goes here"}' -H 'Content-Type: application/json' 
> http://0.0.0.0:5000/api/similarity 
> ```
> * An API response json is returned with the similarity score.
> 

&nbsp;


---

&nbsp;

## 2.  Pull from Docker Hub / Build Docker Image Locally.
*   Pull image from docker hub.
    ```console
    foo@bar:~$ docker pull likithponnanna/python-similarity:submission
    ```
*   Run the image that was pulled. Below port 5000 is mapped between the external and docker container.
    ```console
    foo@bar:~$ docker run -p 5000:5000 python-similarity 
    ```

> *  NOTE : To run the server follow the steps mentioned in section __1.2__ API Call.

&nbsp;
&nbsp;

* [OPTIONAL]   To build the docker image using the dockerfile locally run the following command before initiating docker run.
    ```console
    foo@bar:~$ git clone https://github.com/likith11/text-similarity-scorer.git
    foo@bar:~$ cd text-similarity-scorer
    foo@bar:~$ docker build -t python-similarity .
    ```


