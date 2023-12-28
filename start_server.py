from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from database.db_manager import base_manager
from users import router as users_router
from store import router as store_router
from Workers import router as Workers_router
from Providers import router as Providers_router
from Orders import router as Orders_router
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH

app = FastAPI()

app.include_router(users_router, prefix='/users')
app.include_router(Workers_router, prefix="/workers")
app.include_router(store_router, prefix='/store')
app.include_router(Providers_router, prefix='/Providers')
app.include_router(Orders_router, prefix='/Orders')




@app.get('/')
def root():
    return RedirectResponse('/docs')
