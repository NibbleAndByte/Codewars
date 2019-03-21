def domain_name(url):
    beginningChaff =  {"https://", "http://", "www."}
    for chaff in beginningChaff:
        if (url.find(chaff) == 0):
            url = url.replace(chaff, "")
    index = url.find(".")
    return url[0:index]