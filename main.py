from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from os.path import isdir, isfile
from typing import Optional


app = FastAPI()


@app.get('/')
def return_file(filename: Optional[str] = ''):
    if not filename:
        return RedirectResponse('/?filename=index.html')
    filepath = f'./root/{filename}'.replace('../', '').replace('..\\', '').rstrip('/').rstrip('\\')
    print(filepath)
    while '../' in filepath or '..\\' in filepath:
        filepath = filepath.replace('../', '').replace('..\\', '')

    if filepath.split('.')[-1] not in ('html', 'txt'):
        raise HTTPException(
                status_code=406,
                detail='I will NOT let you open it.'
            )

    if not isdir(filepath) and isfile(filepath):
        return FileResponse(filepath)

    raise HTTPException(
            status_code=404,
            detail=f"Requested file('/{filename}') does not exist."
        )


@app.get('/favicon.ico')
def fake_favicon():
    return ''

