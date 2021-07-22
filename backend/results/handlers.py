from datetime import datetime

def genereate_id():
    return "result-"+datetime.now().strftime("%Y%m%d-%H%M%S-")+str(datetime.now().timestamp()).replace('.', '-')

def generate_user_result_id():
        return "userResult-"+datetime.now().strftime("%Y%m%d-%H%M%S-")+str(datetime.now().timestamp()).replace('.', '-')

def generate_non_user_result_id():
        return "non_userResult-"+datetime.now().strftime("%Y%m%d-%H%M%S-")+str(datetime.now().timestamp()).replace('.', '-')
