from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

description = """
To use the interactive docs:
- Click on an endpoint
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

app = FastAPI(
    title='DS API',
    description=description, 
    docs_url='/',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)