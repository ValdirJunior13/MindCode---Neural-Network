
# MindCode ![Static Badge](https://img.shields.io/badge/MindCode-red?style=for-the-badge)

Projeto desenvolvido como parte da disciplina de PI4 na Universidade Federal Rural de Pernambuco, Unidade Acadêmica de Belo Jardim. Esta iniciativa visa oferecer uma abordagem ágil para instruir de maneira eficiente um recém-contratado sobre o código utilizado pela empresa, em contraste com treinamentos convencionais que costumam se prolongar por semanas. Destaca-se, ainda, a considerável redução de custos associada a essa abordagem, restrita ao investimento no software indispensável.


## Stack utilizada

**Back-end:** ![Static Badge](https://img.shields.io/badge/Python%3D%3C3.8-brightblue?logo=python&color=fefffe)  ![Static Badge](https://img.shields.io/badge/huggingface-yellow?logo=githubcopilot&link=https%3A%2F%2Fhuggingface.co%2F)




### Deploy ![Static Badge](https://img.shields.io/badge/Linux-black?logo=Linux)


```bash
  cd my-project  
  pip install -r requirements.tx 
  chmod +x run.sh  
  ./run.sh  ${ cpu | cuda }
```

> OBS: run.sh enable device "cuda" for default 

### Deploy ![Static Badge](https://img.shields.io/badge/Docker-gray?logo=Docker&link=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2F)

 

```bash
  docker build -t . fastnetwork:latest
  docker run -p 8000:8000 8080:8080 fastnetwork:latest
```
> OBS: docker build requirement GPU

### Deploy ![Static Badge](https://img.shields.io/badge/Windows-cyan?logo=windows)


```bash
  Windows +r
  run.bat ${ cpu | cuda }
```
> OBS: run.bat enable device "cuda" for default 



### Documentação da API ![Static Badge](https://img.shields.io/badge/Swagger-apidocs-brightgreen?logo=swagger)

#### Retorna todos os itens

```http
  GET /localhost:8000/docs
```





## Autores

- [@alyssu][https://github.com/Alyssu]
- [@FelipeBert][https://github.com/FelipeBert]
- [@hellyaxs][ https://github.com/hellyaxs]
- [@JamersonCarlos][https://github.com/JamersonCarlos]
- [@ValdirJunior13][https://github.com/ValdirJunior13]


# Roadmap

- 

- 



