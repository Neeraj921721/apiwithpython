from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message from server ": "You're in root."}

@app.get("/user/{userid}")
async def get_user_details(userid: int):
    
    user_details = {}
    user_details['UserId'] = userid

    if userid == 1:
        user_details['UserName'] = 'Harry Potter'
        user_details['Gender'] = 'Male'
    elif userid == 2:
        user_details['UserName'] = 'Ron Weisely'
        user_details['Gender'] = 'Male'
    elif userid == 3:
        user_details['UserName'] = 'Hermoinie Granger'
        user_details['Gender'] = 'Female'


    return user_details