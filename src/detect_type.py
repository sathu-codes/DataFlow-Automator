import copy
import pandas as pd
import sys 


def required_input(message):

    while True:
        value = input(message).strip()
        if value:
            return value

        print("This feild cant be empty")

def make_table(table_dict:dict):
    type_table = pd.DataFrame.from_dict(table_dict,orient="index")
    type_table.insert(0,"No",range(1,len(type_table)+1))
    print(type_table.round(2).to_string())

    return 0

def phone(phone_number: dict,phone_regex:dict,col_name:str):

    mark = 0
    mark += (phone_regex["Phone_number"])*0.5
    mark += phone_number["digit_ratio"]*0.3
    mark += max(0,15-((phone_number["length_std"])*7.5))
    mark += phone_number["special_ratio"]*0.05

    return ("Phone",round(mark,2))

def email(Email: dict,email_regex:dict,col_name:str):

    mark = 0
    mark += (email_regex["Email"])*0.6
    mark += Email["letter_ratio"]*0.25
    mark += Email["digit_ratio"]*0.1
    mark += Email["special_ratio"]*0.05

    return ("Email",round(mark,2))



def id(id: dict,id_regex:dict,col_name:str):

    mark = 0
    mark += (id_regex["ID"])*0.45
    mark += max(0,40-((id["length_std"])*20))
    mark += id["letter_ratio"]*0.05
    mark += id["digit_ratio"]*0.05
    mark += id["special_ratio"]*0.05
   
    return ["ID" , round(mark,2)]


def date(date: dict,date_regex:dict,col_name:str):

    mark = 0   
    mark += (date_regex["Date"])*0.7
    mark += date["letter_ratio"]*0.05
    mark += date["digit_ratio"]*0.1
    mark += date["special_ratio"]*0.05
   
    return ["Date" , round(mark,2)]

def currency(currency: dict,currency_regex:dict,col_name:str):

    mark = 0   
    mark += currency_regex["Currency"] * 0.2
    mark += currency["deciaml_ratio"] *0.6
    mark += currency["special_ratio"] * 0.2
   
    return ["Currency" , round(mark,2)]

def percentage(percentage:dict , percentage_regex:dict , col_name:str):
    mark=0
    mark+= percentage_regex["Percentage"]*0.3
    mark+= percentage["digit_ratio"]*0.3
    mark+= percentage["deciaml_ratio"]*0.2
    mark+= percentage["special_ratio"]*0.2

    return ["Percentage" , round(mark,2)]

def rating(rating:dict , rating_regex:dict , col_name:str):
    mark=0
    mark+= rating_regex["Rating"]*0.5
    mark+= rating["digit_ratio"]*0.25
    mark+= rating["letter_ratio"]*0.2
    mark+= rating["special_ratio"]*0.05

    return ["Rating" , round(mark,2)]



def dict_make(stats_report: object, gen_report: object,regex_report:dict):
    stats_dict = {}
    packet = {}
    arr = [id,email,phone,date,currency,percentage,rating]

    type_samples = {}

    for col_name in gen_report.columns_name:
        packet["unique_ratio"] = stats_report.unique_ratio[col_name]
        packet["digit_ratio"] = stats_report.digit_ratio[col_name]
        packet["letter_ratio"] = stats_report.letter_ratio[col_name]
        packet["whitespace_ratio"] = stats_report.whitespace_ratio[col_name]
        packet["special_ratio"] = stats_report.special_ratio[col_name]
        packet["deciaml_ratio"] = stats_report.deciaml_ratio[col_name]
        packet["length_std"] = stats_report.length_std[col_name]

        stats_dict[col_name] = packet.copy()
        local_dict = {}

        for [i,value] in  enumerate(arr):
            val = value(stats_dict[col_name],regex_report[col_name],col_name)
            local_dict[val[0]] = val[1]

        type_samples[col_name] = local_dict

    return type_samples


def detect(type_samples:dict,gen_report:object):
    final_type = {}

    for col_name,scores in type_samples.items():
        pocket = {}
        First_type = max(type_samples[col_name],key=type_samples[col_name].get)
        pocket["First_type"] = First_type
        pocket["Score"] = scores[First_type]
        pocket["Secountary"] = gen_report.colums_type[col_name]

        final_type[col_name] = pocket

    make_table(final_type)

    while True:
        choice= required_input("Enter the col_name which you wanna make any changes in the type Y/N").lower()

        if choice=='y':
            new_type = required_input("Enter the new type ")
            section_list = required_input("Enter the col number  which you wanna  apply this change : ").split()
            section_list = [int(x) for x in section_list]
            
            for i in section_list:
                final_type[gen_report.columns_name[i-1]]["First_type"] = new_type

        else :
            break


    return final_type

