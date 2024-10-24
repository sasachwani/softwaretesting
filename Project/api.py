from fastapi import FastAPI

app = FastAPI()

# FastAPI endpoint to get user information
@app.get("/user-info")
def get_user_info(name: str, age: int, location: str, occupation: str):
    return {
        "name": name,
        "age": age,
        "location": location,
        "occupation": occupation
    }
