// express 모듈을 가져온다.
const express = require('express');
// express의 인스턴스를 생성한다.
const app = express();

// 출력할 변수 선언
const temp = "";

// 라우트 설정
app.get('/', (req, res) => {

    // 변수 반환
    res.send(temp);
});

// 서버를 3000번 포트로 실행한다.
app.listen(3000, () => {
    console.log('Server Running Port(3000)');
});