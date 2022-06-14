# rest api
## Tools
1. Language : Python 3.7
2. Dependencies : Fastapi, uvicorn
3. Platform : Ubuntu, Docker

## Usage
On the terminal
> ```` git clone https://github.com/anushapv2000/EXAM.git````</br>

 Navigate to the directory restapi-service</br>
 
 Run the following Command
 1. Build the image
 >````sudo docker build --file dockerfile -t restapi_img .````
 2. Run the container
 >````docker run -d --name restapi_container -p 8080:8080 restapi_img````
 3. Check the container status using
 >````docker ps -a````
 4. Once the container start running ,send the request using curl command
 >````curl -X POST http://localhost:8000/````
 
 Response will be shown in the terminal
 
 
 
 
