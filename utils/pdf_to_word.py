import requests_async as requests
async def pdf_to_word(pdf_file, id):

    response = await requests.post("http://127.0.0.1:8000/api/v1/pdf-to-word/", files={'pdf_file': open(pdf_file, 'rb')})
    res = response.json()
    word_file_url = "http://127.0.0.1:8000" + res.get("result")
    word_file_res = await requests.get(word_file_url)
    with open(f"downloads/{id}.docx", "wb") as file:
        file.write(word_file_res.content)
        print(file.name)
        return file.name
