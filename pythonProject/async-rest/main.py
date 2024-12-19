import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 本项目参考地址 https://www.cnblogs.com/weiweivip666/p/18041425

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8801, reload=True)
