# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
 
 # Se der problean No module distutils.cmd
 #sudo apt-get install python3.7-distutils
 
 #virtualenv .mlops_gcp_env -python=python3.7
 
 # Exportar variáveis de ambiente (dentro do env)
 # export BASIC_AUTH_PASSWORD=junior
 # export BASIC_AUTH_USER=elton
 
 # Na GCP
 
 # sudo apt-get update    (Atualiza)
 
 # sudo apt-get install git-all (Instala git)
 
 # git clone https://github.com/Elton-J/mlops_gcp_alura.git (Clona repo pra dentro da maquina gcp)
 
 # sudo aptget install python3-pip (Instala python)
 
 # sudo pip install virtualenv  (Instala virtual env)
 
 # virtualenv .mlops_gcp_alura (Cria env)
 
 # source .mlops_gcp_alura/bin/activate (Ativa env)
 
 # pip install -r requirements.txt
 
 #  Alterar o caminho de acesso ao modelo de "../../models/modelo.sav" pra "models/modelo.sav""
   
 # python main.py
 
 
 # Serverless (gcloud deploy app)
 
 # Docker
 # docker build -t mlops_gcp_alura --build-arg BASIC_AUTH_USERNAME_ARG=elton --build-arg BASIC_AUTH_PASSWORD_ARG=junior . (pasta onde está o dockerfile)
 
 # docker run -p 5000:5000 mlops_gcp_alura:latest
 
 
 # Cloud RUN
 # gcloud auth configure-docker (Comandos docker com autenticação gcloud)
 
 # docker tag mlops_gcp_alura gcr.io/mlops-gcp-alura/mlops_gcp_alura (tageia a imagem no gcp)
 
 # docker push  gcr.io/mlops-gcp-alura/mlops_gcp_alura (Envia a imagem pro gcp)
 