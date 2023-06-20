

class Config : 
    HOST = 'yhdb.cnwaypyqm4je.ap-northeast-2.rds.amazonaws.com'
    DATABASE = 'memo_db2'
    DB_USER = 'memo_db2_user'
    DB_PASSWORD = '09090909m!!!!'

    # 비번 암호화
    SALT = '23sdfanywayI0382431@@@!!@#'

    # JWT 환경 변수 셋팅
    # 로그인 유효기간 등 셋팅 가능. 디폴트 값등 메뉴얼 보세요.
    JWT_SECRET_KEY = '32829@@!@#!#ejdkdfso'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True

    
