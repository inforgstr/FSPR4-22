def domain_name(url):
    if url.startswith("www"):
        f = url[url.index(".")+1 :]
        return f[: f.index(".")]
    else:
        if "https" in url:
            return url[8:][: url[8:].index(".")]
        elif "http" in url:
            f = url[7:]
            return url[7:][: url[7:].index(".")]
        return url[: url.index(".")]


print(domain_name("google.com"))
