DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_NAME = "housing"

DB_CONNECTION_STRING = f"postgresql://admin:admin@postgres:5432/housing"

PREDICT_API_URL = "http://localhost:12347/predict"

BOSTON_HOUSING_DATA_PATH = "data/boston_housing.csv"

BOSTON_COLUMNS = [
    "CRIM",  # 人均犯罪率
    "ZN",  # 占地面积大于 25,000 平方英尺的住宅用地比例
    "INDUS",  # 城镇中非零售商用土地所占比例
    "CHAS",  # 是否临近查尔斯河（1=临近, 0=不临近）
    "NOX",  # 一氧化氮浓度（每一千万份）
    "RM",  # 每栋住宅的平均房间数
    "AGE",  # 1940 年以前建成且自住的房屋所占比例
    "DIS",  # 到波士顿五大就业中心的加权距离
    "RAD",  # 公路通达性指数
    "TAX",  # 每 $10,000 美元的全值财产税率
    "PTRATIO",  # 师生比例
    "B",  # 种族指标：1000*(Bk - 0.63)^2，其中 Bk 为地区黑人比例
    "LSTAT",  # 低社会地位人口占比（%）
    "MEDV",  # 房屋中位数价格（千美元）
]
