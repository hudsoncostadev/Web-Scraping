import os
import requests
import zipfile
from bs4 import BeautifulSoup

target_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

download_dir = "downloads"
os.makedirs(download_dir,exist_ok=True)

response = requests.get(target_url)
soup = BeautifulSoup(response.text,"html.parser")

pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.endswith(".pdf") and ("Anexo-I" in href or "Anexo-II in href"):
      pdf_links.append(href)

downloaded_files = []
for pdf_url in pdf_links:
    pdf_name = os.path.join(download_dir, pdf_url.split("/")[-1])
    response = requests.get(pdf_url)
    with open(pdf_name,"wb") as f:
      f.write(response.content)
    downloaded_files.append(pdf_name)
    print(f"Baixado: {pdf_name}")

zip_path = "anexos.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
  for file in downloaded_files:
    zipf.write(file, os.path.basename(file))

print(f"Arquivos compactados em: {zip_path}")