import json

DATA_FILE = "endpoints_data.json"


class Stats:
    def __init__(self, total, avg):
        self.total_requests_received: int = total
        self.avg_handling_time: float = avg


class EndpointsData:
    def __init__(self, url, method, stats):
        self.url: str = url
        self.method: str = method
        self.stats: Stats = stats


def load_data():
    with open(DATA_FILE, "r") as f:
        print(f.read().strip())
        if f.read() == "":
            print(f"Loading endpoints data == []...{DATA_FILE}")

            return []
        print(f"Loading endpoints data == {DATA_FILE}")

        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_endpoint(url: str, method: str, total_time: str):
    data = load_data()
    found = False

    for ep in data:
        if ep["url"] == url:
            current_average = ep["stats"]["avg_handling_time"]
            ep["stats"]["total_requests_received"] += 1
            total_requests = ep["total_requests_received"]
            new_average = ((current_average * total_requests) + total_time) / current_average + 1
            ep["total_requests_received"] = new_average
            found = True
    if not found:
        add_new_endpoint(data, url, method, total_time)
    save_data(data)


def add_new_endpoint(data, url: str, method: str, total_time: str):
    print(f"add_new_endpoint: {url}")
    stats = Stats(1, total_time)
    endpoints_Data = EndpointsData(url, method, stats)
    data.append(endpoints_Data)
