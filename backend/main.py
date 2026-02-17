from fastapi import FastAPI

app = FastAPI()

#It can prefer to as the path operation or the "route"
@app.get("/")
async def root():
    return {"message": "Fraud Detection API Running"} #this is the data that is send back to the user
