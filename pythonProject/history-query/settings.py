TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # MySQL OR Mariadb
            "credentials": {
                "database": "fastapi",
                "host": "localhost",
                "password": "root",
                "port": 3306,
                "user": "root",
                "charset": "utf8mb4",
                "minsize": 1,
                "maxsize": 5,
                "echo": True  # 是否反馈sql语句
            }
        }
    },
    "apps": {
        "models": {
            "models": ["model.models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
}
