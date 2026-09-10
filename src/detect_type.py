import copy


def phone(phone_number: dict,phone_regex:dict,col_name:str):

    mark = 0
    mark += (phone_regex["Phone_number"])*0.4
    mark += phone_number["digit_ratio"]*0.35
    mark += max(0,20-((phone_number["length_std"])*10))
    mark += phone_number["special_ratio"]*0.05

    return ("Phone",mark)

    




def email(phone_number: dict,email_regex:dict,col_name:str):

    local_arr = ["letter_ratio", "digit_ratio","special_ratio"]
    mark = 0

    top3 = sorted(phone_number.items(), key=lambda x: x[1], reverse=True)[:3][::-1]

    for [i, value] in enumerate(top3):
        if value in local_arr:
            mark+=0.5


    if 80<= email_regex["Email"] <=100:
        mark += 2
    elif 50<= email_regex["Email"] <80:
        mark += 1.5
    elif 40<= email_regex["Email"] <50:
            mark += 0.5
    else :
        mark += 0

    mark_percentage = (mark/5)*100

    return ["Email" , mark_percentage]


def id(phone_number: dict,email_regex:dict,col_name:str):

    local_arr = ["special_ratio", "digit_ratio", "unique_ratio","letter_ratio"]
    mark = 0

    top3 = sorted(phone_number.items(), key=lambda x: x[1], reverse=True)[:3][::-1]

    for [i, value] in enumerate(top3):
        """if value[0] in local_arr:
            mark+=0.5"""

    if 0 < phone_number["length_std"]  < 1:
        mark += 1.5
    elif 1 < phone_number["length_std"]  < 1.5:
        mark += 0.5
    elif 1.5 < phone_number["length_std"] < 2:
        mark += 0.25
    else :
        mark +=0
    print(col_name,mark)
    if 80<= email_regex["ID"] <=100:
        mark += 2
    elif 50<= email_regex["ID"] <80:
        mark += 0.5
    elif 40<= email_regex["ID"] <50:
            mark += 0.25
    else :
        mark += 0

    mark_percentage = (mark/5)*100

    return ["ID" , mark_percentage]



def dict_make(stats_report: object, gen_report: object,regex_report:dict):
    stats_dict = {}
    packet = {}
    arr = [id,email,phone]

    type_samples = {}

    for col_name in gen_report.columns_name:
        packet["unique_ratio"] = stats_report.unique_ratio[col_name]
        packet["digit_ratio"] = stats_report.digit_ratio[col_name]
        packet["letter_ratio"] = stats_report.letter_ratio[col_name]
        packet["whitespace_ratio"] = stats_report.whitespace_ratio[col_name]
        packet["special_ratio"] = stats_report.special_ratio[col_name]
        packet["length_std"] = stats_report.length_std[col_name]

        stats_dict[col_name] = packet.copy()
        local_dict = {}

        for [i,value] in  enumerate(arr):
            val = value(stats_dict[col_name],regex_report[col_name],col_name)
            local_dict[val[0]] = val[1]

        type_samples[col_name] = local_dict

    return type_samples
