import json
import sys


def main() -> None:
    # Load your GeoJSON data
    input = sys.argv[1]
    geojson_data = json.load(open(input))

    # Convert the GeoJSON data to OSM XML format
    osm_xml = split_geojson(geojson_data)


if __name__ == '__main__':
    main()

def split_geojson(geojson: dict) -> None
    features = geojson.get("features", [geojson])
    for feature in features:
        properties = feature.get("properties", {})
        name = properties["AREANAME"]
      
        # Save the OSM XML data to a file
        output = name.replace(" ", "_") + ".xml"
        with open(output, 'w') as fp:
            json.dump(feature, fp)
        print('Wrote ' + output)
