class Constant:
    server = '172.168.5.14\SQL2014'
    database_app = 'MesserHP_SP225_A'
    database_sys = 'MesserHP_SP225_B'
    username = 'messerhp'
    password = 'fsd'
    ApiLink = 'https://www.trackabout.com:443/api/'
    headers = {
        "Authorization": "Basic ZmFzdGVycF90YV91c3I6NEhOKlZleF42MjdD",
        "Accept": "application/json",
        "Host": "trackabout.com",
        "Cookie": "xkcd=m0zspu1cicyl3imkigrpxfta",
        "Content-Type": "application/json"
    }

    Store_check = 'exec api_CheckSyncTRA'
    namespace = {'ns': 'urn:schemas-fast-com:fast-api'}