
from fastapi import FastAPI,UploadFile


app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello, World!"}

@app.get('/contact')
def contact():
    return {"message": "Contact us at example@email.com"}

@app.post('/uploads')
def handleImage(file: UploadFile):
    print(file.filename)
    return {"status": "success", "filename": file.filename}
import uvicorn
uvicorn.run(app)  
