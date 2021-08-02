import requests


def get_mc_versions(stable=True):
    req = requests.get("https://meta.fabricmc.net/v2/versions/game")
    res = []

    # Adds only stable releases if true, else adds everything
    for i in req.json():
        if stable and i["stable"]:
            res.append(i)
        elif not stable:
            res.append(i)

    return res
