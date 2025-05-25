from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_methods=["GET"],  # Allow GET method
    allow_headers=["*"],
)

# Dummy data: marks of 100 imaginary students (name: marks)
marks_data = {
    "X": 10,
    "Y": 20,
    "Alice": 78,
    "Bob": 85,
    "Charlie": 90,
    # Add more dummy names and marks here if needed
}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    result = []
    for n in name:
        result.append(marks_data.get(n, None))  # Return None if name not found
    return {"marks": result}
