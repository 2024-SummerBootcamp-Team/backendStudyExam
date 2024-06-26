# 스프링 부트 어플리케이션을 빌드하기 위한 Dockerfile
# gradle 이미지를 기반으로 이미지를 생성
FROM gradle:7.6.1-jdk17 AS builder
WORKDIR /build

# 그래들 파일 변경시에만 의존성 다운로드를 하여 다운로드를 빠르게 할 수 있도록 함
COPY build.gradle settings.gradle /build/
RUN gradle build -x test --parallel --continue > /dev/null 2>&1 || true

# 어플리케이션 이미지 빌드, 해당 방식으로 빌드된 파일 크기 감소
COPY . /build
RUN gradle build -x test --parallel

# 빌드된 이미지에서 jar 파일을 추출
FROM openjdk:17.0-slim
WORKDIR /app
COPY --from=builder /build/build/libs/sample-0.0.1-SNAPSHOT.jar .

# 어플리케이션 실행
CMD ["java", "-jar", "sample-0.0.1-SNAPSHOT.jar"]