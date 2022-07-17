import psycopg2


def GetConnectionString():
    """
    Give back connection with database!
    """
    # postgresql URI heroku
    POSTGRESQL_URI = "postgres://lvwcicxncrwxcg:9ccbcf890a4cbaae505e0864590aab79606bf4aff835d140cc9a062ab3dde74e@ec2-18-204-142-254.compute-1.amazonaws.com:5432/d79r2kcmsirp15"
    connection = psycopg2.connect(POSTGRESQL_URI)
    return connection


def row_to_dict(description, row):
    if row is None:
        return None
    d = {}
    for i in range(0, len(row)):
        value = row[i]
        key = description[i][0]
        try:
            d[key] = value
        except NameError:
            print("Variable x is not defined")
    return d

