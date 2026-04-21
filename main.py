from fastapi import FastAPI
from api.routes.brinquedo_routes import router as brinquedo_routes
from api.routes.crianca_routes import router as crianca_routes
from api.routes.emprestimos_routes import router as emprestimos_routes


app = FastAPI(title="API_emprestimo_de_brinquedos")


@app.get("/")
def home():
    return {"Api funcional"}



app.include_router(brinquedo_routes)
app.include_router(crianca_routes)
app.include_router(emprestimos_routes)

