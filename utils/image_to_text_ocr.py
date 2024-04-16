import requests_async as requests
import asyncio
async def Image_to_text(image_path, lang):

    response = await requests.post("http://127.0.0.1:8000/api/v1/image-to-text/", data={"lang":lang},files={'image': open(image_path, 'rb')})
    res = response.json()
    
    result = res.get("data").get("result")
    return result


    