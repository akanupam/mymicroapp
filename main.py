from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="MyMicroApp", version="1.0.0")

# ============ Data Models ============
class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    title: str
    description: str

# ============ In-Memory Storage ============
users_db = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
]

items_db = [
    Item(id=1, title="Laptop", description="High-performance laptop"),
    Item(id=2, title="Mouse", description="Wireless mouse"),
]

# ============ Endpoints ============

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to MyMicroApp API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "users": "/api/users",
            "items": "/api/items",
            "docs": "/docs"
        }
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "mymicroapp"
    }

@app.get("/api/users", response_model=List[User], tags=["Users"])
def get_users():
    """Get all users"""
    return users_db

@app.get("/api/users/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: int):
    """Get a specific user by ID"""
    for user in users_db:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.post("/api/users", response_model=User, tags=["Users"])
def create_user(user: User):
    """Create a new user"""
    users_db.append(user)
    return user

@app.get("/api/items", response_model=List[Item], tags=["Items"])
def get_items():
    """Get all items"""
    return items_db

@app.get("/api/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    """Get a specific item by ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/api/items", response_model=Item, tags=["Items"])
def create_item(item: Item):
    """Create a new item"""
    items_db.append(item)
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
