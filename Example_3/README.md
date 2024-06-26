# ⭐ 기초적인 docker 스터디 ⭐

# Power By Sangmin Lee

## 📚 준비
- [Docker 설치](https://docs.docker.com/get-docker/)
- [Docker Compose 설치](https://docs.docker.com/compose/install/)

## 🏔️ 목표
- Docker를 사용하여 간단한 서버를 실행할 수 있다.
- Docker Compose를 사용하여 여러 컨테이너를 실행할 수 있다.
- 기본적인 백엔드 서버 설정을 이해할 수 있다.

## 🌈 진행요구사항
- 해당 저장소를 clone 받는다.
- clone 받은 폴더로 이동한다.
- `docker-compose up -d` 명령어를 통해 서버를 실행한다.

## 🏖️ 구조 설명
- 각 폴더의 DockerFile에 자세한 설명이 적혀있습니다.
- 각 폴더의 docker-compose.yml 파일을 통해 여러 컨테이너를 실행할 수 있습니다.


# MacOS 유저 설정 (필수)

*docker-compose.yml 파일 수정*

21번째 줄 <br/>
(기존) `image: tkdals0978/todo-server` <br/>
(수정) `image: tkdals0978/todo-server-mac` <br/>

# 서버 시작하기
```bash
$ git clone https://github.com/sangminlee98/api-practice.git
```

```bash
$ cd api-practice
```

```bash
$ docker-compose up -d
```

# API 명세
![스크린샷 2023-07-11 오전 4 21 15](https://github.com/sangminlee98/api-practice/assets/83197138/c6d8731b-346c-4bfc-9c0c-c0db3e5c3e9b)

## 1. getTodos

### Request

- URL: `api/todos`
- Method: `GET`

### Response

```json
{
  "todos": [
    {
      "id": 1,
      "title": "할일 1",
      "done": false,
      "thumbnail": "https:// ~"
    },
    {
      "id": 2,
      "title": "할일 2",
      "done": true,
      "thumbnail": "https:// ~"
    },
    {
      "id": 3,
      "title": "할일 3",
      "done": false,
      "thumbnail": "https:// ~"
    }
  ]
}
```

## 2. createTodo

### Request

- URL: `api/todos`
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body:
  - `todoData: string`
  - `file?: File`

### Response

```json
{
  "id": 1,
  "title": "할일 1",
  "done": false,
  "thumbnail": "https:// ~"
}
```

## 3. updateTodo

### Request

- URL: `api/todos/:id`
- Method: `PUT`

### Response

```json
{
  "id": 1,
  "title": "할일 1",
  "done": false,
  "thumbnail": "https:// ~"
}
```

## 4. deleteTodo

### Request

- URL: `api/todos/:id`
- Method: `DELETE`

### Response

```json
없음
```
