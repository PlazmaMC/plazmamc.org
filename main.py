from fastapi import *

app = FastAPI(
    docs_url = None,
    redoc_url = None,
    default_response_class = responses.RedirectResponse
)

@app.get("/", status_code = 308)
async def root():
    return "https://github.com/PlazmaMC/PlazmaBukkit"

def main():
    urls = {
        "downloads": "https://docs.plazmamc.org/plazma/about/downloads",
        "discord": "https://discord.gg/AZwXTA9Pgx"
    }

    @app.get("/{target:str}", status_code = 308)
    async def main(target: str):
        if (target not in urls):
            return "/"

        return urls[target]
main()
