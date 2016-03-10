<html>
<head>
    <title>GPS Position</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
</head>
<body>
    <div id="map"></div>
    <script type="text/javascript">
        function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 15,
                center: {
                    lat: {{ latitude }},
                    lng: {{ longitude }}
                }
            });

            var marker = new google.maps.Marker({
                position: {
                    lat: {{ latitude }},
                    lng: {{ longitude }}
                },
                animation: google.maps.Animation.DROP,
                map: map,
                title: 'Current Position'
            });
        }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key={{ api_key }}&callback=initMap" async defer></script>
</body>
</html>
