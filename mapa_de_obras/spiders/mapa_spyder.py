import json

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "mapa"

    def start_requests(self):
        url = "https://a.tiles.mapbox.com/v4/mopc.iobaeb6c/features.json?access_token=pk.eyJ1IjoibW9wYyIsImEiOiJKNFo3aktvIn0.tQGSxRugkpMUIcxUskZHgQ"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # extraer el json del response
        json_obras = json.loads(response.text)

        # iterar sobre las obras, que se encuentran en features
        for obra in json_obras["features"]:

            #obtener el id
            id = obra["id"]

            # obtener informacion que se encuentra en "properties"
            properties = obra["properties"]
            titulo_obra = properties["title"]
            descripcion_obra = properties["description"]

            # obtener la informacion que se encuentra en "geometry"
            geometry = obra["geometry"]
            tipo_geometria = geometry["type"]
            coordenadas = geometry["coordinates"]

            #pprint.pprint(coordenadas)

            # crear el json y hacer yield
            yield {
                "id": id,
                "titulo_obra": titulo_obra,
                "descripcion_obra": descripcion_obra,
                "tipo_geometria": tipo_geometria,
                "coordenadas": coordenadas
            }
