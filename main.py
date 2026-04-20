from fastapi import FastAPI
from api.routes.brinquedoRoutes import router as brinquedo_routes
from api.routes.criancaRoutes import router as crianca_routes
from api.routes.emprestimosRoutes import router as emprestimos_routes


app = FastAPI(title="API_emprestimo_de_brinquedos")


@app.get("/")
def home():
    return {"Api funcional"}



app.include_router(brinquedo_routes)
app.include_router(crianca_routes)
app.include_router(emprestimos_routes)

