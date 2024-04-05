from fastapi import *

app = FastAPI(
    docs_url = None,
    redoc_url = None
)

@app.get("/", status_code = 308, response_class = responses.RedirectResponse)
async def root():
    return "https://github.com/PlazmaMC/PlazmaBukkit"

def main():
    urls = {
        "discord": "https://discord.gg/AZwXTA9Pgx"
    }

    @app.get("/{target:str}", status_code = 308)
    async def main(target: str):
        if (target not in urls):
            return { 404: {"description": "Not found"} }

        return responses.RedirectResponse(urls[target])
main()
