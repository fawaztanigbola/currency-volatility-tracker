def domain_name(url):
    """
    Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

    url = "http://github.com/carbonfive/raygun" -> domain name = "github"
    url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
    url = "https://www.cnet.com"                -> domain name = cnet"
    """

    url = url.split('.')
#     if we can find www the next string in our url split must be domain name
    for i, unit in enumerate(url):
        if unit =='www' or unit.find("www") != -1:
            return url[i+1]
#     if we find http in the first string excluding our www's if we split up that string the next string should be our domain name
    if url[0].find('http') != -1:
        url = url[0].split("//")
        return url[1]
#     if none of the above is true then our first string has to be our domain name
    return url[0]