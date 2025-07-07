from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import piexif
import io

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_image(request: Request, file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid file type"})

    contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    
    # Remove EXIF data
    data = list(img.getdata())
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(data)
    
    # Save the cleaned image to a byte stream
    output = io.BytesIO()
    if new_img.mode == 'RGBA':
        new_img = new_img.convert('RGB')
    new_img.save(output, format='JPEG')
    output.seek(0)
    
    # Return the cleaned image as a downloadable file
    return StreamingResponse(output, media_type="image/jpeg", headers={"Content-Disposition": f"attachment; filename=cleaned_{file.filename}"})
