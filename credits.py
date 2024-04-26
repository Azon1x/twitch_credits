import requests
import datetime
#import time
#start_time = time.time()

start_of_today = datetime.datetime.combine(datetime.datetime.today(), datetime.time(00, 00, 00, 000000)).isoformat()
end_of_today = datetime.datetime.combine(datetime.datetime.today(), datetime.time(23, 59, 59, 999999)).isoformat()

auth = {"Authorization": "Bearer YOUR_AUTH_TOKEN"}
url = 'https://api.streamelements.com/kappa/v2/activities/YOUR_ACTIVITY_ID'

def tippers():
    try:
        data = {"after":start_of_today, "before":end_of_today, "limit":500, "mincheer":2, "minhost":2, "minsub":1, "mintip":10, "origin":"true", "types":"tip"}
        usernames = requests.get(url, headers=auth, params=data).json()

        list_usernames = []
        list_amounts = []
        list_currencies = []
        count = 0

        while count < len(usernames):
            if usernames[count]['data']['username'] in list_usernames:
                index = list_usernames.index(usernames[count]['data']['username'])
                list_usernames.append(usernames[count]['data']['username'])
                list_usernames.pop()
                list_amounts[index] += usernames[count]['data']['amount']
                list_currencies.append(usernames[count]['data']['currency'])
                list_currencies.pop()

            elif usernames[count]['data']['username'] == 'Anonymous':
                list_usernames.append(usernames[count]['data']['username'])
                list_usernames.pop()
                list_currencies.append(usernames[count]['data']['currency'])
                list_currencies.pop()

            else:
                list_usernames.append(usernames[count]['data']['username'])
                list_amounts.append(usernames[count]['data']['amount'])
                list_currencies.append(usernames[count]['data']['currency'])
        
            count += 1  

        result = ""
        count2 = 0

        while count2 < len(list_usernames):
            result += list_usernames[count2] + " donatnul " + str("{:.2f}".format(list_amounts[count2])) + " " + list_currencies[count2] + "\n"
            count2 += 1

        return result
    except:
        print("Vyskytla se chyba: Zkontrolujte připojení k internetu.")

def cheerers():
    data = {"after":start_of_today, "before":end_of_today, "limit":500, "mincheer":2, "minhost":2, "minsub":1, "mintip":10, "origin":"true", "types":"cheer"}
    cheerers = requests.get(url, headers=auth, params=data).json()

    list_usernames = []
    list_amounts = []
    count = 0

    while count < len(cheerers):
        if cheerers[count]['data']['username'] in list_usernames:
            index = list_usernames.index(cheerers[count]['data']['username'])
            list_usernames.append(cheerers[count]['data']['username'])
            list_usernames.pop()
            list_amounts[index] += cheerers[count]['data']['amount']

        elif cheerers[count]['data']['username'] == 'Anonymous':
            list_usernames.append(cheerers[count]['data']['username'])
            list_usernames.pop()

        else:
            list_usernames.append(cheerers[count]['data']['username'])
            list_amounts.append(cheerers[count]['data']['amount'])
    
        count += 1  

    result = ""
    count2 = 0
    while count2 < len(list_usernames):
        result += list_usernames[count2] + " přihodil " + str(list_amounts[count2]) + " bitů\n"
        count2 += 1
    
    return result

def followers():
    data = {"after":start_of_today, "before":end_of_today, "limit":500, "mincheer":2, "minhost":2, "minsub":1, "mintip":10, "origin":"true", "types":"follow"}
    cheerers = requests.get(url, headers=auth, params=data).json()

    list_usernames = []
    count = 0

    while count < len(cheerers):
        if cheerers[count]['data']['username'] == 'Anonymous':
            list_usernames.append(cheerers[count]['data']['username'])
            list_usernames.pop()

        else:
            list_usernames.append(cheerers[count]['data']['username'])
    
        count += 1  

    result = ""
    count2 = 0
    while count2 < len(list_usernames):
        result += list_usernames[count2] + " hodil follow\n"
        count2 += 1
    
    return result

def hosts():
    data = {"after":start_of_today, "before":end_of_today, "limit":500, "mincheer":2, "minhost":2, "minsub":1, "mintip":10, "origin":"true", "types":"host"}
    hosts = requests.get(url, headers=auth, params=data).json()

    list_usernames = []
    list_amounts = []
    count = 0

    while count < len(hosts):
        if hosts[count]['data']['username'] in list_usernames:
            index = list_usernames.index(hosts[count]['data']['username'])
            list_usernames.append(hosts[count]['data']['username'])
            list_usernames.pop()
            list_amounts[index] += hosts[count]['data']['amount']

        elif hosts[count]['data']['amount'] == 1:
            list_usernames.append(hosts[count]['data']['username'])
            list_usernames.pop()
            list_amounts.append(hosts[count]['data']['amount'])
            list_amounts.pop()

        elif hosts[count]['data']['username'] == 'Anonymous':
            list_usernames.append(hosts[count]['data']['username'])
            list_usernames.pop()

        else:
            list_usernames.append(hosts[count]['data']['username'])
            list_amounts.append(hosts[count]['data']['amount'])
    
        count += 1  

    result = ""
    count2 = 0
    while count2 < len(list_usernames):
        if list_amounts[count2] <= 4:
            result += "Od " + list_usernames[count2] + " přišli " + str(list_amounts[count2]) + " lidi\n"
        else:
            result += "Od " + list_usernames[count2] + " přišlo " + str(list_amounts[count2]) + " lidí\n"

        count2 += 1

    return result
    
def raids():
    data = {"after":start_of_today, "before":end_of_today, "limit":500, "mincheer":2, "minhost":2, "minsub":1, "mintip":10, "origin":"true", "types":"raid"}
    raids = requests.get(url, headers=auth, params=data).json()

    list_usernames = []
    list_amounts = []
    count = 0

    while count < len(raids):
        if raids[count]['data']['username'] in list_usernames:
            index = list_usernames.index(raids[count]['data']['username'])
            list_usernames.append(raids[count]['data']['username'])
            list_usernames.pop()
            list_amounts[index] += raids[count]['data']['amount']

        elif raids[count]['data']['amount'] == 1:
            list_usernames.append(raids[count]['data']['username'])
            list_usernames.pop()
            list_amounts.append(raids[count]['data']['amount'])
            list_amounts.pop()

        elif raids[count]['data']['username'] == 'Anonymous':
            list_usernames.append(raids[count]['data']['username'])
            list_usernames.pop()

        else:
            list_usernames.append(raids[count]['data']['username'])
            list_amounts.append(raids[count]['data']['amount'])
    
        count += 1  

    result = ""
    count2 = 0
    while count2 < len(list_usernames):
        if list_amounts[count2] <= 4:
            result += list_usernames[count2] + " vtrhnul na stream se " + str(list_amounts[count2]) + " lidmi\n"
        else:
            result += "Od " + list_usernames[count2] + " vtrhnul na stream s " + str(list_amounts[count2]) + " lidmi\n"

        count2 += 1
    
    return result

def PS():
    return "DĚKUJI MOC ZA DNEŠNÍ STREAM, BYLI JSTE BOŽÍ!"

def FM():
    return "DĚKUJI VŠEM ZA VAŠI PODPORU!"

def printed(func, func2, func3, func4, func5):
    followers = print("FOLLOWERS:\n\n" + func5)
    tippers = print("DONATES:\n\n" + func)
    cheerers = print("CHEERS:\n\n" + func2)
    hosts = print("HOSTS:\n\n" + func3)
    raids = print("RAIDS:\n\n" + func4)

    return followers, tippers, cheerers, hosts, raids

try:
    printed(tippers() + "\n\n", cheerers() + "\n\n", hosts() + "\n\n", raids(), followers() + "\n\n")
except:
    print("Vyskytla se chyba: Nebylo možné vypsat titulky.")

try:
    with open(r'YOUR CREDITS_FILE.txt', 'w', encoding='utf-8') as f:
        if followers() + tippers() + cheerers() + hosts() + raids() == "":
            f.write("")
        else:
            f.write(FM()+ "\n\n\n")

        if followers() == "":
            f.write("")
        else:
            f.write("FOLLOWERS:\n\n" + followers() + "\n\n")

        if tippers() == "":
            f.write("")
        else:
            f.write("DONATES:\n\n" + tippers() + "\n\n")

        if cheerers() == "":
            f.write("")
        else:
            f.write("CHEERS:\n\n" + cheerers() + "\n\n")

        if hosts() == "":
            f.write("")
        else:
            f.write("HOSTS:\n\n" + hosts() + "\n\n")

        if raids() == "":
            f.write("")
        else:
            f.write("RAIDS:\n\n" + raids() + "\n\n\n\n")

        f.write(PS())

    f.close()
except:
    print("Vyskytla se chyba: Nebylo možné zapsat data do textového souboru.")

#print ("My program took", time.time() - start_time, "to run")




