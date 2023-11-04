def get_values_url_params(url):
    params = url.rsplit(sep="?")[1]
    var_values = params.rsplit("&")
    values = [ value.rsplit("=")[1] for value in var_values ]
    print(values)

url = "https://retosdeprogramacion.com?year=2023&challenge=0"

get_values_url_params(url)