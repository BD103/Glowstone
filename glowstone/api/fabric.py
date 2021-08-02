import requests

meta_url = "https://meta.fabricmc.net"


def get_mc_versions(stable=True):
    req = requests.get(meta_url + "/v2/versions/game")
    res = []

    # Adds only stable releases if true, else adds everything
    for i in req.json():
        if stable and i["stable"]:
            res.append(i)
        elif not stable:
            res.append(i)

    return res


def get_fabric_versions(stable=False):
    req = requests.get(meta_url + "/v2/versions/loader")
    res = []

    for i in req.json():
        if stable and i["stable"]:
            res.append(i)
        elif not stable:
            res.append(i)

    return res
