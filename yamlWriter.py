import yaml

# Add some error handling here

try:
    config = yaml.safe_load(open("config.yml"))

    polic = config["policy"]
    passw = config["password"]
    black = config["blacklist"]
    sized = config["size"]
    thresh = config["threshold"]
    fn = config["filename"]
except ( TypeError, FileNotFoundError):
    x = open("config.yml", "a+")
    polic = "normal"
    passw = "Quack"
    black = ""
    sized = 0
    thresh = 30
    fn = "log.txt"


def trainer(policy=polic, password=passw, blacklist=black, size=sized, filename=fn):
    global thresh
    data = dict(policy=policy, password=password, blacklist=blacklist, threshold=thresh, size=size,filename=filename)
    with open('config.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def trainer_avg(policy=polic, password=passw, blacklist=black, threshold=thresh, size=sized, filename=fn):
    data = dict(policy=policy, password=password, blacklist=blacklist, threshold=threshold, size=size, filename=filename)
    with open('config.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
