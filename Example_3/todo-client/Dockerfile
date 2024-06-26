# Todo 리스트 클라이언트를 위한 Dockerfile
# Dockerfile은 이미지를 생성하기 위한 설정 파일

# 최신 노드 이미지를 기반으로 이미지를 생성
FROM node:latest

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

COPY package.json ./
COPY yarn.lock ./

# yarn을 설치하고, 의존성을 설치
RUN npm install yarn --global --force
RUN yarn install --immutable --immutable-cache --check-cache

# 소스 코드를 작업 디렉토리로 복사
COPY . .

# 포트 3000을 열기
EXPOSE 3000

# 어플리케이션 실행
CMD ["yarn", "start"]